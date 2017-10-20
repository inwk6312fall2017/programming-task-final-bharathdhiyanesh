import weather from Weather
api="https://github.com/stevob21/weather-api"
weather=Weather()

lookup=weather.lookup()
condition=lookup()
print(condition['text']
