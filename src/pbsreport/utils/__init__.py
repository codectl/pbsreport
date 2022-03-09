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
    logs = {
        'b': 0, 'k': 10, 'm': 20, 'g': 30,
        't': 40, 'p': 50, 'e': 60, 'z': 70, 'y': 80
    }
    if value < 0:
        raise ValueError("")
    factor = logs[from_unit[0]] - logs[to_unit[0]]
    return int(value * 2 ** factor)
