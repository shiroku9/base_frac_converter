def dec2base(number, base):
    if not isinstance(number, int) or isinstance(number, bool):
        raise ValueError('Input must be a numeric scalar.')
    if base < 2 or base > 36 or int(base) != base:
        raise ValueError('Base must be an integer between 2 and 36.')
    if number < 0:
        raise ValueError('Input must be a non-negative number.')
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number = number // base
    return result
