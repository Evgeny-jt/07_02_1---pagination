import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


with open('data-398-2018-08-30.csv', 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    new_csv = []
    for row in csv_reader:
        if row[1] == 'Name':
            continue
        else:
            new_csv.append({'Name': row[1], 'Street': row[4], 'District': row[6]})
# print(new_csv)


def bus_stations(request):
    number_page = int(request.GET.get('page', 1))
    print(number_page)
    paginator_bus_stations = Paginator(new_csv, 10)
    page = paginator_bus_stations.get_page(number_page)
    context = {
        'bus_stations': paginator_bus_stations.get_page(number_page),
        'page': page
    }
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    # context = {
    # #     'bus_stations': ...,
    # #     'page': ...,
    # }
    return render(request, 'stations/index.html', context)
