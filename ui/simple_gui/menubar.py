import tkinter
from tkinter import filedialog

from app import event


class MenuBar(tkinter.Menu):
    def __init__(self, master):
        super().__init__(master)
        # Options Menuebar
        options_bar = tkinter.Menu(self, tearoff=False, font=("Arial", 14))
        # -> Open dictionary
        options_bar.add_command(label="Open dictionary", command=self.__open_dictionary_clicked)
        # -> Searched language
        self.selected_language = tkinter.IntVar()
        self.selected_language.set(1)  # ToDo not so nice
        self.searched_language_bar = tkinter.Menu(self, tearoff=False, font=("Arial", 14))
        # ->-> German radiobutton
        self.searched_language_bar.add_radiobutton(label="-", command=self.__switch_language,
                                                   variable=self.selected_language, value=0)
        # ->-> English radiobutton
        self.searched_language_bar.add_radiobutton(label="-", command=self.__switch_language,
                                                   variable=self.selected_language, value=1)
        options_bar.add_cascade(label="Searched language", menu=self.searched_language_bar)
        # -> Info
        options_bar.add_command(label="Info", command=self.__info_clicked)
        # -> Exit
        options_bar.add_separator()
        options_bar.add_command(label="Exit", command=self.quit)
        self.add_cascade(label="Options", menu=options_bar)

    def __open_dictionary_clicked(self):
        filename = filedialog.askopenfilename(initialdir="./data/", title="Select a dictionary CSV file")
        print(filename)
        event.post_event("new_dictionary", filename)

    def set_up_dictionary_language_information(self, native: str, foreign) -> None:
        # change select language radiobuttons
        self.searched_language_bar.entryconfig(0, label=native)
        self.searched_language_bar.entryconfig(1, label=foreign)

    #
    def __switch_language(self) -> None:
        """ This method is called when the searched language radiobuttons are pushed. """
        event.post_event("change_searched_language", self.selected_language.get())

    @staticmethod
    def __info_clicked() -> None:
        event.post_event("show_info_window")