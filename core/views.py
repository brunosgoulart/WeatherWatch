from django.shortcuts import render
from api.api_forecast import read_forecast
from classes.data_forecast import Forecast
import datetime

# Create your views here.

def home (request):
    forecast_data = read_forecast()
    return render (request, 'index.html', {'data': forecast_data})

def chart (request):
    timestamp_list = list()
    temperature_list = list()
    forecast_data = read_forecast()
    for data in forecast_data:
        timestamp_list.append(data.timestamp)
        temperature_list.append (data.temperature)

    return render (request, 'chart.html', {'timestamp': timestamp_list, 'temperature': temperature_list})