from Tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Title")

        # Input frame
        self.inputFrame=Frame(master)
        self.inputFrame.pack(side=TOP)

        self.inputText = Text(self.inputFrame, height=20, width=80)
        self.inputText.insert(END, "Insert test text")
        self.inputText.pack(side=LEFT)

        self.scroll = Scrollbar(self.inputFrame, command=self.inputText.yview)
        self.inputText.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)

        # Regex frame
        self.regexFrame=Frame(master)
        self.regexFrame.pack()

        # Regex flag frame
        self.regexFlagFrame=Frame(self.regexFrame)
        self.regexFlagFrame.pack()

        # Output frame
        self.outputFrame=Frame(master)
        self.outputFrame.pack()

        # Group frame
        self.outputGroupFrame=Frame(self.outputFrame)
        self.outputGroupFrame.pack()

        # Button frame
        self.buttonFrame=Frame(master)
        self.buttonFrame.pack()



        # self.xlabel = []
        # for i in range(5):
        #     self.xlabel.append(Label(self.inputFrame, text=str(i)))
        #     self.xlabel[i].pack()
        #
        # self.label = Label(master, text="This is our first GUI!")
        # self.label.pack(side=TOP)



        self.greet_button = Button(self.buttonFrame, text="Greet", command=self.greet)
        self.greet_button.pack(side=LEFT)
        self.greet_button.pack()

        self.close_button = Button(self.buttonFrame, text="Close", command=master.quit)
        self.close_button.pack(side=RIGHT)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()