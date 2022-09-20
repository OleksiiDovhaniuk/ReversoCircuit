"""
Parent class for all cards.

Author: Oleksii Dovhaniuk
Date: 20.09.2022
"""

import tkinter as tk

class Label(tk.Frame):
    """ Line where first element is a title of the parameter and last is a value of its parameter.

    Parameters
    ----------
    var : Tkinter StringVar
        Variable to change value of the parameter.
    """
    def __init__(self, master, title='Unknown', value='NaN', level=0, bg='gray', *args, **kwargs):
        """ Generate a Label tkinter Frame.
        Arguments
        ----------
        title = 'Unknown' : str
            Title of the parameter.
        value = 'NaN' : str
            Value of the parameter.
        level = 0 : int
            The hiegher the level the more tabs is at the begin of the line.
        """
        super().__init__(master, bg=bg, *args, **kwargs)
        self.var = tk.StringVar(self, value)

        level_lbl = tk.Label(self, text='  '*level, bg=bg)
        title_lbl = tk.Label(self, text=f'{title}:', bg=bg)
        value_lbl = tk.Label(self, textvariable=self.var, justify='right', bg=bg)

        level_lbl.pack(side='left')
        title_lbl.pack(side='left', fill='both')
        value_lbl.pack(side='right', fill='both')

class Card(tk.Frame):
    """ The card frame has two main sections top and body. The top section contains
    expend button, title and whole card can be move inside the masters window by holding
    and draging by the top section. Body section is informational section of the card and
    veries along different card types.

    Parameters
    ----------
    title : str
        Title of the card.
    is_expend : bool
        If True, the body section is shown; and if False only the top section is shown.
    _colour : str
        Hex value of the top section colour.

    """
    _top_bg = '#C0EBF9'
    _body_bg = 'white'

    def __init__(self, master, fields, title='Unknown', *args, **kwargs):
        super().__init__(master, bg=self._body_bg, *args, **kwargs)
        self.variables = variables = {}
        
        # Set up top section.
        top = tk.Frame(self, bg=self._top_bg)
        expand_btn = tk.Button(top, text='-', relief='flat', bg=self._top_bg)
        title_lbl = tk.Label(top, text=title, bg=self._top_bg)
        empty_btn = tk.Button(top, text=' ', relief='flat', state='disabled', bg=self._top_bg)

        expand_btn.pack(side='left')
        title_lbl.pack(side='left', expand=1, fill='both')
        empty_btn.pack(side='right')

        
        # Set up body section.
        body = tk.Frame(self, bg=self._body_bg)

        for field in fields:
            if field[0] == 'Label':
                label = Label(body, field[1], field[2], field[3], bg=self._body_bg)
                variables[field[1]] = label.var
                label.pack(side='top', fill='x')


        # Pack sections
        top.pack(side='top')
        body.pack(side='bottom')