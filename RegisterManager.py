import tkinter as tk
from tkinter import ttk

#from csv import messagebox

class RegisterManager:
  def __init__(self, root, frame):
    self.root = root
    self.frame = frame
    self.main_lst=[]

    self.registerA = tk.Label(text="Register A", bg="#44505A", fg="white", font="timesnewroman").place(relx=0,rely=0)
    self.registerB = tk.Label(text="Register B", bg="#44505A", fg="white", font="timesnewroman").place(relx=0.34, rely=0)
    self.registerC = tk.Label(text="Register C", bg="#44505A", fg="white", font="timesnewroman").place(relx=0.67, rely=0)
    
    self.separator = ttk.Separator(orient="horizontal").place(relx=0, rely=0.48, relwidth=2, relheight=0.003)

    #register A
    #nickels-----------------------------
    self.nickelsA = tk.DoubleVar()
    self.nickelsA.trace_add("write", self.calculate)
    self.nickelAEntry = tk.Entry(textvariable=self.nickelsA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.nickelAEntry.place(relx=0, rely=0.035)
    self.nickelALab = tk.Label(text="Nickels:", bg="#44505A", fg='white').place(relx=0.07, rely=0.035)
    self.nickelAWorthLab = tk.Label(text=self.nickelsA.get())
    self.nickelAWorthLab.place(relx=0.14, rely=0.035)
    #dimes-----------------------------
    self.dimesA = tk.DoubleVar()
    self.dimesA.trace_add("write", self.calculate)
    self.dimeAEntry = tk.Entry( textvariable=self.dimesA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.dimeAEntry.place(relx=0, rely=0.07)
    self.dimeALabel = tk.Label( text="Dimes:", bg="#44505A", fg='white').place(relx=0.07, rely=0.07)
    self.dimeAWorthLab = tk.Label( text=self.dimesA.get())
    self.dimeAWorthLab.place(relx=0.14, rely=0.07)
    #quarter----------------------------------
    self.quartersA = tk.DoubleVar()
    self.quartersA.trace_add("write", self.calculate)
    self.quarterAEntry = tk.Entry(textvariable=self.quartersA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.quarterAEntry.place(relx=0, rely=0.105)
    self.quarterALabel = tk.Label(text="Quarters:", bg="#44505A", fg='white').place(relx=0.07, rely=0.105)
    self.quarterAWorthLab = tk.Label(text=self.quartersA.get())
    self.quarterAWorthLab.place(relx=0.14, rely=0.105)
    #loonies----------------------------------
    self.looniesA = tk.DoubleVar()
    self.looniesA.trace_add("write", self.calculate)
    self.loonieAEntry = tk.Entry(textvariable=self.looniesA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.loonieAEntry.place(relx=0, rely=0.14)
    self.loonieALabel = tk.Label(text="Loonies:", bg="#44505A", fg='white').place(relx=0.07, rely=0.14)
    self.loonieAWorthLab = tk.Label(text=self.looniesA.get())
    self.loonieAWorthLab.place(relx=0.14, rely=0.14)
    #toonies----------------------------------
    self.tooniesA = tk.DoubleVar()
    self.tooniesA.trace_add("write", self.calculate)
    self.toonieAEntry = tk.Entry(textvariable=self.tooniesA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.toonieAEntry.place(relx=0, rely=0.175)
    self.toonieALabel = tk.Label(text="Toonies:", bg="#44505A", fg='white').place(relx=0.07, rely=0.175)
    self.toonieAWorthLab = tk.Label(text=self.tooniesA.get())
    self.toonieAWorthLab.place(relx=0.14, rely=0.175)
    #$5 bill----------------------------------
    self.fiveA = tk.DoubleVar()
    self.fiveA.trace_add("write", self.calculate)
    self.fiveAEntry = tk.Entry(textvariable=self.fiveA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiveAEntry.place(relx=0, rely=0.21)
    self.fiveALabel = tk.Label(text="$5 Bill:", bg="#44505A", fg='white').place(relx=0.07, rely=0.21)
    self.fiveAWorthLab = tk.Label(text=self.fiveA.get())
    self.fiveAWorthLab.place(relx=0.14, rely=0.21)
    #$10 bill----------------------------------
    self.tenA = tk.DoubleVar()
    self.tenA.trace_add("write", self.calculate)
    self.tenAEntry = tk.Entry(textvariable=self.tenA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.tenAEntry.place(relx=0, rely=0.245)
    self.tenALabel = tk.Label(text="$10 Bill:", bg="#44505A", fg='white').place(relx=0.07, rely=0.245)
    self.tenAWorthLab = tk.Label(text=self.tenA.get())
    self.tenAWorthLab.place(relx=0.14, rely=0.245)
    #$20 bill----------------------------------
    self.twentyA = tk.DoubleVar()
    self.twentyA.trace_add("write", self.calculate)
    self.twentyAEntry = tk.Entry(textvariable=self.twentyA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.twentyAEntry.place(relx=0, rely=0.28)
    self.twentyALabel = tk.Label(text="$20 Bill:", bg="#44505A", fg='white').place(relx=0.07, rely=0.28)
    self.twentyAWorthLab = tk.Label(text=self.twentyA.get())
    self.twentyAWorthLab.place(relx=0.14, rely=0.28)
    #$50 bill----------------------------------
    self.fiftyA = tk.DoubleVar()
    self.fiftyA.trace_add("write", self.calculate)
    self.fiftyAEntry = tk.Entry(textvariable=self.fiftyA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiftyAEntry.place(relx=0, rely=0.315)
    self.fiftyALabel = tk.Label(text="$50 Bill:", bg="#44505A", fg='white').place(relx=0.07, rely=0.315)
    self.fiftyAWorthLab = tk.Label(text=self.fiftyA.get())
    self.fiftyAWorthLab.place(relx=0.14, rely=0.315)
    #total-----------------------------------
    self.totalWord = tk.Label(text="     Total:", bg="#44505A", fg='white').place(relx=0.07, rely=0.37)
    self.totalA = self.nickelsA.get() + self.dimesA.get() + self.quartersA.get() + self.looniesA.get() + self.tooniesA.get() + self.fiveA.get()  + self.tenA.get() + self.twentyA.get()  + self.fiftyA.get()
    self.totalALab = tk.Label(self.totalA)
    self.totalALab.place(relx=0.14, rely=0.37)
    #Register B
    #nickels B-----------------------------
    self.nickelsB = tk.DoubleVar()
    self.nickelsB.trace_add("write", self.calculate)
    self.nickelBEntry = tk.Entry(textvariable=self.nickelsB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.nickelBEntry.place(relx=0.34, rely=0.035)
    self.nickelBLab = tk.Label(text="Nickels:", bg="#44505A", fg='white').place(relx=0.41, rely=0.035)
    self.nickelBWorthLab = tk.Label(text=self.nickelsB.get())
    self.nickelBWorthLab.place(relx=0.48, rely=0.035)
    #dimes B----------------------------------
    self.dimesB = tk.DoubleVar()
    self.dimesB.trace_add("write", self.calculate)
    self.dimeBEntry = tk.Entry(textvariable=self.dimesB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.dimeBEntry.place(relx=0.34, rely=0.07)
    self.dimeBLabel = tk.Label(text="Dimes:", bg="#44505A", fg='white').place(relx=0.41, rely=0.07)
    self.dimeBWorthLab = tk.Label(text=self.dimesB.get())
    self.dimeBWorthLab.place(relx=0.48, rely=0.07)
    #quarter----------------------------------
    self.quartersB = tk.DoubleVar()
    self.quartersB.trace_add("write", self.calculate)
    self.quarterBEntry = tk.Entry(textvariable=self.quartersB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.quarterBEntry.place(relx=0.34, rely=0.105)
    self.quarterBLabel = tk.Label(text="Quarters:", bg="#44505A", fg='white').place(relx=0.41, rely=0.105)
    self.quarterBWorthLab = tk.Label(text=self.quartersB.get())
    self.quarterBWorthLab.place(relx=0.48, rely=0.105)
    #loonies----------------------------------
    self.looniesB = tk.DoubleVar()
    self.looniesB.trace_add("write", self.calculate)
    self.loonieBEntry = tk.Entry(textvariable=self.looniesB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.loonieBEntry.place(relx=0.34, rely=0.14)
    self.loonieBLabel = tk.Label(text="Loonies:", bg="#44505A", fg='white').place(relx=0.41, rely=0.14)
    self.loonieBWorthLab = tk.Label(text=self.looniesB.get())
    self.loonieBWorthLab.place(relx=0.48, rely=0.14)
    #toonies----------------------------------
    self.tooniesB = tk.DoubleVar()
    self.tooniesB.trace_add("write", self.calculate)
    self.toonieBEntry = tk.Entry(textvariable=self.tooniesB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.toonieBEntry.place(relx=0.34, rely=0.175)
    self.toonieBLabel = tk.Label(text="Toonies:", bg="#44505A", fg='white').place(relx=0.41, rely=0.175)
    self.toonieBWorthLab = tk.Label(text=self.tooniesB.get())
    self.toonieBWorthLab.place(relx=0.48, rely=0.175)
    #$5 bill----------------------------------
    self.fiveB = tk.DoubleVar()
    self.fiveB.trace_add("write", self.calculate)
    self.fiveBEntry = tk.Entry(textvariable=self.fiveB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiveBEntry.place(relx=0.34, rely=0.21)
    self.fiveBLabel = tk.Label(text="$5 Bill:", bg="#44505A", fg='white').place(relx=0.41, rely=0.21)
    self.fiveBWorthLab = tk.Label(text=self.fiveB.get())
    self.fiveBWorthLab.place(relx=0.48, rely=0.21)
    #$10 bill----------------------------------
    self.tenB = tk.DoubleVar()
    self.tenB.trace_add("write", self.calculate)
    self.tenBEntry = tk.Entry(textvariable=self.tenB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.tenBEntry.place(relx=0.34, rely=0.245)
    self.tenBLabel = tk.Label(text="$10 Bill:", bg="#44505A", fg='white').place(relx=0.41, rely=0.245)
    self.tenBWorthLab = tk.Label(text=self.tenB.get())
    self.tenBWorthLab.place(relx=0.48, rely=0.245)
    #$20 bill----------------------------------
    self.twentyB = tk.DoubleVar()
    self.twentyB.trace_add("write", self.calculate)
    self.twentyBEntry = tk.Entry(textvariable=self.twentyB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.twentyBEntry.place(relx=0.34, rely=0.28)
    self.twentyBLabel = tk.Label(text="$20 Bill:", bg="#44505A", fg='white').place(relx=0.41, rely=0.28)
    self.twentyBWorthLab = tk.Label(text=self.twentyB.get())
    self.twentyBWorthLab.place(relx=0.48, rely=0.28)
    #$50 bill----------------------------------
    self.fiftyB = tk.DoubleVar()
    self.fiftyB.trace_add("write", self.calculate)
    self.fiftyBEntry = tk.Entry(textvariable=self.fiftyB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiftyBEntry.place(relx=0.34, rely=0.315)
    self.fiftyBLabel = tk.Label(text="$50 Bill:", bg="#44505A", fg='white').place(relx=0.41, rely=0.315)
    self.fiftyBWorthLab = tk.Label(text=self.fiftyB.get())
    self.fiftyBWorthLab.place(relx=0.48, rely=0.315)
    #total-----------------------------------
    self.totalBWord = tk.Label(text="     Total:", bg="#44505A", fg='white').place(relx=0.41, rely=0.37)
    self.totalB = self.nickelsB.get() + self.dimesB.get() + self.quartersB.get() + self.looniesB.get() + self.tooniesB.get() + self.fiveB.get()  + self.tenB.get() + self.twentyB.get()  + self.fiftyB.get()
    self.totalBLab = tk.Label(text=self.totalB)
    self.totalBLab.place(relx=0.48, rely=0.37)
    #Register C
    #nickels-----------------------------
    self.nickelsC = tk.DoubleVar()
    self.nickelsC.trace_add("write", self.calculate)
    self.nickelCEntry = tk.Entry(textvariable=self.nickelsC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.nickelCEntry.place(relx=0.67, rely=0.035)
    self.nickelCLab = tk.Label(text="Nickels:", bg="#44505A", fg='white').place(relx=0.74, rely=0.035)
    self.nickelCWorthLab = tk.Label(text=self.nickelsC.get())
    self.nickelCWorthLab.place(relx=0.81, rely=0.035)
    #dimes----------------------------------
    self.dimesC = tk.DoubleVar()
    self.dimesC.trace_add("write", self.calculate)
    self.dimeCEntry = tk.Entry(textvariable=self.dimesC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.dimeCEntry.place(relx=0.67, rely=0.07)
    self.dimeCLabel = tk.Label(text="Dimes:", bg="#44505A", fg='white').place(relx=0.74, rely=0.07)
    self.dimeCWorthLab = tk.Label(text=self.dimesC.get())
    self.dimeCWorthLab.place(relx=0.81, rely=0.07)
    #quarter----------------------------------
    self.quartersC = tk.DoubleVar()
    self.quartersC.trace_add("write", self.calculate)
    self.quarterCEntry = tk.Entry(textvariable=self.quartersC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.quarterCEntry.place(relx=0.67, rely=0.105)
    self.quarterCLabel = tk.Label(text="Quarters:", bg="#44505A", fg='white').place(relx=0.74, rely=0.105)
    self.quarterCWorthLab = tk.Label(text=self.quartersC.get())
    self.quarterCWorthLab.place(relx=0.81, rely=0.105)
    #loonies----------------------------------
    self.looniesC = tk.DoubleVar()
    self.looniesC.trace_add("write", self.calculate)
    self.loonieCEntry = tk.Entry(textvariable=self.looniesC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.loonieCEntry.place(relx=0.67, rely=0.14)
    self.loonieCLabel = tk.Label(text="Loonies:", bg="#44505A", fg='white').place(relx=0.74, rely=0.14)
    self.loonieCWorthLab = tk.Label(text=self.looniesC.get())
    self.loonieCWorthLab.place(relx=0.81, rely=0.14)
    #toonies----------------------------------
    self.tooniesC = tk.DoubleVar()
    self.tooniesC.trace_add("write", self.calculate)
    self.toonieCEntry = tk.Entry(textvariable=self.tooniesC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.toonieCEntry.place(relx=0.67, rely=0.175)
    self.toonieCLabel = tk.Label(text="Toonies:", bg="#44505A", fg='white').place(relx=0.74, rely=0.175)
    self.toonieCWorthLab = tk.Label(text=self.tooniesC.get())
    self.toonieCWorthLab.place(relx=0.81, rely=0.175)
    #$5 bill----------------------------------
    self.fiveC = tk.DoubleVar()
    self.fiveC.trace_add("write", self.calculate)
    self.fiveCEntry = tk.Entry(textvariable=self.fiveC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiveCEntry.place(relx=0.67, rely=0.21)
    self.fiveCLabel = tk.Label(text="$5 Bill:", bg="#44505A", fg='white').place(relx=0.74, rely=0.21)
    self.fiveCWorthLab = tk.Label(text=self.fiveC.get())
    self.fiveCWorthLab.place(relx=0.81, rely=0.21)
    #$10 bill----------------------------------
    self.tenC = tk.DoubleVar()
    self.tenC.trace_add("write", self.calculate)
    self.tenCEntry = tk.Entry(textvariable=self.tenC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.tenCEntry.place(relx=0.67, rely=0.245)
    self.tenCLabel = tk.Label(text="$10 Bill:", bg="#44505A", fg='white').place(relx=0.74, rely=0.245)
    self.tenCWorthLab = tk.Label(text=self.tenC.get())
    self.tenCWorthLab.place(relx=0.81, rely=0.245)
    #$20 bill----------------------------------
    self.twentyC = tk.DoubleVar()
    self.twentyC.trace_add("write", self.calculate)
    self.twentyCEntry = tk.Entry(textvariable=self.twentyC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.twentyCEntry.place(relx=0.67, rely=0.28)
    self.twentyCLabel = tk.Label(text="$20 Bill:", bg="#44505A", fg='white').place(relx=0.74, rely=0.28)
    self.twentyCWorthLab = tk.Label(text=self.twentyC.get())
    self.twentyCWorthLab.place(relx=0.81, rely=0.28)
    #$50 bill----------------------------------
    self.fiftyC = tk.DoubleVar()
    self.fiftyC.trace_add("write", self.calculate)
    self.fiftyCEntry = tk.Entry(textvariable=self.fiftyC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiftyCEntry.place(relx=0.67, rely=0.315)
    self.fiftyCLabel = tk.Label(text="$50 Bill:", bg="#44505A", fg='white').place(relx=0.74, rely=0.315)
    self.fiftyCWorthLab = tk.Label(text=self.fiftyC.get())
    self.fiftyCWorthLab.place(relx=0.81, rely=0.315)
    #total-----------------------------------
    self.totalCWord = tk.Label(text="     Total:", bg="#44505A", fg='white').place(relx=0.74, rely=0.37)
    self.totalC = self.nickelsC.get() + self.dimesC.get() + self.quartersC.get() + self.looniesC.get() + self.tooniesC.get() + self.fiveC.get()  + self.tenC.get() + self.twentyC.get()  + self.fiftyC.get()
    self.totalCLab = tk.Label(text=self.totalC)
    self.totalCLab.place(relx=0.81, rely=0.37)

    #grand total------------------------------
    self.registerTotal = tk.Label(text="Total of all registers:", bg="#44505A", fg='white').place(relx=0, rely=0.79)
    self.grandTotal = self.totalA + self.totalB + self.totalC
    self.registerTotalLab = tk.Label(text = self.grandTotal)
    self.registerTotalLab.place(relx=0.15, rely=0.79)
    #float/net profit-------------------------------------
    self.floatAndNet = tk.DoubleVar()
    self.floatAndNet.trace_add("write", self.calculate)
    self.NetProfitText = tk.Label(text= "Net Profit (-$489 float): ", bg="#44505A", fg='white').place(relx=0, rely=0.85)
    self.NetProfitLab = tk.Label(text=(self.floatAndNet.get()))
    self.NetProfitLab.place(relx=0.165, rely=0.85)

    #punch card total-----------------------------
    self.punchCardA = tk.DoubleVar()
    self.punchCardA.trace_add("write", self.calculate)
    self.punchCardALab = tk.Label(text="Register A Punch Cards: $", bg="#44505A", fg='white').place(relx=0, rely=0.59)
    self.punchCardAEntry = tk.Entry( textvariable=self.punchCardA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.punchCardAEntry.place(relx=0.14, rely=0.59)

    self.punchCardB = tk.DoubleVar()
    self.punchCardB.trace_add("write", self.calculate)
    self.punchCardBLab = tk.Label( text="Register B Punch Cards: $", bg="#44505A", fg='white').place(relx=0, rely=0.62)
    self.punchCardBEntry = tk.Entry(textvariable=self.punchCardB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.punchCardBEntry.place(relx=0.14, rely=0.62)

    self.punchCardC = tk.DoubleVar()
    self.punchCardC.trace_add("write", self.calculate)
    self.punchCardCLab = tk.Label(text="Register C Punch Cards: $", bg="#44505A", fg='white').place(relx=0, rely=0.65)
    self.punchCardCEntry = tk.Entry( textvariable=self.punchCardC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.punchCardCEntry.place(relx=0.14, rely=0.65)

    self.punchCardTotal = tk.Label(text="Punch Cards Total:", bg="#44505A", fg='white').place(relx=0, rely=0.7)

    self.punchCardTotalLabel = tk.Label( text="0.0")
    self.punchCardTotalLabel.place(relx=0.14, rely=0.7)

    #vouchers-----------------------------
    self.voucherA = tk.DoubleVar()
    self.voucherA.trace_add("write", self.calculate)
    self.voucherALab = tk.Label(text="Register A Vouchers: $", bg="#44505A", fg='white').place(relx=0.3, rely=0.59)
    self.voucherAEntry = tk.Entry(textvariable=self.voucherA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.voucherAEntry.place(relx=0.425, rely=0.59)
    self.voucherAWorthLab = tk.Label(text=self.voucherA.get())
    self.voucherAWorthLab.place(relx=0.5, rely=0.59)

    self.voucherB = tk.DoubleVar()
    self.voucherB.trace_add("write", self.calculate)
    self.voucherBLab = tk.Label(text="Register B Vouchers: $", bg="#44505A", fg='white').place(relx=0.3, rely=0.62)
    self.voucherBEntry = tk.Entry(textvariable=self.voucherB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.voucherBEntry.place(relx=0.425, rely=0.62)
    self.voucherBWorthLab = tk.Label(text=self.voucherB.get())
    self.voucherBWorthLab.place(relx=0.5, rely=0.62)

    self.voucherC = tk.DoubleVar()
    self.voucherC.trace_add("write", self.calculate)
    self.voucherCLab = tk.Label(text="Register C Vouchers: $", bg="#44505A", fg='white').place(relx=0.3, rely=0.65)
    self.voucherCEntry = tk.Entry(textvariable=self.voucherC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.voucherCEntry.place(relx=0.425, rely=0.65)
    self.voucherCWorthLab = tk.Label(text=self.voucherC.get())
    self.voucherCWorthLab.place(relx=0.5, rely=0.65)

    self.voucherTotal = tk.Label( text="Vouchers Total:", bg="#44505A", fg='white').place(relx=0.3, rely=0.7)

    self.voucherTotalLabel = tk.Label( text=0.0)
    self.voucherTotalLabel.place(relx=0.425, rely=0.7)

    self.delete()
    #clear button
    self.clear = tk.Button(text="Clear", command=self.delete) 
    self.clear.place(relx=0.02,rely=0.92)
    #add button
    self.add = tk.Button(text="Add", command=self.addData) 
    self.add.place(relx=0.09,rely=0.92)
    #save button
    self.save = tk.Button(text="Save", command=self.saveData) 
    self.save.place(relx=0.15,rely=0.92)

  def calculate(self, *args):

    #punch cards
    #register A
    try: PCA = self.punchCardA.get()
    except: PCA = 0.0
    #register B
    try: PCB = self.punchCardB.get()
    except: PCB = 0.0
    #register C
    try: PCC = self.punchCardC.get()
    except: PCC = 0.0
    self.punchCardTotalLabel['text'] = round((PCA + PCB + PCC), 2)

    #vouchers
    #register A
    try: VA = self.voucherA.get()
    except: VA = 0
    self.voucherAWorthLab['text'] = round((VA * 5.0), 2)
    #register B
    try: VB = self.voucherB.get()
    except: VB = 0
    self.voucherBWorthLab['text'] = round((VB * 5.0), 2)
    #register C
    try: VC = self.voucherC.get()
    except: VC = 0
    self.voucherCWorthLab['text'] = round((VC * 5.0), 2)
    self.voucherTotalLabel['text'] = round((self.voucherAWorthLab['text'] + self.voucherBWorthLab['text'] + self.voucherCWorthLab['text']), 2)

    #Register A
    #nickels
    try: nickelAAmount = self.nickelsA.get()
    except: nickelAAmount = 0
    self.nickelAWorthLab['text'] = round((nickelAAmount * 0.05), 2)
    #dimes
    try: dimeAAmount = self.dimesA.get()
    except: dimeAAmount = 0
    self.dimeAWorthLab['text'] = round((dimeAAmount * 0.10), 2)
    #quarters
    try: quarterAAmount = self.quartersA.get()
    except: quarterAAmount = 0
    self.quarterAWorthLab['text'] = round((quarterAAmount * 0.25), 2)
    #loonies
    try: loonieAAmount = self.looniesA.get()
    except: loonieAAmount = 0
    self.loonieAWorthLab['text'] = round((loonieAAmount * 1.0), 2)
    #toonies
    try: toonieAAmount = self.tooniesA.get()
    except: toonieAAmount = 0
    self.toonieAWorthLab['text'] = round((toonieAAmount * 2.0), 2)
    #5 dollar bill
    try: fiveAAmount = self.fiveA.get()
    except: fiveAAmount = 0
    self.fiveAWorthLab['text'] = round((fiveAAmount * 5.0), 2)
    #10 dollar bill
    try: tenAAmount = self.tenA.get()
    except: tenAAmount = 0
    self.tenAWorthLab['text'] = round((tenAAmount * 10.0), 2)
    #20 dollar bill
    try: twentyAAmount = self.twentyA.get()
    except: twentyAAmount = 0
    self.twentyAWorthLab['text'] = round((twentyAAmount * 20.0), 2)
    #50 dollar bill
    try: fiftyAAmount = self.fiftyA.get()
    except: fiftyAAmount = 0
    self.fiftyAWorthLab['text'] = round((fiftyAAmount * 50.0), 2)
    #total
    self.CalculateTotalA = self.nickelAWorthLab['text'] + self.dimeAWorthLab['text'] + self.quarterAWorthLab['text'] + self.loonieAWorthLab['text'] + self.toonieAWorthLab['text'] + self.fiveAWorthLab['text'] + self.tenAWorthLab['text'] + self.twentyAWorthLab['text'] + self.fiftyAWorthLab['text']
    self.totalALab['text'] = round((self.CalculateTotalA), 2)
    #Register B
    #nickels
    try: nickelBAmount = self.nickelsB.get()
    except: nickelBAmount = 0
    self.nickelBWorthLab['text'] = round((nickelBAmount * 0.05), 2)
    #dimes
    try: dimeBAmount = self.dimesB.get()
    except: dimeBAmount = 0
    self.dimeBWorthLab['text'] = round((dimeBAmount * 0.10), 2)
    #quarters
    try: quarterBAmount = self.quartersB.get()
    except: quarterBAmount = 0
    self.quarterBWorthLab['text'] = round((quarterBAmount * 0.25), 2)
    #loonies
    try: loonieBAmount = self.looniesB.get()
    except: loonieBAmount = 0
    self.loonieBWorthLab['text'] = round((loonieBAmount * 1.0), 2)
    #toonies
    try: toonieBAmount = self.tooniesB.get()
    except: toonieBAmount = 0
    self.toonieBWorthLab['text'] = round((toonieBAmount * 2.0), 2)
    #5 dollar bill
    try: fiveBAmount = self.fiveB.get()
    except: fiveBAmount = 0
    self.fiveBWorthLab['text'] = round((fiveBAmount * 5.0), 2)
    #10 dollar bill
    try: tenBAmount = self.tenB.get()
    except: tenBAmount = 0
    self.tenBWorthLab['text'] = round((tenBAmount * 10.0), 2)
    #20 dollar bill
    try: twentyBAmount = self.twentyB.get()
    except: twentyBAmount = 0
    self.twentyBWorthLab['text'] = round((twentyBAmount * 20.0), 2)
    #50 dollar bill
    try: fiftyBAmount = self.fiftyB.get()
    except: fiftyBAmount = 0
    self.fiftyBWorthLab['text'] = round((fiftyBAmount * 50.0), 2)
    #total
    self.CalculateTotalB = self.nickelBWorthLab['text'] + self.dimeBWorthLab['text'] + self.quarterBWorthLab['text'] + self.loonieBWorthLab['text'] + self.toonieBWorthLab['text'] + self.fiveBWorthLab['text'] + self.tenBWorthLab['text'] + self.twentyBWorthLab['text'] + self.fiftyBWorthLab['text']
    self.totalBLab['text'] = round((self.CalculateTotalB), 2)
    #Register C
    #nickels
    try: nickelCAmount = self.nickelsC.get()
    except: nickelCAmount = 0
    self.nickelCWorthLab['text'] = round((nickelCAmount * 0.05), 2)
    #dimes
    try: dimeCAmount = self.dimesC.get()
    except: dimeCAmount = 0
    self.dimeCWorthLab['text'] = round((dimeCAmount * 0.10), 2)
    #quarters
    try: quarterCAmount = self.quartersC.get()
    except: quarterCAmount = 0
    self.quarterCWorthLab['text'] = round((quarterCAmount * 0.25), 2)
    #loonies
    try: loonieCAmount = self.looniesC.get()
    except: loonieCAmount = 0
    self.loonieCWorthLab['text'] = round((loonieCAmount * 1.0), 2)
    #toonies
    try: toonieCAmount = self.tooniesC.get()
    except: toonieCAmount = 0
    self.toonieCWorthLab['text'] = round((toonieCAmount * 2.0), 2)
    #5 dollar bill
    try: fiveCAmount = self.fiveC.get()
    except: fiveCAmount = 0
    self.fiveCWorthLab['text'] = round((fiveCAmount * 5.0), 2)
    #10 dollar bill
    try: tenCAmount = self.tenC.get()
    except: tenCAmount = 0
    self.tenCWorthLab['text'] = round((tenCAmount * 10.0), 2)
    #20 dollar bill
    try: twentyCAmount = self.twentyC.get()
    except: twentyCAmount = 0
    self.twentyCWorthLab['text'] = round((twentyCAmount * 20.0), 2)
    #50 dollar bill
    try: fiftyCAmount = self.fiftyC.get()
    except: fiftyCAmount = 0
    self.fiftyCWorthLab['text'] = round((fiftyCAmount * 50.0), 2)
    #total
    self.CalculateTotalC = self.nickelCWorthLab['text'] + self.dimeCWorthLab['text'] + self.quarterCWorthLab['text'] + self.loonieCWorthLab['text'] + self.toonieCWorthLab['text'] + self.fiveCWorthLab['text'] + self.tenCWorthLab['text'] + self.twentyCWorthLab['text'] + self.fiftyCWorthLab['text']
    self.totalCLab['text'] = round((self.CalculateTotalC), 2)

    #grand total
    self.registerTotalLab['text'] = round((self.CalculateTotalA + self.CalculateTotalB + self.CalculateTotalC), 2)
    #float/net profit
    self.NetProfitLab['text'] = round((self.registerTotalLab['text'] - 489), 2)

  def delete(self): #delete 0.0 in entry boxes
    #register A
    self.nickelAEntry.delete(0, 'end')
    self.dimeAEntry.delete(0, 'end')
    self.quarterAEntry.delete(0, 'end')
    self.loonieAEntry.delete(0, 'end')
    self.toonieAEntry.delete(0, 'end')
    self.fiveAEntry.delete(0, 'end')
    self.tenAEntry.delete(0, 'end')
    self.twentyAEntry.delete(0, 'end')
    self.fiftyAEntry.delete(0, 'end')
    #register B
    self.nickelBEntry.delete(0, 'end')
    self.dimeBEntry.delete(0, 'end')
    self.quarterBEntry.delete(0, 'end')
    self.loonieBEntry.delete(0, 'end')
    self.toonieBEntry.delete(0, 'end')
    self.fiveBEntry.delete(0, 'end')
    self.tenBEntry.delete(0, 'end')
    self.twentyBEntry.delete(0, 'end')
    self.fiftyBEntry.delete(0, 'end')
    #register C
    self.nickelCEntry.delete(0, 'end')
    self.dimeCEntry.delete(0, 'end')
    self.quarterCEntry.delete(0, 'end')
    self.loonieCEntry.delete(0, 'end')
    self.toonieCEntry.delete(0, 'end')
    self.fiveCEntry.delete(0, 'end')
    self.tenCEntry.delete(0, 'end')
    self.twentyCEntry.delete(0, 'end')
    self.fiftyCEntry.delete(0, 'end')
    #delete 0.0 in punch card entry boxes
    self.punchCardAEntry.delete(0, 'end') 
    self.punchCardBEntry.delete(0, 'end')
    self.punchCardCEntry.delete(0, 'end')   
    #delete 0.0 in vouchers entry boxes
    self.voucherAEntry.delete(0, 'end')
    self.voucherBEntry.delete(0, 'end')
    self.voucherCEntry.delete(0, 'end')

  
  main_lst=[]

  def addData(self): #add data to csv file
   lst=[self.NetProfitLab['text'], self.punchCardTotalLabel['text'], self.voucherTotalLabel['text']]
   lst1=[]
   self.main_lst.append(lst)
   tk.messagebox.showinfo("Information","The data has been successfully added")

  def saveData(self): #save data to csv file
   with open("AutoCashierData.xlsx","w") as file:
      Writer=writer(file)
      Writer.writerow(["Net Profit (-$489 float)\n" "Punch Cards Total\n" "Vouchers Total\n"])
      Writer.writerow(self.main_lst)
      tk.messagebox.showinfo("Information", "The data has been succesfully saved")

from csv import writer
from tkinter import messagebox
  

    