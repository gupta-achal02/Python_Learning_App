import tkinter
import mysql.connector as SQL


def update_result():    # function for updating Mysql database
    global nam
    global clas
    global total
    global user_name
    global password

    mydb = SQL.connect(host="localhost", user=user_name, passwd=password)
    mycursor = mydb.cursor()

    if mydb.is_connected() == False:
        print("Can't establish connection")

    try:
        mycursor.execute("CREATE DATABASE result")
    except:
        mycursor.execute("USE result")

    try:
        mycursor.execute("CREATE TABLE marksheet (Name VARCHAR(255), Class VARCHAR(255), MarksOb INT(1))")
        comm = "INSERT INTO marksheet (Name, Class, MarksOb) VALUES (%s, %s, %s)"
        val = (nam, clas, total)
        mycursor.execute(comm, val)
        mydb.commit()
    except:
        comm = "INSERT INTO marksheet (Name, Class, MarksOb) VALUES (%s, %s, %s)"
        val = (nam, clas, total)
        mycursor.execute(comm, val)
        mydb.commit()

    windows6.destroy()


total = 0    # counter for the total score of teh candidate

# creating lists for the questions and answers

q = [

    "Q1.Which of these is not a core data type?",
    "Q2.What data type is the object below ?: L = [1, 23, ‘hello’, 1]",
    "Q3.Which of the following function convert a string to a float in python?",
    "Q4.What is the output of the following program: print 'Hello World'[::-1]",

]

a0 = ["Lists", "Dictionary", "Tuples", "Class"]
a1 = ["List", "Dictionary", "Tuple", "Array"]
a2 = ["int(x[.base])", "long(x[,base])", "float(x)", "str(x)"]
a3 = ["dlroW olleH", "Hello Worl", "d", "Error"]


def bnext():  # function to be used as a command for the Submit Button

   global windows
   windows = tkinter.Toplevel(root)  # Toplevel() creates a new window on top of the root window
   windows.title("Question 1")
   windows.geometry("850x360")
   windows.resizable(width=False, height=False)
   windows.configure(background='#36abcb')
   windows.rowconfigure(0, weight=1)
   windows.rowconfigure(6, weight=1)
   windows.columnconfigure(0, weight=5)
   windows.columnconfigure(2, weight=5)
   root.withdraw()   # withdraw() hides the root window

   Q1_Label = tkinter.Label(windows, text=q[0], font=('consolas', 12), bg='#36abcb')
   Q1_Label.grid(row=0, column=1)

   # RadioButtons for answer selection
   Q1b1 = tkinter.Radiobutton(windows, text=a0[0], value=0, variable=v0,
                              command=checked, bg='#36abcb', font='consolas').grid(row=2, column=1)
   Q1b2 = tkinter.Radiobutton(windows, text=a0[1], value=1, variable=v0,
                              command=checked, bg='#36abcb', font='consolas').grid(row=3, column=1)
   Q1b3 = tkinter.Radiobutton(windows, text=a0[2], value=2, variable=v0,
                              command=checked, bg='#36abcb', font='consolas').grid(row=4, column=1)
   Q1b4 = tkinter.Radiobutton(windows, text=a0[3], value=3, variable=v0,
                              command=checked, bg='#36abcb', font='consolas').grid(row=5, column=1)

   btn1 = tkinter.Button(windows, text="Next", font=('consolas', 12, 'bold'), bg="#13759c", fg="white",
                 command=bnext2).grid(row=6, column=2)
   btn2 = tkinter.Button(windows, text="Back", font=('consolas', 12, 'bold'), bg="#13759c", fg="white",
                 command=bback).grid(row=6, column=0)
   windows.mainloop()

# further command definitions for Next Buttons
def bnext2():

   global windows3
   windows3 = tkinter.Toplevel(windows)
   windows3.title("Question 2")
   windows3.geometry("850x360")
   windows3.resizable(width=False, height=False)
   windows3.configure(background='#36abcb')
   windows3.rowconfigure(0, weight=1)
   windows3.rowconfigure(6, weight=1)
   windows3.columnconfigure(0, weight=5)
   windows3.columnconfigure(2, weight=5)
   windows.withdraw()

   Q2_Label = tkinter.Label(windows3, text=q[1], font=('consolas', 12), bg='#36abcb')
   Q2_Label.grid(row=0, column=1)
   Q2b1 = tkinter.Radiobutton(windows3, text=a1[0], value=0, variable=v1,
                              command=checked, bg='#36abcb', font='consolas').grid(row=2, column=1)
   Q2b2 = tkinter.Radiobutton(windows3, text=a1[1], value=1, variable=v1,
                              command=checked, bg='#36abcb', font='consolas').grid(row=3, column=1)
   Q2b3 = tkinter.Radiobutton(windows3, text=a1[2], value=2, variable=v1,
                              command=checked, bg='#36abcb', font='consolas').grid(row=4, column=1)
   Q2b4 = tkinter.Radiobutton(windows3, text=a1[3], value=3, variable=v1,
                              command=checked, bg='#36abcb', font='consolas').grid(row=5, column=1)

   btn3 = tkinter.Button(windows3, text="Next", font=('consolas', 12, 'bold'), bg="#13759c", fg="white",
                         command=bnext3).grid(row=6, column=2)
   btn4 = tkinter.Button(windows3, text="Back", font=('consolas', 12, 'bold'), bg="#13759c", fg="white",
                         command=bback2).grid(row=6, column=0)
   windows3.mainloop()


