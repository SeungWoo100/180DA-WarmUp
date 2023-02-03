# Import Required Library
from tkinter import *
import random
import sys
import cv2
 
# Create Object
root = Tk()
 
# Set geometry
root.geometry("600x600")
 
# Set title
root.title("Rock Paper Scissor Game")
 
# Computer Value
computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}
 
win_img = cv2.imread("win.png", 1)
lose_img = cv2.imread("lose.png", 1)
draw_img = cv2.imread("draw.png", 1)
# Reset The Game
 
 
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player              ")
    l3.config(text="Computer")

# Disable the Button
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
 
 
 
# If player selected rock
 
 
def isrock():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":

        cv2.imshow("Draw", draw_img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
    elif c_v == "Scissor":

        cv2.imshow("Win", win_img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
    else:

        cv2.imshow("Lose", lose_img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
    l1.config(text="Rock            ")
    l3.config(text=c_v)
    button_disable()

 
# If player selected paper
 
 
def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":

        cv2.imshow("Draw", draw_img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
    elif c_v == "Scissor":

        cv2.imshow("Lose", lose_img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
    else:
    
        cv2.imshow("Win", win_img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
        
    l1.config(text="Paper           ")
    l3.config(text=c_v)
    button_disable()
 
# If player selected scissor
 
 
def isscissor():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Rock":
        cv2.imshow("Lose", lose_img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
        
    elif c_v == "Scissor":
        cv2.imshow("Draw", draw_img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
      
    else:
        cv2.imshow("Win", win_img)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
 
    l1.config(text="Scissor         ")
    l3.config(text=c_v)
    button_disable()
 
 
# Add Labels, Frames and Button
Label(root,
      text="Rock Paper Scissor",
      font="normal 20 bold",
      fg="blue").pack(pady=20)
 
frame = Frame(root)
frame.pack()
 
l1 = Label(frame,
           text="Player              ",
           font=20)
 
l2 = Label(frame,
           text="VS             ",
           font="normal 10 bold")
 
l3 = Label(frame, text="Computer", font=20)
 
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()
 
frame1 = Frame(root)
frame1.pack()
 
b1 = Button(frame1, text="Rock",
            font=10, width=7,
            command=isrock)
 
b2 = Button(frame1, text="Paper ",
            font=10, width=7,
            command=ispaper)
 
b3 = Button(frame1, text="Scissor",
            font=10, width=7,
            command=isscissor)
 
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)
 
Button(root, text="Reset Game",
       font=10, fg="red",
       bg="black", command=reset_game).pack(pady=20)
 
# Execute Tkinter
root.mainloop()
