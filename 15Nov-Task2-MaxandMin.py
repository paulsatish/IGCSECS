# find the maximum and minimum numbers
# Task 2
# replace count<4 with "count<18"

max=-999
min=999
count=1
while count<4:
      a=int(input("enter the temperature"))
      if a>max:
            max=a
            print(max)
      if a<min:
            min=a
            print(min)
      count=count+1
      difference=max-min
print("The maximum temperature is: " +str(max))
print("The minimum temperature is: " +str(min))
print("The difference between the maximum and the minimum temperature is:"+str(difference))

