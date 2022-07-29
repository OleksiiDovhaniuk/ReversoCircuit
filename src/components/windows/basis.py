"""
Basis windows.

Author: Oleksii Dovhaniuk
Date: 21.06.2022
"""

import tkinter as tk

from src.components.windows.window import Window
from src.assets.common.table import Table


class Family(tk.Frame):
    is_checked = False
    is_expand = False
    title = 'Untitled Family'
    onCheck = lambda: print('[WARNING][Family obj Initialization]: There is a None onCheck() function transmited to this Family')
    onRefresh = lambda: print('[WARNING][Family obj Initialization]: There is a None onRefresh() function transmited to this Family')

    # def onAction(self):
    #     # if self.is_expand:
    #     #     self.expand_btn.config(text='+')
    #     # else:
    #     #     self.expand_btn.config(text='-')
    #     self.onRefresh()
    #     self.is_expand = not self.is_expand
    #     self.expand_btn.config(text=('-', '+')[self.is_expand])

    def __init__(self, master, checked=is_checked, expand=is_expand, title=title, bg='gray', onCheck=onCheck, onRefresh=onRefresh, *args, **kwargs):
        super().__init__(master, bg=bg, relief='flat', *args, **kwargs)
        self.is_checked = checked
        self.is_expand = expand
        self.title = title
        self.bg = bg
        self.onCheck = onCheck
        # self.onRefresh = onRefresh

        self.check_btn = tk.Checkbutton(self, bg=bg, relief='flat', command=self.onCheck)
        if checked: self.check_btn.config(state='active')
        self.expand_btn = tk.Button(self, bg=bg, text='+', relief='flat', command=onRefresh)
        if expand: self.expand_btn.config(text='-')
        self.title_lbl = tk.Label(self, bg=bg, text=title)

        self.check_btn.pack(side='left', fill='both')
        self.expand_btn.pack(side='left', fill='both')
        self.title_lbl.pack(side='left', fill='both')

        print(f'[Added]: {self}')


class Gate(tk.Frame):
    is_checked = False
    is_expand = False
    title = 'Untitled Gate'
    value = 0
    percent = 0
    onRefresh = lambda: print('[WARNING][Gate obj Initialization]: There is a None onRefresh() function transmited to this Gate')
    useGate = lambda: print('[WARNING][Gate obj Initialization]: There is a None useGate() function transmited to this Gate')

    _padx = 8

    def __init__(self, master, checked=is_checked, expand=is_expand, title=title, value=value, percent=percent, bg='gray', onRefresh=onRefresh, useGate=useGate, *args, **kwargs):
        super().__init__(master, bg=bg, relief='flat', *args, **kwargs)
        self.is_checked = checked
        self.is_expand = expand
        self.title = title
        self.value = value
        self.percent = percent
        self.bg = bg

        self.wpad = tk.Button(self, text=' ', bg=bg, relief='flat', state='disabled')
        self.check_btn = tk.Checkbutton(self, bg=bg, relief='flat')
        if checked: self.check_btn.config(state='active')
        self.expand_btn = tk.Button(self, bg=bg, text='+', relief='flat', command=onRefresh)
        if expand: self.expand_btn.config(text='-')
        self.title_lbl = tk.Label(self, bg=bg, text=title)
        self.value_ent = tk.Entry(self, bg='white', )
        self.value_ent.insert(0, str(value))
        self.value_ent.config(width=8)
        self.percent_lbl = tk.Label(self, bg=bg, text=f'{percent}%')
        self.add_btn = tk.Button(self, bg=bg, text='Add', command=useGate, state='disabled')

        self.wpad.pack(side='left', fill='both')
        self.check_btn.pack(side='left', fill='both')
        self.expand_btn.pack(side='left', fill='both')
        self.title_lbl.pack(side='left', fill='both', padx=self._padx)
        self.add_btn.pack(side='right', fill='x', padx=self._padx)
        self.percent_lbl.pack(side='right', fill='both', padx=self._padx)
        self.value_ent.pack(side='right', fill='none', padx=self._padx)

        print(f'[Added]: {self}')


