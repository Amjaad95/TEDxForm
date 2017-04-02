from django.shortcuts import render
from core.forms import RegestirationForm
from core.models import Regestiration
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def handl_regesteration(request):
    if request.method == 'POST':
        form = RegestirationForm(request.POST)
        if form.is_valid():
            new_regesteration = form.save()
            return HttpResponseRedirect(reverse('/thanks/'))
    else:
        form = RegestirationForm()
    context = {'form': form}
    return render(request, 'index.html', context)

def list_regesteration_participants(request, pk):
    regestiration = get.object.all()
    context = {'regestiration': regestiration}
    return render(request, '', context)
