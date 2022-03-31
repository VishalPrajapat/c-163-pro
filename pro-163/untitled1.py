from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("fever-report")
root.geometry("400x400")
root.configure(bg="pink")


question1_Radio=StringVar(value="0")
question_1=Label(root,text="Do You have headache & sourethroat")
question_1.pack()
question1_r1=Radiobutton(root,text="Yes",var=question_1,value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root,text="No",var=question_1,value="no")
question1_r2.pack()

question2_Radio=StringVar(value="0")
question_2=Label(root,text="Is Your body Tempreture Is high")
question_2.pack()
question2_r1=Radiobutton(root,text="Yes",var=question_2,value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root,text="No",var=question_2,value="no")
question2_r2.pack()

question3_Radio=StringVar(value="0")
question_3=Label(root,text="Are There any symptoms of eye redness")
question_3.pack()
question3_r1=Radiobutton(root,text="Yes",var=question_3,value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root,text="No",var=question_3,value="no")
question3_r2.pack()
def fever_score():
    score=0
    if question1_Radio.get()=="yes":
       score=score+20 
       print(score)
    if question2_Radio.get()=="yes":
       score=score+20 
       print(score)   
    if question3_Radio.get()=="yes":
       score=score+20 
       print(score)   
    if score<=20:
        message.showinfo("Report","No Need To Visit the doctor")
    elif score>20 and score <=40:
        message.showinfo("Report","You might perhaps Hve to Visit the doctor")
    else:
        message.showinfo("Report","I Strongly Advice you to Visit the doctor")    
        
btn=Button(root,text="Check Suggestion",command=fever_score)
btn.pack()


root.mainloop()
