from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from congresvoorstel.voorstel.forms import  *
from congresvoorstel.voorstel.models import  *


def new_amendement(request):
    if request.method == "POST":
        form = AmendementForm(request.POST)
        if form.is_valid():
            am = Amendement()
            am.email = form.cleaned_data['email']
            am.title = form.cleaned_data['title']
            am.gen_random_key()
            am.save()
            return HttpResponseRedirect(am.key)
    else:
        form = AmendementForm()
    c = {
        'submit':  '/amendement/',
        'title': 'Nieuw amendement indienen',
        'form':form
    }
    c.update(csrf(request))
    return render_to_response("new.html", c)


