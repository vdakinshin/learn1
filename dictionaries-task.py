weather = {'city': 'Москва', 'temperature': '20', 'wind': 'Восточный'}
print(weather)

print(weather.get('city'))
print(weather['city'])

weather['temperature'] = 23
print(weather.get('temperature'))

dic_len = len(weather)
print(dic_len)

print(weather.get('country'))

country_in_weather = 'country' in weather
print(country_in_weather)

weather['date'] = '27.05.2017'
print(weather)


weather2 = {'city': 'Москва', 'temperature': '19', 'wind': 'Западный', 'date': '26.05.2017'}
weather3 = {'city': 'Москва', 'temperature': '18', 'wind': 'Южный', 'date': '25.05.2017'}

weather_history = []

print(weather_history)
weather_history.append(weather)
print(weather_history)
weather_history.append(weather2)
print(weather_history)
weather_history.append(weather3)
print(weather_history)

