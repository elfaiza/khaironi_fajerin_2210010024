import PySimpleGUI as sg
susunan=[[sg.VPush()],
          [sg.Text("UNISKA MAAB",font=("arial",24))],
          [sg.Text("BANJARMASIN",font=("Courier", 18))],
          [sg.VPush()]]
window = sg.Window(title="Element Text",
                   layout=susunan,
                   element_justification="center",
                   size=(430,200))
window.read()
window.close()