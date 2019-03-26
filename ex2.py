import tkinter as tk

def helloCallBack():
  print( "Hello Python", "Hello World")
  
root = tk.Tk()

lbl1 = tk.Label(root,text="ระบบกำลังเริ่มทำงาน")

B = tk.Button(root, text ="Hello", command = helloCallBack)

B.pack()
lbl1.pack()
root.mainloop()
