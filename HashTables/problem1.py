# 1.nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

arr = []
with open('nyc_weather.csv','r') as f:
    for row in f:
        row_values = row.split(',')
        try:
            arr.append(int(row_values[1]))
        except:
            print('Invalid Row: ',row)
    print('Average Temp: ', sum(arr)/len(arr))
    print('Max Temp: ', max(arr))
