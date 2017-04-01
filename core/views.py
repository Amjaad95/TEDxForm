from django.shortcuts import render
from core.forms import RegestirationForm
from core.models import Regestiration

def handl_regesteration(request):
    if request.method == 'POST':
        form = RegestirationForm(request.POST)
        if form.is_valid():
            regesteration = form.save()
            return HttpResponseRedirect(reverse('core:'))
    else:
        form = RegestirationForm()
    context = {'form': form}
    return render(request, 'index.html', context)

def list_regesteration_participants(request, pk):
    regestiration = get.object.all()
    context = {'regestiration': regestiration}
    return render(request, '', context)
