from csv import DictReader

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    
    list_of_stantions = []
    with open('data-398-2018-08-30.csv', newline='', encoding='utf8') as file:
        for row in DictReader(file):
            list_of_stantions.append({'Name': row.get('Name'),
                                      'Street': row.get('Street'),
                                      'District': row.get('District')})
    print(f'{list_of_stantions=}')
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(list_of_stantions, 10)
    page = paginator.get_page(page_number)
    context = {
            'bus_stations': page.object_list,
            'page': page,
        }

    return render(request, 'stations/index.html', context)
