import tkinter as tk
import tkinter.messagebox as tkmsg

def helloCallBack():
  print( "Hello Python", "Hello World")
  tk.messagebox.showinfo("ข้อความส่วนหัว","ข้อความส่วนอธิบายผล")
  
def onLED1CallBack():
  tk.messagebox.showinfo("Output","หลอดLED 1 ติด")
def offLED1CallBack():
  tk.messagebox.showinfo("Output","หลอดLED 1 ดับ")
def onLED2CallBack():
  tk.messagebox.showinfo("Output","หลอดLED 2 ติด")
def offLED2CallBack():
  tk.messagebox.showinfo("Output","หลอดLED 2 ดับ")
def onLED3CallBack():
  tk.messagebox.showinfo("Output","หลอดLED 3 ติด")
def offLED3CallBack():
  tk.messagebox.showinfo("Output","หลอดLED 3 ดับ")
def onLED4CallBack():
  tk.messagebox.showinfo("Output","หลอดLED 4 ติด")
def offLED4CallBack():
  tk.messagebox.showinfo("Output","หลอดLED 4 ดับ")  

  
root = tk.Tk()

lbl1 = tk.Label(root,text="ระบบกำลังเริ่มทำงาน")

f1 = tk.Frame(root, bd = 5, height = 50, width = 100, relief = GROOVE)
f1.pack(side=TOP)
B1 = tk.Button(f1, text ="On LED 1", command = onLED1CallBack)
B2 = tk.Button(f1, text ="Off LED 1", command = offLED1CallBack)
B3 = tk.Button(f1, text ="On LED 2", command = onLED2CallBack)
B4 = tk.Button(f1, text ="Off LED 2", command = offLED2CallBack)
f2 = tk.Frame(root, bd = 5, height = 50, width = 100, relief = GROOVE)
f2.pack(side=BOTTOM)
B5 = tk.Button(f2, text ="On LED 3", command = onLED3CallBack)
B6 = tk.Button(f2, text ="Off LED 3", command = offLED3CallBack)
B7 = tk.Button(f2, text ="On LED 4", command = onLED4CallBack)
B8 = tk.Button(f2, text ="Off LED 4", command = offLED4CallBack)

B1.pack(side=LEFT)
B2.pack(side=LEFT)
B3.pack(side=LEFT)
B4.pack(side=LEFT)
B5.pack(side=LEFT)
B6.pack(side=LEFT)
B7.pack(side=LEFT)
B8.pack(side=LEFT)

root.mainloop()
