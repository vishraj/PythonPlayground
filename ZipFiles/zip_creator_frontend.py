import FreeSimpleGUI as sg
from zip_creator_backend import extract_archive

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")
exit_button = sg.Button("Exit")

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])

window = sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3],
                           [extract_button],
                           [exit_button]],
                           font=("Helvetica", 20))

while True:
    event, values = window.read()

    match event:
        case "Extract":
            archive_path = values["archive"].strip()
            dest_dir = values["folder"].strip()
            extract_archive(archive_path, dest_dir)
            window["output"].update(value="Extract Completed.")

        case "Exit":
            break

window.close()

