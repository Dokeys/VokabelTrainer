import tkinter
from tkinter import ttk
from app import event

import app.app_informations as app_informations


class InfoWindow(tkinter.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Info")
        self.geometry("600x200")
        self.protocol('WM_DELETE_WINDOW', self.__x_button_pushed)
        __lbl_header = ttk.Label(self, text=f"Vokabel Trainer {app_informations.VERSION}", font=("Arial", 26))
        __lbl_header.pack(pady=14)

        __lbl_developer_info = ttk.Label(self, text="Developed by Dominik Knoll", font=("Arial", 12))
        __lbl_developer_info.pack(pady=2)
        self.__lbl_dictionary_path = ttk.Label(self, text=f"Dictionary file: no file", font=("Arial", 12))
        self.__lbl_dictionary_path.pack(pady=2)
        __tipp_key = ttk.Label(self, text="Press control key to get letter byy letter for searched word.",
                               font=("Arial", 12))
        __tipp_key.pack(pady=2)

        InfoWindowListener(self)

    def set_dictionary_file_path(self, path: str):
        self.__lbl_dictionary_path.config(text=f"Dictionary file: {path}")

    def __x_button_pushed(self):
        self.withdraw()


class InfoWindowListener:
    def __init__(self, info_window_for_listener: InfoWindow):
        self.__listener = info_window_for_listener
        self.__setup_event_handlers()

    def __handle_new_dictionary(self, file_path: str) -> None:
        self.__listener.set_dictionary_file_path(file_path)

    def __setup_event_handlers(self):
        event.subscribe("new_dictionary", self.__handle_new_dictionary)
