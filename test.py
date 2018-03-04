#Oct 2017
#Python 2.7


filename='esk_data.txt'

file = open(filename, 'r') 
data = file.readlines()
#print('type(data)')

for line in data:
	print (line.rstrip())

#print ('-----------------')

max=len(data)
#print (max)

last= data[max-1]
#print (last)

#data2=data.strip()
#print data2

d=type(data)
print(d)

#a,b,c,d,e=last.split("   ",5)
#print (a)

#list = first.split("	",5)
#print list
#list2=str(list)
#print list2
#list3=list2[2]
#print list3


#DATE=list[1]
#print DATE
#TIME=list[1]


#lines = file.readlines()
#lines = file.read().split(" ")
#print lines
#print len(lines)
file.close()
