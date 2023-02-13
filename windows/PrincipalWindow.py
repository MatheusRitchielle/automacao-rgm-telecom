from tkinter import *

import pro_cep.main as pro_cep
import google_earth.main as google_earth
import simplifique.main as simplifique
import procep_consulta_cnpj.main as find_cnpj

window = Tk()
window.title('Automação ProCep')

text_orientation = Label(window, text='   ---- Informe o arquivo com os CEPs ----   ')
text_orientation.grid(column=0, row=0)

button_find_cnpjs = Button(window, text='PROCEP', command=pro_cep.find_cnpjs)
button_find_cnpjs.grid(column=0, row=2)

button_google_earth = Button(window, text='GOOGLE EARTH', command=google_earth.search_google_earth)
button_google_earth.grid(column=0, row=3)

button_simplifique = Button(window, text='SIMPLIFIQUE', command=simplifique.synergy_client)
button_simplifique.grid(column=0, row=4)

button_find_cnpj = Button(window, text='PROCEP - Busca CNPJ', command=find_cnpj.find_cnpj)
button_find_cnpj.grid(column=0, row=5)

button_position_mouse = Button(window, text='[ X ] POSIÇÃO DO MOUSE [ X ]', command=google_earth.mouse_position)
button_position_mouse.grid(column=0, row=6)

window.mainloop()
