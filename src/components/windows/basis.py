"""
Basis windows.

Author: Oleksii Dovhaniuk
Date: 21.06.2022
"""

import tkinter as tk

from src.components.windows.window import Window

class Basis(Window):
    _row_no = 32
    title = 'Basis'
    # bg = '#FFFFFF'

    _basis = (
        ("SWAP", 'bit', 1, 1, "α+β+γ", 1, 1),
        ("CS", 'bit', 5, 5, "α+β+γ", 1, 1),
        ("C'S", 'bit', 5, 5, "α+β+γ", 1, 0),
        ("CCS", 'bit', 15, 15, "α+β+γ", 1, 0),
        ("C'CS", 'bit', 15, 15, "α+β+γ", 1, 0),
        ("C'C'S", 'bit', 15, 15, "α+β+γ", 1, 0),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title_var.set(self.title)
        

        rows = [Row(self.body, i) for i in range(self._row_no)]
        for row in rows:
            row.pack(fill='x', expand=0)
        top = 0

        gfrg_collection = Collection(rows[top], 'GFRG Family', 0, top)
        gfrg_collection.pack(fill='x', expand=1)
        top += 1

        items = [Item(rows[top+i], item[0], item[-1], top+i) for i, item in enumerate(self._basis)]
        for item in items:
            item.pack(fill='x', expand=1)
        top += len(self._basis)
        
        gfrg_collection.bind_checker(items)

class Row(tk.Frame):
    size = 52
    _bgs = ('#F2F2F2', '#FFFFFF')
    is_empty = True

    def __init__(self, container, index, *args, **kwargs):
        self.bg = self._bgs[index % 2]
        super().__init__(container, bg=self.bg, height=self.size, *args, **kwargs)


class Item(tk.Frame):
    size = 24
    pad = 8
    pad_x = 24


    def __init__(self, container, designation, state, index, *args, **kwargs):
        self.index= index
        self._more_closed_png = tk.PhotoImage(file=r"./src/assets/icons/more_closed.png").subsample(3, 3)
        self._more_opened_png = tk.PhotoImage(file=r"./src/assets/icons/more_opened.png").subsample(3, 3)
        self._checkbox_png = tk.PhotoImage(file=r"./src/assets/icons/checkbox.png", height=30, width=30)
        self._check_png = tk.PhotoImage(file=r"./src/assets/icons/check.png", height=30, width=30)
        size = self.size
        super().__init__(container, bg=container.bg, height=size, *args, **kwargs)

        tk.Frame(self, width=self.pad_x*2, bg=container.bg).pack(side='left', fill='both')

        self.btn_more = tk.Button(
            self, 
            text='More...',
            image=self._more_closed_png,
            width=size, 
            height=size,
            relief='flat',
            bg=container.bg,
            command=lambda x: print(x)
            )
        self.btn_more.pack_propagate(0)
        self.btn_more.pack(side='left')

        self.lbl_designation = tk.Label(self, text=designation, bg=container.bg)
        self.lbl_designation.pack(side='left', ipadx=self.pad)      

        tk.Frame(self,).pack(fill='x', expand=1)

        self.state = tk.IntVar(value=state)   
        self.state_checkbox = tk.Checkbutton(
            self, 
            variable=self.state, 
            image=self._checkbox_png, 
            selectimage=self._check_png,
            indicatoron=0,
            onvalue=1, 
            offvalue=0,
            relief='ridge',
            bg=container.bg,
            )
        self.state_checkbox.pack(side='right', padx=self.pad_x)

class Collection(tk.Frame):
    size = 24
    pad = 8
    pad_x = 24 

    def __init__(self, container, title, state, index, *args, **kwargs):
        self.index=index
        self._more_opened_png = tk.PhotoImage(file=r"./src/assets/icons/more_opened.png").subsample(3, 3)
        self._checkbox_png = tk.PhotoImage(file=r"./src/assets/icons/checkbox.png", height=30, width=30)
        self._check_png = tk.PhotoImage(file=r"./src/assets/icons/check.png", height=30, width=30)
        size = self.size
        super().__init__(container, bg=container.bg, height=size, *args, **kwargs)

        tk.Frame(self, width=self.pad_x, bg=container.bg).pack(side='left', fill='both')
        tk.Label(self, image=self._more_opened_png, width=size, height=size, relief='flat', bg=container.bg).pack(side='left', fill='both')

        self.lbl_title = tk.Label(self, text=title, bg=container.bg)
        self.lbl_title.pack(side='left', ipadx=self.pad)     

        tk.Frame(self,).pack(fill='x', expand=1)
        self.state = tk.IntVar(value=state)   
        self.state_checkbox = tk.Checkbutton(
            self, 
            variable=self.state, 
            image=self._checkbox_png, 
            selectimage=self._check_png,
            indicatoron=0,
            onvalue=1,
            offvalue=0,
            relief='ridge',
            bg=container.bg,
            )
        self.state_checkbox.pack(side='right', padx=self.pad_x)

    def bind_checker(self, items):
        self.state_checkbox.config(command=lambda: self.check_all(items))

    def check_all(self, items):
        for item in items:
            if self.state.get() == 1: 
                item.state.set(1)
            else:
                item.state.set(0)