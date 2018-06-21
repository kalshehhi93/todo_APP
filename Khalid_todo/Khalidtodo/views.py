from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            return render(request, 'home.html', {'all_items' : all_items})

    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def about(request):
    return render(request, 'about.html', {})
# Create your views here.

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    return  redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.complete = True
    item.save()
    return  redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.complete = False
    item.save()
    return  redirect('home')
