"""
Archive Windows.

Author: Oleksii Dovhaniuk
Date: 15.07.2022
"""

import tkinter as tk
import datetime as dt
import time

from src.components.windows.window import Window
from src.assets.common.table import Table


class SavePoint(tk.Frame):
    _states = ('Panding', 'Initialization', 'Synthesis', 'Optimization')

    progress = 0
    state = 'Panding'
    bg = 'black'

    def __init__ (self, master, selection, datetime=None, progress=progress, state=state, bg=bg, *args, **kwargs):
        super().__init__(master, bg=bg, *args, **kwargs)
        if datetime:
            self.datetime = datetime
        else:
            self.datetime = dt.datetime.now(time.tzname).strftime("%c")
        self.progress = progress
        if state in self._states:
            self.state = state
        else:
            print(f'[WARNING][SavePoint obj Initialization]: There is no state {state}')

        self.wpad = tk.Button(self, text=' ', bg=bg, relief='flat', state='disabled')
        self.datetime_btn = tk.Radiobutton(self, text=self.datetime, variable=selection, value=str(self), indicator=0, bg=bg)
        self.progress_lbl = tk.Label(self, text=f'{progress}%', bg=bg)
        self.state_lbl = tk.Label(self, text=self.state[0], bg=bg)

        self.wpad.pack(side='left', fill='both')
        self.datetime_btn.pack(side='left', fill='x')
        self.state_lbl.pack(side='right', fill='both')
        self.progress_lbl.pack(side='right', fill='both')


class Collection(tk.Frame):
        is_expand = False
        title = 'Untitled Collection'
        jobs_done = 0
        jobs_total = 1
        onRefresh = lambda: print('[WARNING][Collection obj Initialization]: There is a None onRefresh() function transmited to this Collection')

        def __init__ (self, master, expand=is_expand, title=title, done=jobs_done, total=jobs_total, bg='gray', onRefresh=onRefresh, *args, **kwargs):
            super().__init__(master, bg=bg, relief='flat', *args, **kwargs)
            self.is_expand = expand
            self.title = title
            self.jobs_done = done
            self.jobs_total = total
            self.onRefresh = onRefresh

            self.expand_btn = tk.Button(self, bg=bg, text='+', relief='flat', command=self.onRefresh)
            if expand:
                self.expand_btn.config(text='-')
            self.title_lbl = tk.Label(self, bg=bg, text=title)
            self.jobs_lbl = tk.Label(self, bg=bg, text=f'{done}/{total}')

            self.expand_btn.pack(side='left', fill='both')
            self.title_lbl.pack(side='left', fill='both')
            self.jobs_lbl.pack(side='right', fill='both')

