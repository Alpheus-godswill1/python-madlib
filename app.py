# So suppose we want to create a string that said  "Hello my name is ______, happy to see you!"

# name = "" #some string variables

# a few ways to do this 
# print("Hello my name is " + name + ", happy to see you!")
# print("Hello my name is  {}, happy to see you!" . format(name))
# print(f"Hello my name is  {name},  happy to see you!")

# Getting started with the madlib project it self
adj = str(input("adj: "))
verb = str(input("ver: "))
verb2 = str(input("verb2: "))
verb3 = str(input("verb3: "))
madlib = f'Setting up a kubernetes cluster is so {adj}! to balance this docs on the cloud 9 server is very {verb} \n it makes it so {verb2}. Stay hydrated and {verb3} to learn in other to master this DevOps path'
print(madlib)

