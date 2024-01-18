<h1> Hello and welcome! </h1>

---

This is a python gauntlet, whoever has the best code performance and style will win a cash prize, MORE PUZZLES WILL RELEASE ON 31ST JAN AND DEADLINE IS FEB 10th.

Add your name to the top of your code using a # comment.

Each task will have a hint or piece of code that will help you in solving it but I recommend learning how to google code solutions, [w3schools](https://www.w3schools.com/python/) is a great learning tool for novices :D

There is no "right" way to code, especially in python. So long as your code is readable and not incredibly slow its good code!

_My DMs are always open for advice and support_

---

<h2> Getting started </h2>
I personally recommend getting:<br>

[IDLE: Windows](https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe)<br>
[IDLE: All downloads](https://www.python.org/downloads/release/python-3121/)<br>
[VSCode: All downloads](https://code.visualstudio.com/download)<br>
This is a barebones python IDE developed by the python foundation with all python docs included inapp!

However, if you want a linter (autocomplete), VSCode and PyCharm community edition are great IDEs to use.

---
<h3> Tasks </h3>

_`print("hello world")`_

<h4> Task 1: My 'hello world'</h4>

- Ask the user to input two numbers
- Return the sum of the numbers IF the former > the latter

<details>
<summary>
Hints for task:
</summary>

> Use int(input()) and print()
</details>

<br />

<h4> Task 2: Fruit loops</h4>

- Write a function that takes any number of number inputs, meaning integer and float types
- Return the max value of these numbers
- I want this code to exit the loop if the number input is 0

<details>
<summary>
Hints for task:
</summary>

> Use a while loop, a for loop and a list! p.s max() is your friend.

```py
list = []
inp = float(input())
while inp != -1:
for value in range(start, end, jump):
```
</details>

<br />

<h4> Task 3: Introduction to functions</h4>

- Create a function that takes two integer inputs
- Return the power of each, so x ** y and y ** x

<details>
<summary>
Hints for task:
</summary>

```py
def func(input_parameters):
    # Code
    return
```
</details>

<br />
<br />

Great! Now we have a basic understanding of the majority of the content that is used in the structured programming labs, now its time to link everything together.

Wait...
I forgot something

erm

FILE HANDLING!
Python has two methods to open files, the good way and the bad way!
<br />

<h4> Task 4: File handling</h4>

- Create a file
- Write to a file
- Read a file
- Append to a file

<details>
<summary>
Hints for task:
</summary>

```py
a = file.open("text.txt", "r")
b = a.read()
a.close()
# Bad and stinky
with open("text.txt", "r") as file:
    # for line in file
    # b = a.read()
# good and will close the file for you outside of the loop!
```
</details>

<br />

<h4> Task 5: Classes</h4>

- I will keep this brief
- Make a class named "Person"
    - This person will have a name and age variable
    - Case sensitive
- Add a function for setting the age of the person
- Add a function for getting the name of the person
<details>
<summary>
Hints for task:
</summary>

Good luck `:P`
</details>

<br />

Final one I promise

This will require the power of google (w3schools <3)

I will also have solutions posted for all of these \^_\^

<br />

<h4> Task 999: Calculator</h4>

_SHOCK AND HORROR - a viable github project!_

- Write a calculator
- This will loop until an exit code is given
- This will take a string input, e.g "4 + 2" -> The space is necessary
- This will call a function with your input
- This function will split the input and cast the numbers [cast](https://www.w3schools.com/python/python_casting.asp) to a float
- This can be done with if statements or error handling
- This will output the result
- This calculator will support:
    - All arithmetic operations:
        - \+ \- * ** / // %
    - All logic operations:
        - < > == != >= <= [is]()
- This calculator will have an opcode and two operands, as seen in the example



<details>
<summary>
Hints for task:
</summary>
Have fun, plan it out, w3 has what you need (my DMs are always open, too)
</details>

# Happy coding, losers!

<h2>To submit, either zip your files and send them to me (no zipbombs please) or clone this repository to your own github and send me the link, I do not mind!</h2>
