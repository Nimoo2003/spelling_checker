from tkinter import*
from textblob import TextBlob

def check_spelling():
    word=spell_check.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs= Label(window, text="Correct is: ",font=("Arial",15,"bold"),bg="#f9e2e2",fg="black")
    cs.place(x=224,y=290)

    
    spell1.config(text=right)



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


spell_check = Entry(window,justify="center",width=30, font=("Arial",15,"bold"),bg="white", fg="black")
spell_check.pack(pady=150)
spell_check.focus()

button= Button(window, text="Check!!", font=("Arial",15,"bold"), bg="white", fg="black",command=check_spelling)
button.place(x=300,y=210)

spell1= Label(window,font=("Arial",15,"bold"),bg="#f9e2e2",fg="black")
spell1.place(x=350,y=290)

window.mainloop()

