# q1
print("hello word")

print("=======================================")
# q2
c=input("enter number")
decimal=int(c,2)
print(decimal)


# q3


def getstring(number) :
    if int(number)%3==0 and int(number)%5==0:
        return("fizzbuzz")
    elif  int(number)%3==0:
        return("fizz")
    elif int(number)%5==0:
        return("buzz")  
    else:
        return("inter valid number")
    

print(getstring(20))
print(getstring(3))
print(getstring(15))
# q4
radius=float(input("inter radius"))

area=float(3.14*radius*radius)
print(round(area,2))

# q5
while True:
    name = input("Enter your name: ").strip()
    
    if name.isalpha():
        email = input("Enter your email: ").strip()
        if '@'in email and '.' in email:
            print("email",email) 
        else:
            print("Invalid name! Please enter letters only")      

        break
    else:
        print("Invalid name! Please enter letters only.")





print("Name:", name)
print("Email:", email)

# q6
s="welcome to iti that make me strong in any fields of ai and iti,ITI"
if s.lower():
    print("the number of iti accesss",s.count("iti"))

        




      

