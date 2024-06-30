from urllib.request import urlopen
from classes.data_forecast import Forecast
import json, datetime

def read_forecast():
    url = "https://api.open-meteo.com/v1/forecast?latitude=-27.6667&longitude=-48.5505&hourly=temperature_2m&timeformat=unixtime&timezone=America%2FSao_Paulo"

    response = urlopen(url)
    data_json = json.loads(response.read())
    
    forecast_list = list()
    x = 0
    for data in data_json['hourly']['time']:
        #forecast_timestamp_iso = datetime.datetime.fromtimestamp(int(data_json['hourly']['time'][x])).strftime('%d/%m/%Y %H:%M')
        forecast_data = Forecast(data_json['hourly']['time'][x], data_json['hourly']['temperature_2m'][x])
        forecast_list.append(forecast_data)
        x = x+1

    return forecast_list