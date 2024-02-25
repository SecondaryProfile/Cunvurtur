import subprocess
from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class CunvurturApp(App):
    def build(self):
        # Setting window size
        Window.size = (400, 300)

        # Read options from text file
        with open('conversion_types.txt', 'r') as file:
            script_options = [line.strip() for line in file.readlines()]

        # Main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=[10])

        # Dropdown
        dropdown = DropDown()
        for option in script_options:
            btn = Button(text=option, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        main_button = Button(text='Select a script to execute', size_hint=(1, None), height=44)
        main_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(main_button, 'text', x))

        layout.add_widget(main_button)

        # Execute and Exit buttons
        button_layout = BoxLayout(spacing=10)

        execute_button = Button(text='Execute', size_hint=(0.5, None), height=44)
        execute_button.bind(on_release=lambda btn: self.execute_script(main_button.text))

        exit_button = Button(text='Exit', size_hint=(0.5, None), height=44)
        exit_button.bind(on_release=lambda btn: self.stop())

        button_layout.add_widget(execute_button)
        button_layout.add_widget(exit_button)

        layout.add_widget(button_layout)

        return layout

    def execute_script(self, selected_script):
        print(selected_script)
        subprocess.Popen(['python', 'conversion_scripts\\' + selected_script + '.py'])

if __name__ == '__main__':
    CunvurturApp().run()
