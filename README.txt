Programming Language Write Up
By: Drew Sadler


(1) describes in detail the language you're parsing


The language is a simple almost english type language that is set up a bit like a movie script, so statements read like simple lines you would see in a script. The variables you use in the code are the characters you introduce into the program, and you must have them enter and exit the scene in order to assign them any value. If you add any sort of modification to an assigned variable, then you must use a and or but in order to use another function in the sentence. You can technically finish a program just by having your assigned characters buzz out of the scene, and not using the Exit function, but it was added to reset variables in case you wanted longer programs so 1 variable could have multiple outputs. But it is split up into multiple math functions with basic keywords of the operator like “added”,”multiplied”,”divided”, etc.. that you assign to your characters name, you must have the name of the variable you want to modify constantly being brought up in the code, so it can easily modify it, without having a complicated parse of sentence. So even though the sentence above says it would be saying a certain thing or that it would equal a certain amount, it can always be changed or modified before it buzzes out.




 (2) tells me any interesting things I should take note of in your grammar or code 


When designing my grammar I was not able to use the -> function to name offsets of a variable, so I ended up with a very long and messy grammar that I wish could be more cleaned up, also my grammar has multiple functions to assign/allocate variable to try and fit a normal sentence set up and allow for multiple uses of variable if wanting to change it in the program. If a character is to die it will exit the whole program despite what is compiled and will be circumstantial if it prints or not.


(3) gives me clear instructions on how to run your code from the command line.


You must have a Character/name enter the screen, assigning it in a square bracket with a capital Enter to introduce it. You are able to assign it through plenty of variable, by allocating it with the name and then “bee” whatever you want to set it equal to, or by assigning it with the name of your character along with some variant of “buzz in” along with a speech or equal phrase to indicate what the character is set equal to a letter or number. If you are using equal statements to numbers, then you are able to follow it up with a and or but depending on the math you were wanting to execute that fits in the sentence ending with a times or more. After that you must have the character exit the scene by buzzing out in some variation which would print your name/variable. Then in order to reset everything, and finish the program then you must put the characters name in a square bracket line with a capital “Exit” before the name.














Sample Programs:
[Enter Barry]
Barry buzzed in saying Hello
[Enter Ann]
Ann buzzed in having 4 cans, and Ann added 3 more
Ann buzzed out
Barry buzzed out
[Exit Ann]
[Exit Barry]


[Enter Barry]
Barry buzzed in and collected 3 books, but Barry also got 4 more
Barry buzzed out
[Exit Barry]


[Enter Barry]
Barry buzzed in collected 3 cans, but Barry multiplied it 2 times
Barry buzzed out
[Exit Barry]


[Enter Barry]
Barry buzzed in collected 6 cans, but Barry divided 2 times
Barry buzzed out
[Exit Barry]


[Enter Barry]
Let Barry bee 3
but Barry lost 2
Barry buzzed out
[Exit Barry]


[Enter Barry]
Barry buzzed in collected 3 cans
Barry died
[Exit Barry]


[Enter Barry]
Barry buzzed in saying Hello!
Barry buzzed out
[Exit Barry]


[Enter Barry]
Barry buzzed in and collected 3 books
Barry buzzed in saying NO
Barry buzzed out
[Exit Barry]


[Enter Barry]
Barry buzzed in and collected 3 books
Barry buzzed in saying NO
Let Barry bee 9
Barry buzzed out
[Exit Barry]
