from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def results(request):
    response = "You're looking at the results of question %s."
    return HttpResponse(response)
