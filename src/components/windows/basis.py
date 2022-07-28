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
    onExpand = lambda: print('[WARNING][Family obj Initialization]: There is a None onExpand() function transmited to this Family')
    onCollapse = lambda: print('[WARNING][Family obj Initialization]: There is a None onCollapse() function transmited to this Family')

    def onAction(self):
        if self.is_expand:
            self.onCollapse()
            self.expand_btn.config(text='+')
            self.is_expand = False
        else:
            self.onExpand()
            self.expand_btn.config(text='-')
            self.is_expand = True

    def __init__(self, master, checked=is_checked, expand=is_expand, title=title, bg='gray', onCheck=onCheck, onExpand=onExpand, onCollapse=onCollapse, *args, **kwargs):
        super().__init__(master, bg=bg, relief='flat', *args, **kwargs)
        self.is_checked = checked
        self.is_expand = expand
        self.title = title
        self.bg = bg
        self.onCheck = onCheck
        self.onExpand = onExpand
        self.onCollapse = onCollapse

        self.check_btn = tk.Checkbutton(self, bg=bg, relief='flat', command=self.onCheck)
        if checked: self.check_btn.config(state='active')
        self.expand_btn = tk.Button(self, bg=bg, text='+', relief='flat', command=self.onAction)
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
    onExpand = lambda: print('[WARNING][Gate obj Initialization]: There is a None onExpand() function transmited to this Gate')
    onCollapse = lambda: print('[WARNING][Gate obj Initialization]: There is a None onCollapse() function transmited to this Gate')
    useGate = lambda: print('[WARNING][Gate obj Initialization]: There is a None useGate() function transmited to this Gate')

    def onAction(self):
        if self.is_expand:
            self.onCollapse()
            self.expand_btn.config(text='+')
            self.is_expand = False
        else:
            self.onExpand()
            self.expand_btn.config(text='-')
            self.is_expand = True

    def __init__(self, master, checked=is_checked, expand=is_expand, title=title, value=value, percent=percent, bg='gray', onExpand=onExpand, onCollapse=onCollapse, useGate=useGate, *args, **kwargs):
        super().__init__(master, bg=bg, relief='flat', *args, **kwargs)
        self.is_checked = checked
        self.is_expand = expand
        self.title = title
        self.value = value
        self.percent = percent
        self.bg = bg
        self.onExpand = onExpand
        self.onCollapse = onCollapse

        self.wpad = tk.Button(self, text=' ', bg=bg, relief='flat', state='disabled')
        self.check_btn = tk.Checkbutton(self, bg=bg, relief='flat')
        if checked: self.check_btn.config(state='active')
        self.expand_btn = tk.Button(self, bg=bg, text='+', relief='flat', command=self.onAction)
        if expand: self.expand_btn.config(text='-')
        self.title_lbl = tk.Label(self, bg=bg, text=title)
        self.value_ent = tk.Entry(self, bg=bg)
        self.value_ent.insert(0, str(value))
        self.percent_lbl = tk.Label(self, bg=bg, text=f'{percent}%')
        self.add_btn = tk.Button(self, bg=bg, text='Add', command=useGate, state='disabled')

        self.wpad.pack(side='left', fill='both')
        self.check_btn.pack(side='left', fill='both')
        self.expand_btn.pack(side='left', fill='both')
        self.title_lbl.pack(side='left', fill='both')
        self.add_btn.pack(side='right', fill='both')
        self.percent_lbl.pack(side='right', fill='both')
        self.value_ent.pack(side='right', fill='both')

        print(f'[Added]: {self}')


