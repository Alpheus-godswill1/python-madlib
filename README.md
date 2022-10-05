# In a traditional Madlib, one would have a bunch of blanks in a paragraph, and have someone fill out those blanks, and read the paragraph out loud with the words that they chose for the blanks


1. This will only be made possible and available by using string concatenation in python

2. There are 3 main ways to concatenate strings in python
>>String concatenation (aka how to put strings together)
>> So suppose we want to create a string that said  "Hello my name is ______, happy to see you!"

 
# A few ways to do this 
name = ""  -- 'some string variables' 
1. print("Hello my name is " + name + ", happy to see you!")
2. print("Hello my name is  {}, happy to see you!" . format(name))
3. print(f"Hello my name is  {name},  happy to see you!")