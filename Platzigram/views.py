''' Platzigram views'''

#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime

def hello_world(request):
    ''' Return a greeting'''
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse('Oh hi! Current server time is {now}'.format(now=str(now)))

def hi(request):
    return HttpResponse('Hi')

def default(request):
    return HttpResponse('Wenas noshes')