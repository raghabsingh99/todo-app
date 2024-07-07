import PySimpleGUI as sg
from zip_extractor import extract_archive
sg.theme("black")

label1 = sg.Text("select archive.")
input1 = sg.Input()
chose_button1 = sg.FilesBrowse("Choose", key="archive")

label2 = sg.Text("select dest dir.")
input2 = sg.Input()
chose_button2 = sg.FolderBrowse("Choose",key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output",text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, chose_button1],
                           [label2, input2, chose_button2],
                           [extract_button,output_label]])

while True:
    event,values = window.read()
    print(event,values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath,dest_dir)
    window["output"].update(value = "extraction completed")

window.close()

