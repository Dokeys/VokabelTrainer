from app import event
from .main_window import MainWindow
from .menubar import MenuBar
from .info_window import InfoWindow


class Gui:
    def __init__(self):
        self.main_window = MainWindow()

        self.menubar = MenuBar(self.main_window)
        self.main_window.config(menu=self.menubar)

        self.info_window = InfoWindow()
        self.info_window.withdraw()  # hide info window

        GuiListener(self)

    def set_searched_word(self, searched_word: str) -> None:
        self.main_window.set_searched_words_untranslated(searched_word)

    def get_user_input(self) -> str:
        return str(self.main_window.entry_field.get())

    def clear_user_input(self):
        self.main_window.entry_field.set("")

    def set_response_to_last_input(self, response: str, text_color="black") -> None:
        self.main_window.set_response_to_last_input(response, text_color)

    def set_info_field(self, info: str):
        self.main_window.lbl_info_field.config(text=info)

    def start(self):
        self.main_window.mainloop()


class GuiListener:
    def __init__(self, gui_for_listener: Gui):
        self.__listener_gui = gui_for_listener
        self.__setup_gui_event_handlers()

    def __handle_setup_dictionary_language_information(self, native: str, foreign: str) -> None:
        self.__listener_gui.menubar.set_up_dictionary_language_information(native, foreign)

    def __handle_show_info_window(self):
        self.__listener_gui.info_window.deiconify()

    def __setup_gui_event_handlers(self):
        event.subscribe("setup_dictionary_language_information", self.__handle_setup_dictionary_language_information)
        event.subscribe("show_info_window", self.__handle_show_info_window)



