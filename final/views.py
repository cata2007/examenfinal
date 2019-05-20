from django.shortcuts import render
from django.http import HttpResponse
from .models import Users


def persons(request):
    if request.method == 'GET':
     persons = Users.objects.all()
     return render(request, 'list.html', {'persons': persons})




from django_pandas.io import read_frame
qs = persons.objects.all()
df = read_frame(qs)