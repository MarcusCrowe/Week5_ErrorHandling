Error Handling

When unhandled errors arise in a python program, the entire program crashes. Error handling allows us to write code to detect and handle errors preventing our program from crashing. It also allows the programmer to provide the user of the python program with a more meaningful description of what the error means.


The try/except statement can be used to provide error handling within python programs. The syntax is as follows:

try:

# Some Code....

except:

# optional block

# Handling of exception (if needed)

else:

# execute if no exception

finally:

# Some code .....(always executed)


Consider the following function.

def divtest(x): return 42 / x

Executing divtest(0) produces the following:

>>> divtest(0) Traceback (most recent call last): File "<stdin>", line 1, in <module> File "<stdin>", line 2, in divtest ZeroDivisionError: division by zero


Note the "ZeroDivisionError". This is the exception thrown because we are dividing by zero. The following code can be written to detect and handle this error without crashing our program.


def divtest(x): try:

42 / x except ZeroDivisionError: print('Error: Invalid Argument. A division by zero has been attempted') else: return 42 / x finally: print('42 divided by {} is:'.format(x))


Executing divtest(3) would then produce the following:

>>> divtest(3) 42 divided by 3 is: 14.0


But executing divtest(0) produces this rather than crashing:

>>> divtest(0) Error: Invalid Argument. A division by zero has been attempted 42 divided by 0 is:


1. Create a new GitHub repository and clone it.

2. Add the contents of this file to README.md and add it, commit with appropriate comment, and push it.

3. Write a script with a function that does the following:

a. Uses the input function to prompt the user for a number between 1 and 10 and store that value in a variable.

i. Note do not perform any casting at this stage

b. Use the try/except clause along with the int function to test if the value entered is a number.

c. If it is a number multiply the number entered by 3.14

d. If it is not a number, handle the error and produce a message indicating something other than a number was entered and ask the user to please enter a number.

4. Demonstrate your function with a valid number and with a letter.

5. Add, commit with comment, and push.

6. Submit your source code, git log, screenshots of both demonstrations, and screenshot of GitHub repo.
