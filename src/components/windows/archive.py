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

class Collection(tk.Frame):
        is_expand = False
        title = 'Untitled Collection'
        jobs_done = 0
        jobs_total = 1
        onExpand = lambda: print('[WARNING][Collection obj Initialization]: There is a None onExpand() function transmited to this Collection')
        onCollapse = lambda: print('[WARNING][Collection obj Initialization]: There is a None onCollapse() function transmited to this Collection')

        # """
        # An empty method, to show that the on_expand function was not 
        # given as an argument during initialization of this Collection.
        # """
        def onAction(self):
            if self.is_expand:
                self.onCollapse()
                self.expand_btn.config(text='+')
                self.is_expand = False
            else:
                self.onExpand()
                self.expand_btn.config(text='-')
                self.is_expand = True

            # print('[WARNING][Collection obj Initialization]: There is a None on_expan() function transmited to this Collection')

        def __init__ (self, master, expand=is_expand, title=title, done=jobs_done, total=jobs_total, bg='gray', onExpand=onExpand, onCollapse=onCollapse, *args, **kwargs):
            super().__init__(master, bg=bg, relief='flat', *args, **kwargs)
            self.is_expand = expand
            self.title = title
            self.jobs_done = done
            self.jobs_total = total
            self.onExpand = onExpand
            self.onCollapse = onCollapse

            self.expand_btn = tk.Button(self, bg=bg, text='+', relief='flat', command=self.onAction)
            if expand:
                self.expand_btn.config(text='-')
            self.title_lbl = tk.Label(self, bg=bg, text=title)
            self.jobs_lbl = tk.Label(self, bg=bg, text=f'{done}/{total}')

            self.expand_btn.pack(side='left', fill='both')
            self.title_lbl.pack(side='left', fill='both')
            self.jobs_lbl.pack(side='right', fill='both')

            # print(f'New Collection added to row {index}')

class SavePoint(tk.Frame):
    _states = ('Panding', 'Initialization', 'Synthesis', 'Optimization')

    progress = 0
    state = 'Panding'
    bg = 'black'

    def __init__ (self, master, datetime=None, progress=progress, state=state, bg=bg, *args, **kwargs):
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
        self.datetime_lbl = tk.Label(self, text=self.datetime, bg=bg)
        self.progress_lbl = tk.Label(self, text=f'{progress}%', bg=bg)
        self.state_lbl = tk.Label(self, text=self.state[0], bg=bg)

        self.wpad.pack(side='left', fill='both')
        self.datetime_lbl.pack(side='left', fill='both')
        self.state_lbl.pack(side='right', fill='both')
        self.progress_lbl.pack(side='right', fill='both')


class Archive(Window):
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

    "Deletes all rows' data after row with inputed index"
    def deleteAfter(self, index):
        
        index += 1
        for row in self.data[index:]:
            # print(row)
            row.destroy()
            self.data.remove(row)

        print(f'After Delete: {len(self.data)}')

    def addCollection(self, collection, static_index, dynamic_index):
        new_collection = Collection(
                master=self.table.getRow(dynamic_index), 
                expand=collection['expand'], 
                title=collection['title'], 
                done=len([item for item in collection['saves'] if item['progress']==100]),
                total=len(collection['saves']),
                onExpand=lambda s=static_index, d=dynamic_index: self.openCollection(s, d),
                onCollapse=lambda s=static_index, d=dynamic_index: self.closeCollection(s, d),
                bg=self.table.getBg(dynamic_index),
                )
        new_collection.master.clear()
        new_collection.pack(side='bottom', fill='x')
        self.data.append(new_collection)

        return new_collection

    def addSavePoint(self, save_point, dynamic_index):
        new_save_point = SavePoint(
                        master=self.table.getRow(dynamic_index),
                        datetime=save_point['datetime'],
                        progress=save_point['progress'], 
                        state=save_point['state'], 
                        bg=self.table.getBg(dynamic_index),
                    )
        new_save_point.master.clear()
        new_save_point.pack(side='bottom', fill='x')
        self.data.append(new_save_point)

    "Expends hiden rows with save points under the current collections"
    def openCollection(self, static_index, dynamic_index=None):
        if dynamic_index == None:
            dynamic_index = static_index
        self.deleteAfter(dynamic_index)
        self._data[static_index]['expand'] = True

        for save_point in self._data[static_index]['saves']:
            self.addSavePoint(save_point, len(self.data))

        for i, collection in enumerate(self._data[static_index+1:]):
            new_collection = self.addCollection(collection, static_index+i+1, len(self.data))
            if new_collection.is_expand:
                for save_point in collection['saves']:
                    self.addSavePoint(save_point, len(self.data))
                
        print(f'Collection in Row #{dynamic_index} Is Opened')

    "Hides rows with save points under the current collections"
    def closeCollection(self, static_index, dynamic_index=None):
        if dynamic_index == None:
            dynamic_index = static_index
        self.deleteAfter(dynamic_index)
        self._data[static_index]['expand'] = False

        for i, collection in enumerate(self._data[static_index+1:]):
            new_collection = self.addCollection(collection, static_index+i+1, len(self.data))
            if new_collection.is_expand:
                for save_point in collection['saves']:
                    self.addSavePoint(save_point, len(self.data))

        print(f'Collection in Row #{dynamic_index} Is Collapced')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title_var.set(self.title)
        self.table = table = Table(self.body, bg_odd=self.bg_odd)
        self.load_btn = tk.Button(self.right, text='Load', command=self.loadSaving)
        self.add_btn = tk.Button(self.right, text='Add', command=self.addSaving)
        self.data = [
            Collection(
                master=table.getTop(), 
                expand=collection['expand'], 
                title=collection['title'], 
                done=len([item for item in collection['saves'] if item['progress']==100]),
                total=len(collection['saves']),
                onExpand=lambda i=index: self.openCollection(i),
                onCollapse=lambda i=index: self.closeCollection(i),
                bg=table.getBg(),
                )
            for index, collection in enumerate(self._data)
            ]
        # print(f'Initialize: {len(self.data)}')
        self.table.pack(fill='both', expand=1)
        self.load_btn.pack(side='left', fill='both')
        self.add_btn.pack(side='right', fill='both')
        for row in self.data:
            row.master.clear()
            row.pack(side='top', fill='x')

