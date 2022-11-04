print("This program converts Kilometers to Miles")

km=float(input("enter the number in kilometers:"))
miles=float(input("enter the number of miles:"))

print(km,"km","equals to",round((1/1.609344),3),"miles")
print(miles,"miles","equals to",round((km*1.609344),3),"km")
