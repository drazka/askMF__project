from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
from redis import Redis
from rq import Queue

# Create your views here.
from django.views import View

from NIP_checker_app.forms import NIPForm, Login4Form
from NIP_checker_app.models import NIP
from NIP_checker_app.worker import nip_worker
from askMF_project.askMF2 import NIPExtractor


class NIPView(View):
    def get(self, request):
        ctx = {
            'form' : NIPForm,
        }

        return render(request, "create_nip.html", ctx)

    def post(self, request):
        form = NIPForm(request.POST)
        if form.is_valid():
            nip_number = form.cleaned_data['nip_number']
            my_date = datetime.datetime.now() + datetime.timedelta(hours=2)
            add_date = my_date.strftime("%Y-%m-%d %H:%M:%S")
            nip = NIP.objects.create(nip_number=nip_number,
                                     add_date=add_date)
            nip.save()
            return redirect('nip_list')
        ctx = {
            'form' : NIPForm,
        }
        return render(request, "nip_list.html", ctx)
"""
    def post(self, request):
        form = NIPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nip_list')
        ctx = {
            'form' : NIPForm,
        }
        return render(request, "create_nip.html", ctx)
    
"""

class Login4View(View):
    def get(self, request):
        ctx = {
            'form': Login4Form
        }
        return render(request, 'login_form.html', ctx)

    def post(self,request):
        form = Login4Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                url = request.GET.get('next')
                if url:
                    return redirect(url)
                return HttpResponse("zostales zalogowany")

            form.add_error(field=None, error='zly login lub haslo')
        ctx = {
            'form': form
        }
        return render(request, 'login_form.html', ctx)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponse('wylogowales sie')


class NipListView(View):
    def get(self, request):
        nips = NIP.objects.all()
        ctx = {
            'nips_list' : nips,
        }

        return render(request, "nip_list.html", ctx)


class NipListCheckView(View):
    def get(self, request):
        import django_rq
        django_rq.enqueue(nip_worker)

        ctx = {
            'message' : 'poinformujemy o wynikach wkrotce',
        }

        return render(request, "nip_checked.html", ctx)
