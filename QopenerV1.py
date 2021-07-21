from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import webbrowser as op
import datetime
import time
import sys

root = Tk()
root.title("Zoom Classes")
root.geometry("630x620")
root.config(bg="#262626")
#
bgcol = "#262626"
fgcol = "white"
bcol = "#7a0099"
bOnHover = "#a100c9"
lcol = "#a3a3a3"
state = "mini"


dayslist = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

Monday = {
    "Computer": "Your timing here(change in code)",
    "English": "Your timing here(change in code)",
    "Maths": "Your timing here(change in code)",
    "Physics": "Your timing here(change in code)",
    "Chemistry": "Your timing here(change in code)",
    "Biology": "Your timing here(change in code)",
}

Tuesday = {
    "Computer": "Your timing here(change in code)",
    "Chemistry": "Your timing here(change in code)",
    "Maths": "Your timing here(change in code)",
    "English": "Your timing here(change in code)",
    "Physics": "Your timing here(change in code)",
    "Biology": "Your timing here(change in code)",
}

Wednesday = {
    "Computer": "Your timing here(change in code)",
    "Chemistry": "Your timing here(change in code)",
    "Maths": "Your timing here(change in code)",
    "Physics": "Your timing here(change in code)",
    "English": "Your timing here(change in code)",
    "Biology": "Your timing here(change in code)",
}

Thursday = {
    "Computer": "Your timing here(change in code)",
    "Chemistry": "Your timing here(change in code)",
    "Maths": "Your timing here(change in code)",
    "Physics": "Your timing here(change in code)",
    "English": "Your timing here(change in code)",
    "Biology": "Your timing here(change in code)",
}

Friday = {
    "Computer": "Your timing here(change in code)",
    "Chemistry": "Your timing here(change in code)",
    "Maths": "Your timing here(change in code)",
    "Physics": "Your timing here(change in code)",
    "English": "Your timing here(change in code)",
    "Biology": "Your timing here(change in code)",
}

Saturday = {
    "Computer": "Your timing here(change in code)",
    "Chemistry": "Your timing here(change in code)",
    "Maths": "Your timing here(change in code)",
    "Physics": "Your timing here(change in code)",
    "English": "12:30 PM",
    "Biology": "Your timing here(change in code)",
}

userp = [
    "Computer Science",
    "https://github.com/sabzdotpy/QopenerV1.0",
    "Maths",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Physics",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Chemistry",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "English",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "Biology",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
]
#


def createNewFile():
    with open("userprefs.txt", "a") as newfile:
        for line in userp:
            newfile.write(line + "\n")


try:
    linkspath = open("userprefs.txt")
    link = linkspath.readlines()
except IOError:
    createNewFile()
    tkinter.messagebox.showinfo(
        "Error",
        "'userprefs.txt' appears to be missing. A new file has been created with the default values. Please update the links the next time you open the application.",
    )
    sys.exit()


try:
    cs = link[1]
    ma = link[3]
    ph = link[5]
    ch = link[7]
    en = link[9]
    bi = link[11]
    s1 = link[0].strip("\n")
    s2 = link[2].strip("\n")
    s3 = link[4].strip("\n")
    s4 = link[6].strip("\n")
    s5 = link[8].strip("\n")
    s6 = link[10].strip("\n")

except IndexError:
    tkinter.messagebox.showinfo(
        "Error",
        "'userprefs.txt' is damaged. Some lines are missing. Please download the program again.",
    )
    sys.exit()


sub_options = [s1, s2, s3, s4, s5, s6]  # <----------        for combobox
#
date = datetime.datetime.now()
date = date.strftime("%d %b %Y")
day = datetime.date.today()
day = day.weekday()
day = dayslist[day]
datenday = day + " " + date

# Functions here
def comp():
    op.open(cs)


def math():
    op.open(ma)


def phy():
    op.open(ph)


def chem():
    op.open(ch)


def eng():
    op.open(en)


def bio():
    op.open(bi)


def tick():
    global time
    time = datetime.datetime.now()
    h = time.strftime("%H")
    h = int(h)
    if h > 12:
        h -= 12
    m = time.strftime("%M")
    s = time.strftime("%S")
    p = time.strftime("%p")
    time = (h, ":", m, ":", s, p)
    timelabel.config(text=time)
    timelabel.after(500, tick)


def changeOnHover(button, colorOnHover, colorOnLeave):
    # Hover color
    button.bind("<Enter>", func=lambda e: button.config(bg=colorOnHover))

    # Leave color
    button.bind("<Leave>", func=lambda e: button.config(bg=colorOnLeave))


