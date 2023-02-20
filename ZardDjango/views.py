import datetime
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    now=datetime.datetime.now()
    html="<html><body><h2>Now time is %s.</h2><body><html>"%now
    return HttpResponse(html)
def welcome(request):
    return HttpResponse("Welcome to Django Class")
def emobilis(request):
    return HttpResponse("eMobilis mobile technology Institute")
def