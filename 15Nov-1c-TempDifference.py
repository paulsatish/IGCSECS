#Task 3
Temperaturerange=[]
MinTemperature=36.0
MaxTemperature=37.5
CurrentTemp=0
counter=0
for i in range(1,4):
    CurrentTemp=float(input("Please enter current temp: "))
    DifferenceMin=MinTemperature-CurrentTemp
    DifferenceMax=CurrentTemp-MaxTemperature
   
    if DifferenceMin>1.0 or DifferenceMax>1.0:
        counter=counter+1
    if counter>2:
        print("The temperature difference is morethan 1 is already twice in three hours")
                      
