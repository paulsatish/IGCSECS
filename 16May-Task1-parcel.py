

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
if weight<1 or weight >12:
    print("Parcel weight should be >1 and <12.  Hence parcel rejected")
else:
    print("Parcel accepted")
             

 
