def fracbin2dex(fracbin):
    if not isinstance(fracbin, str):
        raise ValueError('Input must be a string representing a binary number.')
    if not all(c in '01.' for c in fracbin):
        raise ValueError('Input must contain only binary digits (0 and 1) and at most one decimal point.')
    if fracbin.count('.') > 1:
        raise ValueError('Input must contain at most one decimal point.')
    dotPot = fracbin.find('.')
    if dotPot == -1:
        integerPart = fracbin
        fractionalPart = ''
    else:
        integerPart = fracbin[:dotPot]
        fractionalPart = fracbin[dotPot + 1:]
    if integerPart == '':
        integerPart = '0'
    if fractionalPart == '':
        fractionalPart = '0'
    integerDecimal = int(integerPart, 2)
    if fractionalPart != '':
        fractionalDecimal = int(fractionalPart, 2) / 2 ** len(fractionalPart)
        fracdex = integerDecimal + fractionalDecimal
    else:
        fracdex = integerDecimal
    return fracdex
