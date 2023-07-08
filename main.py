import random

from mystdout import BackgroundColor, ForegroundColor, TextStyle, mystdout
from myutils import clear_terminal


def pick_number() -> str:
    return "".join(random.sample([str(i) for i in range(10)], 4))


def wait_player_guess(hint: str) -> str:
    while True:
        player_guess = input()
        try:
            validate_user_input(player_guess)
        except ValueError:
            mystdout(
                hint,
                TextStyle.BOLD,
                background_color=BackgroundColor.YELLOW,
                simulate_typing=False,
            )
        else:
            return player_guess


def validate_user_input(input: str) -> None:
    if len(input) != 4:
        raise ValueError
    if not input.isdigit():
        raise ValueError
    for each in input:
        if input.count(each) > 1:
            raise ValueError


def assess_guess(answer: str, guess: str) -> str:
    a, b = 0, 0
    for i in range(4):
        if answer.find(guess[i]) == i:
            a += 1
        elif answer.find(guess[i]) not in (i, -1):
            b += 1
    return f"{a}A{b}B"


def main() -> None:
    from rule_based_player import RuleBasedPlayer

    player = RuleBasedPlayer()
    records = []
    # player_bingo = False
    # player_try_time = 0

    clear_terminal("hard")
    mystdout("Start", TextStyle.FAINT, simulate_typing=False)
    for _ in range(1000):
        answer = pick_number()
        try_time = 0
        # print("-------------------")
        while True:
            try_time += 1
            guess = player.make_a_guess()
            feedback = assess_guess(answer, guess)
            # print(answer, guess, feedback)
            if feedback == "4A0B":
                records.append(try_time)
                player.refresh()
                break
            else:
                player.receive_feedback(feedback)
    mystdout("Done", TextStyle.FAINT, simulate_typing=False)
    mystdout(f"Min Try Time: {min(records)}")
    mystdout(f"Max Try Time: {max(records)}")
    mystdout(f"Average Try Time: {round(sum(records)/len(records), 1)}")

    # mystdout(
    #     "Welcome! I've picked a number. Try your best to guess it!",
    #     foreground_color=ForegroundColor.BLUE,
    # )
    # while not player_bingo:
    #     player_try_time += 1
    #     hint = f"Please enter {'a' if player_try_time==1 else 'another'} 4-digit number without dupliated digits:"  # noqa: E501

    #     mystdout(hint, TextStyle.FAINT, simulate_typing=False)

    #     player_guess = wait_player_guess(hint)

    #     # Assess Player's Guess
    #     if (result := assess_guess(answer, player_guess)) == "4A0B":
    #         mystdout("Impossible! You win!", foreground_color=ForegroundColor.GREEN)
    #         player_bingo = True
    #     else:
    #         mystdout(f"Wrong! {result}", foreground_color=ForegroundColor.BLUE)
    #     mystdout(
    #         f"Time Used: {player_try_time}", TextStyle.FAINT, simulate_typing=False
    #     )
    #     if not player_bingo:
    #         try:
    #             rule_based_player.playOnceWithHuman()
    #         except Exception:
    #             mystdout(
    #                 "You lied! Get out!",
    #                 foreground_color=ForegroundColor.WHITE,
    #                 background_color=BackgroundColor.RED,
    #             )
    #             break
    #         if rule_based_player.mes == "4A0B":
    #             mystdout("Haha! You lose!", foreground_color=ForegroundColor.MAGENTA)
    #             mystdout(
    #                 f"My number is: {answer}", foreground_color=ForegroundColor.BLUE
    #             )
    #             break


if __name__ == "__main__":
    main()
