import PySimpleGUI as sg
susunan=[[sg.Text("UNISKA MAAB", font=("arial",24))],
          [sg.Text("BANJARMASIN", font=("courier",18))]]
window = sg.Window(title="New Icon",
                   layout=susunan,
                   element_justification="center",
                   icon="favicon.ico",
                   size=(420,200))
window.read()
window.close()