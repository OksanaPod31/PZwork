# https://www.oreilly.com/library/view/html5-themissing/9781449312671/httpatomoreillycomsourceoreillyimages1731680.png

import tkinter
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton

root = Tk()
root.title("12.1")
lbl = Label(root, text="Zoo Keeper Application Form", font=("Arial Bold", 40))
lbl.grid(column=0, row=0)
lbl2 = Label(root, text="Please complete the form. Mandatory fields are marked with a*", font=("Silkscreen", 16))
lbl2.grid(column=0, row=1, sticky=NW)

frame_one = Frame(root, relief=tkinter.GROOVE, bd=3, padx=10, pady=5)
frame_two = Frame(root, relief=tkinter.GROOVE, bd=3, padx=10)
frame_three = Frame(root, relief=tkinter.GROOVE, bd=3, padx=10, pady=5)


lbl_one_1 = Label(master=frame_one, text="Contact Details", font=("Arial Bold", 17))
lbl_one_2 = Label(master=frame_one, text="Name*", font=("Arial Bold", 14))
lbl_one_3 = Label(master=frame_one, text="Telephone", font=("Arial Bold", 14))
lbl_one_4 = Label(master=frame_one, text="Email*", font=("Arial Bold", 14))

lbl_one_1.grid(column=0, row=0, sticky=NW)
lbl_one_2.grid(column=0, row=1, sticky=NW)
lbl_one_3.grid(column=0, row=2, sticky=NW)
lbl_one_4.grid(column=0, row=3, sticky=NW)

txt_one_1 = Entry(master=frame_one, width=53)
txt_one_2 = Entry(master=frame_one, width=53)
txt_one_3 = Entry(master=frame_one, width=53)

txt_one_1.grid(column=1, row=1)
txt_one_2.grid(column=1, row=2)
txt_one_3.grid(column=1, row=3)


lbl_two_1 = Label(master=frame_two, text="Personal Information", font=("Arial Bold", 17))
lbl_two_2 = Label(master=frame_two, text="*Age", font=("Arial Bold", 14))
lbl_two_3 = Label(master=frame_two, text="Gender", font=("Arial Bold", 14))
lbl_two_4 = Label(master=frame_two, text="When did you\n first know you\n"
                                         " wanted to be a\n zoo-keeper?", font=("Arial Bold", 14))

lbl_two_1.grid(column=0, row=0, sticky=NW)
lbl_two_2.grid(column=0, row=1, sticky=NW)
lbl_two_3.grid(column=0, row=2, sticky=NW)
lbl_two_4.grid(column=0, row=3, sticky=NW, pady=10)

txt_two_1 = Entry(master=frame_two, width=30)
scrtex = scrolledtext.ScrolledText(master=frame_two, width=30, height=10)

combo = Combobox(master=frame_two, width=30, height=1)
combo['values'] = ('Female', 'Male')
combo.current(0)

combo.grid(column=1, row=2)
txt_two_1.grid(column=1, row=1)
scrtex.grid(column=1, row=3)

lbl_three_1 = Label(master=frame_three, text="Pick Your Favorite Animals", font=("Arial Bold", 17))
lbl_three_1.grid(column=0, row=0, sticky=NW)

chk_state_1 = BooleanVar()
chk_state_1.set(False)
chk_state_2 = BooleanVar()
chk_state_2.set(False)
chk_state_3 = BooleanVar()
chk_state_3.set(False)
chk_state_4 = BooleanVar()
chk_state_4.set(False)
chk_state_5 = BooleanVar()
chk_state_5.set(False)
chk_state_6 = BooleanVar()
chk_state_6.set(False)
chk_state_7 = BooleanVar()
chk_state_7.set(False)
chk_state_8 = BooleanVar()
chk_state_8.set(False)

chb_1 = Checkbutton(master=frame_three, text="Zebra", var=chk_state_1)
chb_2 = Checkbutton(master=frame_three, text="Elephant", var=chk_state_2)
chb_3 = Checkbutton(master=frame_three, text="Cat", var=chk_state_3)
chb_4 = Checkbutton(master=frame_three, text="Wildebeest", var=chk_state_4)
chb_5 = Checkbutton(master=frame_three, text="Anaconda", var=chk_state_5)
chb_6 = Checkbutton(master=frame_three, text="Pigeon", var=chk_state_6)
chb_7 = Checkbutton(master=frame_three, text="Human", var=chk_state_7)
chb_8 = Checkbutton(master=frame_three, text="Crab", var=chk_state_8)

chb_1.grid(column=0, row=1, sticky=NW, padx=10, pady=7)
chb_3.grid(column=1, row=1, sticky=NW, padx=10, pady=7)
chb_5.grid(column=2, row=1, sticky=NW, padx=10, pady=7)
chb_7.grid(column=3, row=1, sticky=NW, padx=10, pady=7)
chb_2.grid(column=0, row=2, sticky=NW, padx=10, pady=7)
chb_4.grid(column=1, row=2, sticky=NW, padx=10, pady=7)
chb_6.grid(column=2, row=2, sticky=NW, padx=10, pady=7)
chb_8.grid(column=3, row=2, sticky=NW, padx=10, pady=7)

btn = Button(root, text='Submit Application', width=30, height=2)
btn.grid(column=0, row=5, sticky=NW)

frame_one.grid(column=0, row=2, sticky=NW)
frame_two.grid(column=0, row=3, sticky=NW)
frame_three.grid(column=0, row=4, sticky=NW)

root.mainloop()
