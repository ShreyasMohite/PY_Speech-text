from tkinter import *
import pyjokes
import speech_recognition as sr
import threading
import tkinter.messagebox

class Jokes:
    def __init__(self,root):
        self.root=root
        self.root.title("Speech to Text")
        self.root.geometry("510x300")
        self.root.resizable('0','0')
        self.root.iconbitmap("logo179.ico")


        #=================================================

        def on_enter1(e):
            generatespeech['background']="black"
            generatespeech['foreground']="cyan"
  
        def on_leave1(e):
            generatespeech['background']="SystemButtonFace"
            generatespeech['foreground']="SystemButtonText"


        def on_enter2(e):
            clear['background']="black"
            clear['foreground']="cyan"
  
        def on_leave2(e):
            clear['background']="SystemButtonFace"
            clear['foreground']="SystemButtonText"

        
        def clear():
            Txt.delete('1.0',END)
            lab_speak.config(text="")


        def generate():
            try:

                r=sr.Recognizer()
                with sr.Microphone() as source:
                    lab_speak.config(text="Speak please")
                    audio=r.listen(source)
                Txt.insert("end",r.recognize_google(audio))
            except:
                tkinter.messagebox.showerror("Error","you did not speak any thing")

        def thread_speech():
            t=threading.Thread(target=generate)
            t.start()








        Mainframe=LabelFrame(self.root,text="Speech to text",font=("times new roman",14,'bold'),width=509,height=300,bg="#7777ff",fg="black")
        Mainframe.place(x=1,y=0)

        Txt=Text(Mainframe,font=('times new roman',12,'bold'),width=62,height=10,fg="cyan",bg="#3b3b3b",bd=3)
        Txt.place(x=1,y=0)

        generatespeech=Button(Mainframe,text="Speak",width=12,font=('times new roman',11,'bold'),bd=2,cursor="hand2",command=thread_speech)
        generatespeech.place(x=60,y=220)
        generatespeech.bind("<Enter>",on_enter1)
        generatespeech.bind("<Leave>",on_leave1)

        lab_speak=Label(Mainframe,text="",font=('times new roman',14),bg="#7777ff",fg="black")
        lab_speak.place(x=210,y=220)

        clear=Button(Mainframe,text="Clear",width=12,font=('times new roman',11,'bold'),bd=2,cursor="hand2",command=clear)
        clear.place(x=330,y=220)
        clear.bind("<Enter>",on_enter2)
        clear.bind("<Leave>",on_leave2)


    
        



if __name__ == "__main__":
    root=Tk()
    app=Jokes(root)
    root.mainloop()
