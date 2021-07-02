import json
from datetime import timedelta, datetime
import requests
import lxml
import lxml.html.clean
from bs4 import BeautifulSoup

def get_event_time_investing(country_check, volatility_check):

    data_to_send = []

    gmt_time_optimization_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    gmt_time_optimization_end = gmt_time_optimization_start + timedelta(days=1) + timedelta(minutes=1)

    url = 'https://sslecal2.forexprostools.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://sslecal2.forexprostools.com/'}
    data = requests.get(url, headers=headers)

    soup = BeautifulSoup(data.content, 'lxml')
    match = soup.body.div.form.div.table.tbody

    if country_check is None and volatility_check is not None:

        if volatility_check == 3:
            volatility_status = "High Volatility Expected"
        elif volatility_check == 2:
            volatility_status = "Moderate Volatility Expected"
        elif volatility_check == 1:
            volatility_status = "Low Volatility Expected"

        for tag in match.find_all('tr'):
            if tag.get("event_timestamp") != None:
                time = tag.get("event_timestamp")
                date_time_table_time_clock = datetime.strptime(time, '%Y-%m-%d %H:%M:%S') + timedelta(hours=3)
                volatility = tag.find('td', {'sentiment'}).get("title")
                if volatility == "High Volatility Expected":
                    volatility_send = 3
                elif volatility == "Moderate Volatility Expected":
                    volatility_send = 2
                elif volatility == "Low Volatility Expected":
                    volatility_send = 1
                if gmt_time_optimization_start <=date_time_table_time_clock <= gmt_time_optimization_end and str(volatility) == volatility_status:
                    rate_change_time = date_time_table_time_clock.strftime("%Y-%m-%d, %H:%M:%S")
                    country = tag.find('span').get('title')
                    event_name = tag.find('td', {'class':"left event"}).text
                    event_name = event_name.replace(u'\xa0',u'')
                    data_to_send.append([rate_change_time, country, event_name, volatility_send])
                    #print(rate_change_time, country, event_name, volatility_send)
        return data_to_send
    
    elif country_check is not None and volatility_check is not None:

        if volatility_check == 3:
            volatility_status = "High Volatility Expected"
        elif volatility_check == 2:
            volatility_status = "Moderate Volatility Expected"
        elif volatility_check == 1:
            volatility_status = "Low Volatility Expected"
        
        for tag in match.find_all('tr'):
            if tag.get("event_timestamp") != None:
                time = tag.get("event_timestamp")
                date_time_table_time_clock = datetime.strptime(time, '%Y-%m-%d %H:%M:%S') + timedelta(hours=3)
                volatility = tag.find('td', {'sentiment'}).get("title")
                country = tag.find('span').get('title')
                if volatility == "High Volatility Expected":
                    volatility_send = 3
                elif volatility == "Moderate Volatility Expected":
                    volatility_send = 2
                elif volatility == "Low Volatility Expected":
                    volatility_send = 1
                if gmt_time_optimization_start <=date_time_table_time_clock <= gmt_time_optimization_end and str(volatility) == volatility_status and str(country) == str(country_check):
                    rate_change_time = date_time_table_time_clock.strftime("%Y-%m-%d, %H:%M:%S")
                    event_name = tag.find('td', {'class':"left event"}).text
                    event_name = event_name.replace(u'\xa0',u'')
                    data_to_send.append([rate_change_time, country, event_name, volatility_send])
                    #print(rate_change_time, country, event_name, volatility_send)
        return data_to_send

    elif country_check is not None and volatility_check is None:
        for tag in match.find_all('tr'):
            if tag.get("event_timestamp") != None:
                time = tag.get("event_timestamp")
                date_time_table_time_clock = datetime.strptime(time, '%Y-%m-%d %H:%M:%S') + timedelta(hours=3)
                volatility = tag.find('td', {'sentiment'}).get("title")
                country = tag.find('span').get('title')
                if volatility == "High Volatility Expected":
                    volatility_send = 3
                elif volatility == "Moderate Volatility Expected":
                    volatility_send = 2
                elif volatility == "Low Volatility Expected":
                    volatility_send = 1
                if gmt_time_optimization_start <=date_time_table_time_clock <= gmt_time_optimization_end and str(country) == str(country_check):
                    rate_change_time = date_time_table_time_clock.strftime("%Y-%m-%d, %H:%M:%S")
                    event_name = tag.find('td', {'class':"left event"}).text
                    event_name = event_name.replace(u'\xa0',u'')
                    data_to_send.append([rate_change_time, country, event_name, volatility_send])
                    #print(rate_change_time, country, event_name, volatility_send)
        return data_to_send

    elif country_check is None and volatility_check is None:
        for tag in match.find_all('tr'):
            if tag.get("event_timestamp") != None:
                time = tag.get("event_timestamp")
                date_time_table_time_clock = datetime.strptime(time, '%Y-%m-%d %H:%M:%S') + timedelta(hours=3)
                volatility = tag.find('td', {'sentiment'}).get("title")
                country = tag.find('span').get('title')
                if volatility == "High Volatility Expected":
                    volatility_send = 3
                elif volatility == "Moderate Volatility Expected":
                    volatility_send = 2
                elif volatility == "Low Volatility Expected":
                    volatility_send = 1
                if gmt_time_optimization_start <=date_time_table_time_clock <= gmt_time_optimization_end:
                    rate_change_time = date_time_table_time_clock.strftime("%Y-%m-%d, %H:%M:%S")
                    event_name = tag.find('td', {'class':"left event"}).text
                    event_name = event_name.replace(u'\xa0',u'')
                    data_to_send.append([rate_change_time, country, event_name, volatility_send])
                    #print(rate_change_time, country, event_name, volatility_send)
        return data_to_send