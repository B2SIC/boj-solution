month, date = map(int, input().split())
md=[31,28,31,30,31,30,31,31,30,31,30,31]
total = 0
result=['SUN','MON','TUE','WED','THU','FRI','SAT']
for i in range(month-1):
	total = total+md[i]
total = total + date
print (result[total%7])