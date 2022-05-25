import random
from game.terminal_service import TerminalService

class Dictionary:
    """The dictionary with the list of words and the mystery_word. 
    
    The responsibility of Dictionary is to choose a word from the list, evaluate guesses, and
    keep track of the mystery_word status.
    
    Attributes:
        _word_list [list(str)]: The list of words.
        _mystery_word (str): The selected mystery_word.
        _evaluation (boolean): Whether the latest letter guess was in the mystery_word or not.
        _revealed_letters (str): The letters guessed that are in the word.
    """
    def __init__(self):
        self._word_list = ['boy', 'mat', 'pen']
        # self._word_list = ['boy']
        self._mystery_word = self._word_list[random.randint(0, 2)]
        # self._mystery_word = self._word_list[0]
        self._revealed_letters = ""
        self._evaluation = True
        self._current_letter = ""
        self._guessed_letters = []
        self._correct_letters = []
        self._terminal_service = TerminalService()


    def _evaluate_guess(self, guess):
        self._current_letter = guess

        if guess not in self._guessed_letters:
            self._guessed_letters.append(guess)

        if guess not in self._mystery_word:
            self._evaluation = False
        else:
            if guess not in self._correct_letters:
                self._correct_letters.append(guess)

            self._evaluation = True


    def _update_letters(self, guess):
        blank = "_"
        ending = " "

        for letter in self._mystery_word:
            if letter in self._guessed_letters:
                self._terminal_service.write_text(letter, ending)
            else:
                self._terminal_service.write_text(blank, ending)

        self._terminal_service.write_text("")

    def _is_game_won(self):
        if set(self._correct_letters) == set(self._mystery_word):
            return True


