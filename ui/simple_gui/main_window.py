import tkinter
from tkinter import ttk

import app.app_informations as app_informations
from app import event

SEARCHED_WORD_UNTRANSLATED_DEFAULT_FONT_SIZE = 25
RESPONSE_TO_LAST_INPUT_DEFAULT_FONT_SIZE = 16


class MainWindow(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"Vokabel Trainer {app_informations.VERSION}")
        self.geometry("600x180")

        # Label for searched untranslated word
        self.lbl_searched_words_untranslated = ttk.Label(self)
        self.lbl_searched_words_untranslated.config(font=("Arial", SEARCHED_WORD_UNTRANSLATED_DEFAULT_FONT_SIZE))
        self.lbl_searched_words_untranslated.pack(padx=10, pady=10)
        # Entry field for user input
        self.entry_field = tkinter.StringVar()
        txt_translation_user_input_field = ttk.Entry(self, textvariable=self.entry_field, font=("Arial", 16),
                                                     justify="center")
        txt_translation_user_input_field.pack()
        # Label contains the answer to last input
        self.lbl_response_to_last_input = ttk.Label(self, text="Enter correct translation",
                                                    font=("Arial", RESPONSE_TO_LAST_INPUT_DEFAULT_FONT_SIZE),
                                                    foreground='gray51')
        self.lbl_response_to_last_input.pack(padx=0, pady=0)
        # Label for special infos, like other right answers or a tipp for the searched word
        self.lbl_info_field = ttk.Label(self, font=("Arial", 14), foreground='blue')
        self.lbl_info_field.pack(padx=0, pady=0)
        # Key pressed actions
        txt_translation_user_input_field.bind("<Return>", self.__enter_key_pushed)
        txt_translation_user_input_field.bind("<Control_L>", self.__tipp_key_pushed)

    def set_searched_words_untranslated(self, searched_word: str) -> None:
        self.lbl_searched_words_untranslated.config(text=searched_word)
        self.__adjust_font_size_with_window_size(self.lbl_searched_words_untranslated,
                                                 font_size=SEARCHED_WORD_UNTRANSLATED_DEFAULT_FONT_SIZE,
                                                 min_font_size=10)

    def set_response_to_last_input(self, response: str, text_color="black") -> None:
        self.lbl_response_to_last_input.config(text=response, foreground=text_color)
        self.__adjust_font_size_with_window_size(self.lbl_response_to_last_input,
                                                 font_size=RESPONSE_TO_LAST_INPUT_DEFAULT_FONT_SIZE,
                                                 min_font_size=10)

    ''' private methods '''

    @staticmethod
    def __enter_key_pushed(__event) -> None:
        event.post_event("enter_key_pushed")

    @staticmethod
    def __tipp_key_pushed(__event) -> None:
        event.post_event("tipp_key_pushed")

    def __adjust_font_size_with_window_size(self, master: tkinter.Widget, font_size: int, min_font_size: int) -> None:
        while True:
            master.config(font=("Arial", font_size))
            master.update()
            if master.winfo_width() < self.winfo_width()-20 or font_size <= min_font_size:
                return
            font_size -= 1
