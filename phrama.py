from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector

from tkinter import messagebox

class PharmacyManagementSystem:
    # Creating window
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

#        =======AddMed variable========================
        self.addmed_var=StringVar()
        self.refMed_var=StringVar()
        # Creating label title
        lbltitle = Label(
            self.root,
            text="PHARMACY MANAGEMENT SYSTEM",
            bd=15,
            relief=RIDGE, 
            bg='white',
            fg="darkgreen",
            font=("times new roman", 50, "bold"),
            padx=2,
            pady=4
        )
        lbltitle.pack(side=TOP, fill=X)

        # Adding the logo to the title and adding the path address
        # Use raw string (r"...") or replace backslashes with forward slashes
        img1 = Image.open(r"C:\Users\SUHAS JADHAV\Desktop\Pharma\pharma_logo.png")

        # Resize the image (Updated ANTIALIAS usage)
        img1 = img1.resize((60, 60), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Creating button
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0)
        # setting the data from left side 70 pixel and from top 20 px
        b1.place(x=80, y=30)

#================DataFrame==============================
        # creating a dataframe main Frame to input the data
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)


        # left side Frame to encript the data
        # i want to create left fram in the dataframe not over root means window
        # we can add the label frame
        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)


        # right side frame to add the medicine
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg="darkgreen",font=("arial", 12, "bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

#====================buttonsFrame=======================
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1530,height=65)


#====================Main Button=========================
        btnAddData=Button(ButtonFrame,text="Medicine Add",font=("arial", 12, "bold"),bg="darkgreen",fg="white")  
        #now i want to place but the button in frame so we grid the button and apply column androw
        btnAddData.grid(row=0,column=0) 

        btnUpdateMed=Button(ButtonFrame,text="UPDATE",font=("arial", 13, "bold"),width=14,bg="darkgreen",fg="white")  
        #now i want to place but the button in frame so we grid the button and apply column androw
        btnUpdateMed.grid(row=0,column=1)   

        btnDeleteMed=Button(ButtonFrame,text="DELETE",font=("arial", 13, "bold"),width=14,bg="red",fg="white")  
        #now i want to place but the button in frame so we grid the button and apply column androw
        btnDeleteMed.grid(row=0,column=2)  

        btnRestMed=Button(ButtonFrame,text="RESET",font=("arial", 13, "bold"),width=14,bg="darkgreen",fg="white")  
        #now i want to place but the button in frame so we grid the button and apply column androw
        btnRestMed.grid(row=0,column=3)   

        btnExitMed=Button(ButtonFrame,text="EXIT",font=("arial", 13, "bold"),width=14,bg="darkgreen",fg="white")  
        #now i want to place but the button in frame so we grid the button and apply column androw
        btnExitMed.grid(row=0,column=4)   

#========================Search By=======================
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

#========================creating Search combo-box===============
        search_combo=ttk.Combobox(ButtonFrame,width=12,font=("arial",13,"bold"),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)     
        # for searching first value is always zero
        search_combo.current(0)

        
        txtSearch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)

        #for searching 
        searchBtn=Button(ButtonFrame,text="SEARCH",font=("arial", 13, "bold"),width=14,bg="darkgreen",fg="white")  
        searchBtn.grid(row=0,column=8)  
        
        #for show all button
        showAll=Button(ButtonFrame,text="SHOW ALL",font=("arial", 13, "bold"),width=14,bg="darkgreen",fg="white")  
        showAll.grid(row=0,column=9)  

