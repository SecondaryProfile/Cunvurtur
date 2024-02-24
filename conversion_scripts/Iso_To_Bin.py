import PySimpleGUI as sg
import subprocess
import sys

def check_bchunk():
    try:
        subprocess.run(['bchunk', '--help'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_bchunk():
    print("bchunk is required for this program. Please install it using your system's package manager.")
    # Include installation instructions here based on the user's operating system
    sys.exit(1)

def iso_to_bin_cue(iso_file, bin_file, cue_file):
    try:
        subprocess.run(['bchunk', iso_file, bin_file, cue_file], check=True)
        sg.popup("Conversion complete!", title="Success")
    except subprocess.CalledProcessError as e:
        sg.popup_error(f"Error: {e}", title="Conversion Error")

layout = [
    [sg.Text("Select ISO file:")],
    [sg.InputText(key="iso_file"), sg.FileBrowse()],
    [sg.Text("Enter BIN file name (output):")],
    [sg.InputText(key="bin_file"), sg.FileSaveAs()],
    [sg.Text("Enter CUE file name (output):")],
    [sg.InputText(key="cue_file"), sg.FileSaveAs()],
    [sg.Button("Convert"), sg.Button("Exit")]
]

window = sg.Window("ISO to BIN/CUE Converter", layout)
if not check_bchunk():
    install_bchunk()
else:
    print("bchunk is installed. Proceeding with the program...")

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "Convert":
            iso_file = values["iso_file"]
            bin_file = values["bin_file"]
            cue_file = values["cue_file"]
            
            if not iso_file or not bin_file or not cue_file:
                sg.popup_error("Please enter all files!", title="Error")
            else:
                iso_to_bin_cue(iso_file, bin_file, cue_file)

window.close()
