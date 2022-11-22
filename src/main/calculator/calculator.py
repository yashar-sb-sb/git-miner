import re


def add(input_string):
    if not len(input_string):
        return 0

    if not input_string[-1].isdigit():
        raise Exception("invalid")

    numbers = tokenize(input_string)

    return sum(filter(lambda number: number < 1001, numbers))


def get_separators_and_input(input_string):
    if input_string[:2] != '//':
        return input_string, [',', '\n']

    separators, numbers = input_string[2:].split('\n')
    return numbers, [separators]


def tokenize(input_string):
    input_string, separators = get_separators_and_input(input_string)
    candidate_tokens = re.split('|'.join(map(re.escape, separators)), input_string)
    numbers = list(map(int, filter(is_number, candidate_tokens)))

    validate_tokens(candidate_tokens, input_string, numbers, separators)

    return numbers


def validate_tokens(candidate_tokens, input_string, numbers, separators):
    invalid_sep_exception, invalid_char = create_invalid_token_exception(candidate_tokens, input_string, separators)

    if invalid_char:
        candidate_tokens = re.split('|'.join(map(re.escape, separators + [invalid_char])), input_string)
        numbers = list(map(int, filter(is_number, candidate_tokens)))

    neg_exception = create_negative_number_exception(numbers)
    exception = '\n'.join(filter(bool, [neg_exception, invalid_sep_exception]))
    if exception:
        raise Exception(exception)


def create_negative_number_exception(numbers):
    negatives = list(filter(lambda number: number < 0, numbers))
    if len(negatives):
        return f"Negative number(s) not allowed: {', '.join(map(str, negatives))}"
    return None


def is_number(string):
    try:
        int(string)
        return True
    except Exception:
        return False


def create_invalid_token_exception(candidate_tokens, input_string, separators):
    invalid = next((number for number in candidate_tokens if not is_number(number)), None)
    if invalid:
        invalid_token = next(digit for digit in candidate_tokens if not digit.isdigit())
        invalid_char = next(char for char in invalid_token if not char.isdigit())
        invalid_char_position = input_string.index(invalid_char)
        return f"`{separators[0]}' expected but `{invalid_char}' found at position {invalid_char_position}.", invalid_char
    return None, None
