"""
Basis window.

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
    

    def addChecker(self, check_var):
        # Setting check_var of a Gate to the Family objet
        check_var.trace('w', self.checkByGates)
        self.gate_checks.append(check_var)
        self.previous_gate_states = all([check.get() for check in self.gate_checks])

    def checkByGates(self, *args):
        current_gate_states = all([check.get() for check in self.gate_checks])
        if current_gate_states:
            self.is_checked.set(True)
        elif self.previous_gate_states:
            self.is_checked.set(False)

        self.previous_gate_states = current_gate_states

    def checkFamily(self, *args):
        if self.is_checked.get():
            for check in self.gate_checks:
                check.set(True)
        elif all([check.get() for check in self.gate_checks]):
            for check in self.gate_checks:
                check.set(False)


    def __init__(self, master, checked=is_checked, expand=is_expand, title=title, bg='gray', onCheck=onCheck, onRefresh=onRefresh, *args, **kwargs):
        super().__init__(master, bg=bg, relief='flat', *args, **kwargs)
        self.is_checked = tk.BooleanVar(self, checked)
        self.is_expand = expand
        self.title = title
        self.bg = bg
        self.onCheck = onCheck
        self.gate_checks = []
        self.previous_gate_states = False

        self.check_btn = tk.Checkbutton(self, bg=bg, relief='flat', variable=self.is_checked,
        #  command=self.checkFamilty
        )
        if checked: self.check_btn.config(state='active')
        self.expand_btn = tk.Button(self, bg=bg, text='+', relief='flat', command=onRefresh)
        if expand: self.expand_btn.config(text='-')
        self.title_lbl = tk.Label(self, bg=bg, text=title)

        self.check_btn.pack(side='left', fill='both')
        self.expand_btn.pack(side='left', fill='both')
        self.title_lbl.pack(side='left', fill='both')

        self.is_checked.trace('w', self.checkFamily)


class Gate(tk.Frame):
    onRefresh = lambda: print('[WARNING][Gate obj Initialization]: There is a None onRefresh() function transmited to this Gate')
    useGate = lambda: print('[WARNING][Gate obj Initialization]: There is a None useGate() function transmited to this Gate')

    _padx = 8

    def addChecker(self, check_var):
        # Setting check_var of a Gate to the Family objet
        check_var.trace('w', self.checkByGates)
        self.gate_checks.append(check_var)
        self.previous_gate_states = all([check.get() for check in self.gate_checks])

    def changeIputState(self, *args):
        if self.is_checked.get():
                
            self.value_ent.config(state='normal', )
            self.percent_lbl.config(state='normal')
            if self.value.get() == 0:
                self.str_value.set('1.0')
            self.value.set(float(self.value_ent.get()))
        else:
            self.value.set(0.0)
            self.value_ent.config(state='disabled')
            self.percent_lbl.config(text='0.0%', state='disabled')

    def setPercent(self, *args):
        self.percent_lbl.config(text=f'{self.percent.get()}%')

    def readValue(self, *args):
        try:
            self.value.set(float(self.str_value.get()))
        except:
            print(f'[Input Error][Basis Window]: Invalid input in {self.title} gate row')

    def __init__(self, master, checked=False, expand=False, title='Untitled Gate', value=1.0, percent=0, bg='gray', onRefresh=onRefresh, useGate=useGate, *args, **kwargs):
        super().__init__(master, bg=bg, relief='flat', *args, **kwargs)
        self.is_checked = tk.BooleanVar(self, checked)
        self.is_expand = expand
        self.title = title
        self.value = tk.DoubleVar(self, value)
        self.str_value = tk.StringVar(self, str(value))
        self.percent = tk.DoubleVar(self, percent)
        self.bg = bg
        self.gate_checks = []

        self.is_checked.trace('w', self.changeIputState)
        self.percent.trace('w', self.setPercent)

        self.wpad = tk.Button(self, text=' ', bg=bg, relief='flat', state='disabled')
        self.check_btn = tk.Checkbutton(self, bg=bg, relief='flat', variable=self.is_checked)
        self.expand_btn = tk.Button(self, bg=bg, text='+', relief='flat', command=onRefresh)
        self.title_lbl = tk.Label(self, bg=bg, text=title)
        self.value_ent = tk.Entry(self, bg='white', textvariable=self.str_value)
        self.percent_lbl = tk.Label(self, bg=bg, text=f'{percent}%')
        self.add_btn = tk.Button(self, bg=bg, text='Add', command=useGate, state='disabled')

        self.wpad.pack(side='left', fill='both')
        self.check_btn.pack(side='left', fill='both')
        self.expand_btn.pack(side='left', fill='both')
        self.title_lbl.pack(side='left', fill='both', padx=self._padx)
        self.add_btn.pack(side='right', fill='x', padx=self._padx)
        self.percent_lbl.pack(side='right', fill='both', padx=self._padx)
        self.value_ent.pack(side='right', fill='none', padx=self._padx)

        if checked: self.check_btn.config(state='active')
        if expand: self.expand_btn.config(text='-')
        self.str_value.trace('w', self.readValue)
        self.changeIputState()
        self.value_ent.config(width=8)

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


class Basis(Window):
    """ The class represents a window with table of a basis elements. Inherited from a Window class.
    """
    title = 'Basis'
    bg = '#FFFFFF'
    bg_odd = '#F7F1F1'
    data = []
    gate_values = []

    _data = [
        {
            'title': 'General',
            'checked': False,
            'expand': True,
            'gates':[
                {
                    'title': 'Empty Gate',
                    'value': 1.0,
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
                    'value': 1.0,
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
                    'value': 1.0,
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
                    'value': 1.0,
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
                    'value': 1.0,
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
                    'value': 1.0,
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
                    'value': 1.0,
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
                    'value': 1.0,
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
                    'value': 1.0,
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
                    'value': 1.0,
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

    def addGateValues(self, check_var, value_var, percent_var):
        # Setting check_var of a Gate to the Family objet
        check_var.trace('w', self.checkByGates)
        self.gate_checks.append(check_var)
        self.previous_gate_states = all([check.get() for check in self.gate_checks])

        # Setting value_var and percent_var of a Gate to the Family objet
        value_var.trace('w', self.calcPersents)
        self.gate_values.append([value_var, percent_var])

    """
    Adds Property data to the row.
    args: 
        title - property title (str);
        value - property value;
        dndex - row index where to input this data. 
    """
    def addProperty(self, title, value, dndex):
        new_property = Property(
            master=self.table.addRow(dndex), 
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
        gate - gate values from the self._data;
        family - name of the family;
        index - familty index to add from the self._data nested list;
        jndex - gate index within a family to add from the self._data nested list;
        dndex - dynamic index of the gate's family;
    """
    def addGate(self, gate, index, dindex, jndex):
        djndex = len(self.data) # local dynamic index
        new_gate = Gate(
            master=self.table.addRow(djndex), 
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
            for i, (title, value) in enumerate(gate['properties'].items()):
                self.addProperty(title, value, djndex+i+1)

        return new_gate

    def addGateValues(self, check_var, value_var, percent_var):
        # Create triger on when gate is checked to calc values
        check_var.trace('w', self.calcPersents)

        # Setting value_var and percent_var of a Gate to the Family objet
        value_var.trace('w', self.calcPersents)
        self.gate_values.append([value_var, percent_var])


    def calcPersents(self, *args):
        total = sum([value.get() for value, _ in self.gate_values])
        for value, percent in self.gate_values:
            if total:
                percent.set(round(value.get()/total*100, 1))
            else:
                percent.set(0.0)

    """
    Adds Family data to the row.
    args: 
        family - family object;
        index - familty index to add from the self._data nested list;
    """
    def addFamily(self, family, index):
        dindex = len(self.data)
        new_family = Family(
            master=self.table.addRow(dindex), 
            checked=family['checked'], 
            expand=family['expand'], 
            title=family['title'], 
            onRefresh=lambda i=index, d=dindex: self.onRefresh(i, d),
            bg=self.table.getBg(dindex),
        )

        new_family.master.clear()
        new_family.pack(side='bottom', fill='x')
        self.data.append(new_family)

        family_checker = new_family.is_checked
        if family['expand']:
            for j, gate in enumerate(family['gates']):
                new_gate = self.addGate(gate, index, dindex, j)

                gate_checker = new_gate.is_checked
                gate_value = new_gate.value
                gate_percent = new_gate.percent

                new_family.addChecker(gate_checker)
                self.addGateValues(gate_checker, gate_value, gate_percent)

                # Trace variables updates
                gate_checker.trace('w', lambda *_, c=gate_checker, fi=index, gi=j: self.updateGateChecker(c, fi, gi))
                gate_value.trace('w', lambda *_, v=gate_value, fi=index, gi=j: self.updateValue(v, fi, gi))
                gate_percent.trace('w', lambda *_, p=gate_percent, fi=index, gi=j: self.updatePercent(p, fi, gi))
                # family_checker.trace('w', lambda *_, v=gate_value, fi=index, gi=j: self.updateValue(v, fi, gi))
                # family_checker.trace('w', lambda *_, p=gate_percent, fi=index, gi=j: self.updatePercent(p, fi, gi))


        family_checker.trace(	'w', lambda *_, c=family_checker, i=index: self.updateFamilyChecker(c, i))

    def updateFamilyChecker(self, checker, index, *args):
        is_checked = checker.get()
        self._data[index]['checked'] = is_checked

        # for gate in self._data[index]['gates']:
        #     gate['checked'] = is_checked

        print('Hello')

    def updateGateChecker(self, checker, family_index, gate_index, *args):
        self._data[family_index]['gates'][gate_index]['checked'] = checker.get()

    def updateValue(self, value, family_index, gate_index, *args):
        self._data[family_index]['gates'][gate_index]['value'] = value.get()

    def updatePercent(self, percent, family_index, gate_index, *args):
        self._data[family_index]['gates'][gate_index]['percent'] = percent.get()

    """
    Refreshes the table 
    args: 
        index - familty index to add from the self._data nested list;
        jndex - gate index within a family to add from the self._data nested list;
        dndex - row index where to input this data. 
    """
    def onRefresh(self, index=0, dindex=None, jndex=None, djndex=None ):
        if dindex == None: dindex = index

        # Save current checker value
        if jndex == None: 
            self._data[index]['expand'] = not self.data[dindex].is_expand
        else: 
            self._data[index]['gates'][jndex]['expand'] = not self.data[djndex].is_expand

        # Delete rows's data
        for row in self.data[dindex:]:
            self.data.remove(row)
            self.table.deleteRow(row.master)

            # deleting values and percent only if row contains Gate data
            try:
                self.gate_values.remove([row.value, row.percent])
            except:
                pass
                print(f'[Warning][Basis]: Can not remove (row.value, row.percent) from self.gate_values in {row}') 

        # Restore row's data
        for i, family in enumerate(self._data[index:]):
            self.addFamily(family, index+i)

    # def saveDynamicChanges(self, *args):
    #     for collection in self._data:


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
