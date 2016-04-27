from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings


def home(request):
    """
    Default view
    """
    return render(request, 'bets/home.html')