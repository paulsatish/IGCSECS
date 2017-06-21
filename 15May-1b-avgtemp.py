#replace (1,3) with (1,7) later

TempMidday=[]
TempMidnight=[]
MiddayAvg=0
MidnightAvg=0
MiddayTotal=0
MidNightTotal=0    
for i in range(1,3):
    temp1=float(input("Please enter the Temperature for MidDay"))
    TempMidday.append(temp1)
    MiddayTotal=MiddayTotal+temp1

    temp2=float(input("Please enter the Temperature for MidNight"))
    TempMidnight.append(temp2)
    MidNightTotal=MidNightTotal+temp2

print(TempMidday)
print(TempMidnight)
MiddayAvg=MiddayTotal/3
MidnightAvg=MidNightTotal/3


print("The average temperature for midnight is: "+ str(MiddayAvg))
print("The average temperature for midnight is: "+ str(MidnightAvg))


