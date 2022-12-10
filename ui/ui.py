from typing import Protocol


class UI(Protocol):
    def set_searched_word(self, searched_word: str) -> None:
        raise NotImplementedError()

    def get_user_input(self) -> str:
        raise NotImplementedError()

    def clear_user_input(self) -> None:
        raise NotImplementedError()

    def set_response_to_last_input(self, response: str, text_color: str) -> None:
        raise NotImplementedError()

    def set_info_field(self, info: str) -> None:
        raise NotImplementedError()

    def start(self) -> None:
        raise NotImplementedError()
