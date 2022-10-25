from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import pandas as pd

CONTENT = pd.read_csv('data-398-2018-08-30.csv')
result = []
for row_number in range(1, len(CONTENT)):
    row = [i for i in CONTENT.loc[row_number, ['Name', 'Street', 'District']]]
    result.append({'Name': row[0], 'Street': row[1], 'District': row[2]})


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(result, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
