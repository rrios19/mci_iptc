from tkinter import *
import json

def ardn_led():
    print('Hola')

def write_json():
    param = {"a":50, "b":30}
    str_json = json.dumps(param,indent=2)
    FH = open("data.json","w")
    FH.write(str_json)
    FH.close()

def exit_app():
    exit


app = Tk()
app.title('GUI IPTC')
#app.configure(bg="#ACCEC0",width=1280,height=720)
app.configure(bg="#ACCEC0",bd=20)
app.geometry("270x150")


button1 = Button(app,text='Ard',fg='black',bg='red',command=lambda:ardn_led(),height=2,width=8)
button1.grid(row=0,column=0)

button2 = Button(app,text='Ard',fg="black",bg="red",command=lambda:write_json(),height=2,width=8)
button2.grid(row=0,column=2)

button3 = Button(app,text='Ard',fg='black',bg='red',command=lambda:ardn_led(),height=2,width=8)
button3.grid(row=0,column=3)

button4 = Button(app,text='Ard',fg='black',bg='red',command=lambda:exit_app(),height=2,width=8)
button4.grid(row=2,column=2)



app.mainloop()

