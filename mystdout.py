import random
import time
from enum import StrEnum


class TextStyle(StrEnum):
    NORMAL = "0"
    BOLD = "1"
    FAINT = "2"
    ITALIC = "3"
    UNDERLINED = "4"


class ForegroundColor(StrEnum):
    DEFAULT = "39"
    BLACK = "30"
    RED = "31"
    GREEN = "32"
    YELLOW = "33"
    BLUE = "34"
    MAGENTA = "35"
    CYAN = "36"
    WHITE = "97"


class BackgroundColor(StrEnum):
    DEFAULT = "49"
    BLACK = "40"
    RED = "41"
    GREEN = "42"
    YELLOW = "43"
    BLUE = "44"
    MAGENTA = "45"
    CYAN = "46"
    WHITE = "107"


def _simulate_typing(text: str, new_line: bool = True):
    for char in text:
        print(char, end="", flush=True)
        if char == " ":
            wait_time = 0.25
        elif char in (".", "!", "?", ":"):
            wait_time = 0.5
        else:
            wait_time = random.randrange(1, 7) * 0.02
        time.sleep(wait_time)
    if new_line:
        print()


def mystdout(
    content,
    text_style: TextStyle = TextStyle.NORMAL,
    foreground_color: ForegroundColor = ForegroundColor.DEFAULT,
    background_color: BackgroundColor = BackgroundColor.DEFAULT,
    simulate_typing: bool = True,
) -> None:
    prefix = f"\033[{text_style};{foreground_color};{background_color}m"
    suffix = "\033[0m"
    if not simulate_typing:
        print(f"{prefix}{content}{suffix}")
    else:
        print(prefix, end="")
        _simulate_typing(content, new_line=False)
        print(suffix)


if __name__ == "__main__":
    mystdout("hello world", TextStyle.ITALIC, simulate_typing=True)
