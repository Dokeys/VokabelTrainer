import random
import dataclasses

from .vocablepicker import VocablePicker


IN_DECREASE_PROBABILITY_FACTOR = 0.10
PROBABILITY_MIN_VALUE = 0.1
PROBABILITY_MAX_VALUE = 1.0


class RandomVocablePicker:
    @staticmethod
    def get_next_vocable(vocable_picker: VocablePicker) -> int:
        return random.randint(0, len(vocable_picker.dictionary.vocables)-1)


@dataclasses.dataclass
class ProbabilityFactor:
    __native: float = 1.0  # The greater the value, the greater the probability that the word will be queried.
    __foreign: float = 1.0

    @property
    def native(self) -> float:
        return self.__native

    @native.setter
    def native(self, new_value: float) -> None:
        if PROBABILITY_MIN_VALUE <= new_value <= PROBABILITY_MAX_VALUE:  # probability factor limitation
            self.__native = new_value

    @property
    def foreign(self) -> float:
        return self.__foreign

    @foreign.setter
    def foreign(self, new_value: float) -> None:
        if PROBABILITY_MIN_VALUE <= new_value <= PROBABILITY_MAX_VALUE:  # probability factor limitation
            self.__foreign = new_value


class ProbabilityVocablePicker:  # ToDo
    def __init__(self, dictionary):

        self.dictionary = dictionary

    def get_next_vocable(self) -> int:
        raise NotImplementedError()