def authorHover(label):
    label.bind("<Enter>", func=lambda e: label.config(fg="#575757"))

    label.bind("<Leave>", func=lambda e: label.config(fg="#383838"))


subjects = ["Computer", "Maths", "English", "Physics", "Chemistry", "Biology"]


def subId():
    todaysub = {}
    if day == "Monday":
        for sub in subjects:
            timing = Monday.get(sub)
            msg = "Today at " + timing
            todaysub[sub] = msg

    if day == "Tuesday":
        for sub in subjects:
            timing = Tuesday.get(sub)
            msg = "Today at " + timing
            todaysub[sub] = msg

    if day == "Wednesday":
        for sub in subjects:
            timing = Wednesday.get(sub)
            msg = "Today at " + timing
            todaysub[sub] = msg

    if day == "Thursday":
        for sub in subjects:
            timing = Thursday.get(sub)
            msg = "Today at " + timing
            todaysub[sub] = msg
    if day == "Friday":
        for sub in subjects:
            timing = Friday.get(sub)
            msg = "Today at " + timing
            todaysub[sub] = msg
    if day == "Saturday":
        for sub in subjects:
            timing = Saturday.get(sub)
            msg = "Today at " + timing
            todaysub[sub] = msg
    if day == "Sunday":
        for sub in subjects:
            msg = "Today is a holiday"
            todaysub[sub] = msg
    csLabel.config(text=todaysub.get("Computer"))
    maLabel.config(text=todaysub.get("Maths"))
    phLabel.config(text=todaysub.get("Physics"))
    enLabel.config(text=todaysub.get("English"))
    chLabel.config(text=todaysub.get("Chemistry"))
    bioLabel.config(text=todaysub.get("Biology"))


def hide():
    csLabel.config(fg=bgcol)
    phLabel.config(fg=bgcol)
    maLabel.config(fg=bgcol)
    chLabel.config(fg=bgcol)
    enLabel.config(fg=bgcol)
    bioLabel.config(fg=bgcol)


def show():
    csLabel.config(fg=lcol)
    phLabel.config(fg=lcol)
    maLabel.config(fg=lcol)
    chLabel.config(fg=lcol)
    enLabel.config(fg=lcol)
    bioLabel.config(fg=lcol)


def gettext():
    ent.get()
    print(ent)


t = 0


def easterEgg():
    global t
    emsg = ["Made by Sabz", "instagram.com/incrediblesabari", "©Sabari", "something"]
    if t >= 3:
        t = 0
        eee = emsg[t]
    else:
        eee = emsg[t]
        t += 1
    author.config(text=eee, cursor="hand1")
    author.after(3000, easterEgg)


def extra():
    global state
    z = 10
    if state == "mini":
        root.geometry("630x700")
        extra.config(text="▽")
        state = "max"
    elif state == "max":
        root.geometry("630x620")
        extra.config(text="▷")
        state = "mini"


def subchanged(self):
    print(drop.get())
    if drop.get() == s5:
        ent.delete(0, "end")
        ent.insert(END, en)
    elif drop.get() == s2:
        ent.delete(0, "end")
        ent.insert(END, ma)
    elif drop.get() == s1:
        ent.delete(0, "end")
        ent.insert(END, cs)
    elif drop.get() == s4:
        ent.delete(0, "end")
        ent.insert(END, ch)
    elif drop.get() == s6:
        ent.delete(0, "end")
        ent.insert(END, bi)
    elif drop.get() == s3:
        ent.delete(0, "end")
        ent.insert(END, ph)


def updatelink():
    selectedsub = drop.get()
    entered = textentered.get()
    if selectedsub == s1:
        print(entered)
        insertline = 1
    elif selectedsub == s2:
        insertline = 3
    elif selectedsub == s3:
        insertline = 5
    elif selectedsub == s4:
        insertline = 7
    elif selectedsub == s5:
        insertline = 9
    elif selectedsub == s6:
        insertline = 11
    try:
        with open("userprefs.txt", "r") as file:
            # read a list of lines into data
            data = file.readlines()

        # now change the 2nd line, note that you have to add a newline
        data[insertline] = entered + "\n"

        # and write everything back
        with open("userprefs.txt", "w") as file:
            file.writelines(data)
        updateinfo.config(fg="white")
    except UnboundLocalError:
        pass


def open_url(url):
    op.open(url)


url = ""

author = Label(root, text="Made by Sabz", bg=bgcol, fg="#404040", font=("Lato", 10))
author.place(x=280, y=5)
easterEgg()
authorHover(author)
author.bind(
    "<Button-1>",
    lambda e, url=url: open_url("https://github.com/sabzdotpy/QopenerV1.0"),
)

