#replace (1,3) with (1,7) later
TempMidday=[]
DayMax=-999
DateMax=0
for i in range(1,3):

    temp1=float(input("Please enter the Temperature for MidDay"))
    TempMidday.append(temp1)
    print(TempMidday)
    if temp1>DayMax:
        DayMax=temp1
        DateMax=i
print("The day with maximum Mid-day temperatureis: " + str(DayMax))
print("The date of Maximum temperature recorded is on: " + str(DateMax))
