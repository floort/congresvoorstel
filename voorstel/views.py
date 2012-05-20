from django.shortcuts import render_to_response, get_object_or_404
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


def amendement(request, slug):
    am = get_object_or_404(Amendement, key=slug)
    if request.method == "POST":
        form = AmendementCommentForm(request.POST)
        if form.is_valid():
            ac = AmendementComment()
            ac.amendement = am
            ac.author = "Indiener"
            ac.text = form.cleaned_data['text']
            ac.save()
            form = AmendementCommentForm()
    else:
        form = AmendementCommentForm()
    comments = AmendementComment.objects.filter(amendement=am)
    c = {
        'form': form,
        'amendement': am,
        'comments': comments,
    }
    c.update(csrf(request))
    return render_to_response("amendement.html", c)




