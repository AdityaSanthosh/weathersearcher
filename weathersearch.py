def weather_search():
    import urllib3
    import json
    import os
    os.system('cls')
    API_KEY = 'c38ae4a54f9df72a168974b5fda1e86f'
    cityinput = input("Enter City Location to get weather data\n")
    link = 'api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cityinput, API_KEY)
    http = urllib3.PoolManager()
    r = http.request('GET', link)
    os.system('cls')
    print("Here is the data....")
    raw_data = r.data.decode('utf-8')
    data = json.loads(raw_data)
    print("city:", data['name'])
    print("humidity:", data['main']['humidity'])
    print("pressure:", data['main']['pressure'])
    print("temperature:", data['main']['temp'])
    print("wind speed:", data['wind']['speed'])
    print("city:", data['wind']['deg'])
    choice = input("Press x to search new city or any other key to quit")
    if choice == 'x':
        weather_search()
