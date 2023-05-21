from tkinter import *
from tkinter import messagebox, filedialog


def interface(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']


def fonts(mode):
    text_fild['font'] = fonts_mode[mode]['font']


def exit_file():
    answer = messagebox.askokcancel('exit', 'Would you like to exit?')
    if answer:
        window.destroy()


def open_file():
    file_path = filedialog.askopenfilename(
        title='Files',
        filetypes=(
            ('Text documents (*.txt)', '*.txt'),
            ('All files', '*.*'))
    )
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())


def save_file():
    file_path = filedialog.asksaveasfilename(
        filetypes=(
            ('Text documents (*.txt)', '*.txt'),
            ('All files', '*.*'))
    )
    f = open(file_path, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()


window = Tk()
window.title('NoteBook')
window.geometry('600x700')

main_menu = Menu(window)

# file
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Close', command=exit_file)
window.config(menu=file_menu)

# view
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Black', command=lambda: interface('dark'))
view_menu_sub.add_command(label='Light', command=lambda: interface('light'))
view_menu.add_cascade(label='Interface', menu=view_menu_sub)
font_menu_sub.add_command(label='Arial', command=lambda: fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: fonts('Comic Sans MS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: fonts('Times New Roman'))
view_menu.add_cascade(label='Fonts', menu=font_menu_sub)
window.config(menu=view_menu)

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='View', menu=view_menu)
window.config(menu=main_menu)

frame_text = Frame(window)
frame_text.pack(fill=BOTH, expand=1)

view_colors = {
    'dark': {
        'text_bg': 'black',
        'text_fg': 'lime',
        'cursor': 'brown',
        'select_bg': '#80917A'
    },
    'light': {
        'text_bg': 'white',
        'text_fg': 'black',
        'cursor': '#A5A5A5',
        'select_bg': '#FAEEDD'
    }
}

fonts_mode = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'Comic Sans MS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'Times New Roman': {
        'font': ('Times New Roman', 14, 'bold')
    }
}

text_fild = Text(
    frame_text,
    bg='black',
    fg='lime',
    padx=10,
    pady=10,
    wrap=WORD,
    insertbackground='brown',
    selectbackground='#8D917A',
    spacing3=10,
    width=30,
    font='Arial 14 bold',
)
text_fild.pack(expand=1, fill=BOTH, side=LEFT)
scroll = Scrollbar(frame_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

window.mainloop()
