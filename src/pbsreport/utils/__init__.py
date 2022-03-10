import re


class bcolors:
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    GREY = "\033[90m"
    BLACK = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    DEFAULT = "\033[99m"


def color_state(state: str):
    if state == "free":
        return bcolors.GREEN
    elif any(bad_state in state for bad_state in ["offline", "down", "busy"]):
        return bcolors.RED
    else:
        return bcolors.YELLOW


def color_resource(available: int, free: int):
    if available == 0:
        return bcolors.DEFAULT
    elif free == 0:
        return bcolors.RED
    elif free == available:
        return bcolors.GREEN
    else:
        return bcolors.YELLOW


def colored_line(line: str, color: str):
    return f"{color}{line}{bcolors.ENDC}"


def convert_bytes(value: int, from_unit="b", to_unit="b"):
    factors = {
        "b": 0,
        "k": 10,
        "m": 20,
        "g": 30,
        "t": 40,
        "p": 50,
        "e": 60,
        "z": 70,
        "y": 80,
    }
    if value < 0:
        raise ValueError("value must be >= 0")
    from_unit_val = from_unit[0]
    to_unit_val = to_unit[0]
    if from_unit_val not in factors or to_unit_val not in factors:
        raise ValueError("invalid unit")
    factor = factors[from_unit_val] - factors[to_unit_val]
    return int(value * 2**factor)


def convert_raw_bytes(value: str, to_unit="b"):
    b, u = bytes_split(value)
    return convert_bytes(value=b, from_unit=u, to_unit=to_unit)


def bytes_split(value: str) -> tuple:
    b, u = re.match(r"(\d+)\s*(\w+)", value).groups()
    return int(b), u


def human_size(bytes: int):
    for unit in ["b", "Kb", "Mb", "Gb", "Tb", "Pb", "Eb", "Zb"]:
        if abs(bytes) < 1024:
            return f"{bytes:.0f}{unit}"
        bytes /= 1024
    return f"{bytes:.0f}Yb"
