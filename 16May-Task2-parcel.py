TotalNotAccepted=0
TotalAccepted=0
TotalWeight=0
continue1="yes"
while continue1=="yes":
    print("Please enter the parcel dimensions")
    height=float(input("Please enter the height of the parcel in cm: "))
    width=float(input("Please enter the width of the parcel in cm: "))
    length=float(input("Please enter the length of the parcel in cm: "))

    dimSum=height+width+length

    if height>80 or width>80 or length>80:
        print("One of the dimensions are more than 80cm.  Please enter <=80")

    if dimSum>200:
        print("Sum of three dimensions should be <= 200")

    weight=float(input("Please enter the weight of the parcel in KG"))
    if weight<1 or weight >12 or height>80 or width>80 or length>80 or dimSum>200:
        print("Parcel rejected")
        TotalNotAccepted=TotalNotAccepted+1
    else:
        print("Parcel accepted")
        TotalWeight=TotalWeight+weight
        TotalAccepted=TotalAccepted+1
    continue1=input("Do you want to continue?")
print("Total number of parcels accepted are :" + str(TotalAccepted))
print("Total number of parcels not accepted are :" + str(TotalNotAccepted))  
print("Total weight of all the accepted parcels is:" +str(TotalWeight))
             

 
