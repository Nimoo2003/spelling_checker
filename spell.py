from tkinter import*
from textblob import TextBlob

def check_spelling():
    a=TextBlob(spell_check.get())
    spell= Label(window, text="Correct is: ",font=("Arial",15,"bold"),bg="#f9e2e2",fg="black").place(x=224,y=290)

    correct_text= Label(window,text=str(a.correct()),font=("Arial",15,"bold"),bg="#f9e2e2",fg="black").place(x=350,y=290)
   



window = Tk()
window.title("The spell check")
window.geometry("700x400")
img= PhotoImage(file= 'projects/back.jpg', master=window)
img_label= Label(window, image=img)
img_label.place(x=0,y=0)

frame= Frame(window,height=60,width=500,bg='#ddbea9')
frame.place(x=100,y=50)

heading= Label(frame, text="Spelling checker",bg="#ddbea9",fg="white",font=("Arial",30,"bold"))
heading.place(x=100,y=5)

frame1= Frame(window,height=40,width=200,bg='#ddbea9')
frame1.place(x=240,y=150)


spell_check = Entry(frame1, font=("Arial",15,"bold"),bg="white", fg="black")
spell_check.pack()

button= Button(window, text="Check!!", font=("Arial",15,"bold"), bg="white", fg="black",command=check_spelling).place(x=300,y=210)


window.mainloop()
