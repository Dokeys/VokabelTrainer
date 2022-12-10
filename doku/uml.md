classDiagram
    App --* Gui
    App --* Dictionary
    class App{
        -dictionoary: Dictionary
        -gui: Gui
        -show_tipp_index: int
        -word_for_tipp: str

        -enter_key_pushed(event)
        -key_for_tipp_pushed(event)
        -get_tipp_string()
        -check_user_input(user_input: str)
        -correct_translation_output(untranslated_words: list)
        -incorrect_translation_output(untranslated_words: list, translated_words, user_input: str)
        -get_correct_input_string(untranslated_words: List, user_input: str): str
        -get_multiple_correct_answers_string(translated_words: list, user_input: str): str
        -get_string_for_incorrect_input(untranslated_words: List[str], translated_words: List[str], user_input: str): str
        -set_new_word()
        -get_words_string_with_comma(words: list): str
    }
    Dictionary --* ProbabilityManager
    class Dictionary{
        -__languages: List[str]
        -__vocables: List[Vocable]
        -__file_path: str
        -__searched_vocable_index: int
        -__searched_language: Language

        +read_dictionary_file(dictionary_path: str)
        +get_searched_words(): List[str]
        +get_untranslated_words(): List[str]
        +set_new_searched_word()
        -__read_header_from_file(dictionary_file_path: str)
        -__read_vocables_from_file(dictionary_file_path: str)
        -__read_probability_factor_from_file()
    }
    class ProbabilityManager{
        +read_probability_factor_from_file()
        -__weighted_choice(choices: tuple): str
    }
    Gui --* MenuBar
    class Gui{

    }
    MenuBar --* InfoWindow
    class MenuBar{

    
    }
    class InfoWindow{

    }

