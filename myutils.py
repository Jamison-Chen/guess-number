import os
from typing import Literal


def clear_terminal(mode: Literal["soft", "hard"] = "soft") -> None:
    if mode == "hard":
        print("\033c")
    # "nt" stands for Windows, "posix" stands for Mac and Linux
    os.system("cls") if os.name == "nt" else os.system("clear")
