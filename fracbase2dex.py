def fracbase2dex(fracbase, base):
    if not isinstance(fracbase, str):
        raise ValueError('Input must be a string representing a number in the specified base.')
    if base < 2 or base > 36 or int(base) != base:
        raise ValueError('Base must be an integer between 2 and 36.')
    d = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:base]
    if not all(c in d + '.' for c in fracbase):
        raise ValueError('Input must contain only valid digits for the specified base.')
    if fracbase.count('.') > 1:
        raise ValueError('Input must contain at most one decimal point.')
    dotPot = fracbase.find('.')
    if dotPot == -1:
        integerPart = fracbase
        fractionalPart = ''
    else:
        integerPart = fracbase[:dotPot]
        fractionalPart = fracbase[dotPot + 1:]
    if integerPart == '':
        integerPart = '0'
    if fractionalPart == '':
        fractionalPart = '0'
    integerDecimal = int(integerPart, base)
    if fractionalPart != '':
        fractionalDecimal = int(fractionalPart, base) / base ** len(fractionalPart)
        fracdex = integerDecimal + fractionalDecimal
    else:
        fracdex = integerDecimal
    return fracdex
