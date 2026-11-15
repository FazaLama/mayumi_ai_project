import subprocess
import webbrowser
import os


class DesktopTools:

    @staticmethod
    def open_notepad():

        subprocess.Popen("notepad.exe")

        return "Notepad berhasil dibuka."

    @staticmethod
    def open_calculator():

        subprocess.Popen("calc.exe")

        return "Calculator berhasil dibuka."

    @staticmethod
    def open_browser(url="https://www.google.com"):

        webbrowser.open(url)

        return "Browser berhasil dibuka."

    @staticmethod
    def open_folder(path):

        if os.path.exists(path):

            os.startfile(path)

            return f"Folder berhasil dibuka: {path}"

        return "Folder tidak ditemukan."