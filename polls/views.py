from django.shortcuts import render

# Creatfrom django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")e your views here.
from django.shortcuts import render


def polls(request):
    return render(request, 'polls/home.html', locals())

def text(request):
    return render(request, 'polls/text.html', locals())

def objects(request):

    return render(request, 'polls/objects.html', {'content': ['Don’t cross the bridge until you come to it.', 'The cat is out of the bag', 'People who live in glass houses should not throw stones'] })
