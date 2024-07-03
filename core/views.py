from django.shortcuts import render
from api.api_forecast import read_forecast
from classes.data_forecast import Forecast
import datetime

# Create your views here.

def home (request):
    forecast_data = read_forecast()
    return render (request, 'index.html', {'data': forecast_data})

def chart (request):
    forecast_list = list()
    forecast_data = read_forecast()
    for data in forecast_data:
        forecast_list.append(f'x: {data.timestamp}, y: {data.temperature}')

    return render (request, 'chart.html', {'forecast_data': forecast_list})