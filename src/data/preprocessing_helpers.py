def convert_to_int(number_with_commas):
    """
    Bug: The int conversion is missing
    """
    return int(number_with_commas.replace(",", ""))


def row_to_list(row):
    row = row.rstrip()
    for separator in ["\t", "    "]:
        separated_entries = row.split(separator)
        if len(separated_entries) == 2 and "" not in separated_entries:
            return True
    return None
