import sys
import weather from Weather
api="https://github.com/stevob21/weather-api"
weather=Weather()

x = None
current_max = 0
y = None

for line in sys.stdin:
    line = line.strip()

    y, temp = line.rsplit('\t', 1)

    try:
        temp = float(temp)
    

lookup=weather.lookup()
condition=lookup()
print(condition['text']

