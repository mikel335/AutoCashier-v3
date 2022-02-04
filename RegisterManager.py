import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

#from csv import messagebox

class RegisterManager:
  def __init__(self, root, frame):
    self.root = root
    self.frame = frame
    self.main_lst=[]

    self.registerA = tk.Label(self.frame, text="Register A", bg="#44505A", fg="white", font="timesnewroman").place(relx=0,rely=0)
    self.registerB = tk.Label(self.frame, text="Register B", bg="#44505A", fg="white", font="timesnewroman").place(relx=0.34, rely=0)
    self.registerC = tk.Label(self.frame, text="Register C", bg="#44505A", fg="white", font="timesnewroman").place(relx=0.67, rely=0)
    
    self.separator = ttk.Separator(orient="horizontal").place(relx=0, rely=0.48, relwidth=2, relheight=0.003)

    #register A
    #nickels-----------------------------
    self.nickelsA = tk.DoubleVar()
    self.nickelsA.trace_add("write", self.calculate)
    self.nickelAEntry = tk.Entry(self.frame, textvariable=self.nickelsA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.nickelAEntry.place(relx=0, rely=0.035)
    self.nickelALab = tk.Label(self.frame, text="Nickels:    $", bg="#44505A", fg='white').place(relx=0.07, rely=0.035)
    self.nickelAWorthLab = tk.Label(self.frame, text=self.nickelsA.get())
    self.nickelAWorthLab.place(relx=0.15, rely=0.035)
    #dimes-----------------------------
    self.dimesA = tk.DoubleVar()
    self.dimesA.trace_add("write", self.calculate)
    self.dimeAEntry = tk.Entry(self.frame, textvariable=self.dimesA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.dimeAEntry.place(relx=0, rely=0.07)
    self.dimeALabel = tk.Label(self.frame, text="Dimes:     $", bg="#44505A", fg='white').place(relx=0.07, rely=0.07)
    self.dimeAWorthLab = tk.Label(self.frame, text=self.dimesA.get())
    self.dimeAWorthLab.place(relx=0.15, rely=0.07)
    #quarter----------------------------------
    self.quartersA = tk.DoubleVar()
    self.quartersA.trace_add("write", self.calculate)
    self.quarterAEntry = tk.Entry(self.frame, textvariable=self.quartersA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.quarterAEntry.place(relx=0, rely=0.105)
    self.quarterALabel = tk.Label(self.frame,text="Quarters: $", bg="#44505A", fg='white').place(relx=0.07, rely=0.105)
    self.quarterAWorthLab = tk.Label(self.frame, text=self.quartersA.get())
    self.quarterAWorthLab.place(relx=0.15, rely=0.105)
    #loonies----------------------------------
    self.looniesA = tk.DoubleVar()
    self.looniesA.trace_add("write", self.calculate)
    self.loonieAEntry = tk.Entry(self.frame, textvariable=self.looniesA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.loonieAEntry.place(relx=0, rely=0.14)
    self.loonieALabel = tk.Label(self.frame, text="Loonies:   $", bg="#44505A", fg='white').place(relx=0.07, rely=0.14)
    self.loonieAWorthLab = tk.Label(self.frame, text=self.looniesA.get())
    self.loonieAWorthLab.place(relx=0.15, rely=0.14)
    #toonies----------------------------------
    self.tooniesA = tk.DoubleVar()
    self.tooniesA.trace_add("write", self.calculate)
    self.toonieAEntry = tk.Entry(self.frame, textvariable=self.tooniesA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.toonieAEntry.place(relx=0, rely=0.175)
    self.toonieALabel = tk.Label(self.frame, text="Toonies:   $", bg="#44505A", fg='white').place(relx=0.07, rely=0.175)
    self.toonieAWorthLab = tk.Label(self.frame, text=self.tooniesA.get())
    self.toonieAWorthLab.place(relx=0.15, rely=0.175)
    #$5 bill----------------------------------
    self.fiveA = tk.DoubleVar()
    self.fiveA.trace_add("write", self.calculate)
    self.fiveAEntry = tk.Entry(self.frame, textvariable=self.fiveA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiveAEntry.place(relx=0, rely=0.21)
    self.fiveALabel = tk.Label(self.frame, text="$5 Bill:     $", bg="#44505A", fg='white').place(relx=0.07, rely=0.21)
    self.fiveAWorthLab = tk.Label(self.frame, text=self.fiveA.get())
    self.fiveAWorthLab.place(relx=0.15, rely=0.21)
    #$10 bill----------------------------------
    self.tenA = tk.DoubleVar()
    self.tenA.trace_add("write", self.calculate)
    self.tenAEntry = tk.Entry(self.frame, textvariable=self.tenA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.tenAEntry.place(relx=0, rely=0.245)
    self.tenALabel = tk.Label(self.frame, text="$10 Bill:   $", bg="#44505A", fg='white').place(relx=0.07, rely=0.245)
    self.tenAWorthLab = tk.Label(self.frame, text=self.tenA.get())
    self.tenAWorthLab.place(relx=0.15, rely=0.245)
    #$20 bill----------------------------------
    self.twentyA = tk.DoubleVar()
    self.twentyA.trace_add("write", self.calculate)
    self.twentyAEntry = tk.Entry(self.frame, textvariable=self.twentyA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.twentyAEntry.place(relx=0, rely=0.28)
    self.twentyALabel = tk.Label(self.frame, text="$20 Bill:   $", bg="#44505A", fg='white').place(relx=0.07, rely=0.28)
    self.twentyAWorthLab = tk.Label(self.frame, text=self.twentyA.get())
    self.twentyAWorthLab.place(relx=0.15, rely=0.28)
    #$50 bill----------------------------------
    self.fiftyA = tk.DoubleVar()
    self.fiftyA.trace_add("write", self.calculate)
    self.fiftyAEntry = tk.Entry(self.frame, textvariable=self.fiftyA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiftyAEntry.place(relx=0, rely=0.315)
    self.fiftyALabel = tk.Label(self.frame,text="$50 Bill:   $", bg="#44505A", fg='white').place(relx=0.07, rely=0.315)
    self.fiftyAWorthLab = tk.Label(self.frame,text=self.fiftyA.get())
    self.fiftyAWorthLab.place(relx=0.15, rely=0.315)
    #total-----------------------------------
    self.totalWord = tk.Label(self.frame, text="Total (-$163 float):  $", bg="#44505A", fg='white').place(relx=0, rely=0.37)
    self.totalA = self.nickelsA.get() + self.dimesA.get() + self.quartersA.get() + self.looniesA.get() + self.tooniesA.get() + self.fiveA.get()  + self.tenA.get() + self.twentyA.get()  + self.fiftyA.get()
    self.totalALab = tk.Label(self.frame, text=self.totalA)
    self.totalALab.place(relx=0.15, rely=0.37)
    #Register B
    #nickels B-----------------------------
    self.nickelsB = tk.DoubleVar()
    self.nickelsB.trace_add("write", self.calculate)
    self.nickelBEntry = tk.Entry(self.frame, textvariable=self.nickelsB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.nickelBEntry.place(relx=0.34, rely=0.035)
    self.nickelBLab = tk.Label(self.frame,text="Nickels:    $", bg="#44505A", fg='white').place(relx=0.41, rely=0.035)
    self.nickelBWorthLab = tk.Label(self.frame,text=self.nickelsB.get())
    self.nickelBWorthLab.place(relx=0.49, rely=0.035)
    #dimes B----------------------------------
    self.dimesB = tk.DoubleVar()
    self.dimesB.trace_add("write", self.calculate)
    self.dimeBEntry = tk.Entry(self.frame,textvariable=self.dimesB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.dimeBEntry.place(relx=0.34, rely=0.07)
    self.dimeBLabel = tk.Label(self.frame,text="Dimes:     $", bg="#44505A", fg='white').place(relx=0.41, rely=0.07)
    self.dimeBWorthLab = tk.Label(self.frame,text=self.dimesB.get())
    self.dimeBWorthLab.place(relx=0.49, rely=0.07)
    #quarter----------------------------------
    self.quartersB = tk.DoubleVar()
    self.quartersB.trace_add("write", self.calculate)
    self.quarterBEntry = tk.Entry(self.frame,textvariable=self.quartersB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.quarterBEntry.place(relx=0.34, rely=0.105)
    self.quarterBLabel = tk.Label(self.frame,text="Quarters: $", bg="#44505A", fg='white').place(relx=0.41, rely=0.105)
    self.quarterBWorthLab = tk.Label(self.frame,text=self.quartersB.get())
    self.quarterBWorthLab.place(relx=0.49, rely=0.105)
    #loonies----------------------------------
    self.looniesB = tk.DoubleVar()
    self.looniesB.trace_add("write", self.calculate)
    self.loonieBEntry = tk.Entry(self.frame,textvariable=self.looniesB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.loonieBEntry.place(relx=0.34, rely=0.14)
    self.loonieBLabel = tk.Label(self.frame,text="Loonies:   $", bg="#44505A", fg='white').place(relx=0.41, rely=0.14)
    self.loonieBWorthLab = tk.Label(self.frame,text=self.looniesB.get())
    self.loonieBWorthLab.place(relx=0.49, rely=0.14)
    #toonies----------------------------------
    self.tooniesB = tk.DoubleVar()
    self.tooniesB.trace_add("write", self.calculate)
    self.toonieBEntry = tk.Entry(self.frame,textvariable=self.tooniesB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.toonieBEntry.place(relx=0.34, rely=0.175)
    self.toonieBLabel = tk.Label(self.frame,text="Toonies:   $", bg="#44505A", fg='white').place(relx=0.41, rely=0.175)
    self.toonieBWorthLab = tk.Label(self.frame,text=self.tooniesB.get())
    self.toonieBWorthLab.place(relx=0.49, rely=0.175)
    #$5 bill----------------------------------
    self.fiveB = tk.DoubleVar()
    self.fiveB.trace_add("write", self.calculate)
    self.fiveBEntry = tk.Entry(self.frame,textvariable=self.fiveB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiveBEntry.place(relx=0.34, rely=0.21)
    self.fiveBLabel = tk.Label(self.frame,text="$5 Bill:     $", bg="#44505A", fg='white').place(relx=0.41, rely=0.21)
    self.fiveBWorthLab = tk.Label(self.frame,text=self.fiveB.get())
    self.fiveBWorthLab.place(relx=0.49, rely=0.21)
    #$10 bill----------------------------------
    self.tenB = tk.DoubleVar()
    self.tenB.trace_add("write", self.calculate)
    self.tenBEntry = tk.Entry(self.frame,textvariable=self.tenB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.tenBEntry.place(relx=0.34, rely=0.245)
    self.tenBLabel = tk.Label(self.frame,text="$10 Bill:   $", bg="#44505A", fg='white').place(relx=0.41, rely=0.245)
    self.tenBWorthLab = tk.Label(self.frame,text=self.tenB.get())
    self.tenBWorthLab.place(relx=0.49, rely=0.245)
    #$20 bill----------------------------------
    self.twentyB = tk.DoubleVar()
    self.twentyB.trace_add("write", self.calculate)
    self.twentyBEntry = tk.Entry(self.frame,textvariable=self.twentyB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.twentyBEntry.place(relx=0.34, rely=0.28)
    self.twentyBLabel = tk.Label(self.frame,text="$20 Bill:   $", bg="#44505A", fg='white').place(relx=0.41, rely=0.28)
    self.twentyBWorthLab = tk.Label(self.frame,text=self.twentyB.get())
    self.twentyBWorthLab.place(relx=0.49, rely=0.28)
    #$50 bill----------------------------------
    self.fiftyB = tk.DoubleVar()
    self.fiftyB.trace_add("write", self.calculate)
    self.fiftyBEntry = tk.Entry(self.frame,textvariable=self.fiftyB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiftyBEntry.place(relx=0.34, rely=0.315)
    self.fiftyBLabel = tk.Label(self.frame,text="$50 Bill:   $", bg="#44505A", fg='white').place(relx=0.41, rely=0.315)
    self.fiftyBWorthLab = tk.Label(self.frame,text=self.fiftyB.get())
    self.fiftyBWorthLab.place(relx=0.49, rely=0.315)
    #total-----------------------------------
    self.totalBWord = tk.Label(self.frame,text="Total (-$163 float):  $", bg="#44505A", fg='white').place(relx=0.34, rely=0.37)
    self.totalB = self.nickelsB.get() + self.dimesB.get() + self.quartersB.get() + self.looniesB.get() + self.tooniesB.get() + self.fiveB.get()  + self.tenB.get() + self.twentyB.get()  + self.fiftyB.get()
    self.totalBLab = tk.Label(self.frame,text=self.totalB)
    self.totalBLab.place(relx=0.49, rely=0.37)
    #Register C
    #nickels-----------------------------
    self.nickelsC = tk.DoubleVar()
    self.nickelsC.trace_add("write", self.calculate)
    self.nickelCEntry = tk.Entry(self.frame,textvariable=self.nickelsC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.nickelCEntry.place(relx=0.67, rely=0.035)
    self.nickelCLab = tk.Label(self.frame,text="Nickels:    $", bg="#44505A", fg='white').place(relx=0.74, rely=0.035)
    self.nickelCWorthLab = tk.Label(self.frame,text=self.nickelsC.get())
    self.nickelCWorthLab.place(relx=0.82, rely=0.035)
    #dimes----------------------------------
    self.dimesC = tk.DoubleVar()
    self.dimesC.trace_add("write", self.calculate)
    self.dimeCEntry = tk.Entry(self.frame,textvariable=self.dimesC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.dimeCEntry.place(relx=0.67, rely=0.07)
    self.dimeCLabel = tk.Label(self.frame,text="Dimes:     $", bg="#44505A", fg='white').place(relx=0.74, rely=0.07)
    self.dimeCWorthLab = tk.Label(self.frame,text=self.dimesC.get())
    self.dimeCWorthLab.place(relx=0.82, rely=0.07)
    #quarter----------------------------------
    self.quartersC = tk.DoubleVar()
    self.quartersC.trace_add("write", self.calculate)
    self.quarterCEntry = tk.Entry(self.frame,textvariable=self.quartersC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.quarterCEntry.place(relx=0.67, rely=0.105)
    self.quarterCLabel = tk.Label(self.frame,text="Quarters: $", bg="#44505A", fg='white').place(relx=0.74, rely=0.105)
    self.quarterCWorthLab = tk.Label(self.frame,text=self.quartersC.get())
    self.quarterCWorthLab.place(relx=0.82, rely=0.105)
    #loonies----------------------------------
    self.looniesC = tk.DoubleVar()
    self.looniesC.trace_add("write", self.calculate)
    self.loonieCEntry = tk.Entry(self.frame,textvariable=self.looniesC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.loonieCEntry.place(relx=0.67, rely=0.14)
    self.loonieCLabel = tk.Label(self.frame,text="Loonies:   $", bg="#44505A", fg='white').place(relx=0.74, rely=0.14)
    self.loonieCWorthLab = tk.Label(self.frame,text=self.looniesC.get())
    self.loonieCWorthLab.place(relx=0.82, rely=0.14)
    #toonies----------------------------------
    self.tooniesC = tk.DoubleVar()
    self.tooniesC.trace_add("write", self.calculate)
    self.toonieCEntry = tk.Entry(self.frame,textvariable=self.tooniesC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.toonieCEntry.place(relx=0.67, rely=0.175)
    self.toonieCLabel = tk.Label(self.frame,text="Toonies:   $", bg="#44505A", fg='white').place(relx=0.74, rely=0.175)
    self.toonieCWorthLab = tk.Label(self.frame,text=self.tooniesC.get())
    self.toonieCWorthLab.place(relx=0.82, rely=0.175)
    #$5 bill----------------------------------
    self.fiveC = tk.DoubleVar()
    self.fiveC.trace_add("write", self.calculate)
    self.fiveCEntry = tk.Entry(self.frame,textvariable=self.fiveC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiveCEntry.place(relx=0.67, rely=0.21)
    self.fiveCLabel = tk.Label(self.frame,text="$5 Bill:     $", bg="#44505A", fg='white').place(relx=0.74, rely=0.21)
    self.fiveCWorthLab = tk.Label(self.frame,text=self.fiveC.get())
    self.fiveCWorthLab.place(relx=0.82, rely=0.21)
    #$10 bill----------------------------------
    self.tenC = tk.DoubleVar()
    self.tenC.trace_add("write", self.calculate)
    self.tenCEntry = tk.Entry(self.frame,textvariable=self.tenC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.tenCEntry.place(relx=0.67, rely=0.245)
    self.tenCLabel = tk.Label(self.frame,text="$10 Bill:   $", bg="#44505A", fg='white').place(relx=0.74, rely=0.245)
    self.tenCWorthLab = tk.Label(self.frame,text=self.tenC.get())
    self.tenCWorthLab.place(relx=0.82, rely=0.245)
    #$20 bill----------------------------------
    self.twentyC = tk.DoubleVar()
    self.twentyC.trace_add("write", self.calculate)
    self.twentyCEntry = tk.Entry(self.frame,textvariable=self.twentyC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.twentyCEntry.place(relx=0.67, rely=0.28)
    self.twentyCLabel = tk.Label(self.frame,text="$20 Bill:   $", bg="#44505A", fg='white').place(relx=0.74, rely=0.28)
    self.twentyCWorthLab = tk.Label(self.frame,text=self.twentyC.get())
    self.twentyCWorthLab.place(relx=0.82, rely=0.28)
    #$50 bill----------------------------------
    self.fiftyC = tk.DoubleVar()
    self.fiftyC.trace_add("write", self.calculate)
    self.fiftyCEntry = tk.Entry(self.frame,textvariable=self.fiftyC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.fiftyCEntry.place(relx=0.67, rely=0.315)
    self.fiftyCLabel = tk.Label(self.frame,text="$50 Bill:   $", bg="#44505A", fg='white').place(relx=0.74, rely=0.315)
    self.fiftyCWorthLab = tk.Label(self.frame,text=self.fiftyC.get())
    self.fiftyCWorthLab.place(relx=0.82, rely=0.315)
    #total-----------------------------------
    self.totalCWord = tk.Label(self.frame,text="Total (-$163 float):  $", bg="#44505A", fg='white').place(relx=0.67, rely=0.37)
    self.totalC = self.nickelsC.get() + self.dimesC.get() + self.quartersC.get() + self.looniesC.get() + self.tooniesC.get() + self.fiveC.get()  + self.tenC.get() + self.twentyC.get()  + self.fiftyC.get()
    self.totalCLab = tk.Label(self.frame,text=self.totalC)
    self.totalCLab.place(relx=0.82, rely=0.37)

    #grand total------------------------------
    self.registerTotal = tk.Label(self.frame,text="Total of all registers:", bg="#44505A", fg='white').place(relx=0, rely=0.79)
    self.grandTotal = self.totalA + self.totalB + self.totalC
    self.registerTotalLab = tk.Label(self.frame,text = self.grandTotal)
    self.registerTotalLab.place(relx=0.15, rely=0.79)
    #float/net profit-------------------------------------
    self.floatAndNet = tk.DoubleVar()
    self.floatAndNet.trace_add("write", self.calculate)
    self.NetProfitText = tk.Label(self.frame, text= "Net Profit (-$489 float): ", bg="#44505A", fg='white').place(relx=0, rely=0.85)
    self.NetProfitLab = tk.Label(self.frame, text=(self.floatAndNet.get()))
    self.NetProfitLab.place(relx=0.165, rely=0.85)

    #punch card total-----------------------------
    self.punchCardA = tk.DoubleVar()
    self.punchCardA.trace_add("write", self.calculate)
    self.punchCardALab = tk.Label(self.frame, text="Register A Punch Cards: $", bg="#44505A", fg='white').place(relx=0, rely=0.59)
    self.punchCardAEntry = tk.Entry(self.frame, textvariable=self.punchCardA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.punchCardAEntry.place(relx=0.17, rely=0.59)

    self.punchCardB = tk.DoubleVar()
    self.punchCardB.trace_add("write", self.calculate)
    self.punchCardBLab = tk.Label(self.frame, text="Register B Punch Cards: $", bg="#44505A", fg='white').place(relx=0, rely=0.62)
    self.punchCardBEntry = tk.Entry(self.frame,textvariable=self.punchCardB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.punchCardBEntry.place(relx=0.17, rely=0.62)

    self.punchCardC = tk.DoubleVar()
    self.punchCardC.trace_add("write", self.calculate)
    self.punchCardCLab = tk.Label(self.frame, text="Register C Punch Cards: $", bg="#44505A", fg='white').place(relx=0, rely=0.65)
    self.punchCardCEntry = tk.Entry(self.frame, textvariable=self.punchCardC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.punchCardCEntry.place(relx=0.17, rely=0.65)

    self.punchCardTotal = tk.Label(self.frame, text="Punch Cards Total:", bg="#44505A", fg='white').place(relx=0, rely=0.7)

    self.punchCardTotalLabel = tk.Label(self.frame, text="0.0")
    self.punchCardTotalLabel.place(relx=0.14, rely=0.7)

    #vouchers-----------------------------
    self.voucherA = tk.DoubleVar()
    self.voucherA.trace_add("write", self.calculate)
    self.voucherALab = tk.Label(self.frame, text="Register A Vouchers: $", bg="#44505A", fg='white').place(relx=0.3, rely=0.59)
    self.voucherAEntry = tk.Entry(self.frame, textvariable=self.voucherA, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.voucherAEntry.place(relx=0.46, rely=0.59)
    self.voucherAWorthLab = tk.Label(self.frame, text=self.voucherA.get())
    self.voucherAWorthLab.place(relx=0.54, rely=0.59)

    self.voucherB = tk.DoubleVar()
    self.voucherB.trace_add("write", self.calculate)
    self.voucherBLab = tk.Label(self.frame, text="Register B Vouchers: $", bg="#44505A", fg='white').place(relx=0.3, rely=0.62)
    self.voucherBEntry = tk.Entry(self.frame, textvariable=self.voucherB, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.voucherBEntry.place(relx=0.46, rely=0.62)
    self.voucherBWorthLab = tk.Label(self.frame, text=self.voucherB.get())
    self.voucherBWorthLab.place(relx=0.54, rely=0.62)

    self.voucherC = tk.DoubleVar()
    self.voucherC.trace_add("write", self.calculate)
    self.voucherCLab = tk.Label(self.frame, text="Register C Vouchers: $", bg="#44505A", fg='white').place(relx=0.3, rely=0.65)
    self.voucherCEntry = tk.Entry(self.frame, textvariable=self.voucherC, width="7", justify=tk.RIGHT, bg="lightgrey")
    self.voucherCEntry.place(relx=0.46, rely=0.65)
    self.voucherCWorthLab = tk.Label(self.frame, text=self.voucherC.get())
    self.voucherCWorthLab.place(relx=0.54, rely=0.65)

    self.voucherTotal = tk.Label(self.frame, text="Vouchers Total:", bg="#44505A", fg='white').place(relx=0.3, rely=0.7)

    self.voucherTotalLabel = tk.Label(self.frame, text=0.0)
    self.voucherTotalLabel.place(relx=0.425, rely=0.7)

    self.delete()
    #clear button
    self.clear = tk.Button(self.frame, text="Clear", command=self.delete) 
    self.clear.place(relx=0.02,rely=0.92)
    #add button
    self.add = tk.Button(self.frame, text="Add", command=self.addData) 
    self.add.place(relx=0.79,rely=0.92)
    #save button
    self.save = tk.Button(self.frame, text="Save", command=self.saveData) 
    self.save.place(relx=0.85,rely=0.92)

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
    self.totalALab['text'] = round((self.CalculateTotalA - 163), 2)
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
    self.totalBLab['text'] = round((self.CalculateTotalB - 163), 2)
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
    self.totalCLab['text'] = round((self.CalculateTotalC - 163), 2)
    
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

  main_curdate = []
  main_exportRegisterA = []
  main_exportRegisterB = []
  main_exportRegisterC = []

  main_exportABCTotals = []
  main_exportBTotals = []
  main_exportCTotals = []

  main_exportRegAPunchCards = []
  main_exportRegBPunchCards = []
  main_exportRegCPunchCards = []

  main_exportRegAVouchers = []
  main_exportRegBVouchers = []
  main_exportRegCVouchers = []

  main_exportRegAVoucherTotal = []
  main_exportRegBVoucherTotal = []
  main_exportRegCVoucherTotal = []

  main_exportNetProfit = []

  def addData(self): #add data to csv file
   
   #adds the data
   yesterday = datetime.now() - timedelta(1)
   type(yesterday)
   curdate = datetime.strftime(yesterday,'%Y %m %d')  
   #amount of coins and $bills in registers
   exportRegisterA = "[REGISTER A] " + "[Nickel Amount: " + self.nickelAEntry.get() + "] | " + "[Dime Amount: " + self.dimeAEntry.get() + "] | " + "[Quarter Amount: " + self.quarterAEntry.get() + "] | " + "[Loonie Amount: " + self.loonieAEntry.get() + "] | " + "[Toonie Amount: " + self.toonieAEntry.get() + "] | " + "[$5 Bill Amount: " + self.fiveAEntry.get() + "] | " + "[$10 Bill Amount: " + self.tenAEntry.get() + "] | " + "[$20 Bill Amount: " + self.twentyAEntry.get() + "] | " + "[$50 Bill Amount: " + self.fiftyAEntry.get() + "]\n" 
   exportRegisterB = "[REGISTER B] " + "[Nickel Amount: " + self.nickelBEntry.get() + "] | " + "[Dime Amount: " + self.dimeBEntry.get() + "] | " + "[Quarter Amount: " + self.quarterBEntry.get() + "] | " + "[Loonie Amount: " + self.loonieBEntry.get() + "] | " + "[Toonie Amount: " + self.toonieBEntry.get() + "] | " + "[$5 Bill Amount: " + self.fiveBEntry.get() + "] | " + "[$10 Bill Amount: " + self.tenBEntry.get() + "] | " + "[$20 Bill Amount: " + self.twentyBEntry.get() + "] | " + "[$50 Bill Amount: " + self.fiftyBEntry.get() + "]\n"
   exportRegisterC = "[REGISTER C] " + "[Nickel Amount: " + self.nickelCEntry.get() + "] | " + "[Dime Amount: " + self.dimeCEntry.get() + "] | " + "[Quarter Amount: " + self.quarterCEntry.get() + "] | " + "[Loonie Amount: " + self.loonieCEntry.get() + "] | " + "[Toonie Amount: " + self.toonieCEntry.get() + "] | " + "[$5 Bill Amount: " + self.fiveCEntry.get() + "] | " + "[$10 Bill Amount: " + self.tenCEntry.get() + "] | " + "[$20 Bill Amount: " + self.twentyCEntry.get() + "] | " + "[$50 Bill Amount: " + self.fiftyCEntry.get() + "]"
   #punch cards and vouchers
   exportRegAPunchCards = "[REGISTER A PUNCH CARDS] $" + self.punchCardAEntry.get() 
   exportRegBPunchCards = "[REGISTER B PUNCH CARDS] $" + self.punchCardBEntry.get() 
   exportRegCPunchCards = "[REGISTER C PUNCH CARDS] $" + self.punchCardCEntry.get()

   exportRegAVouchers = "[REGISTER A VOUCHERS] " + self.voucherAEntry.get() 
   exportRegBVouchers = "[REGISTER B VOUCHERS] " + self.voucherBEntry.get() 
   exportRegCVouchers = "[REGISTER C VOUCHERS] " + self.voucherCEntry.get()

   exportRegAVoucherTotal = ["Register A Voucher Total:  $", self.voucherAWorthLab['text']] 
   exportRegBVoucherTotal = ["Register B Voucher Total: $", self.voucherBWorthLab['text']] 
   exportRegCVoucherTotal = ["Register C Voucher Total: $", self.voucherCWorthLab['text']]
   #total amount of money in each register
   exportABCTotals = ["Register A Total: ", self.totalALab['text']]
   exportBTotals = ["Register B Total: ", self.totalBLab['text']]
   exportCTotals = ["Register C Total: ", self.totalCLab['text']]

   exportNetProfit = ["NET PROFIT: $", self.NetProfitLab['text']] 

   self.main_curdate.append(curdate)
   self.main_exportRegisterA.append(exportRegisterA)
   self.main_exportRegisterB.append(exportRegisterB)
   self.main_exportRegisterC.append(exportRegisterC)
   self.main_exportABCTotals.append(exportABCTotals)
   self.main_exportBTotals.append(exportBTotals)
   self.main_exportCTotals.append(exportCTotals)

   self.main_exportRegAPunchCards.append(exportRegAPunchCards)
   self.main_exportRegBPunchCards.append(exportRegBPunchCards)
   self.main_exportRegCPunchCards.append(exportRegCPunchCards)

   self.main_exportRegAVouchers.append(exportRegAVouchers)
   self.main_exportRegBVouchers.append(exportRegBVouchers)
   self.main_exportRegCVouchers.append(exportRegCVouchers)

   self.main_exportRegAVoucherTotal.append(exportRegAVoucherTotal)
   self.main_exportRegBVoucherTotal.append(exportRegBVoucherTotal)
   self.main_exportRegCVoucherTotal.append(exportRegCVoucherTotal)

   self.main_exportNetProfit.append(exportNetProfit)
   tk.messagebox.showinfo("Information","The data has been successfully added")

  def saveData(self): #save data to csv file
   yesterday = datetime.now() - timedelta(1)
   type(yesterday)
   curdate = datetime.strftime(yesterday,'%Y %m %d')
   with open(curdate + " AutoCashier_Data.csv","w") as file:
      Writer = writer(file)
      #add the names of the data
      Writer.writerow(self.main_curdate)
      Writer.writerow(self.main_exportRegisterA)
      Writer.writerow(self.main_exportRegisterB)
      Writer.writerow(self.main_exportRegisterC)
      Writer.writerow(self.main_exportABCTotals)
      Writer.writerow(self.main_exportBTotals)
      Writer.writerow(self.main_exportCTotals)
      
      Writer.writerow(self.main_exportRegAPunchCards)
      Writer.writerow(self.main_exportRegBPunchCards)
      Writer.writerow(self.main_exportRegCPunchCards)

      Writer.writerow(self.main_exportRegAVouchers)
      Writer.writerow(self.main_exportRegBVouchers)
      Writer.writerow(self.main_exportRegCVouchers)

      Writer.writerow(self.main_exportRegAVoucherTotal)
      Writer.writerow(self.main_exportRegBVoucherTotal)
      Writer.writerow(self.main_exportRegCVoucherTotal)
      Writer.writerow(self.main_exportNetProfit)
      tk.messagebox.showinfo("Information", "The data has been succesfully saved")

from csv import writer
from tkinter import messagebox
  

    