#====================labels and Entry===================
 # "Reference No" Combo Box
        lblrefno = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No", padx=2)
        lblrefno.grid(row=0, column=0, sticky=W)

        ref_combo = ttk.Combobox(DataFrameLeft, width=27, font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"] = ("Ref1", "Medname", "Lot")  # Replace with actual reference values
        ref_combo.grid(row=0, column=1)
        ref_combo.current(0)  # Default to the first item

# company Name
        lblCompanyName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Company Name:", padx=2, pady=6)
        lblCompanyName.grid(row=1, column=0, sticky=W)

        lblCompanyName = Entry(DataFrameLeft, font=("arial", 12, "bold"), bg="white",bd=2,relief=RIDGE,width=29)
        lblCompanyName.grid(row=1, column=1)


# "Type of medicine" Combo Box
        lblTypeMedicineName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Type of Medicine:", padx=2, pady=6)
        lblTypeMedicineName.grid(row=2, column=0, sticky=W)

        comTypeMedicineName = ttk.Combobox(DataFrameLeft, width=27, font=("arial", 12, "bold"), state="readonly")
        comTypeMedicineName["values"] = ("Tablets","Drops","Capsule","Injection","Liquid","inhales","Topical Medicine")  # Replace with actual medicine names
        comTypeMedicineName.grid(row=2, column=1)
        comTypeMedicineName.current(0) 

# "Medicine Name" Combo Box
        lblMedicineName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medicine Name:", padx=2, pady=6)
        lblMedicineName.grid(row=3, column=0, sticky=W)

        comMedicineName = ttk.Combobox(DataFrameLeft, width=27, font=("arial", 12, "bold"), state="readonly")
        comMedicineName["values"] = ("Paracetamol", "Aspirin", "Ibuprofen")  # Replace with actual medicine names
        comMedicineName.grid(row=3, column=1)
        comMedicineName.current(0)  # Default to the first item


        lblLotNo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot No:", padx=2, pady=6)
        lblLotNo.grid(row=4, column=0, sticky=W)
        txtLotNo = Entry(DataFrameLeft, font=("arial", 12, "bold"), bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4, column=1)

        lblIssueDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5, column=1)

        lblExDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExDate.grid(row=6, column=0, sticky=W)
        txtExDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white",bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6, column=1)

        lblUses = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Uses:", padx=2, pady=6)
        lblUses.grid(row=7, column=0, sticky=W)
        txtUses = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=7, column=1)

        lblSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="sideeffect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white",bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=8, column=1)



        lblPreWarning = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Pre&Warning:", padx=15)
        lblPreWarning.grid(row=0, column=2, sticky=W)
        txtPreWarning = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white",bd=2,relief=RIDGE,width=29)
        txtPreWarning.grid(row=0, column=3)

        lblDosage = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dosage:", padx=15, pady=6)
        lblDosage.grid(row=1, column=2, sticky=W)
        txtDosage = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white",bd=2,relief=RIDGE,width=29)
        txtDosage.grid(row=1, column=3)

        lblTabletsPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Tablets Price:", padx=15, pady=6)
        lblTabletsPrice.grid(row=2, column=2, sticky=W)
        txtTabletsPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white",bd=2,relief=RIDGE,width=29)
        txtTabletsPrice.grid(row=2, column=3)

        lblProductQT = Label(DataFrameLeft, font=("arial", 12, "bold"), text="ProductQT:", padx=15, pady=6)
        lblProductQT.grid(row=3, column=2, sticky=W)
        txtProductQT = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white",bd=2,relief=RIDGE,width=29)
        txtProductQT.grid(row=3, column=3,sticky=W)

