today='1221/23/12'
date=int(today[-2:])
dt=[]
dt.append(today)
for i in range(6):
	d=today[0:8]+str(date-i-1)
	dt.append(d)
print(dt)
for i in range(7):
	a=dt[i][5:].split("/")
	a.reverse()
	dt[i]="/".join(a)
dt.reverse()
print(dt)