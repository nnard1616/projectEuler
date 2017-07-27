
tdays = 365*75+366*25
year =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
lyear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print sum(year)

count = 0
day =1
for y in range(1,101):
    
    if y%4 == 0:
        months = lyear
    else:
        months = year
    for m in year:
        if day%7 == 6:
            count+=1
        day += m

print count, tdays
        