class Archive(Window):
    """ The class represents a window with table of a saved jobs. Inherited from a Window class.
    """
    title = 'Archive'
    bg = '#FFFFFF'
    bg_odd = '#E8EEF2'
    data = []

    _data = [
        {   
            'expand': False,                #Bool
            'title': '3-bit Full Adder',    #Str
            'saves': [                      #Nested list
                {
                    'datetime': '20.07.2022 - 10:22',   #Str
                    'progress': 10,                      #Int
                    'state': 'Panding',                 #Str (selection from a tuple)
                },
            ]
        },
        {   
            'expand': False,                #Bool
            'title': '8-bit Full Adder',    #Str
            'saves': [                      #Nested list
                {
                    'datetime': '21.07.2022 - 14:13',   #Str
                    'progress': 0.00,                      #Int
                    'state': 'Panding',                 #Str (selection from a tuple)
                },
                {
                    'datetime': '21.07.2022 - 11:13',   #Str
                    'progress': 100,                      #Int
                    'state': 'Panding',                 #Str (selection from a tuple)
                },
                {
                    'datetime': '26.07.2022 - 09:03',   #Str
                    'progress': 30,                      #Int
                    'state': 'Panding',                 #Str (selection from a tuple)
                },
                # {
                #     'datetime': '26.07.2022 - 17:20',   #Str
                #     'progress': 0,                      #Int
                #     'state': 'Panding',                 #Str (selection from a tuple)
                # },
            ]
        },
        {   
            'expand': False,                #Bool
            'title': 'IRP of 4-bit RRG',    #Str
            'saves': [                      #Nested list
                {
                    'datetime': '21.07.2022 - 17:27',   #Str
                    'progress': 50,                      #Int
                    'state': 'Panding',                 #Str (selection from a tuple)
                },
                {
                    'datetime': '21.07.2022 - 17:27',   #Str
                    'progress': 50,                      #Int
                    'state': 'Panding',                 #Str (selection from a tuple)
                },
                {
                    'datetime': '21.07.2022 - 17:27',   #Str
                    'progress': 50,                      #Int
                    'state': 'Panding',                 #Str (selection from a tuple)
                },
                {
                    'datetime': '21.07.2022 - 17:27',   #Str
                    'progress': 50,                      #Int
                    'state': 'Panding',                 #Str (selection from a tuple)
                },
            ]
        },
    ]

    def loadSaving(self):
        print('Load a Saving')

    def addSaving(self):
        print('Add a Saving')

    """
    Adds Save Point data to the table.
    args: 
        save_point - Save Point date from the ;
    """
    def addSavePoint(self, save_point):
        djndex = len(self.data) # local dynamic index
        new_save_point = SavePoint(
                        master=self.table.addRow(djndex),
                        datetime=save_point['datetime'],
                        progress=save_point['progress'], 
                        state=save_point['state'], 
                        # is_selected=False,
                        selection=self.selected,
                        bg=self.table.getBg(djndex),
                    )
        new_save_point.master.clear()
        new_save_point.pack(side='bottom', fill='x')
        self.data.append(new_save_point)

    """
    Adds Collection data to the table.
    args: 
        collection - Collection;
        index - familty index to add from the self._data nested list;
    """
    def addCollection(self, collection, index):
        dindex = len(self.data) # dynamic index
        new_collection = Collection(
            master=self.table.addRow(dindex), 
            expand=collection['expand'], 
            title=collection['title'], 
            done=len([item for item in collection['saves'] if item['progress']==100]),
            total=len(collection['saves']),
            onRefresh=lambda i=index, d=dindex: self.onRefresh(i, d),
            # is_selected = False,
            bg=self.table.getBg(dindex),
            )

        new_collection.master.clear()
        new_collection.pack(side='bottom', fill='x')
        self.data.append(new_collection)

        if collection['expand']:
            for save_points in collection['saves']:
                self.addSavePoint(save_points)

    """
    Refreshes the table 
    args: 
        index - familty index to add from the self._data nested list;
        jndex - gate index within a family to add from the self._data nested list;
        dndex - row index where to input this data. 
    """
    def onRefresh(self, index=0, dindex=None):
        if dindex == None: dindex = index
        self._data[index]['expand'] = not self.data[dindex].is_expand

        # # Delete rows's data
        for row in self.data[dindex:]:
            self.data.remove(row)
            self.table.deleteRow(row.master)

        # Restore row's data
        for i, collection in enumerate(self._data[index:]):
            self.addCollection(collection, index+i)


    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title_var.set(self.title)
        self.table = Table(self.body, bg_odd=self.bg_odd)
        self.load_btn = tk.Button(self.right, text='Load', command=self.loadSaving)
        self.add_btn = tk.Button(self.right, text='Add', command=self.addSaving)
        self.selected = tk.StringVar(self, 0)

        for index, collection in enumerate(self._data):
            self.addCollection(collection, index)
        
        self.table.pack(fill='both', expand=1)
        self.load_btn.pack(side='left', fill='both')
        self.add_btn.pack(side='right', fill='both')
        for row in self.data:
            row.master.clear()
            row.pack(side='top', fill='x')