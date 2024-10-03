import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.configure(bg='#f0f0f0')
        
        self.display = tk.Entry(master, font=('Courier', 20), justify='right', bd=5)
        self.display.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky='nsew')
        
        self.create_buttons()
        self.history = []
        
    def create_buttons(self):
        button_list = [
            'C', '√', '^', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', 'sin',
            'cos', 'tan', 'log', 'ln'
        ]
        
        row = 1
        col = 0
        for button in button_list:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.master, text=button, command=cmd, font=('Courier', 14), 
                      width=5, height=2, bg='#e0e0e0', activebackground='#d0d0d0'
                     ).grid(row=row, column=col, sticky='nsew')
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1)
        
    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.history.append(f"{self.display.get()} = {result}")
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == 'C':
            self.display.delete(0, tk.END)
        elif key in ['sin', 'cos', 'tan', 'log', 'ln', '√']:
            try:
                num = float(self.display.get())
                if key == 'sin':
                    result = math.sin(math.radians(num))
                elif key == 'cos':
                    result = math.cos(math.radians(num))
                elif key == 'tan':
                    result = math.tan(math.radians(num))
                elif key == 'log':
                    result = math.log10(num)
                elif key == 'ln':
                    result = math.log(num)
                elif key == '√':
                    result = math.sqrt(num)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, key)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()