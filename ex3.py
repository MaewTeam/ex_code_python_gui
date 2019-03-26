import tkinter as tk

def helloCallBack():
  print( "Hello Python", "Hello World")
  
root = tk.Tk()

lbl1 = tk.Label(root,text="ระบบกำลังเริ่มทำงาน")

B1 = tk.Button(root, text ="Hello1", command = helloCallBack)
B2 = tk.Button(root, text ="Hello2", command = helloCallBack)
B3 = tk.Button(root, text ="Hello3", command = helloCallBack)

B1.pack(side = TOP)
B2.pack(side = RIGHT)
B3.pack(side = LEFT)

root.mainloop()
