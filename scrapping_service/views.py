from django.shortcuts import render
import datetime

def index(request):
    date = datetime.datetime.now().date()
    name = 'Dave'
    my_dict = {'date': date, 'name': name}
    return render(request, 'index.html', my_dict)
