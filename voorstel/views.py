from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from congresvoorstel.voorstel.forms import  *
from congresvoorstel.voorstel.views import  *


def new_amendement(request):
    if request.method == "POST":
        form = AmendementForm(method.POST)
    else:
        form = AmendementForm()
    c = {'form':form}
    c.update(csrf(request))
    return render_to_response("form.html", c)


