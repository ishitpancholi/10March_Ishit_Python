# Program to check multiple keys exist in a dictionary

mystudent= {
    "Name": "Ishit",
    "Roll No": "40",
    "class": "A"

}
print(mystudent.keys()>={"class","Name"})
print(mystudent.keys()>={"Roll No","Name"})
print(mystudent.keys()>={"class","Ishit"})
print(mystudent.keys()>={"Ishit","40"})