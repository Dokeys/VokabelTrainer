'''
Vokabel Trainer

Author: Dominik Knoll

'''
from app import app
from ui.simple_gui import gui

DEFAULT_DICTIONARY_PATH = r"data/Vocabeln.dict"


def main():
    ui = gui.Gui()
    app.App(dictionary_file_path=DEFAULT_DICTIONARY_PATH, ui=ui)


if __name__ == '__main__':
    main()