class Property (tk.Frame):
    title = 'Untitled Property'
    value = 'None'

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
        self.value_lbl.pack(side='right', fill='both')
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
            'expand': False,
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
            'expand': False,
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

    "Deletes all rows' data after row with inputed index"
    def deleteAfter(self, index):
        index += 1
        for row in self.data[index:]:
            # print(row)
            row.destroy()
            self.data.remove(row)

        print(f'After Delete: {len(self.data)}')

    def addFamily(self, family, static_index, dynamic_index=None):
        if dynamic_index == None:
            dynamic_index = static_index
        new_family = Family(
            master=self.table.getRow(dynamic_index), 
            checked=family['checked'], 
            expand=family['expand'], 
            title=family['title'], 
            onCheck=self.checkFamily,
            onExpand=lambda s=static_index, d=dynamic_index: self.openFamily(s, d),
            onCollapse=lambda s=static_index, d=dynamic_index: self.closeFamily(s, d),
            bg=self.table.getBg(dynamic_index),
        )
        new_family.master.clear()
        new_family.pack(side='bottom', fill='x')
        self.data.append(new_family)

    def addGate(self, gate, family, static_index, dynamic_index):
        new_gate = Gate(
            master=self.table.getRow(dynamic_index), 
            checked=gate['checked'], 
            expand=gate['expand'], 
            title=gate['title'], 
            value=gate['value'],
            percent=gate['percent'],
            onExpand=lambda f=family, s=static_index, d=dynamic_index: self.openGate(f, s, d),
            onCollapse=lambda f=family, s=static_index, d=dynamic_index: self.closeGate(f, s, d),
            bg=self.table.getBg(dynamic_index),
        )
        new_gate.useGate = lambda: self.useGate(new_gate)
        new_gate.master.clear()
        new_gate.pack(side='bottom', fill='x')
        self.data.append(new_gate)

    def addProperty(self, title, value, dynamic_index):
        new_property = Property(
            master=self.table.getRow(dynamic_index), 
            title=title,
            value=value,
        )
        new_property.master.clear()
        new_property.pack(side='bottom', fill='x')
        self.data.append(new_property)

    "Expends hiden rows with Gates under the current Family"
    def openFamily(self, static_index, dynamic_index=None):
        if dynamic_index == None:
            dynamic_index = static_index
        self.deleteAfter(dynamic_index)
        family = self._data[static_index]
        family['expand'] = True

        for i, gate in enumerate(family['gates']):
            self.addGate(gate, family['gates'], i, len(self.data))
            if gate['expand']: self.openGate(family['gates'], i, len(self.data))


        for i, family in enumerate(self._data[static_index+1:]):
            self.addFamily(family, static_index+i+1, len(self.data))
            if family['expand']:
                for gate in family['gates']:
                    self.addGate(gate, family['gates'], len(self.data))
                    if gate['expand']: self.openGate(family['gates'], i, len(self.data))

        print(f'Family in Row #{dynamic_index} Is Opened!')

    "Hides rows with Gates under the current Family"
    def closeFamily(self, static_index, dynamic_index=None):
        if dynamic_index == None:
            dynamic_index = static_index
        self.deleteAfter(dynamic_index)
        self._data[static_index]['expand'] = False

        for i, family in enumerate(self._data[static_index+1:]):
            self.addFamily(family, static_index+i+1, len(self.data))
            if family['expand']:
                for gate in family['gates']:
                    self.addGate(gate, len(self.data))
                    if gate['expand']: self.openGate()

        print(f'Family in Row #{dynamic_index} Is Collapced')

    "Expends hiden rows with Properties under the current Gate"
    def openGate(self, family, static_index, dynamic_index=None):
        if dynamic_index == None:
            dynamic_index = static_index
        self.deleteAfter(dynamic_index)
        family[static_index]['expand'] = True

        for title in family[static_index]['gates']['properties']:
            self.addProperty(title, family[static_index]['gates'][title], len(self.data))

        for i, gate in enumerate(family[static_index+1:]):
            self.addGate(family, static_index+i+1, len(self.data))
            if gate['expand']:
                for title in gate['properties']:
                    self.addProperty(title, gate['properties'][title], len(self.data))

    "Hides rows with Properties under the current Gate"
    def closeGate(self, family, static_index, dynamic_index=None):
        if dynamic_index == None:
            dynamic_index = static_index
        self.deleteAfter(dynamic_index)
        family[static_index]['expand'] = False

        for i, gate in enumerate(family[static_index+1:]):
            self.addGate(family, static_index+i+1, len(self.data))
            if gate['expand']:
                for title in gate['properties']:
                    self.addProperty(title, gate['properties'][title], len(self.data))

    def checkFamily(self, family):
        print(f'{family} is checked!')


    def useGate(self, gate):
        print(f'{gate} is used!')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title_var.set(self.title)
        self.table = Table(self.body, bg_odd=self.bg_odd)
        self.reset_btn = tk.Button(self.right, text='Reset', command=self.resetBasis)
        self.equal_btn = tk.Button(self.right, text='Equalize', command=self.equalize)

        self.table.pack(fill='both', expand=1)
        self.reset_btn.pack(side='left', fill='both')
        self.equal_btn.pack(side='right', fill='both')

        for index, family in enumerate(self._data):
            self.addFamily(family, index, index+3)
            if family['expand']: self.openFamily(index)

        


        # rows = [Row(self.body, i) for i in range(self._row_no)]
        # for row in rows:
        #     row.pack(fill='x', expand=0)
        # top = 0

        # gfrg_collection = Collection(rows[top], 'GFRG Family', 0, top)
        # gfrg_collection.pack(fill='x', expand=1)
        # top += 1

        # items = [Item(rows[top+i], item[0], item[-1], top+i) for i, item in enumerate(self._basis)]
        # for item in items:
        #     item.pack(fill='x', expand=1)
        # top += len(self._basis)
        
        # gfrg_collection.bind_checker(items)

