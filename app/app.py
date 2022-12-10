'''
ToDo:
-probability for new word
-
'''
import random

from ui.ui import UI
from .dictionary import read_dictionary
from .vocablepicker import VocablePicker
from .selection_mechanism import RandomVocablePicker
import app.event as event


class App:
    def __init__(self, dictionary_file_path: str, ui: UI):
        AppListener(self)

        self.vocable_picker = self.setup_dictionary(dictionary_file_path)

        self.ui = ui

        self.__show_tipp_index = 0  # wird nur in einer Funktion gebraucht
        self.__word_for_tipp = ""

        self.vocable_picker.set_next_vocable()
        self.refresh_window()
        ui.start()

    @staticmethod
    def setup_dictionary(file_path: str) -> VocablePicker:  # ToDo ugly
        dictionary = read_dictionary(file_path)
        random_vocable_picker = RandomVocablePicker()
        vocable_picker = VocablePicker(dictionary, random_vocable_picker)

        event.post_event("setup_dictionary_language_information", dictionary.languages[0], dictionary.languages[1])

        return vocable_picker

    def enter_key_pushed(self) -> None:
        self.__check_user_input_and_show_answer(self.ui.get_user_input())
        self.vocable_picker.set_next_vocable()
        self.refresh_window()

    def tipp_key_pushed(self) -> None:
        self.ui.set_info_field(f"Tipp: {self.__get_tipp_string()}")

    def refresh_window(self):
        self.ui.set_searched_word(get_words_string_with_comma(self.vocable_picker.searched_words_untranslated))
        self.__show_tipp_index = 0
        self.ui.clear_user_input()

    # ToDo überarbeiten
    def __get_tipp_string(self) -> str:
        if self.__show_tipp_index == 0:
            random_word_number = random.randrange(0, len(self.vocable_picker.searched_words))
            self.__word_for_tipp = self.vocable_picker.searched_words[random_word_number]
        self.__show_tipp_index += 1
        return self.__word_for_tipp[:self.__show_tipp_index]

    def __check_user_input_and_show_answer(self, user_input: str) -> None:
        untranslated_words = self.vocable_picker.searched_words_untranslated
        translated_words = self.vocable_picker.searched_words
        if user_input in translated_words:
            self.__correct_translation_output(untranslated_words, translated_words, user_input)
        else:
            self.__incorrect_translation_output(untranslated_words, translated_words, user_input)

    def __correct_translation_output(self, untranslated_words: list[str], translated_words: list[str], user_input: str) -> None:
        response_string = App.__get_correct_input_string(untranslated_words, user_input)
        self.ui.set_response_to_last_input(response_string, text_color="green")
        info_string = App.__get_multiple_correct_answers_string(translated_words, user_input)
        self.ui.set_info_field(info_string)

    def __incorrect_translation_output(self, untranslated_words: list[str], translated_words: list[str], user_input: str) -> None:
        response_string = self.__get_string_for_incorrect_input(untranslated_words, translated_words, user_input)
        self.ui.set_response_to_last_input(response_string, text_color="red")
        self.ui.set_info_field("")

    @staticmethod
    def __get_correct_input_string(untranslated_words: list[str], user_input: str) -> str:
        return f"Richtig: {user_input} für {get_words_string_with_comma(untranslated_words)} war richtig"

    @staticmethod
    def __get_multiple_correct_answers_string(translated_words: list[str], user_input: str) -> str:
        if len(translated_words) == 1:
            return ""
        response_string = "Alternative:"  # if there are more than one correct answer possibility's
        alternative_words = list(
            set(translated_words).difference(set([user_input])))  # filter out word that user has entered
        for word in alternative_words:
            response_string += f" {word},"
        response_string = response_string[:-1]  # delete last ","
        return response_string

    @staticmethod
    def __get_string_for_incorrect_input(untranslated_words: list[str], translated_words: list[str],
                                         user_input: str) -> str:
        return f"Falsch: {get_words_string_with_comma(untranslated_words)} = {get_words_string_with_comma(translated_words)}, nicht {user_input}."


def get_words_string_with_comma(words: list[str]) -> str:
    searched_words_string = ""
    for word in words:
        searched_words_string += f"{word}, "
    searched_words_string = searched_words_string[:-2]  # remove last ", "
    return searched_words_string


class AppListener:
    def __init__(self, app_for_listener: App):
        self.__listener_app = app_for_listener
        self.__setup_gui_event_handlers()

    def __handle_enter_key_pushed(self):
        self.__listener_app.enter_key_pushed()

    def __handle_tipp_key_pushed(self):
        self.__listener_app.tipp_key_pushed()

    def __handle_new_word(self):
        self.__listener_app.refresh_window()

    def __handle_new_dictionary(self, file_path: str) -> None:
        self.__listener_app.vocable_picker = self.__listener_app.setup_dictionary(file_path)
        self.__listener_app.vocable_picker.set_next_vocable()
        self.__listener_app.refresh_window()

    def __setup_gui_event_handlers(self):
        event.subscribe("enter_key_pushed", self.__handle_enter_key_pushed)
        event.subscribe("tipp_key_pushed", self.__handle_tipp_key_pushed)
        event.subscribe("new_word", self.__handle_new_word)
        event.subscribe("new_dictionary", self.__handle_new_dictionary)
