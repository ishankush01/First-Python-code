#It's a small fun game which i had made in my first year for college.
#it's my first code of programming.

#install the tkinter library

from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry("400x250")
root.title( "Your future")
def d_1():
    messagebox.showinfo("About love","Love is the 7th sence of human that destroys all the six senses and make the person non-sense \n See more")
    messagebox.showinfo("See More about Love","batau abhi }:-)")
b1=Button(root, text = "About love", command = d_1)
def d_2():
    messagebox.showinfo("About your study.","life is a race... if you don't run fast... you will be like a broken undaa.")
    messagebox.showinfo("sry","tumhri study ke bare me itna hi kuch or try kro")
b2=Button(root, text = "About your study.", command = d_2)
def d_3():
    messagebox.showinfo("About your future","baba ranchorddas kahete...bachcha kabil bano,kabil...kamyabi toh saali jhak maarke peeche bhagegi")
    messagebox.showinfo("3 ideat ke raju ban gye","jaan liya apna future aagaya maja hahahaha ")
    messagebox.showinfo("aree","So finally you got time to run this code.")
    messagebox.showinfo("ruk abhi or hai ","chal ab massege krke bata code kesa tha.")
    messagebox.showinfo("last","chal chal ab kuch nhi hai katam code")
    messagebox.showinfo("abhi kese","Aree abhi kese")
    messagebox.showinfo("last","ab message krke batao bhi kesa laga mera code?")
b3=Button(root, text = "About your future", command = d_3)
def d_4():
    messagebox.showinfo("No","iss box me kuch nhi milna.")
b4=Button(root, text = "NO", command =d_4)
l = Label(text = "\nHii, I am Ishan here!\n \n What do you want to know from me:\n To know - Click on anyone option\n If not Interested - click on the 'No' button and getout\n \n")
l.pack()
b2.pack()
b1.pack()
b3.pack()
b4.pack()
root.mainloop()
