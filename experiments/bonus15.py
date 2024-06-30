import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
chose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destinatinon folder")
input2 = sg.Input()
chose_button2 = sg.FolderBrowse("Choose")
compress_button = sg.Button("compress")
window = sg.Window("file Compressor",
                   layout=[[label1, input1, chose_button1],
                           [label2, input2, chose_button2],[compress_button]])

window.read()
window.close()
