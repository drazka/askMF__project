import datetime

from redis import Redis
from rq import Queue
from django_rq import job

from askMF_project.askMF2 import NIPExtractor

q = Queue(connection=Redis())


@job
def nip_worker():
    from NIP_checker_app.models import NIP
    nips = NIP.objects.all()
    nip_extractor = NIPExtractor()
    result = nip_extractor.check_list_of_nips(nips.values_list('nip_number', flat=True))
    for krotka in result:
        nip = NIP.objects.get(nip_number=krotka[0])
        nip.result_from_MF = krotka[1]
        my_time = datetime.datetime.now() + datetime.timedelta(hours=2)
        nip.check_date = my_time.strftime("%Y-%m-%d %H:%M:%S")
        nip.save()



