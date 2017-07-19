from Tkinter import *
import re


# Flag function
def getcheckbox(parent, name):
    var = BooleanVar(value=False)
    box = Checkbutton(parent, text=name, var=var)
    box.pack(side=LEFT)
    return box, var


class RegexTestGUI:
    def __init__(self, master):
        self.master = master
        master.title("RegexTest")

        # Input frame
        self.inputFrame = Frame(master)
        self.inputFrame.pack(side=TOP, fill=BOTH, expand=YES)

        # Input text
        self.inputText = Text(self.inputFrame, height=5, width=60)
        self.inputText.insert(END, "Insert test text")
        self.inputText.pack(side=LEFT, fill=BOTH, expand=YES)

        # Input scrollbar
        self.inputScroll = Scrollbar(self.inputFrame, command=self.inputText.yview)
        self.inputText.configure(yscrollcommand=self.inputScroll.set)
        self.inputScroll.pack(side=RIGHT, fill=Y)

        # Regex frame
        self.regexFrame = Frame(master)
        self.regexFrame.pack(fill=X)

        # Regex text
        self.regexText = Text(self.regexFrame, height=3, width=60)
        self.regexText.insert(END, "")
        self.regexText.pack(side=LEFT, fill=X, expand=YES)

        # Regex scrollbar
        self.regexScroll = Scrollbar(self.regexFrame, command=self.regexText.yview)
        self.regexText.configure(yscrollcommand=self.regexScroll.set)
        self.regexScroll.pack(side=RIGHT, fill=Y)

        # Flag frame
        self.regexFlagFrame = Frame(master)
        self.regexFlagFrame.pack(anchor=W)

        # Flags
        self.flagMultiline, self.flagMultilineVar = getcheckbox(self.regexFlagFrame, "Multiline")
        self.flagIgnoreCase, self.flagIgnoreCaseVar = getcheckbox(self.regexFlagFrame, "IgnoreCase")
        self.flagDotAll, self.flagDotAllVar = getcheckbox(self.regexFlagFrame, "DotAll")
        self.flagUnicode, self.flagUnicodeVar = getcheckbox(self.regexFlagFrame, "Unicode")

        # Output frame
        self.outputFrame = Frame(master)
        self.outputFrame.pack(fill=BOTH, expand=YES)

        # Output text
        self.outputText = Text(self.outputFrame, height=5, width=60)
        self.outputText.insert(END, "")
        self.outputText.pack(side=LEFT, fill=BOTH, expand=YES)
        self.outputText.bind("<Key>", lambda e: "break")

        # Output scrollbar
        self.outputScroll = Scrollbar(self.outputFrame, command=self.outputText.yview)
        self.outputText.configure(yscrollcommand=self.outputScroll.set)
        self.outputScroll.pack(side=RIGHT, fill=Y)

        # Group frame
        self.outputGroupFrame = Frame(master)
        self.outputGroupFrame.pack(anchor=W)

        # Group checkboxes
        self.groupCheckboxVar = []
        self.outputGroupCheckbox = []
        for i in range(9):
            self.groupCheckboxVar.append(BooleanVar(value=False))
            self.outputGroupCheckbox.append(Checkbutton(self.outputGroupFrame, text=i + 1, var=self.groupCheckboxVar[i], state=DISABLED))
            self.outputGroupCheckbox[i].pack(side=LEFT)

        # Button frame
        self.buttonFrame = Frame(master)
        self.buttonFrame.pack(side=BOTTOM)

        # Execute button
        self.executeButton = Button(self.buttonFrame, text="Execute", command=self.execute)
        self.executeButton.pack(side=LEFT)

        # Exit button
        self.exitButton = Button(self.buttonFrame, text="Close", command=master.quit)
        self.exitButton.pack(side=LEFT)

    def execute(self):

        input_text = self.inputText.get('1.0', 'end-1c')
        regex_text = self.regexText.get('1.0', 'end-1c')

        regex_flag = 0
        if self.flagMultilineVar.get() is True:
            regex_flag |= re.MULTILINE
        if self.flagIgnoreCaseVar.get() is True:
            regex_flag |= re.IGNORECASE
        if self.flagDotAllVar.get() is True:
            regex_flag |= re.DOTALL
        if self.flagUnicodeVar.get() is True:
            regex_flag |= re.UNICODE

        try:
            result = re.match(regex_text, input_text, regex_flag)
            self.outputText.delete(1.0, END)
            if result:
                self.outputText.insert(END, result.group(0))
                self.outputText.insert(END, "\n")

                for i in range(9):
                    try:
                        group_text = result.group(i+1)
                        self.outputGroupCheckbox[i].configure(state='normal')
                        if self.groupCheckboxVar[i].get():
                            self.outputText.insert(END, i+1)
                            self.outputText.insert(END, ": [")
                            self.outputText.insert(END, group_text)
                            self.outputText.insert(END, "]\n")
                    except IndexError:
                        self.outputGroupCheckbox[i].configure(state='disabled')
                        self.groupCheckboxVar[i].set(False)
            else:
                for i in range(9):
                    self.outputGroupCheckbox[i].configure(state='disabled')

        except Exception as error:
            self.outputText.delete(1.0, END)
            self.outputText.insert(END, 'Error: '+error.message)


root = Tk()
my_gui = RegexTestGUI(root)

root.update()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()