datendaylabel = Label(root, text=datenday, bg=bgcol, fg=fgcol, font=("Dense", 16))
datendaylabel.place(x=10, y=30)

timelabel = Label(root, bg=bgcol, fg=fgcol, font=("Dense", 16))
timelabel.place(x=480, y=30)
tick()
### 								--------------------------------------------------------
csBtn = Button(
    root,
    text=s1,
    bg=bcol,
    fg=fgcol,
    activebackground=bOnHover,
    height=2,
    width=20,
    cursor="hand2",
    command=comp,
)
csBtn.place(x=250, y=100)
changeOnHover(csBtn, bOnHover, bcol)

csLabel = Label(root, text="Today at", bg=bgcol, fg=bgcol)
csLabel.place(x=155, y=142)
### 								--------------------------------------------------------
maBtn = Button(
    root,
    text=s2,
    bg=bcol,
    fg=fgcol,
    activebackground=bOnHover,
    height=2,
    width=20,
    cursor="hand2",
    command=math,
)
maBtn.place(x=250, y=180)
changeOnHover(maBtn, bOnHover, bcol)

maLabel = Label(root, text="Today at", bg=bgcol, fg=bgcol)
maLabel.place(x=275, y=222)
### 								--------------------------------------------------------
phBtn = Button(
    root,
    text=s3,
    bg=bcol,
    fg=fgcol,
    activebackground=bOnHover,
    height=2,
    width=20,
    cursor="hand2",
    command=phy,
)
phBtn.place(x=250, y=260)
changeOnHover(phBtn, bOnHover, bcol)

phLabel = Label(root, text="Today at", bg=bgcol, fg=bgcol)
phLabel.place(x=275, y=302)

### 								--------------------------------------------------------
enBtn = Button(
    root,
    text=s4,
    bg=bcol,
    fg=fgcol,
    activebackground=bOnHover,
    height=2,
    width=20,
    cursor="hand2",
    command=eng,
)
enBtn.place(x=250, y=340)
changeOnHover(enBtn, bOnHover, bcol)

enLabel = Label(root, text="Today at", bg=bgcol, fg=bgcol)
enLabel.place(x=275, y=382)

### 								--------------------------------------------------------
chBtn = Button(
    root,
    text=s5,
    bg=bcol,
    fg=fgcol,
    activebackground=bOnHover,
    height=2,
    width=20,
    cursor="hand2",
    command=chem,
)
chBtn.place(x=250, y=420)
changeOnHover(chBtn, bOnHover, bcol)

chLabel = Label(root, text="Today at", bg=bgcol, fg=bgcol)
chLabel.place(x=275, y=462)

### 								--------------------------------------------------------
bioBtn = Button(
    root,
    text=s6,
    bg=bcol,
    fg=fgcol,
    activebackground=bOnHover,
    height=2,
    width=20,
    cursor="hand2",
    command=bio,
)
bioBtn.place(x=250, y=500)
changeOnHover(bioBtn, bOnHover, bcol)

bioLabel = Label(root, text="Today at", bg=bgcol, fg=bgcol)
bioLabel.place(x=275, y=542)
subId()

#
timeshow = IntVar()
timeshow.set(1)
hidetime = Radiobutton(
    root,
    text="Hide Timetable",
    variable=timeshow,
    bg=bgcol,
    fg=fgcol,
    value=0,
    command=hide,
)
hidetime.place(x=220, y=570)
showtime = Radiobutton(
    root,
    text="Show Timetable",
    variable=timeshow,
    bg=bgcol,
    fg=fgcol,
    value=1,
    command=show,
)
showtime.place(x=340, y=570)

extra = Button(
    root, text="▷", fg=fgcol, bg=bgcol, bd=0, activebackground=bgcol, command=extra
)
extra.place(x=30, y=590)


clicked = StringVar()
textentered = StringVar()

drop = ttk.Combobox(root, value=sub_options, height=50, state="readonly")
drop.bind("<<ComboboxSelected>>", subchanged)
drop.place(x=10, y=650)

ent = Entry(root, textvariable=textentered, width=60, bg="#6e6c66", fg="white")
ent.place(x=170, y=650)

update = Button(root, text="Update Link", command=updatelink, bg="#5e5063", fg="white")
update.place(x=550, y=646)

updateinfo = Label(
    root,
    text="Link updated. Please restart the application to see changes.",
    fg=bgcol,
    bg=bgcol,
)
updateinfo.place(x=180, y=675)


try:
    root.iconbitmap("icon.ico")
except:
    pass

root.resizable(width=False, height=False)
root.mainloop()

# Program END.
