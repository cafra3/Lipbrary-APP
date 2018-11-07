from backend import Database
from tkinter import *

database=Database("book.db")

class Window(object):
    def __init__(self,window):
        window.wm_title("Library App")
        self.window = window

        #Title
        l1=Label(window,text="Title")
        l1.grid(row=0,column=0)

        self.title_val=StringVar()
        self.e1=Entry(window,textvariable=self.title_val)
        self.e1.grid(row=0,column=1)

        #Author
        l2=Label(window,text="Author")
        l2.grid(row=0,column=2)

        self.author_val=StringVar()
        self.e2=Entry(window,textvariable=self.author_val)
        self.e2.grid(row=0,column=3)

        #Year
        l3=Label(window,text="Year")
        l3.grid(row=1,column=0)

        self.year_val=StringVar()
        self.e3=Entry(window,textvariable=self.year_val)
        self.e3.grid(row=1,column=1)

        #ISBN
        l4=Label(window,text="ISBN")
        l4.grid(row=1,column=2)

        self.isbn_val=StringVar()
        self.e4=Entry(window,textvariable=self.isbn_val)
        self.e4.grid(row=1,column=3)

        #Buttons
        b1=Button(window,text="View all",width=12,command=self.view_command)
        b1.grid(row=2,column=3)

        b1=Button(window,text="Search Entry",width=12,command=self.search_command)
        b1.grid(row=3,column=3)

        b1=Button(window,text="Add entry",width=12,command=self.add_command)
        b1.grid(row=4,column=3)

        b1=Button(window,text="Update",width=12,command=self.update_command)
        b1.grid(row=5,column=3)

        b1=Button(window,text="Delete",width=12,command=self.delete_command)
        b1.grid(row=6,column=3)

        b1=Button(window,text="Close",width=12,command=window.destroy)
        b1.grid(row=7,column=3)

        # listbox group
        self.list=Listbox(window,height=6,width=35)
        self.list.grid(row=2,column=0,rowspan=6,columnspan=2)

        scroll =Scrollbar(window)
        scroll.grid(row=2,column=2,rowspan=6)

        self.list.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.list.yview)

        self.list.bind('<<ListboxSelect>>',self.get_selected_row)


    def get_selected_row(self,event):
        try:
            # global selected_tuple
            index=self.list.curselection()[0]
            # print(list)
            self.selected_tuple=self.list.get(index)
            # print(self.selected_tuple)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass




    def view_command(self):
        self.list.delete(0,END)
        for row in database.view():
            self.list.insert(END,row)

    def search_command(self):
        self.list.delete(0, END)
        for row in database.search(self.title_val.get(),self.author_val.get(),self.year_val.get(),self.isbn_val.get()):
            self.list.insert(END,row)

    def add_command(self):
        database.insert(self.title_val.get(),self.author_val.get(),self.year_val.get(),self.isbn_val.get())
        self.list.delete(0,END)
        self.list.insert(END,(self.title_val.get(),self.author_val.get(),self.year_val.get(),self.isbn_val.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0],self.title_val.get(),self.author_val.get(),self.year_val.get(),self.isbn_val.get())
        # print(self.selected_tuple[0],title_val.get(),author_val.get(),year_val.get(),isbn_val.get())


window=Tk()
Window(window)
window.mainloop()
