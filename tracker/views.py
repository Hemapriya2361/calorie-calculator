from django.shortcuts import render, redirect
from django.shortcuts import *
from .models import Entry
from django.http import HttpResponse
import csv

def index(request):
    entries = Entry.objects.all().order_by('-date')
    intake = sum(e.calories for e in entries if e.type == "Intake")
    burn = sum(e.calories for e in entries if e.type == "Burn")
    net = intake - burn
    return render(request, 'tracker/index.html', {
        'entries': entries,
        'intake': intake,
        'burn': burn,
        'net': net
    })

def add_entry(request):
    if request.method == 'POST':
        date = request.POST['date']
        type = request.POST['type']
        description = request.POST['description']
        calories = request.POST['calories']
        Entry.objects.create(date=date, type=type, description=description, calories=calories)
    return redirect('index')

def delete_entry(request, id):
    entry = get_object_or_404(Entry, id=id)
    entry.delete()
    return redirect('index')

def edit_entry(request, id):
    entry = get_object_or_404(Entry, id=id)
    if request.method == 'POST':
        entry.date = request.POST['date']
        entry.type = request.POST['type']
        entry.description = request.POST['description']
        entry.calories = request.POST['calories']
        entry.save()
        return redirect('index')
    return render(request, 'tracker/edit.html', {'entry': entry})

def export_csv(request):
    entries = Entry.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fitness_log.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'Type', 'Description', 'Calories'])
    for entry in entries:
        writer.writerow([entry.date.strftime('%Y-%m-%d'), entry.type, entry.description, entry.calories])

    return response
