## Weather Information System

Search Weather Data by City

To run this App
1. Clone the Repository
2. Create a Virtual Python Environment
3. Run ```pip install -r requirements.txt``` to install all the necessary packages
4. Create an API key at https://openweathermap.org/api by creating an Account
5. Place the key at .env file in the source code
6. Run ```python main.py``` to run the App
7. The Instructions to use the App are present in the App itself

###### How it Works

1. The Weather Data is fetched from OpenWeatherMap API
2. You need an Account and API key for that.
3. The data is fetched using ```urllib3``` library
4. The returned data is parsed and displayed on the Console.
5. The login System is implemented using ```bcrypt``` library