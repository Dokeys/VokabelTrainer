class CLI:
    def set_searched_word(self, searched_word: str) -> None:
        print(f"searched words are {searched_word}")

    def get_user_input(self) -> str:
        return input()

    def clear_user_input(self):
        print("__________________________________")

    def set_response_to_last_input(self, response: str, text_color: str) -> None:
        print(response)

    def set_info_field(self, info: str):
        print(f"info: {info}")

    def start(self):
        while True:
            pass