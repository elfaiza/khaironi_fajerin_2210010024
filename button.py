import PySimpleGUI as sg  
sg.theme("DarkAmber")  
sg.theme_text_color("#FF00FF")  
window = sg.Window(title="Contoh Button",  
                    layout=[[sg.Text("Contoh Button")],  
                            [sg.Button("Button Simpan")],  
                            [sg.Button("Button Keluar")]  
                           ],  
                    size=(400, 200),  
                    font=("Arial", 18))  
kejadian,nilai = window.read()  
print(kejadian, "=>", nilai)  
window.close()