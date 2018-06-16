from tkinter import Tk, Label, Button, Entry, Text, END, INSERT, messagebox
from tkinter.scrolledtext import ScrolledText 
from Class_Encryptor import Encryptor
from tkinter.messagebox import showinfo
class GUI(Encryptor):
    __encrpytType = " "
    def pushString(self, typeEn):
        print(typeEn)
        x=super().__init__(
            's', 
            typeEn,
            self.dataInput.get(index1=1.0, index2=END
            ))
        self.dataInput.delete('1.0', END)
        self.dataInput.insert(INSERT, self.standardInput())
    def __init__(self):
        self.root = Tk()
        self.text = Label(
            self.root,
            text = "Enter text: "
        )
        self.dataInput = ScrolledText(self.root)
        #self.temp = self.dataInput.get(index1=1.0, index2=END)
        self.execButton = Button(
            self.root,
            text = "Encrypt",
            command = lambda: self.pushString("En")
            #background = "green"
        )
        self.execButton1 = Button(
            self.root,
            text = "Decrypt",
            command = lambda: self.pushString("De")
            #background = "green"
        )
        self.text.grid(
            row = 0,
            column = 0,
            pady = 10,
            padx = 10
        )
        self.dataInput.grid(
            row = 1,
            column = 1,
            columnspan = 10,
            pady = 10,
            padx = 10
        )
        self.execButton.grid(
            row =3,
            column = 8,
            pady = 10,
            padx = 10
        )
        self.execButton1.grid(
            row =3,
            column = 9,
            pady = 10,
            padx = 10
        )
        self.root.mainloop()
     
#label = tkinter.Label(master = top, text = "Hello World") 
#label.grid(row=1, column = 2, columnspan = 1)
#label1 = tkinter.Label(master = top, text = "ZZZZZZZZZ") 
#label1.grid(row=2, column = 7, columnspan = 10)
#def test():
#    print("PEOP")
#top.config(bg = "black")
#button = tkinter.Button( self.root , text = "Click here", command = test )
#button.pack()
test = GUI()