def bnext3():

   global windows4
   windows4 = tkinter.Toplevel(windows3)
   windows4.title("Question 3")
   windows4.geometry("850x360")
   windows4.resizable(width=False, height=False)
   windows4.configure(background='#36abcb')
   windows4.rowconfigure(0, weight=1)
   windows4.rowconfigure(6, weight=1)
   windows4.columnconfigure(0, weight=5)
   windows4.columnconfigure(2, weight=5)
   windows3.withdraw()

   Q3_Label = tkinter.Label(windows4, text=q[2], font=('consolas', 12), bg='#36abcb')
   Q3_Label.grid(row=0, column=1)
   Q3b1 = tkinter.Radiobutton(windows4, text=a2[0], value=0, variable=v2,
                              command=checked, bg='#36abcb', font='consolas').grid(row=2, column=1)
   Q3b2 = tkinter.Radiobutton(windows4, text=a2[1], value=1, variable=v2,
                              command=checked, bg='#36abcb', font='consolas').grid(row=3, column=1)
   Q3b3 = tkinter.Radiobutton(windows4, text=a2[2], value=2, variable=v2,
                              command=checked, bg='#36abcb', font='consolas').grid(row=4, column=1)
   Q3b4 = tkinter.Radiobutton(windows4, text=a2[3], value=3, variable=v2,
                              command=checked, bg='#36abcb', font='consolas').grid(row=5, column=1)

   btn5 = tkinter.Button(windows4, text="Next", font=('consolas', 12, 'bold'), bg="#13759c", fg="white",
                         command=bnext4).grid(row=6, column=2)
   btn6 = tkinter.Button(windows4, text="Back", font=('consolas', 12, 'bold'), bg="#13759c", fg="white",
                         command=bback3).grid(row=6, column=0)
   windows4.mainloop()


def bnext4():

   global windows5
   windows5 = tkinter.Toplevel(windows4)
   windows5.title("Question 4")
   windows5.geometry("850x360")
   windows5.resizable(width=False, height=False)
   windows5.configure(background='#36abcb')
   windows5.rowconfigure(0, weight=1)
   windows5.rowconfigure(6, weight=1)
   windows5.columnconfigure(0, weight=5)
   windows5.columnconfigure(2, weight=5)
   windows4.withdraw()

   Q4_Label = tkinter.Label(windows5, text=q[3], font=('consolas', 12), bg='#36abcb')
   Q4_Label.grid(row=0, column=1)
   Q4b1 = tkinter.Radiobutton(windows5, text=a3[0], value=0, variable=v3,
                              command=checked, bg='#36abcb', font='consolas').grid(row=2, column=1)
   Q4b2 = tkinter.Radiobutton(windows5, text=a3[1], value=1, variable=v3,
                              command=checked, bg='#36abcb', font='consolas').grid(row=3, column=1)
   Q4b3 = tkinter.Radiobutton(windows5, text=a3[2], value=2, variable=v3,
                              command=checked, bg='#36abcb', font='consolas').grid(row=4, column=1)
   Q4b4 = tkinter.Radiobutton(windows5, text=a3[3], value=3, variable=v3,
                              command=checked, bg='#36abcb', font='consolas').grid(row=5, column=1)

   btn7 = tkinter.Button(windows5, text="Next", font=('consolas', 12, 'bold'), bg="#13759c", fg="white",
                         command=bnext5).grid(row=6, column=2)
   btn8 = tkinter.Button(windows5, text="Back", font=('consolas', 12, 'bold'), bg="#13759c", fg="white",
                         command=bback4).grid(row=6, column=0)

   windows5.mainloop()


