# Python Learning App

It is a Python GUI software built with Tkinter that teaches the fundamentals of Python programming.

### Prerequisites

 MySQL must be installed in the user's system


### Layout and working

Running the program will prompt the user for an input to select either of these three:
- Tutorial
- Quiz
- Result


Selecting Tutorial will open a window with instructions and a button below them with the text "Try it yourself!!". 

![Home](https://github.com/hailASG/Python_Learning_App/blob/main/Images/Home.png)


Clicking the button will open a Python shell in a new window.

![Shell](https://github.com/hailASG/Python_Learning_App/blob/main/Images/Shell.png)


At any time, all the windows can be closed and a new input can be added in the running program.

Now if Quiz is selected then first the user will be prompted the enter the Username and the Password for MySQL, this is needed to store the final results. After entering the Username and the Password, a window will open asking for the details of the user.

![Details](https://github.com/hailASG/Python_Learning_App/blob/main/Images/Details.png)

After entering the details in the text field, first the "Enter" button has to be clicked, then the "Submit" button.

Now, four questions will be asked from the user. 
Selecting the correct answer's radio button will grant 1 point out of 4.

![Q1](https://github.com/hailASG/Python_Learning_App/blob/main/Images/Q1.png)

At any point, previous questions can be viewed again and their answers can be changed. 
Once the user clicks "Next" on the fourth question. The Final results will be displayed.

Finally, clicking the "Compute and Quit" button will store the result in the MySQL Database and close the window.

![Result](https://github.com/hailASG/Python_Learning_App/blob/main/Images/Result.png)


On the input screen, if Result is selected, then the user will be prompted to enter the Username and the Password for MySQL.
After that, the results of all the previous conducted quizes will be displayed in this format:

```('Name', 'Class', Score)```


### Files

#### Tutorial.txt

This contains the textual data of the instructions that will be used when 'Tutorial' is selected in input screen.


#### Proj.py

This contains the source code that implements the main program, the Tutorial window and is also responsible for displaying the results after fetching them from the MySQL Database.

This is the file that needs to be executed when the user needs to start the execution of the program.

#### Quiz.py

This contains the source code for implementing the quiz and for storing the result as a MySQL Database.


**P.S. I built this project in my 12th grade; I didn't have a Github account at the time, and I only recently discovered it in my old computer and decided to post it here.**
