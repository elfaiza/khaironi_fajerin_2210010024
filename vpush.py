import PySimpleGUI as sg
susunan=[[sg.VPush(),
          sg.Text("UNISKA MAAB",font=("arial",24)),
          sg.Push()],
          [sg.Push(),
          sg.Text("BANJARMASIN", font=("Courier",18)),
          sg.VPush()]
          ]
window = sg.Window(title="Elemen Text",  
                   layout=susunan,  
                   size=(430,200))  
window.read()  
window.close()