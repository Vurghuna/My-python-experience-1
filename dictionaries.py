print("This program provides information which a user wants to know about the person")

person={"name":"Vurghuna","gender":"female","age":"20","adress":"Akhundzade","phone":"+994775212765"}
key=input("What information do you want to know about the person? ").lower()
result=person.get(key,"That information is not available")
print(result)
