import dataclasses


@dataclasses.dataclass
class Vocable:
    native: list[str]
    foreign: list[str]


class Dictionary:
    def __init__(self):
        self.languages: list[str] = []
        self.vocables: list[Vocable] = []


def read_header_from_file(dictionary: Dictionary, dictionary_file_path: str) -> None:
    with open(dictionary_file_path, "r") as dictionary_file:
        header = dictionary_file.readline()

    languages = header.split(";", 2)
    del languages[2]
    dictionary.languages = languages


def read_vocables_from_file(dictionary: Dictionary, dictionary_file_path: str) -> None:
    dictionary.vocables.clear()
    with open(dictionary_file_path, "r", encoding="utf-8") as dictionary_file:
        dictionary_file.readline()  # ignore first line
        while True:
            line = dictionary_file.readline()
            if not line:
                break
            words = line.strip().split(";")
            dictionary.vocables.append(
                Vocable(native=words[0].split(","), foreign=words[1].split(",")))


def read_dictionary(file_path: str) -> Dictionary:
    dictionary = Dictionary()
    read_header_from_file(dictionary, file_path)
    read_vocables_from_file(dictionary, file_path)
    return dictionary
