Temperaturerange=[]
MinTemperature=36.0
MaxTemperature=37.5
CurrentTemp=0
for i in range(1,3):
    CurrentTemp=float(input("Enter the present temperature of the baby: "))  
    if CurrentTemp < 36.0 :
        print("The temperature is too low")
    elif CurrentTemp >37.5:
        print("The temperature is too high")
    else:
        print("The temperature is fine")



