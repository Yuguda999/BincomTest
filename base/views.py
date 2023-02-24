from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PollingUnitForm
from .models import PollingUnit, AnnouncedPuResults, Lga, Party, AnnouncedLgaResults, Ward


# Create your views here.


def home(req):
    all_polling_units = PollingUnit.objects.all().distinct()
    return render(req, 'index.html', {'all_polling_units': all_polling_units})


def polling_unit_result(request, uniqueid):
    results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=uniqueid)
    context = {
        'results': results,
    }
    return render(request, 'polling_unit_result.html', context)


def lga(request):
    lgas = Lga.objects.all()
    context = {
        'lgas': lgas,
    }
    return render(request, 'lga.html', context)


def lga_result_details(request, lga_name, lga_id):
    results = {}
    total_votes = 0
    announced_votes = 0
    try:
        uniqueid = PollingUnit.objects.filter(lga_id=lga_id).first().polling_unit_id
    except AttributeError:
        pass
    else:
        results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=uniqueid).all()

    for result in results:
        total_votes += result.party_score
    anounced_lga_result = AnnouncedLgaResults.objects.filter(lga_name=lga_id)
    for anounced_result in anounced_lga_result:
        announced_votes+=anounced_result.party_score
    print(anounced_lga_result)
    context = {
        'lga': lga_name,
        'total_votes': total_votes,
        'announced_votes': announced_votes
    }
    return render(request, 'lga_result.html', context)


def add_polling_unit_result(request):
    form = PollingUnitForm()
    if request.method == 'POST':
        form = PollingUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'new_polling_unit.html', context)
