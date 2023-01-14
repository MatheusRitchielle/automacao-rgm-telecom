from tkinter import *

import services.ProCep as proCep
import services.GoogleEarth as googleEarth

window = Tk()
window.title('Automação ProCep')

text_orientation = Label(window, text='   ---- Informe o arquivo com os CEPs ----   ')
text_orientation.grid(column=0, row=0)

button_explorer_files = Button(window, text='Buscar arquivos:', command=proCep.explorer_files)
button_explorer_files.grid(column=0, row=1)

button_find_cnpjs = Button(window, text='PROCEP', command=proCep.find_cnpjs)
button_find_cnpjs.grid(column=0, row=2)

button_google_earth = Button(window, text='GOOGLE EARTH', command=googleEarth.find_google_earth)
button_google_earth.grid(column=0, row=3)

button_position_mouse = Button(window, text='POSIÇÃO DO MOUSE', command=googleEarth.position_mouse)
button_position_mouse.grid(column=0, row=4)

window.mainloop()
