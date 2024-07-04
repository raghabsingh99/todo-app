import FreeSimpleGUI as sg
from zip_creater import make_archive


from zip_creater import make_archive

label1 = sg.Text("Select files to compress")
input1 = sg.Input(key="files")
chose_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder")
input2 = sg.Input(key="folder")
chose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, chose_button1],
                           [label2, input2, chose_button2],
                           [compress_button]])

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == "Compress":
        filepaths = values["files"]
        folder = values["folder"]
        try:
            make_archive(filepaths, folder)
            sg.popup("Compression Completed Successfully!")
        except Exception as e:
            sg.popup("Error", e)

window.close()