class Property (tk.Frame):
    title = 'Untitled Property'
    value = 'None'
    
    
    _padx = 8

    def __init__(self, master, title=title, value=value, bg='gray', *args, **kwargs):
        super().__init__(master, bg=bg, relief='flat', *args, **kwargs)
        self.title = title
        self.value = value
        self.bg = bg

        self.wpad = tk.Button(self, text=' ', bg=bg, relief='flat', state='disabled')
        self.wpad2 = tk.Button(self, text=' ', bg=bg, relief='flat', state='disabled')
        self.title_lbl = tk.Label(self, bg=bg, text=title)
        self.value_lbl = tk.Label(self, bg=bg, text=value)
        self.epad = tk.Button(self, text=' ', bg=bg, relief='flat', state='disabled')

        self.wpad.pack(side='left', fill='both')
        self.wpad2.pack(side='left', fill='both')
        self.title_lbl.pack(side='left', fill='both')
        self.value_lbl.pack(side='right', fill='both', padx=self._padx)
        self.epad.pack(side='right', fill='both')

        print(f'[Added]: {self}')


class Basis(Window):
    title = 'Basis'
    bg = '#FFFFFF'
    bg_odd = '#F7F1F1'
    data = []

    _data = [
        {
            'title': 'General',
            'checked': False,
            'expand': True,
            'gates':[
                {
                    'title': 'Empty Gate',
                    'value': 0,
                    'percent': 0,
                    'checked': False,
                    'expand': False,
                    'properties':{
                        'Q-Cost': 0,
                        'Delay': 0,
                        'HC': 0,
                        'Line No.': 0,
                        'Parity': 'Preserved',
                    }
                }
            ]
        },
        {
            'title': 'GFRG Family',
            'checked': False,
            'expand': True,
            'gates':[
                {
                    'title': 'SWAP',
                    'value': 0,
                    'percent': 0,
                    'checked': False,
                    'expand': False,
                    'properties':{
                        'Q-Cost': 1,
                        'Delay': 1,
                        'HC': 1,
                        'Line No.': 2,
                        'Parity': 'Preserved',
                    }
                },
                {
                    'title': 'CS',
                    'value': 0,
                    'percent': 0,
                    'checked': False,
                    'expand': True,
                    'properties':{
                        'Q-Cost': 5,
                        'Delay': 5,
                        'HC': 5,
                        'Line No.': 3,
                        'Parity': 'Preserved',
                    }
                },
                {
                    'title': "C'S",
                    'value': 0,
                    'percent': 0,
                    'checked': False,
                    'expand': False,
                    'properties':{
                        'Q-Cost': 5,
                        'Delay': 5,
                        'HC': 5,
                        'Line No.': 3,
                        'Parity': 'Preserved',
                    }
                },
                {
                    'title': "CCS",
                    'value': 0,
                    'percent': 0,
                    'checked': False,
                    'expand': False,
                    'properties':{
                        'Q-Cost': 15,
                        'Delay': 15,
                        'HC': 13,
                        'Line No.': 4,
                        'Parity': 'Preserved',
                    }
                },
                {
                    'title': "C'CS",
                    'value': 0,
                    'percent': 0,
                    'checked': False,
                    'expand': False,
                    'properties':{
                        'Q-Cost': 15,
                        'Delay': 15,
                        'HC': 14,
                        'Line No.': 4,
                        'Parity': 'Preserved',
                    }
                },
                {
                    'title': "C'C'S",
                    'value': 0,
                    'percent': 0,
                    'checked': False,
                    'expand': False,
                    'properties':{
                        'Q-Cost': 15,
                        'Delay': 15,
                        'HC': 15,
                        'Line No.': 4,
                        'Parity': 'Preserved',
                    }
                }
            ]
        },
        {
            'title': 'NTC Family',
            'checked': False,
            'expand': False,
            'gates':[
                {
                    'title': 'NOT',
                    'value': 0,
                    'percent': 0,
                    'checked': False,
                    'expand': False,
                    'properties':{
                        'Q-Cost': 0,
                        'Delay': 0,
                        'HC': 0,
                        'Line No.': 1,
                        'Parity': 'NaN',
                    }
                },
                {
                    'title': 'CNOT',
                    'value': 0,
                    'percent': 0,
                    'checked': False,
                    'expand': False,
                    'properties':{
                        'Q-Cost': 5,
                        'Delay': 5,
                        'HC': 4,
                        'Line No.': 2,
                        'Parity': 'NaN',
                    }
                },
                {
                    'title': "C'NOT",
                    'value': 0,
                    'percent': 0,
                    'checked': False,
                    'expand': False,
                    'properties':{
                        'Q-Cost': 5,
                        'Delay': 5,
                        'HC': 5,
                        'Line No.': 2,
                        'Parity': 'NaN',
                    }
                },
            ]
        }
    ]


    def resetBasis(self):
        print('Basis Reset')

    def equalize(self):
        print('Basis Equalized')

    """
    Adds Property data to the row.
    args: 
        title - property title (str);
        value - property value;
        dndex - row index where to input this data. 
    """
    def addProperty(self, title, value, dndex):
        new_property = Property(
            master=self.table.getRow(dndex), 
            title=title,
            value=value,
            bg=self.table.getBg(dndex),
        )

        new_property.master.clear()
        new_property.pack(side='bottom', fill='x')
        self.data.append(new_property)


    """
    Adds Gate data to the row.
    args: 
        gate - family object;
        index - familty index to add from the self._data nested list;
        jndex - gate index within a family to add from the self._data nested list;
        dndex - dynamic index of the gate's family
    """
    def addGate(self, gate, index, dindex, jndex):
        djndex = len(self.data) # local dynamic index
        new_gate = Gate(
            master=self.table.getRow(djndex), 
            checked=gate['checked'], 
            expand=gate['expand'], 
            title=gate['title'], 
            value=gate['value'],
            percent=gate['percent'],
            onRefresh=lambda i=index, di=dindex, j=jndex, dj=djndex: self.onRefresh(i, di, j, dj),
            bg=self.table.getBg(djndex),
        )
        new_gate.useGate = lambda: self.useGate(new_gate)
        new_gate.master.clear()
        new_gate.pack(side='bottom', fill='x')
        self.data.append(new_gate)

        if gate['expand']: 
            for i, key in enumerate(gate['properties']):
                self.addProperty(key, gate['properties'][key], djndex+i+1)

    """
    Adds Family data to the row.
    args: 
        family - family object;
        index - familty index to add from the self._data nested list;
    """
    def addFamily(self, family, index):
        dindex = len(self.data)
        new_family = Family(
            master=self.table.getRow(dindex), 
            checked=family['checked'], 
            expand=family['expand'], 
            title=family['title'], 
            onCheck=self.checkFamily,
            onRefresh=lambda i=index, d=dindex: self.onRefresh(i, d),
            bg=self.table.getBg(dindex),
        )

        new_family.master.clear()
        new_family.pack(side='bottom', fill='x')
        self.data.append(new_family)

        if family['expand']:
            for j, gate in enumerate(family['gates']):
                self.addGate(gate, index, dindex, j)

    """
    Expends deleted rows' date after the row with inputed index 
    args: 
        index - familty index to add from the self._data nested list;
        jndex - gate index within a family to add from the self._data nested list;
        dndex - row index where to input this data. 
    """
    def onRefresh(self, index=0, dindex=None, jndex=None, djndex=None ):
        if dindex == None: dindex = index
        if jndex == None: 
            self._data[index]['expand'] = not self.data[dindex].is_expand
        else: 
            self._data[index]['gates'][jndex]['expand'] = not self.data[djndex].is_expand

        # # Delete rows's data
        for row in self.data[dindex:]:
            row.destroy()
            self.data.remove(row)

        # Restore row's data
        for i, family in enumerate(self._data[index:]):
            self.addFamily(family, index+i)

        print('\n---------------------------------------------------------------\n')


    def checkFamily(self, family):
        print(f'{family} is checked!')


    def useGate(self, gate):
        print(f'{gate} is used!')


    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title_var.set(self.title)
        self.table = Table(self.body, bg_odd=self.bg_odd, row_no=65)
        self.reset_btn = tk.Button(self.right, text='Reset', command=self.resetBasis)
        self.equal_btn = tk.Button(self.right, text='Equalize', command=self.equalize)

        # Fill the table
        for i, family in enumerate(self._data):
            self.addFamily(family, i)
        
        self.table.pack(fill='both', expand=1)
        self.reset_btn.pack(side='left', fill='both')
        self.equal_btn.pack(side='right', fill='both')
