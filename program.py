"""program module"""


def main(*args):
    """main method"""
    list_of_reports = read_data("input_data.txt")
    ascending = []
    descending = []
    safe = []

    for report_index, report in enumerate(list_of_reports):
        if is_ascending(report):
            ascending.append(report)
        elif is_descending(report):
            descending.append(report)

    for report_index, report in enumerate(ascending):
        if is_low_step(report):
            safe.append(report)

    for report_index, report in enumerate(descending):
        if is_low_step(report):
            safe.append(report)

    no_of_safe = len(safe)
    print(no_of_safe)


def is_low_step(report):
    report_length = len(report)
    for level_index, level in enumerate(report):
        if level_index == report_length - 1:
            return True
        if abs(level - report[level_index + 1]) > 3:
            return False


def is_ascending(report) -> bool:
    report_length = len(report)
    for level_index, level in enumerate(report):
        if level_index == report_length - 1:
            return True
        if level > report[level_index + 1]:
            return False
        if level == report[level_index + 1]:
            return False


def is_descending(report) -> bool:
    report_length = len(report)
    for level_index, level in enumerate(report):
        if level_index == report_length - 1:
            return True
        if level < report[level_index + 1]:
            return False
        if level == report[level_index + 1]:
            return False


def read_data(filename):
    list_of_reports = []
    with open(filename, "r") as f:
        for line in f:
            stripped = line.strip()
            split_list = stripped.split(" ")
            inted_list = []
            for item in split_list:
                inted_list.append(int(item))
            list_of_reports.append(inted_list)

    return list_of_reports
