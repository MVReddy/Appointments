import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Schedule
from django.core import serializers

# Create your views here.


def home(request):
    if request.method == 'GET':
        search_str = request.GET.get('search_str', None)
        if search_str:
            schedules = Schedule.objects.filter(description__contains=search_str)
        else:
            schedules = Schedule.objects.all()

        response = {'data': schedules}
        return render(request, 'home.html', response)
    elif request.method == 'POST':

        data = request.POST
        s = Schedule()
        s.DATE = data.get('date', datetime.datetime.now().date())
        s.TIME = data.get('time', datetime.datetime.now().time())
        s.description = data.get('description', 'Test')
        s.save()

        schedules = Schedule.objects.all()

        response = {'data': schedules, 'message': "Successfully added new appointment"}
        return render(request, 'home.html', response)


def search_appointments(request):
    search_str = request.GET.get('search_str', None)
    if search_str:
        schedules = Schedule.objects.filter(description__contains=search_str)
    else:
        schedules = Schedule.objects.all()
    json_data = serializers.serialize('json', schedules)
    return HttpResponse(json_data, content_type='application/json')