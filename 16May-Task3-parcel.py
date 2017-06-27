
TotalNotAccepted=0
TotalAccepted=0
TotalWeight=0
totalprice=0
sumTotal=0
weightingrams=0
price=0
maxpay=0
continue1="yes"
while continue1=="yes":
    maxweight=10
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
    elif weight>=1 and weight<=5:
        price=10
        print("please pay $"+ str(price))
    elif weight>5 and weight<=10:
        maxweight=weight-5
        maxweightInGrams=maxweight*1000
        maxpay=1000+(maxweightInGrams*0.10)
        totalPrice=maxpay/100
        print("Please pay $" +str(totalPrice))
        sumTotal=sumTotal+totalPrice
        TotalWeight=TotalWeight+weight
        TotalAccepted=TotalAccepted+1
    print("Total number of parcels accepted are :" + str(TotalAccepted))
    print("Total number of parcels not accepted are :" + str(TotalNotAccepted))  
    print("Total weight of all the accepted parcels is:" +str(TotalWeight))
    print("Total price of all the accepted parcels is:" +str(sumTotal)) 
    continue1=input("Do you want to continue?")
             

 
