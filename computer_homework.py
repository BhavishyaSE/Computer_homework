# # Q-2--------------------------------------------------------------
digit = int(input("Enter a single digit number:"))
if digit == 1:
    print("This is my 1st hello to you")
if digit ==1:
    print("This is my 2nd hello to you") 
if digit ==2:
    print("This is my 3rd hello to you") 
if digit ==3:
    print("This is my 4th hello to you") 
if digit ==4:
    print("This is my 4th hello to you") 
if digit ==5:
    print("This is my 5th hello to you") 
if digit ==6:
    print("This is my 6th hello to you") 
if digit ==7:
    print("This is my 7th hello to you") 
if digit ==8:
    print("This is my 8th hello to you") 
if digit ==9:
    print("This is my 9th hello to you") 

#  Q-3-----------------------------------------------------------------
inp1= int(input("Enter first number:"))
inp2= int(input("Enter Second number:"))
if inp1 > inp2:
    print("First number is greator than second")
elif inp1<inp2:
    print("Second number is greator than first number")
else:
    print("Both numbres are equal")


#Q-4-------------------------------------------------------------------------
day = int(input("Enter The number of day")
if day==1:
    print("SUNDAY")
elif day==2:
    print("MONDAY")
elif day==3:
    print("TUESDAY")
elif day==4:
    print("WEDNESDAY")
elif day==5:
    print("THURSDAY")
elif day==6:
    print("FRIDAY")
elif day==7:
    print("SATURDAY")
else:
    print("invalid input")

#Q-5---------------------------------------------------------------------------------
year = int(input("Enter the year in YYYY format:"))
if year%4==0 and year!=100:
    print("This year is a leap year")
elif year%400==0:
    print("this year is Leap year")
else:
    print("This year is not a leap year")

#Q-6--------------------------------------------------------------------------------
a = float(input("Enter the side a:"))
b = float(input("Enter the side b:"))
c = float(input("Enter The side c:"))
if a==b==c:
    print("This Triangle is equilateral")
elif a==b and a!= c:
    print("This triangles is isoceles")
elif b==c and b!=a:
    print("This triangle is isoceles")
elif c==a and c!=b:
    print("This triangle is isoceles")
elif a!=b!=c:
    print("This triangles is scalene")
else:
    print("Enter A valid input")

#Q-7
month = int(input("Enter The number of month:"))
if month==1:
    print("This month is january and the number of days are 31")
elif month==2:
    print("This month is february and the number of days are 28")
elif month==3:
    print("This month is march and the number of days are 31")
elif month==4:
    print("This month is april and the number of days are 30")
elif month==5:
    print("This month is may and the number of days are 31")
elif month==6:
    print("This month is june and the number of days are 30")
elif month==7:
    print("This month is july and the number of days are 31")
elif month==8:
    print("This month is august and the number of days are 31")
elif month==9:
    print("This month is september and the number of days are 30")
elif month==10:
    print("This month is october and the number of days are 31")
elif month==11:
    print("This month is november and the number of days are 30")
elif month==12:
    print("This month is december and the number of days are 31")
else:
    print("Invalid input")
