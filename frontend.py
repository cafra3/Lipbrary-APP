import backend
from tkinter import *

window=Tk()

window.wm_title("Library App")

def get_selected_row(event):
    try:
        global selected_tuple
        index=list.curselection()[0]
        # print(list)
        selected_tuple=list.get(index)
        # print(selected_tuple)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass




def view_command():
    list.delete(0,END)
    for row in backend.view():
        list.insert(END,row)

def search_command():
    list.delete(0, END)
    for row in backend.search(title_val.get(),author_val.get(),year_val.get(),isbn_val.get()):
        list.insert(END,row)

def add_command():
    backend.insert(title_val.get(),author_val.get(),year_val.get(),isbn_val.get())
    list.delete(0,END)
    list.insert(END,(title_val.get(),author_val.get(),year_val.get(),isbn_val.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_val.get(),author_val.get(),year_val.get(),isbn_val.get())
    # print(selected_tuple[0],title_val.get(),author_val.get(),year_val.get(),isbn_val.get())

#Title
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

title_val=StringVar()
e1=Entry(window,textvariable=title_val)
e1.grid(row=0,column=1)

#Author
l2=Label(window,text="Author")
l2.grid(row=0,column=2)

author_val=StringVar()
e2=Entry(window,textvariable=author_val)
e2.grid(row=0,column=3)

#Year
l3=Label(window,text="Year")
l3.grid(row=1,column=0)

year_val=StringVar()
e3=Entry(window,textvariable=year_val)
e3.grid(row=1,column=1)

#ISBN
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

isbn_val=StringVar()
e4=Entry(window,textvariable=isbn_val)
e4.grid(row=1,column=3)

#Buttons
b1=Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b1=Button(window,text="Search Entry",width=12,command=search_command)
b1.grid(row=3,column=3)

b1=Button(window,text="Add entry",width=12,command=add_command)
b1.grid(row=4,column=3)

b1=Button(window,text="Update",width=12,command=update_command)
b1.grid(row=5,column=3)

b1=Button(window,text="Delete",width=12,command=delete_command)
b1.grid(row=6,column=3)

b1=Button(window,text="Close",width=12,command=window.destroy)
b1.grid(row=7,column=3)

# listbox group
list=Listbox(window,height=6,width=35)
list.grid(row=2,column=0,rowspan=6,columnspan=2)

scroll =Scrollbar(window)
scroll.grid(row=2,column=2,rowspan=6)

list.configure(yscrollcommand=scroll.set)
scroll.configure(command=list.yview)

list.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()
