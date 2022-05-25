from game.terminal_service import TerminalService
from game.skydiver import Skydiver
from game.dictionary import Dictionary

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
        
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._skydiver = Skydiver()
        self._dictionary = Dictionary()
        self._terminal_service = TerminalService()
        self._is_playing = True
        # self._evaluation = True
        self._dictionary._evaluation = True


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._dictionary._update_letters("")
        self._skydiver._draw_figure()

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
    

    def _get_inputs(self):
        new_guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._dictionary._evaluate_guess(new_guess)


    def _do_updates(self): 
        self._skydiver._check_status(self._dictionary._evaluation)
        self._dictionary._is_game_won()

    def _do_outputs(self):
        self._dictionary._update_letters(self._dictionary._current_letter)
        self._skydiver._draw_figure()
        if self._skydiver._is_dead_status():
            self._is_playing = False
            self._terminal_service.write_text("Game Over.")
        if self._dictionary._is_game_won():
            self._is_playing = False
            self._terminal_service.write_text("You Win!")