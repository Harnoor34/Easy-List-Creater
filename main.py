import tkinter as tk

global element
global Dict_list

#Main Tkinter root config
tkinter_root = tk.Tk()
tkinter_root.configure(background="black")
tkinter_root.geometry("800x600")
tkinter_root.title("List GUI")
tkinter_root.minsize(width=800, height=600)
tkinter_root.maxsize(width=800, height=600)

element = tk.Entry(tkinter_root, foreground="white", background="black", font="CascadiaCodeItalic")
element.grid(column=3, row=3)

elements = tk.Entry(tkinter_root, foreground="white", background="black", font="CascadiaCodeItalic")
elements.grid(column=3, row=4)

class List:
    def __init__(self):
        self.Dict_list = {}
        self.lol: tk.Label

    #Used to create a list
    def create_list(self, name):
        self.Dict_list[name] = []

    #Used to print the list
    def print_list(self, name):
        self.lol = tk.Label(tkinter_root, text=f"{self.Dict_list[name]}", background="black", foreground="white", font="CascadiaCodeItalic", borderwidth=0)
        self.lol.grid(column=4, row=1)

    
    #Used to append an element in the list
    def append_element(self, name):
        try:
            self.Dict_list[name].append(element.get())

        except KeyError:
            tk.Label(tkinter_root, text=f"Please Create A List First.", background="black", foreground="white", font="CascadiaCodeItalic", borderwidth=0).grid(column=4, row=2)

    #Used to remove an element from the lilst
    def remove_element(self, name):
        try:
            self.Dict_list[name].remove(elements.get())

        except KeyError:
            tk.Label(tkinter_root, text=f"Please Create A List First.", background="black", foreground="white", font="CascadiaCodeItalic", borderwidth=0).grid(column=4, row=2)
        except ValueError:
            tk.Label(tkinter_root, text=f"This element is not in the list.", background="black", foreground="white", font="CascadiaCodeItalic", borderwidth=0).grid(column=4, row=2)

    #Used to clear the results
    def clear_it(self):
        self.lol.grid_remove()

    
Lists = List()

#Used To Get A Custom List Name
List_name = tk.Entry(tkinter_root, foreground="white", background="black", font="CascadiaCodeItalic")
List_name.grid(column=2,row=0)

#All The Labels Present Here    
tk.Label(tkinter_root, text="Results", background="black", foreground="white", font="CascadiaCodeItalic", borderwidth=0).grid(column=4, row=0)
tk.Label(tkinter_root, text="Enter Your List Name:", foreground="white", background="black", font="CascadiaCodeItalic").grid(column=1, row=0)
tk.Label(tkinter_root, text="Enter Your Element Name:", foreground="white", background="black", font="CascadiaCodeItalic", borderwidth=0).grid(column=2, row=4)
tk.Label(tkinter_root, text="Enter Your Element Name:", foreground="white", background="black", font="CascadiaCodeItalic", borderwidth=0).grid(column=2, row=3)

#All The Buttons Present Here
tk.Button(tkinter_root, text="Create List", command=lambda: Lists.create_list(List_name.get()), padx=52, font="CascadiaCodeItalic", background="Black", foreground="White", borderwidth=0).grid(column=1,row=1)
tk.Button(tkinter_root, text="Print List", command=lambda: Lists.print_list(List_name.get()), padx=60, font="CascadiaCodeItalic", background="Black", foreground="White", borderwidth=0).grid(column=1,row=2)
tk.Button(tkinter_root, text="Append an Element", command=lambda: Lists.append_element(List_name.get()), padx=22, font="CascadiaCodeItalic", background="Black", foreground="White", borderwidth=0).grid(column=1,row=3)
tk.Button(tkinter_root, text="Quit", command=quit, padx=80, font="CascadiaCodeItalic", background="Black", foreground="White", borderwidth=0).grid(column=1,row=6)    
tk.Button(tkinter_root, text="Remove an Element", command=lambda: Lists.remove_element(List_name.get()), padx=22, font="CascadiaCodeItalic", background="Black", foreground="White", borderwidth=0).grid(column=1,row=4)   
tk.Button(tkinter_root, text="Clear Results", command=Lists.clear_it, padx=50, font="CascadiaCodeItalic", background="Black", foreground="White", borderwidth=0).grid(column=1,row=5)
    
tkinter_root.mainloop()
