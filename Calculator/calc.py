"""
    Projeto calculadora -> usando o Tkinter
"""
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        #self.createButton()
        self.createCalc()
       
        
    def createCalc(self):
        self.result = tk.Entry(self.master,width=36)
        self.result.grid(row=1,column=0,padx=5,pady=10,ipady=5)    
        bottons = [
                   "7","8","9","C",
                   "4","5","6","*",
                   "1","2","3","/",
                   "0","-","+","="
                   ]
        i, j = 1, 1
        for btn in bottons:
            pressButton = lambda x=btn:self.calculator(x)
            self.btnCalc = tk.Button(self,text=btn,width=6,height=2,command=pressButton)
            self.btnCalc.grid(row=i,column=j)
            if j >= 4:   
                i+=1
                j=0                        
            j+=1
            
    def calculator(self,value):
        if value == "=":
            try:
                calculation = eval(self.result.get())
                self.result.insert(tk.END,"="+str(calculation))
            except:
                self.result.insert(tk.END, "ERROR")
        elif value == "C" or value == "c":
            self.result.delete(0, tk.END)
        else:
            if "=" in self.result.get():
               self.result.delete(0, tk.END)     
            self.result.insert(tk.END,value)
    
            
root = tk.Tk()

myApp = App(master=root)
myApp.master.title("Calculadora")
#myApp.master.geometry("800x600")

myApp.mainloop()