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


'''
    # ToDo split up
    __native_probability_factor: float = 1.0  # The greater the value, the greater the probability that the word will be queried.
    __foreign_probability_factor: float = 1.0

    @property
    def native_probability_factor(self) -> float:
        return self.__native_probability_factor

    @native_probability_factor.setter
    def native_probability_factor(self, new_value: float) -> None:
        if PROBABILITY_MIN_VALUE <= new_value <= PROBABILITY_MAX_VALUE:  # probability factor limitation
            self.__native_probability_factor = new_value

    @property
    def foreign_probability_factor(self) -> float:
        return self.__foreign_probability_factor

    @foreign_probability_factor.setter
    def foreign_probability_factor(self, new_value: float) -> None:
        if PROBABILITY_MIN_VALUE <= new_value <= PROBABILITY_MAX_VALUE:  # probability factor limitation
            self.__foreign_probability_factor = new_value


class ProbabilityManager:
    def __init__(self, dictionary: dicitonary.Dictionary):
        self.__dictionary = dictionary

    def right_user_input(self):
        if self.__dictionary.searched_language == dicitonary.Language.FOREIGN:
            self.__dictionary.current_vocable.foreign_probability_factor -= IN_DECREASE_PROBABILITY_FACTOR
        else:
            self.__dictionary.current_vocable.native_probability_factor -= IN_DECREASE_PROBABILITY_FACTOR

    def wrong_user_input(self):
        if self.__dictionary.searched_language == dicitonary.Language.FOREIGN:
            self.__dictionary.current_vocable.foreign_probability_factor += IN_DECREASE_PROBABILITY_FACTOR
        else:
            self.__dictionary.current_vocable.native_probability_factor += IN_DECREASE_PROBABILITY_FACTOR

    # ToDo unübersichtlich
    def get_next_index_with_probability(self) -> int:
        random_number_choices_sum = random.uniform(0, self.get_probability_factor_sum())
        weight_sum = 0
        for index, vocable in enumerate(self.__dictionary.__vocables):
            if self.__dictionary.searched_language == dicitonary.Language.FOREIGN:
                weight_sum += vocable.foreign_probability_factor
            else:
                weight_sum += vocable.native_probability_factor

            if random_number_choices_sum < weight_sum:
                return index

    def get_probability_factor_sum(self) -> float:
        probability_factor_sum = 0
        for vocable in self.__dictionary.__vocables:
            if self.__dictionary.searched_language == dicitonary.Language.FOREIGN:
                probability_factor_sum += vocable.foreign_probability_factor
            else:
                probability_factor_sum += vocable.native_probability_factor
        return probability_factor_sum
'''

