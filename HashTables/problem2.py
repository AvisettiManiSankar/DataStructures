# 2. nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
#   (a) What was the temperature on Jan 9?
#   (b) What was the temperature on Jan 4?
#   Figure out data structure that is best for this problem

weather_dict = {}
with open('nyc_weather.csv') as f:
    for row in f:
        row_values = row.split(',')
        try:
            weather_dict[row_values[0]] = int(row_values[1])
        except:
            print('Invalid Row: ', row)

print(weather_dict['Jan 9'])
print(weather_dict['Jan 4'])
