from typing import Final

from main import assess_guess
from permutation import gen_lottery_results

# Algorithm here is not the best one.

NUMBER_CHOICES: Final[list[str]] = [str(i) for i in range(10)]


class RuleBasedPlayer:
    def __init__(self) -> None:
        self.__guess: str | None = None
        self.__feedback_received: str | None = None
        self.__candidates: set[tuple[str]] = set()
        self.refresh()

    def make_a_guess(self) -> str:
        if self.__feedback_received:
            a, b = int(self.__feedback_received[0]), int(self.__feedback_received[2])
            if a < 0 or b < 0 or (a + b) > 4:
                raise ValueError("You provided invalid message to me.")
            elif a == 4:
                raise ValueError("I've already won.")
            elif a + b == 0:
                self.__candidates -= gen_lottery_results(list(self.__guess), 4)  # type: ignore
            elif a + b == 4:
                self.__candidates &= gen_lottery_results(list(self.__guess), 4)  # type: ignore
            self.__remove_impossible_candidates(a, b)
        self.__guess = "".join(self.__candidates.pop())
        return self.__guess

    def __remove_impossible_candidates(self, a: int, b: int) -> None:
        to_remove: set[tuple[str]] = set()
        for each in self.__candidates:
            assessment = assess_guess(self.__guess, "".join(each))  # type: ignore
            _a, _b = int(assessment[0]), int(assessment[2])
            if _a != a or _b != b:
                to_remove.add(each)
        self.__candidates -= to_remove

    def receive_feedback(self, feedback: str) -> None:
        self.__feedback_received = feedback

    def refresh(self) -> None:
        self.__guess = None
        self.__feedback_received = None
        self.__candidates = gen_lottery_results(NUMBER_CHOICES, 4)

    # def playOnceWithHuman(self):
    #     global computerGuess, mes, cGHistroy
    #     # time.sleep(1)
    #     computerGuess = guess(computerGuess, mes)
    #     cGHistroy.append(list(computerGuess))
    #     print("\t\t\t\t" + computerGuess)
    #     # time.sleep(1)
    #     mes = input()


if __name__ == "__main__":
    from mystdout import ForegroundColor, mystdout
    from myutils import clear_terminal

    player = RuleBasedPlayer()
    clear_terminal("hard")
    while True:
        try:
            guess = player.make_a_guess()
        except KeyError:
            mystdout(
                "I think you might have given me some wrong feedbacks.",
                foreground_color=ForegroundColor.YELLOW,
            )
            break
        else:
            mystdout(f"My guess is: {guess}", foreground_color=ForegroundColor.BLUE)
        feedback = input("Your feedback: ").upper()
        if feedback == "4A0B":
            break
        else:
            player.receive_feedback(feedback)
