months=("January","February","March","April","May","June","July","August","September","October","November","December")
day_of_birth=input("Please type your birthday in DD-MM-YYYY format:")

index=int(day_of_birth[3:5])-1
birthdaymonth=months[index]
date=int(day_of_birth[0:2])

print("Your birthday is",birthdaymonth,date)
