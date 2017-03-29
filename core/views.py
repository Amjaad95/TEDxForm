from django.shortcuts import render
from core.forms import RegestirationForm
from core.models import Regestiration

def handl_regesteration(request):
    if request.method == 'POST':
        form = RegestirationForm(request.POST, instance=regesteration)
        if form.is_valid():
            regesteration = form.save()
            return HttpResponseRedirect(reverse('core:recruitment_thanks'))
    else:
        form = RegestirationForm()
    context = {'form': form}
    return render(request, '', context)

def list_regesteration_participants(request, pk):
    regestiration = get_object_or_404(Regestiration, pk=pk)
    context = {'regestiration': regestiration}
    return render(request, '', context)
