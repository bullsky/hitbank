from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import *
from login.models import Account
from bindcard.models import UserCard

# Create your views here.

#def check(request,username,password,verifcode):
