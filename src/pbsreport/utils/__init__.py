import string


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def colored_state(state):
    if state == "free":
        color = bcolors.OKGREEN
    elif state == "busy":
        color = bcolors.FAIL
    else:
        color = bcolors.WARNING
    return f"{color}{state}{bcolors.ENDC}"


def convert_bytes(value: int, from_unit="b", to_unit="b"):
    factors = {
        'b': 0, 'k': 10, 'm': 20, 'g': 30,
        't': 40, 'p': 50, 'e': 60, 'z': 70, 'y': 80
    }
    if value < 0:
        raise ValueError("value must be >= 0")
    from_unit_val = from_unit[0]
    to_unit_val = to_unit[0]
    if from_unit_val not in factors or to_unit_val not in factors:
        raise ValueError("invalid unit")
    factor = factors[from_unit_val] - factors[to_unit[to_unit_val]]
    return int(value * 2 ** factor)


def bytes_as_int(value: str):
    return int(value.rstrip(string.ascii_lowercase))
