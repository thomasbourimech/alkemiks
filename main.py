# encoding: utf-8
# The goal of the exercise is to write the function is_valid_barcode which:
#   - returns True if the given parameter is:
#       - a string
#       - which is a valid GTIN, GSIN or SSCC (see https://www.gs1.org/services/how-calculate-check-digit-manually)
#   - returns False in EVERY other case
# This function should never raise an exception
#
# Precisions on the barcode format:
#   - GTINs are made of 8, 12, 13 or 14 digits, GSIN are 17 characters and SSCC are 18 characters long.
#   - the last one is a check digit, i.e. it can be calculated from the others
#   - if the calculated check digit differs from the actual check digit, then the string is considered as an invalid GTIN

def valid_string(value):

    if not isinstance(value, str):
        return False

    if len(value) not in [8, 12, 13, 14, 17, 18]:
        return False

    if not value.isdigit():
        return False

    return True

def populate_digit_multiply(value):

    token_max_size = 18
    digit_multiply = []
    value_size = len(value)
    offset = token_max_size - value_size

    while offset < token_max_size:
        if offset % 2 == 0:
            digit_multiply.append(3)
        else:
            digit_multiply.append(1)
        offset += 1

    return digit_multiply


def compute_sum(digit_result):

    sum = 0
    for digit in digit_result:
        sum += digit

    return sum

def compute_sup_diz(sum):

    while (sum % 10) != 0:
        sum += 1

    return sum


def is_valid_barcode(value):

    if not valid_string(value):
        return False

    digit_multiply = populate_digit_multiply(value)
    digit_result = []
    i=0
    for digit in value[:-1]:
        digit_result.append(digit_multiply[i] * int(digit))
        i += 1
    sum = compute_sum(digit_result)
    sum_target = compute_sup_diz(sum)
    print("Sum: %s, checkum_target: %s, token en test : %s, checkum :  %s " % (sum, sum_target, digit_result,
                                                                               sum_target - sum))

    result = sum_target - sum
    return result == int(value[-1])


test_cases = [
    ('6291041500213', True),  # <--- example of the spec
    ('6291041500211', False),  # <-- example with wrong check digit
    ('3124482010481', True),
    ('3124482010482', False),
    ('3124482010483', False),
    ('3124482010484', False),
    ('3124482010485', False),
    ('3124482010486', False),
    ('3124482010487', False),
    ('3124482010488', False),
    ('3124482010489', False),
    ('3124482010480', False),
    ('0167053164698', True),
    ('13033490913240', True),
    ('13033490913240.00', False),
    ('123456017450', True),
    ('12345670', True),
    ('000000000000000000000', False),
    ('00000000000000000000', False),
    ('0000000000000000000', False),
    ('000000000000000000', True),
    ('00000000000000000', True),
    ('0000000000000000', False),
    ('000000000000000', False),
    ('00000000000000', True),
    ('0000000000000', True),
    ('000000000000', True),
    ('00000000000', False),
    ('0000000000', False),
    ('000000000', False),
    ('00000000', True),
    ('0000000', False),
    ('000000', False),
    ('00000', False),
    ('0000', False),
    ('000', False),
    ('00', False),
    ('0', False),
    ('zerozerozerozero', False),
    ("I am not a GTIN!4", False),
    ('0000OOOO000000000', False),
    ('ßþéçíæL ĉĥâ®åCẗëR§ ΅œ’', False),
    ([0, 0, 0, 0, 0, 0, 0, 0], False),
    (3124482010481, False),
]

for test, expected in test_cases:
    try:
        result = is_valid_barcode(test)
    except Exception as e:
        print("Failed: %s -> %s" % (test, e))
        raise
    if result != expected:
        print("Failed: %s -> expected %s got %s" % (test, expected, result))
        break
else:
    print("Success")