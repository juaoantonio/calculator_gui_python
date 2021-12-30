import tkinter as tk
from typing import List


def make_root(title: str) -> tk.Tk:
    root = tk.Tk()
    root.title(title)
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    return root


def make_label(root: tk.Tk) -> tk.Label:
    label = tk.Label(
        root,
        text='Nenhuma conta realizada',
        anchor='e',
        justify='right',
        background='#fff'
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label


def make_display(root: tk.Tk) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(
        font=('Helvetica', 40, 'normal'),
        justify='right',
        bd=1,
        relief='flat',
        highlightthickness=1,
        highlightcolor='#ccc'
    )
    display.bind('<Control-a>', _display_control_a)
    return display


def _display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'


def make_button(root) -> List[List[tk.Button]]:
    button_text: List[List[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '='],
    ]

    buttons: List[List[tk.Button]] = []

    for row_index, row_value in enumerate(button_text, start=2):
        button_row = []
        for column_index, column_value in enumerate(row_value):
            btn = tk.Button(root, text=column_value)
            btn.grid(row=row_index, column=column_index, sticky='news', padx=5, pady=5)
            btn.config(
                font=('Helvetica', 15, 'normal'),
                pady=40,
                width=1,
                background='#f1f2f3',
                bd=0,
                cursor='hand2',
                highlightthickness=0,
                highlightcolor='#ccc',
                highlightbackground='#ccc',
                activebackground='#ccc'
            )
            button_row.append(btn)
        buttons.append(button_row)

    return buttons


if __name__ == '__main__':
    pass