#=========================images================
        lblHome = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Stay Home Stay Safe", padx=2, pady=6,bg="white",fg="red",width=37)
        lblHome.place(x=410,y=140)


        img2 = Image.open(r"pharm1.jpg")
        img2 = img2.resize((150, 135), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(self.root, image=self.photoimg2, borderwidth=0)
        b1.place(x=770, y=330)

        
        img3 = Image.open(r"pharm3.jpg")
        img3 = img3.resize((150, 135), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image=self.photoimg3, borderwidth=0)
        b1.place(x=620, y=330)

        img4 = Image.open(r"C:\Users\SUHAS JADHAV\Desktop\Pharma\pharm2.jpg")
        img4 = img4.resize((150, 135), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.root, image=self.photoimg4, borderwidth=0)
        b1.place(x=475, y=330)


#==========================data Frame Right============
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg="darkgreen",font=("arial", 12, "bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        img5 = Image.open(r"C:\Users\SUHAS JADHAV\Desktop\Pharma\pharm2.jpg")
        img5 = img5.resize((200, 75), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.root, image=self.photoimg5, borderwidth=0)
        b1.place(x=960, y=160)

        img6 = Image.open(r"C:\Users\SUHAS JADHAV\Desktop\Pharma\pharm2.jpg")
        img6 = img6.resize((200, 75), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(self.root, image=self.photoimg6, borderwidth=0)
        b1.place(x=1160, y=160)

        img7 = Image.open(r"C:\Users\SUHAS JADHAV\Desktop\Pharma\pharm2.jpg")
        img7 = img7.resize((200, 145), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(self.root, image=self.photoimg7, borderwidth=0)
        b1.place(x=1275, y=160)
        
        lblRrefno = Label(DataFrameRight, font=("arial", 12, "bold"), text="Reference No:", padx=15, pady=6)
        lblRrefno.place(x=0,y=80)
        txtRrefno = Entry(DataFrameRight,textvariable=self.refMed_var,font=("arial", 15, "bold"), bg="white",bd=2,relief=RIDGE,width=14)
        txtRrefno.place(x=135,y=80)

        lblmedName= Label(DataFrameRight, font=("arial", 12, "bold"), text="Medicine Name:", padx=15, pady=6)
        lblmedName.place(x=0,y=110)
        txtmedName = Entry(DataFrameRight,textvariable=self.addmed_var,font=("arial", 15, "bold"), bg="white",bd=2,relief=RIDGE,width=14)
        txtmedName.place(x=135,y=110)

#============================side Frame===========================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)
        
        #this is for scrollbar
        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        #making Treeview with the help of ttk
        self.medicine_table=ttk.Treeview(side_frame,columns=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")
        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)
        # to set the width of the medicine table 
        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("ref",width=100)

        # require button to add update reset
#=================Medicine Add Button=======================
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=150,width=135,height=160)

        btnAddmed=Button(down_frame,text="ADD",font=("arial", 12, "bold"),width=12,bg="lime",fg="white",pady=4)  
        btnAddmed.grid(row=0,column=0) 

        btnUpdatemed=Button(down_frame,text="Update",font=("arial", 12, "bold"),width=12,bg="purple",fg="white",pady=4)  
        btnUpdatemed.grid(row=1,column=0) 

        btnDeletemed=Button(down_frame,text="Delete",font=("arial", 12, "bold"),width=12,bg="red",fg="white",pady=4)  
        btnDeletemed.grid(row=2,column=0) 

        btnClearmed=Button(down_frame,text="Clear",font=("arial", 12, "bold"),width=12,bg="orange",fg="white",pady=4)  
        btnClearmed.grid(row=3,column=0) 

#============================frame Details=========================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1530,height=210)
# #================  main table scroll bar==================
        Table_Frame=Frame(self.root,bd=15,relief=RIDGE)
        Table_Frame.place(x=0,y=580,width=1530,height=210)

        #this is for scrollbar below frame
        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        pharmacy_table = ttk.Treeview(Table_Frame, columns=("reg", "companyname", "type", "tabletname", "lotno", "issuedate",
                                                    "expdate", "uses", "sideeffect", "warning", "dosage", "price", "productqt"),
                              xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=pharmacy_table.xview)
        scroll_y.config(command=pharmacy_table.yview)

# Configure headings for the Pharmacy Table
        pharmacy_table["show"] = "headings"
        pharmacy_table.heading("reg", text="Reference No")
        pharmacy_table.heading("companyname", text="Company Name")
        pharmacy_table.heading("type", text="Type Of Medicine")
        pharmacy_table.heading("tabletname", text="Tablet Name")
        pharmacy_table.heading("lotno", text="Lot No")
        pharmacy_table.heading("issuedate", text="Issue Date")
        pharmacy_table.heading("expdate", text="Exp Date")
        pharmacy_table.heading("uses", text="Uses")
        pharmacy_table.heading("sideeffect", text="Side Effect")
        pharmacy_table.heading("warning", text="Precaution & Warning")
        pharmacy_table.heading("dosage", text="Dosage")
        pharmacy_table.heading("price", text="Price")
        pharmacy_table.heading("productqt", text="Product Quantity")

# Packing the pharmacy table
        pharmacy_table.pack(fill=BOTH, expand=1)
        # just setting the widht
# Correctly setting the width for each column in the pharmacy table
        # self.pharmacy_table.column("reg", width=100)
        # self.pharmacy_table.column("companyname", width=100)
        # self.pharmacy_table.column("type", width=100)
        # self.pharmacy_table.column("tabletname", width=100)
        # self.pharmacy_table.column("lotno", width=100)  # Corrected "lo no" to "lotno"
        # self.pharmacy_table.column("issuedate", width=100)
        # self.pharmacy_table.column("expdate", width=100)
        # self.pharmacy_table.column("uses", width=100)
        # self.pharmacy_table.column("sideeffect", width=100)
        # self.pharmacy_table.column("warning", width=100)
        # self.pharmacy_table.column("dosage", width=100)
        # self.pharmacy_table.column("price", width=100)
        # self.pharmacy_table.column("productqt", width=100)

#=====================Add medicine functionality declaration==================
        def AddMed(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="@Moto#721",database="mydata")
                print("Connected!") if conn.is_connected() else print("Connection failed!")
                #cursor to insert the data
                # my_cursor=conn.cursor()
                # my_cursor.execute("insert into pharma_1(Ref,MedName)values(%s,%s)",(
                #         self.refMed_var.get(),
                #         self.addMed_var.get()
                # ))

                # conn.commit()
                conn.close()
                messagebox.showinfo("Success","Medicine Added")


        
# Main execution
if __name__ == "__main__":
    root = Tk()
    app = PharmacyManagementSystem(root)
    root.mainloop()

