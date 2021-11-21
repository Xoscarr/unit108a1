print("Hello world of python!")

# Variables 
name = "Oscar"
age = 26
total= 99.99 
found = True


print(name)         
print(age)
print(total)
print(found)

print(age +1 )
print(name + " my last")
print(name * 5)


# Conditionals

if found: 
    print("yay you found it!")
    print("test 2")

if age < 99:
    print ("Dont worry you are still young") 
elif age == 99:
    print("Wow you are borderline getting old") 
else:
    print("ouch you are getting old now :(")


def test():
    print("hello, I'm a function")
    print("I'm inside rn")
    print("mee too!")

    if 3 > 2:
        print("Of course is lower than 3")

def Name():
    print("Oscar Rodriguez")      

def say_hello(name):
    print("Hello" + name) 

def sum(num1, num2):
    total = num1 + num2 
    return total 
      

# exec function
test()
Name()
say_hello("Angel")
res = sum(21, 21)
print(res)

person= "Brad pitt"
say_hello(person)