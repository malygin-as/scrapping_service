from django.shortcuts import render
from .models import Vacancy
from .forms import SearchForm


def home_view(request):
    city = request.GET.get('city')
    codelang = request.GET.get('codelang')
    filter_parameters = {}
    query_set = []
    form = SearchForm()

    if city or codelang:
        if city:
            filter_parameters['city__slug'] = city
        if codelang:
            filter_parameters['codelang__slug'] = codelang
        query_set = Vacancy.objects.filter(**filter_parameters)

    return render(request, 'scraping_app\home.html', {'object_list': query_set,
                                                      'form': form})
