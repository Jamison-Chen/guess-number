from typing import Iterable, TypeVar

T = TypeVar("T")


def gen_lottery_results(choices: list[T], length: int) -> set[tuple[T]]:
    results = set()

    def helper(current: tuple = tuple(), remaining_choices: list[T] = choices) -> None:
        if len(current) >= length:
            results.add(current)
            return
        for idx, each in enumerate(remaining_choices):
            helper(
                current + (each,),
                remaining_choices[:idx] + remaining_choices[idx + 1 :],
            )

    helper()
    return results


def gen_password_results(choices: Iterable[T], length: int) -> set[tuple[T]]:
    results = set()

    def helper(current: tuple = tuple()) -> None:
        if len(current) >= length:
            results.add(current)
            return
        for each in choices:
            helper(current + (each,))

    helper()
    return results


if __name__ == "__main__":
    import time

    from mystdout import ForegroundColor, mystdout

    start = time.time()
    n = 10
    for i in range(5, 11):
        result = gen_lottery_results([i for i in range(n)], i)
        # assert len(result) == n**i, "Wrong number of result!"
        mystdout(
            f"({n}, {i}) {round(time.time() - start, 4)} sec",
            foreground_color=ForegroundColor.BLUE,
            simulate_typing=False,
        )