# class Row(tk.Frame):
#     size = 52
#     _bgs = ('#F2F2F2', '#FFFFFF')
#     is_empty = True

#     def __init__(self, container, index, *args, **kwargs):
#         self.bg = self._bgs[index % 2]
#         super().__init__(container, bg=self.bg, height=self.size, *args, **kwargs)


# class Item(tk.Frame):
#     size = 24
#     pad = 8
#     pad_x = 24

    


#     def __init__(self, container, designation, state, index, *args, **kwargs):
#         self.index= index
#         self._more_closed_png = tk.PhotoImage(file=r"./src/assets/icons/more_closed.png").subsample(3, 3)
#         self._more_opened_png = tk.PhotoImage(file=r"./src/assets/icons/more_opened.png").subsample(3, 3)
#         self._checkbox_png = tk.PhotoImage(file=r"./src/assets/icons/checkbox.png", height=30, width=30)
#         self._check_png = tk.PhotoImage(file=r"./src/assets/icons/check.png", height=30, width=30)
#         size = self.size
#         super().__init__(container, bg=container.bg, height=size, *args, **kwargs)

#         tk.Frame(self, width=self.pad_x*2, bg=container.bg).pack(side='left', fill='both')

#         self.btn_more = tk.Button(
#             self, 
#             text='More...',
#             image=self._more_closed_png,
#             width=size, 
#             height=size,
#             relief='flat',
#             bg=container.bg,
#             command=lambda x: print(x)
#             )
#         self.btn_more.pack_propagate(0)
#         self.btn_more.pack(side='left')

#         self.lbl_designation = tk.Label(self, text=designation, bg=container.bg)
#         self.lbl_designation.pack(side='left', ipadx=self.pad)      

#         tk.Frame(self,).pack(fill='x', expand=1)

#         self.state = tk.IntVar(value=state)   
#         self.state_checkbox = tk.Checkbutton(
#             self, 
#             variable=self.state, 
#             image=self._checkbox_png, 
#             selectimage=self._check_png,
#             indicatoron=0,
#             onvalue=1, 
#             offvalue=0,
#             relief='ridge',
#             bg=container.bg,
#             )
#         self.state_checkbox.pack(side='right', padx=self.pad_x)

# class Collection(tk.Frame):
#     size = 24
#     pad = 8
#     pad_x = 24 

#     def __init__(self, container, title, state, index, *args, **kwargs):
#         self.index=index
#         self._more_opened_png = tk.PhotoImage(file=r"./src/assets/icons/more_opened.png").subsample(3, 3)
#         self._checkbox_png = tk.PhotoImage(file=r"./src/assets/icons/checkbox.png", height=30, width=30)
#         self._check_png = tk.PhotoImage(file=r"./src/assets/icons/check.png", height=30, width=30)
#         size = self.size
#         super().__init__(container, bg=container.bg, height=size, *args, **kwargs)

#         tk.Frame(self, width=self.pad_x, bg=container.bg).pack(side='left', fill='both')
#         tk.Label(self, image=self._more_opened_png, width=size, height=size, relief='flat', bg=container.bg).pack(side='left', fill='both')

#         self.lbl_title = tk.Label(self, text=title, bg=container.bg)
#         self.lbl_title.pack(side='left', ipadx=self.pad)     

#         tk.Frame(self,).pack(fill='x', expand=1)
#         self.state = tk.IntVar(value=state)   
#         self.state_checkbox = tk.Checkbutton(
#             self, 
#             variable=self.state, 
#             image=self._checkbox_png, 
#             selectimage=self._check_png,
#             indicatoron=0,
#             onvalue=1,
#             offvalue=0,
#             relief='ridge',
#             bg=container.bg,
#             )
#         self.state_checkbox.pack(side='right', padx=self.pad_x)

#     def bind_checker(self, items):
#         self.state_checkbox.config(command=lambda: self.check_all(items))

#     def check_all(self, items):
#         for item in items:
#             if self.state.get() == 1: 
#                 item.state.set(1)
#             else:
#                 item.state.set(0)