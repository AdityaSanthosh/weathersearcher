def weather_search():
    import urllib3
    import json
    import os
    from dotenv import load_dotenv
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    os.system('cls')
    cityinput = input("Enter City Location to get weather data\n")
    print("Please Wait. This may take some time")
    link = 'api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cityinput, API_KEY)
    http = urllib3.PoolManager()
    r = http.request('GET', link)
    os.system('cls')
    print("Here is the data....")
    raw_data = r.data.decode('utf-8')
    data = json.loads(raw_data)
    try:
        if data['cod']:
            print(data["message"], end='\n')
            key = input("Press Enter to search again")
            if key == '':
                weather_search()
    except:
        print("city:", data['name'])
        print("humidity:", data['main']['humidity'])
        print("pressure:", data['main']['pressure'])
        print("temperature:", data['main']['temp'])
        print("wind speed:", data['wind']['speed'])
        print("city:", data['wind']['deg'])
        choice = input("Press x to search new city or any other key to quit")
        if choice == 'x':
            weather_search()
