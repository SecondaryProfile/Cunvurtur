import PySimpleGUI as sg
import subprocess

# Read options from text file
with open('conversion_types.txt', 'r') as file:
    script_options = [line.strip() for line in file.readlines()]

# Define the layout
layout = [
    [sg.Text('Select a script to execute:')],
    [sg.DropDown(script_options, key='-SCRIPT-', enable_events=True, readonly=True)],
    [sg.Button('Execute'), sg.Button('Exit')]
]

# Create the window
window = sg.Window('Script Executor', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Execute':
        selected_script = values['-SCRIPT-']
        print(selected_script)

        subprocess.Popen(['python', 'conversion_scripts\\' + selected_script + '.py'])


window.close()
