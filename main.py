from Tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Title")


        self.inputFrame=Frame(master)
        self.inputFrame.pack(side=TOP)

        self.inputText = Text(self.inputFrame, height=20, width=80)
        self.inputText.insert(END, "Insert test text")
        self.inputText.pack(side=LEFT)

        self.scroll = Scrollbar(self.inputFrame, command=self.inputText.yview)
        self.inputText.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack(side=TOP)

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack(side=BOTTOM)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side=BOTTOM)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()