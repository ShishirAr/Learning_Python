print('''Twinkle twinkle little star 
       "
      "How I wonder what you are "
      "Up above the world so high "
      "Like a diamond in the sky "
      "Twinkle twinkle little star "
      "How I wonder what you are"
      ''')


import pyttsx3
engine = pyttsx3.init()


engine.say("I love you kritu!")
engine.runAndWait()

a=1 #a is a ineteger

b=5.2 #b is a float

c="Aryan" #c is a string

d=True #d is a boolean

e=None #e is a none type


f= a==b
print(f)

a=int(input("A: "))

b=int(input("B: "))

print(" A+B is : ",a+b)


print("remainder when a is dived by b is ", a%b)