def bnext5():

   global windows6
   windows6 = tkinter.Toplevel(windows5)
   windows6.title("Final Result")
   windows6.geometry("850x360")
   windows6.resizable(width=False, height=False)
   windows6.configure(background='#36abcb')
   windows6.rowconfigure(0, weight=1)
   windows6.rowconfigure(3, weight=1)
   windows6.columnconfigure(0, weight=5)
   windows6.columnconfigure(2, weight=5)
   windows5.withdraw()

   btn9 = tkinter.Button(windows6, text="Back", font=('consolas', 12, 'bold'), bg="#13759c", fg="white",
                         command=bback5).grid(row=3, column=0)
   bquit = tkinter.Button(windows6, text="Compute & Quit", font=('consolas', 12, 'bold'),
                  bg="#13759c", fg="white", command=update_result).grid(row=3, column=2)

   Res_Label = tkinter.Label(windows6, text="Final Result:- ", font=("consolas", 15, "bold"), bg="#36abcb")
   Res_Label.grid(row=0, column=1)

   res = tkinter.Label(windows6, text="{} of Class {} has scored {}/4...".format(nam, clas, total), font=("consolas", 12, "bold"),
                       bg="#36abcb")
   res.grid(row=1, column=1)

   windows6.mainloop()

# command definitions for the Back buttons
def bback():

    windows.withdraw()
    root.deiconify() # deiconify() shows the hidden window
    root.mainloop()


def bback2():

    windows3.withdraw()
    windows.deiconify()
    windows.mainloop()


def bback3():

    windows4.withdraw()
    windows3.deiconify()
    windows3.mainloop()


def bback4():

    windows5.withdraw()
    windows4.deiconify()
    windows4.mainloop()


def bback5():

    windows6.withdraw()
    windows5.deiconify()
    windows5.mainloop()


def checked():  # function for mark evaluation

    global c
    global v0
    global v1
    global v2
    global v3

    c = 0
    if v0.get() == 3:
        c += 1

    if v1.get() == 0:
        c += 1

    if v2.get() == 2:
        c += 1

    if v3.get() == 0:
        c += 1

    global total
    total = c


def string_val(): # function for details evaluation
    global nam
    global clas

    nam = N_Box.get() # .get() returns the value stored in the Entry
    clas = C_Box.get()

nam = ""
clas = ""


def main_Program(): # function for executing the main program
    global root
    global v0
    global v1
    global v2
    global v3
    global N_Box
    global C_Box
    global user_name
    global password
    global mycursor
    global mydb

    # getting user input for MySQL username and password
    user_name = str(input("Enter user name for MySql: "))
    password = str(input("Enter password for MySql: "))

    # establishing connection with the database
    mydb = SQL.connect(host="localhost", user=user_name, passwd=password)
    mycursor = mydb.cursor()

    if mydb.is_connected() == False:
        print("Can't establish connection")

    root = tkinter.Tk() # creating the root window

    v0 = tkinter.IntVar() # IntVar() sets a default value for a RadioButton (default = 0)
    v1 = tkinter.IntVar()
    v2 = tkinter.IntVar()
    v3 = tkinter.IntVar()


    root.title("Quiz Program")
    root.geometry("850x360")
    root.resizable(width=False, height=False)
    root.configure(background='#36abcb')

    root.rowconfigure(0, weight=10)
    root.columnconfigure(0, weight=10)
    root.rowconfigure(7, weight=5)
    root.columnconfigure(2, weight=10)
    root.rowconfigure(3, weight=5)
    root.rowconfigure(9, weight=5)

    # creating Labels and Buttons
    In_Label = tkinter.Label(root, text="Enter the following details and then click 'Submit': ",
                             font=("consolas", 15, "bold"), bg="#36abcb")
    In_Label.grid(row=0, column=1)

    N_Label = tkinter.Label(root, text="Name:", font=("consolas", 15, "bold"), bg="#36abcb")
    N_Label.grid(row=1, column=1)
    N_Box = tkinter.Entry(root)
    N_Box.grid(row=2, column=1)

    C_Label = tkinter.Label(root, text="Class:", font=("consolas", 15, "bold"), bg="#36abcb")
    C_Label.grid(row=4, column=1)
    C_Box = tkinter.Entry(root)
    C_Box.grid(row=5, column=1)

    btn2 = tkinter.Button(root, text="Enter", font=('consolas', 12, 'bold'), bg="#13759c", fg="white", command=string_val)
    btn2.grid(row=6, column=1)
    btn1 = tkinter.Button(root, text="Submit", font=('consolas', 12, 'bold'), bg="#13759c", fg="white", command=bnext)
    btn1.grid(row=8, column=1)


    root.mainloop()

main_Program()

