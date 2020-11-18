#list of elements to calculate mean
import csv

with open('height-weight.csv', newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

#to pop out the first line from the list
file_data.pop(0)

#sorting data to ge the height of the people
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

#getting the median
n=len(new_data)
new_data.sort()

#using floor division to get the nearest number
#floor division is shown by //
if n%2==0:
    #getting the first number
    median1=float(new_data[n//2])
    #getting the second number
    median2=float(new_data[n//2-1])
    #getting the mean of the 2 numbers
    median=(median1+median2)/2
else:
    median=new_data[n//2]

print("The median is: "+ str(median))