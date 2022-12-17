import dataclasses
import enum
from typing import Protocol

from app.dictionary import Dictionary, Vocable
from app import event


class Language(enum.IntEnum):
    NATIVE = 0
    FOREIGN = 1


class SelectionMechanism(Protocol):
    def get_next_vocable(self) -> int:
        ...


class VocablePicker:
    def __init__(self, dictionary: Dictionary, selection_mechanism: SelectionMechanism):
        VocablePickerListener(self)
        self.dictionary = dictionary
        self.selection_mechanism = selection_mechanism
        self.__searched_vocable_index = 0
        self.__searched_language = Language.FOREIGN

    @property
    def current_vocable(self) -> Vocable:
        return self.dictionary.vocables[self.__searched_vocable_index]

    @property
    def searched_words(self) -> list[str]:
        if self.searched_language == Language.NATIVE:
            return self.current_vocable.native
        elif self.searched_language == Language.FOREIGN:
            return self.current_vocable.foreign

    @property
    def searched_words_untranslated(self) -> list[str]:
        if self.searched_language == Language.FOREIGN:
            return self.current_vocable.native
        else:
            return self.current_vocable.foreign

    def set_next_vocable(self) -> None:
        last_word_index = self.__searched_vocable_index  # ToDo maybe its possible to get rid of index?
        while self.__searched_vocable_index == last_word_index:  # prevent the same word from coming twice
            self.__searched_vocable_index = self.selection_mechanism.get_next_vocable(self)

    @property
    def searched_language(self) -> Language:
        return self.__searched_language

    @searched_language.setter
    def searched_language(self, new_language: Language) -> None:
        self.__searched_language = new_language


class VocablePickerListener:
    def __init__(self, vocable_picker_for_listener: VocablePicker):
        self.__listener = vocable_picker_for_listener
        self.__setup_event_handlers()

    def __handle_change_searched_language(self, new_language: Language) -> None:
        self.__listener.searched_language = new_language
        self.__listener.set_next_vocable()
        event.post_event("new_word")

    def __setup_event_handlers(self):
        event.subscribe("change_searched_language", self.__handle_change_searched_language)

