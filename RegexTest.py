from Tkinter import *
import re

def get_tag_index(string, start, end):

    if string:
        if start < end:
            start_index = get_index(start, string)
            end_index = get_index(end, string)
        else:
            start_index = '1.0'
            end_index = '1.0'
    else:
        start_index = '0.0'
        end_index = '0.0'

    return start_index, end_index


def get_index(start, string):
    line_num = string.count('\n', 0, start)
    line_start = string.rfind('\n', 0, start)
    if line_start == -1:
        line_start = 0
    else:
        line_start += 1
    start_tag = str(line_num + 1) + '.' + str(start - line_start)
    return start_tag


def execute():

    input_text = inputText.get('1.0', 'end-1c')
    regex_text = regexText.get('1.0', 'end-1c')

    regex_flag = 0
    if flagMultilineVar.get() is True:
        regex_flag |= re.MULTILINE
    if flagIgnoreCaseVar.get() is True:
        regex_flag |= re.IGNORECASE
    if flagDotAllVar.get() is True:
        regex_flag |= re.DOTALL
    if flagUnicodeVar.get() is True:
        regex_flag |= re.UNICODE

    try:
        result = re.search(regex_text, input_text, regex_flag)
        outputText.delete(1.0, END)
        if result:
            outputText.insert(END, result.group(0))
            outputText.insert(END, "\n")

            for group_index in range(9):
                try:
                    group_text = result.group(group_index+1)
                    outputGroupCheckbox[group_index].configure(state='normal')
                    if groupCheckboxVar[group_index].get():
                        outputText.insert(END, group_index+1)
                        outputText.insert(END, ": [")
                        outputText.insert(END, group_text)
                        outputText.insert(END, "]\n")

                        # Colorize group match
                        start_index, end_index = get_tag_index(result.group(0), result.start(group_index + 1), result.end(group_index + 1))
                        outputText.tag_add('group1', start_index, end_index)
                        outputText.tag_config('group1', background='yellow', foreground='red')

                except IndexError:
                    outputGroupCheckbox[group_index].configure(state='disabled')
                    groupCheckboxVar[group_index].set(False)
        else:
            for group_index in range(9):
                outputGroupCheckbox[group_index].configure(state='disabled')

    except Exception as error:
        outputText.delete(1.0, END)
        outputText.insert(END, 'Error: '+error.message)


# Flag function
def getcheckbox(parent, name):
    var = BooleanVar(value=False)
    box = Checkbutton(parent, text=name, var=var)
    box.pack(side=LEFT)
    return box, var


def button1callback(_):
    execute()


if __name__ == '__main__':

    root = Tk()

    # Input frame
    inputFrame = Frame(root)
    inputFrame.pack(side=TOP, fill=BOTH, expand=YES)

    # Input text
    inputText = Text(inputFrame, height=5, width=60)
    inputText.insert(END, "Insert test text")
    inputText.pack(side=LEFT, fill=BOTH, expand=YES)

    # Input scrollbar
    inputScroll = Scrollbar(inputFrame, command=inputText.yview)
    inputText.configure(yscrollcommand=inputScroll.set)
    inputScroll.pack(side=RIGHT, fill=Y)

    # Regex frame
    regexFrame = Frame(root)
    regexFrame.pack(fill=X)

    # Regex text
    regexText = Text(regexFrame, height=3, width=60)
    regexText.insert(END, "")
    regexText.pack(side=LEFT, fill=X, expand=YES)

    # Regex scrollbar
    regexScroll = Scrollbar(regexFrame, command=regexText.yview)
    regexText.configure(yscrollcommand=regexScroll.set)
    regexScroll.pack(side=RIGHT, fill=Y)

    # Flag frame
    regexFlagFrame = Frame(root)
    regexFlagFrame.pack(anchor=W)

    # Flags
    flagMultiline, flagMultilineVar = getcheckbox(regexFlagFrame, "Multiline")
    flagIgnoreCase, flagIgnoreCaseVar = getcheckbox(regexFlagFrame, "IgnoreCase")
    flagDotAll, flagDotAllVar = getcheckbox(regexFlagFrame, "DotAll")
    flagUnicode, flagUnicodeVar = getcheckbox(regexFlagFrame, "Unicode")

    # Output frame
    outputFrame = Frame(root)
    outputFrame.pack(fill=BOTH, expand=YES)

    # Output text
    outputText = Text(outputFrame, height=5, width=60)
    outputText.insert(END, "")
    outputText.pack(side=LEFT, fill=BOTH, expand=YES)
    outputText.bind("<Key>", lambda e: "break")

    # Output scrollbar
    outputScroll = Scrollbar(outputFrame, command=outputText.yview)
    outputText.configure(yscrollcommand=outputScroll.set)
    outputScroll.pack(side=RIGHT, fill=Y)

    # Group frame
    outputGroupFrame = Frame(root)
    outputGroupFrame.pack(anchor=W)

    # Group checkboxes
    groupCheckboxVar = []
    outputGroupCheckbox = []
    for index in range(9):
        groupCheckboxVar.append(BooleanVar(value=False))
        outputGroupCheckbox.append(Checkbutton(outputGroupFrame,
                                               text=index + 1,
                                               var=groupCheckboxVar[index],
                                               state=DISABLED))

        outputGroupCheckbox[index].pack(side=LEFT)

    # Button frame
    buttonFrame = Frame(root)
    buttonFrame.pack(side=BOTTOM)

    # Execute button
    executeButton = Button(buttonFrame, text="Execute", command=execute)
    executeButton.pack(side=LEFT)

    # Exit button
    exitButton = Button(buttonFrame, text="Close", command=root.quit)
    exitButton.pack(side=LEFT)

    root.title("RegexTest")

    root.bind('<Button-1>', button1callback)
    root.bind('<ButtonRelease-1>', button1callback)
    root.bind('<Key>', button1callback)

    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())

    root.mainloop()

    # Tests
    # (\w+) (\w+) TEXT
    # (\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)
    #
'''
Insert test text asdadfsdfadsf asdfasdf sdfadsfasf
sadfasdfasdf asdf dfasdfas dfasd fasdf asdfas dfas
fsd ggasdgr ergasd fdg sefsg fg fgsg f gasdasdgsdg
'''
