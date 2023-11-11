from tkinter import *
import math

def leftClick(event):
    hight = math.pow(float(txtHight.get())/100,2)
    weight = float(txtWeight.get())
    resultBMI = round(float(weight / hight) , 1)
    text = ""
    if resultBMI >= 30 :
        text = "อ้วนมาก ( BMI :  " + str(resultBMI) + " )"
    elif resultBMI >= 25 and resultBMI <= 29.9:
      text = "อ้วน ( BMI : " + str(resultBMI) + " )"
    elif resultBMI >= 23 and resultBMI <= 24.9:
        text = "น้ำหนักเกิน ( BMI : " + str(resultBMI) + " )"
    elif resultBMI >= 18.6 and resultBMI <= 22.9:
        text = "น้ำหนักปกติ เหมาะสม ( BMI : " + str(resultBMI) + " )"
    elif resultBMI <=18.5:
        text = "ผอมเกินไป ( BMI : " + str(resultBMI) + " )"
        
    labelResult.configure(text=text)

mainWindows = Tk()

labelHight = Label(mainWindows,text="ส่วนสูง (cm.)")
labelHight.grid(row=1,column=0)

txtHight = Entry(mainWindows)
txtHight.grid(row=1,column=1)

labelWeight = Label(mainWindows,text="น้ำหนัก (kg.)")
labelWeight.grid(row=2,column=0)

txtWeight = Entry(mainWindows)
txtWeight.grid(row=2,column=1)
btn = Button(mainWindows,text="คำนวณ")
btn.bind("<Button-1>",leftClick)
btn.grid(row=3)

labelResult = Label(mainWindows)
labelResult.grid(row=3,column=1)


mainWindows.mainloop()