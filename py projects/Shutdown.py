from tkinter import*
import os



#user define function
def shutdown():
    return os.system("shutdown /s /t 1")
def restart():
    return os.system("shutdown /r /t 1")

def logout():
    return os.system("shutdown -l")

def sleep():
    return os.system("Shutdown /r /t 10")

master=Tk()

#background set to gray
master.title("Shutdown Window")
master.configure(bg='grey')
master.geometry("720x500")

#button to submit operations
Button(master,text='Shutdown', font=("times new roman" , 15, "bold"),command=shutdown).grid(row=0)
Button(master,text='Restart', font=("times new roman" , 15, "bold"),command=restart).grid(row=1)
Button(master,text='logout', font=("times new roman" , 15, "bold") ,command=logout).grid(row=2)
Button(master,text='Sleep', font=("times new roman" , 15, "bold"),command=sleep).grid(row=3)
mainloop()
