"""
Table Common Components.

Author: Oleksii Dovhaniuk
Date: 15.07.2022
"""

import tkinter as tk


class ScrollableFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.canvas = canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        self.canvas_frame = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', self.upadateWidthCanvas)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=1)

    def upadateWidthCanvas(self, event):
        self.canvas.itemconfig(self.canvas_frame, width = event.width) 

class Row(tk.Frame):
    bg = 'white'
    placeholder = None
    empty_btn = None

    def __init__(self, master, bg=bg, index=' ', *args, **kwargs):
        super().__init__(master, bg=bg, *args, **kwargs)
        self.bg = bg
        self.index= index

        self.fillPlaceholder()

    def fillPlaceholder(self):
        if self.placeholder: self.clear()
        
        self.placeholder = tk.Frame(self, bg=self.bg)
        self.placeholder.pack(fill='x', side='bottom')

        self.empty_btn = tk.Button(self.placeholder, text=f'{self.index}', bg=self.bg, relief='flat', state='disabled')
        self.empty_btn.pack(fill='both', expand=1)

    def clear(self):
        self.placeholder.destroy()

class Table(tk.Frame):
    row_no = 32

    top = 0
    bg = 'white'
    bg_odd = '#F0F0F0'

    def __init__(self, master, row_no=row_no, bg=bg, bg_odd=bg_odd, *args, **kwargs):
        super().__init__(master, bg=bg, *args, **kwargs)
        self._rows = []
        self.bg = bg
        self.bg_odd = bg_odd

        self.scrollable_frame = ScrollableFrame(self)
        self.box = box = self.scrollable_frame.scrollable_frame

        for i in range(self.row_no):
            if i % 2:
                row = Row(box, bg=bg)
            else:
                row = Row(box, bg=self.bg_odd)
            
            row.pack(fill='x')
            self._rows.append(row)
        
        self.scrollable_frame.pack(fill='both', expand=1)

    def getTop(self):
        row = self._rows[self.top]
        self.top += 1
        
        return row

    def getRow(self, index):
        print(f'[getRow]: {self} <<<{self._rows[index]}>>>')
        return self._rows[index]


    def getBg(self, index=None):
        if index == None:
            return self._rows[self.top-1].bg
        else:
            return self._rows[index].bg