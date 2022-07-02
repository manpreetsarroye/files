obj=open("students.txt","w")
size=int(input("how many students details you want to enter:"))
for i in range(size):
    roll=int(input("enter roll number:"))
    name=input("enter your name:")
    marks=float(input("enter your marks:"))
    value=str(roll)+","+name+","+str(marks)+"\n"
    obj.write(value)
obj.close()