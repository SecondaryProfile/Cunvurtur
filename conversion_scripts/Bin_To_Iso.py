import PySimpleGUI as sg
import subprocess
import sys

def check_bchunk():
    try:
        subprocess.run(['bchunk', '--help'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

def install_bchunk():
    print("bchunk is required for this program. Please install it using your system's package manager or found here.\n") 
    print(b"https://github.com/extramaster/bchunk")
    sys.exit(1)

def bin_cue_to_iso(bin_file, cue_file, iso_file):
    try:
        subprocess.run(['bchunk', '-v', '-r', bin_file, cue_file, iso_file], check=True)
        sg.popup("Conversion complete!", title="Success")
    except subprocess.CalledProcessError as e:
        sg.popup_error(f"Error: {e}", title="Conversion Error")

layout = [
    [sg.Text("Select BIN file:")],
    [sg.InputText(key="bin_file"), sg.FileBrowse()],
    [sg.Text("Select CUE file:")],
    [sg.InputText(key="cue_file"), sg.FileBrowse()],
    [sg.Text("Enter ISO file name (output):")],
    [sg.InputText(key="iso_file"), sg.FileSaveAs()],
    [sg.Button("Convert"), sg.Button("Exit")]
]

window = sg.Window("BIN/CUE to ISO Converter", layout)

if not check_bchunk():
    install_bchunk()
else:
    print("bchunk is installed. Proceeding with the program...")

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == "Exit":
            break
        elif event == "Convert":
            bin_file = values["bin_file"]
            cue_file = values["cue_file"]
            iso_file = values["iso_file"]
            
            if not bin_file or not cue_file or not iso_file:
                sg.popup_error("Please select all files!", title="Error")
            else:
                bin_cue_to_iso(bin_file, cue_file, iso_file)

    window.close()
