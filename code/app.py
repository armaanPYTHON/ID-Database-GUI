from tkinter import *
import tkinter.ttk as ttk
from tkinter import filedialog
import functions as fs
from tkinter import messagebox


def main():
    
    bgcolor = '#1262a3'
    tc = '#212120'
    root = Tk()
    root.title('ID Database')
    root.config(bg=bgcolor)
    
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    
    
    lbdesign = {
        'bd':0,
        'bg':tc,
        'fg':'white',
        'font':('Arial', 11),
        'activestyle':'none',
        'selectforeground':'black',
        'selectbackground':'grey'
    }
    
    btndesign = {
        'bd':0,
        #'compound':'left',
        'fg':'white',
        'bg':tc
    } 
    
    entrydesign = {
        'bd':0,
        'width':'30',
        'font':('Arial',12)
    } 
    
    labeldesign = {
        'bg':bgcolor,
        'font':('Arial', 12),
        'fg':'white'
    }
    
    Namestr = 'Name:                '
    Agestr = 'Age:                  '
    Relationstr = 'Relation:         '
    Phonestr = 'Phone:              '
    Emailstr = 'Email:              '
    Addressstr = 'Address:          '
    Occupationstr = 'Occupation:       '
    
    
    #Frame definitions
    ctrlfr = Frame(root, bg=bgcolor)
    ctrlfr.place(relheight=1, relwidth=0.1, relx=0.3, rely=0)
    
    labelfr = Frame(root, bg=bgcolor)
    labelfr.place(relheight=0.5, relwidth=0.5, relx=0.5, rely=0.15)
    
    
    #Listbox
    lb = Listbox(root, lbdesign)
    lb.place(relheight=1, relwidth=0.3, relx=0, rely=0)
    
    
    #Control buttons
    addbtn = Button(ctrlfr, btndesign, text='Add Identity')
    addbtn.place(relwidth=0.8, relheight=0.125, relx=0.1, rely=0.1)
    
    downloadbtn = Button(ctrlfr, btndesign, text='Download ID')
    downloadbtn.place(relwidth=0.8, relheight=0.125, relx=0.1, rely=0.325)
    
    delbtn = Button(ctrlfr, btndesign, text='Delete')
    delbtn.place(relwidth=0.8, relheight=0.125, relx=0.1, rely=0.55)
    
    delallbtn = Button(ctrlfr, btndesign, text='Delete All')
    delallbtn.place(relwidth=0.8, relheight=0.125, relx=0.1, rely=0.775)
        
    
    
    #Labels
    Label(labelfr,text='Identity Information',bg=bgcolor,fg='white',
          font=(
              'Arial',
              20,
              'italic',
              'bold')
          ).place(relx=0.1, rely=0)
    
    namel = Label(labelfr, labeldesign, text=Namestr)
    namel.place(relx=0.1, rely=0.2)
    agel = Label(labelfr, labeldesign, text=Agestr)
    agel.place(relx=0.1, rely=0.3)
    relationl = Label(labelfr, labeldesign, text=Relationstr)
    relationl.place(relx=0.1, rely=0.4)
    phonel = Label(labelfr, labeldesign, text=Phonestr)
    phonel.place(relx=0.1, rely=0.5)
    emaill = Label(labelfr, labeldesign, text=Emailstr)
    emaill.place(relx=0.1, rely=0.6)
    addressl = Label(labelfr, labeldesign, text=Addressstr)
    addressl.place(relx=0.1, rely=0.7)
    occupationl = Label(labelfr, labeldesign, text=Occupationstr)
    occupationl.place(relx=0.1, rely=0.8)
    
    def updatelb():
        
        namelist = fs.updatelb()
        for item in namelist:
            lb.insert(END, item)
    
    updatelb()
    
    def itemselected(e=None):
        
        info = fs.viewinfo(lb.get(ANCHOR))
        
        namel.config(text=Namestr+info[0])
        agel.config(text=Agestr+info[1])
        relationl.config(text=Relationstr+info[2])
        phonel.config(text=Phonestr+info[3])
        emaill.config(text=Emailstr+info[4])
        addressl.config(text=Addressstr+info[5])
        occupationl.config(text=Occupationstr+info[6])
        
    
    def addidentity(e=None):
        root.destroy()
        win = Tk()
        win.resizable(0,0)
        win.title('ID Database - Add')
        win.config(bg=bgcolor)
        
        def back():
            win.destroy()
            main()
            
            
        def submit():
            info = []

            info.append(nameen.get())
            info.append(ageen.get())
            info.append(relationen.get())
            info.append(phoneen.get())
            info.append(emailen.get())
            info.append(addressen.get())
            info.append(occupationen.get())
            fs.add(info)        

            nameen.delete(0, END)
            ageen.delete(0, END)
            relationen.delete(0, END)
            phoneen.delete(0, END)
            emailen.delete(0, END)
            addressen.delete(0, END)
            occupationen.delete(0, END)
       
        Label(win, text='Add ID', bg=bgcolor, fg='white', font=('Arial', 15)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        Label(win, labeldesign, text='Name of Person').grid(row=1, column=0, padx=10, pady=10)
        Label(win, labeldesign, text='Age').grid(row=2, column=0, padx=10, pady=10)
        Label(win, labeldesign, text='Relation').grid(row=3, column=0, padx=10, pady=10)
        Label(win, labeldesign, text='Phone NO').grid(row=4, column=0, padx=10, pady=10)
        Label(win, labeldesign, text='Email ID').grid(row=5, column=0, padx=10, pady=10)
        Label(win, labeldesign, text='Address').grid(row=6, column=0, padx=10, pady=10)
        Label(win, labeldesign, text='Occupation').grid(row=7, column=0, padx=10, pady=10)
        
        nameen = Entry(win, entrydesign)
        nameen.grid(row=1, column=1, padx=10, pady=10)
        ageen = Entry(win, entrydesign)
        ageen.grid(row=2, column=1, padx=10, pady=10)
        relationen = Entry(win, entrydesign)
        relationen.grid(row=3, column=1, padx=10, pady=10)
        phoneen = Entry(win, entrydesign)
        phoneen.grid(row=4, column=1, padx=10, pady=10)
        emailen = Entry(win, entrydesign)
        emailen.grid(row=5, column=1, padx=10, pady=10)
        addressen = Entry(win, entrydesign)
        addressen.grid(row=6, column=1, padx=10, pady=10)
        occupationen = Entry(win, entrydesign)
        occupationen.grid(row=7, column=1, padx=10, pady=10)
        
        subbtn = Button(win, btndesign, text='Submit', height=2, width=15, command=submit)
        subbtn.grid(row=8, column=1, padx=10, pady=10)      
        backbtn = Button(win, btndesign, text='Back', height=2, width=15, command=back)
        backbtn.grid(row=8, column=0, padx=10, pady=10) 
        
        
        
    def download(e=None):
        info = fs.viewinfo(lb.get(ANCHOR))
        files=(('txt File', '*.txt'), ('All Files', '*.*'))
        
        file = filedialog.asksaveasfilename(
            title='Save File',
            defaultextension=files,
            filetypes=files,
            initialfile='Untitled'
        )
        
        print(file)
        
        fs.download(info, file)
        
    
    def delete(e=None):
        value = lb.get(ANCHOR)
        x = messagebox.askyesno('Delete ID', f'Are you sure you want to delete the ID "{value}"')
        
        if x==True: 
            fs.delete(value)
            lb.delete(0,END)
            updatelb()
            
        else:pass
    
    def delall(e=None):
        value = lb.get(ANCHOR)
        x = messagebox.askyesno('Delete ID', f'Are you sure you want to delete the ID "{value}"')
        
        if x==True: 
            fs.delall(value)
            lb.delete(0,END)
            updatelb()
            
        else:pass
        
        
        
    addbtn.config(command=addidentity)
    delbtn.config(command=delete)
    delallbtn.config(command=delall)
    lb.bind('<<ListboxSelect>>', itemselected)
    downloadbtn.config(command=download)
    
    mainloop()
main()