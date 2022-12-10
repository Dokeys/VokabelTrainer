import tkinter
from tkinter import ttk

import app.app_informations as app_informations


class InfoWindow(tkinter.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Info")
        self.geometry("400x200")
        self.protocol('WM_DELETE_WINDOW', self.__x_button_pushed)
        __lbl_header = ttk.Label(self, text=f"Vokabel Trainer {app_informations.VERSION}", font=("Arial", 26))
        __lbl_header.pack(pady=14)

        __lbl_developer_info = ttk.Label(self, text="Developed by Dominik Knoll", font=("Arial", 12))
        __lbl_developer_info.pack(pady=2)
        self.__lbl_dictionary_path = ttk.Label(self, text=f"Dictionary file: no file", font=("Arial", 12))
        self.__lbl_dictionary_path.pack(pady=2)

    def set_up_dictionary_information(self) -> None:
        # ToDo
        self.__set_dictionary_file_path("dictionary.get_file_path()")

    def __set_dictionary_file_path(self, path: str):
        self.__lbl_dictionary_path.config(text=f"Dictionary file: {path}")

    def __x_button_pushed(self):
        self.withdraw()
