from tkinter import *

root = Tk()

root.geometry('500x500')
root.title("Multidimesinal Arrays")

label = Label(root)

array1d = ['Ali', 'Sam', 'Demarius']
print(array1d[1])
array2d = [['Ali', 'C'], ['Sam', 'B'], ['Demarius', 'A']]
print(array2d[1][1])
array3d = [[["Ali", "C", "Okay"], ['Sam', 'B', 'Good'], ['Demarius', "A", 'Excellant']]]
print(array3d[0][1][2])

def report():
    label['text'] = array3d[0][1][0] + "'s grade is " + array3d[0][1][1] + " and is a " + array3d[0][1][2] + " Student"
    
btn = Button(root, text = 'Show Report', command = report, relief = SUNKEN)

btn.place(relx = 0.5, rely=0.5, anchor = CENTER)
label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()


