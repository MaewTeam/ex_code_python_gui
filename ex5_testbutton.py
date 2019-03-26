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



B1 = tk.Button(root, text ="On LED 1", command = onLED1CallBack)
B2 = tk.Button(root, text ="Off LED 1", command = offLED1CallBack)
B3 = tk.Button(root, text ="On LED 2", command = onLED2CallBack)
B4 = tk.Button(root, text ="Off LED 2", command = offLED2CallBack)
B5 = tk.Button(root, text ="On LED 3", command = onLED3CallBack)
B6 = tk.Button(root, text ="Off LED 3", command = offLED3CallBack)
B7 = tk.Button(root, text ="On LED 4", command = onLED4CallBack)
B8 = tk.Button(root, text ="Off LED 4", command = offLED4CallBack)

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
B6.pack()
B7.pack()
B8.pack()

root.mainloop()
