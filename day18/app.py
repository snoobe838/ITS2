import tkinter as ttk
from tkinter import font
app = ttk.Tk()
app.title('Attendence System')
app.geometry('400x400')
font_=font.Font(size=15)

ttk.Label(app, 
          text='Face Recognition based Attendance System',
          font=font_
          ).pack()






def register():
    app.destroy()
    
    with open('opr','w') as f:
        f.write('register')

    import login_admin
    



def attendance():
    app.destroy()
    import attendance
    attendance.attendance()

def clear_data():
    app.destroy()
    
    with open('opr','w') as f:
        f.write('clear')

    import login_admin

















ttk.Button(
    app, text = 'Register', command=register, font=font_,
    height = 1, width=15, bg='dark blue'
    ).pack(expand=True)

ttk.Button(
    app, text = 'Attendance', command=attendance, font=font_,
    height = 1, width=15, bg='dark blue'
    ).pack(expand=True)

ttk.Button(
    app, text = 'Clear Data', command=clear_data, font=font_,
    height = 1, width=15, bg='dark blue'
    ).pack(expand=True)



app.mainloop()