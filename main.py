from Tkinter import *
import re


class RegexTestGUI:
    def __init__(self, master):
        self.master = master
        master.title("RegexTest")

        # Input frame
        self.inputFrame = Frame(master)
        self.inputFrame.pack(side=TOP)

        # Input text
        self.inputText = Text(self.inputFrame, height=10, width=80)
        self.inputText.insert(END, "Insert test text")
        self.inputText.pack(side=LEFT)

        # Input scrollbar
        self.inputScroll = Scrollbar(self.inputFrame, command=self.inputText.yview)
        self.inputText.configure(yscrollcommand=self.inputScroll.set)
        self.inputScroll.pack(side=RIGHT, fill=Y)

        # Regex frame
        self.regexFrame = Frame(master)
        self.regexFrame.pack()

        # Regex text
        self.regexText = Text(self.regexFrame, height=3, width=80)
        self.regexText.insert(END, "")
        self.regexText.pack(side=LEFT)

        # Regex scrollbar
        self.regexScroll = Scrollbar(self.regexFrame, command=self.regexText.yview)
        self.regexText.configure(yscrollcommand=self.regexScroll.set)
        self.regexScroll.pack(side=RIGHT, fill=Y)

        # Flag frame
        self.regexFlagFrame = Frame(master)
        self.regexFlagFrame.pack()

        # Flag multiline
        self.flagMultilineVar = BooleanVar(value=False)
        self.flagMultiline = Checkbutton(self.regexFlagFrame, text="Multiline", var=self.flagMultilineVar)
        self.flagMultiline.pack(side=RIGHT)

        # Flag ignorecase
        self.flagIgnoreCaseVar = BooleanVar(value=False)
        self.flagIgnoreCase = Checkbutton(self.regexFlagFrame, text="IgnoreCase", var=self.flagIgnoreCaseVar)
        self.flagIgnoreCase.pack(side=RIGHT)

        # Flag dotall
        self.flagDotAllVar = BooleanVar(value=False)
        self.flagDotAll = Checkbutton(self.regexFlagFrame, text="DotAll", var=self.flagDotAllVar)
        self.flagDotAll.pack(side=RIGHT)

        # Output frame
        self.outputFrame = Frame(master)
        self.outputFrame.pack()

        # Output text
        self.outputText = Text(self.outputFrame, height=10, width=80)
        self.outputText.insert(END, "")
        self.outputText.pack(side=LEFT)

        # Output scrollbar
        self.outputScroll = Scrollbar(self.outputFrame, command=self.outputText.yview)
        self.outputText.configure(yscrollcommand=self.outputScroll.set)
        self.outputScroll.pack(side=RIGHT, fill=Y)

        # Group frame
        self.outputGroupFrame = Frame(master)

        # Group checkboxes
        self.groupButton = []
        self.outputGroupButton = []
        for i in range(9):
            self.groupButton.append(BooleanVar(value=False))
            self.outputGroupButton.append(Checkbutton(self.outputGroupFrame, text=i+1, var=self.groupButton[i]))
            self.outputGroupButton[i].pack(side=LEFT)
            self.outputGroupFrame.pack()

        # Button frame
        self.buttonFrame = Frame(master)
        self.buttonFrame.pack()

        # Execute frame
        self.executeButton = Button(self.buttonFrame, text="Execute", command=self.execute)
        self.executeButton.pack(side=LEFT)
        self.executeButton.pack()

        # Exit frame
        self.exitButton = Button(self.buttonFrame, text="Close", command=master.quit)
        self.exitButton.pack(side=RIGHT)
        self.exitButton.pack()

    def execute(self):
        print("Executing!")

        print "Input is [", self.inputText.get('1.0', 'end-1c'), "]"
        input_text = self.inputText.get('1.0', 'end-1c')

        print "Regex is [", self.regexText.get('1.0', 'end-1c'), "]"
        regex_text = self.regexText.get('1.0', 'end-1c')

        print "Output is [", self.outputText.get('1.0', 'end-1c'), "]"

        print "Multi is ", self.flagMultilineVar.get()
        print "IgnoreCase is ", self.flagIgnoreCaseVar.get()
        print "DotAll is ", self.flagDotAllVar.get()
        regex_flag = 0
        if self.flagMultilineVar.get() is True:
            regex_flag |= re.MULTILINE
        if self.flagIgnoreCaseVar.get() is True:
            regex_flag |= re.IGNORECASE
        if self.flagDotAllVar.get() is True:
            regex_flag |= re.DOTALL

        result = re.match(regex_text, input_text, regex_flag)
        if result:
            print "Match!"
            self.outputText.delete(1.0, END)
            self.outputText.insert(END, result.group(0))
            self.outputText.insert(END, "\n")

            for i in range(9):
                print "Group ", i + 1, " is ", self.groupButton[i].get()
                if self.groupButton[i].get():
                    self.outputText.insert(END, i+1)
                    self.outputText.insert(END, ": [")
                    self.outputText.insert(END, result.group(i+1))
                    self.outputText.insert(END, "]\n")


root = Tk()
my_gui = RegexTestGUI(root)
root.mainloop()
