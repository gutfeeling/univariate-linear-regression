def convert_to_int(integer_string_with_commas):
    if len(integer_string_with_commas) > 3 and "," not in integer_string_with_commas:
        return None
    comma_separated_parts = integer_string_with_commas.split(",")
    if not all([len(part) == 3 for part in comma_separated_parts[1:]]) or len(comma_separated_parts[0]) > 3:
        return None
    integer_string_without_commas = "".join(comma_separated_parts)
    try:
        return int(integer_string_without_commas)
    except ValueError:
        return None


def row_to_list(row):
    row = row.rstrip("\n")
    separated_entries = row.split("\t")
    separated_entries = [whitespace_split_entry for entry in separated_entries
                         for whitespace_split_entry in entry.split(" ")
                         ]
    if len(separated_entries) == 2 and "" not in separated_entries:
        return separated_entries
    return None
