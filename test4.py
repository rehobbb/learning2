import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"结果: {result}")
    except ValueError:
        result_label.config(text="请输入数字！")

root = tk.Tk()
root.title("加法计算器")
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
tk.Button(root, text="计算", command=calculate).pack()
result_label = tk.Label(root, text="结果将显示在这里")
entry1.pack(padx=10, pady=5)
entry2.pack(padx=10, pady=5)
result_label.pack(pady=10)
root.mainloop()