import warnings

from dec2base import dec2base


def fracdex2base(fracdex, base):
    if not isinstance(fracdex, (int, float)) or isinstance(fracdex, bool):
        raise ValueError('Input must be a numeric scalar.')
    if base < 2 or base > 36 or int(base) != base:
        raise ValueError('Base must be an integer between 2 and 36.')
    if fracdex < 0:
        raise ValueError('Input must be a non-negative number.')
    integerPart = int(fracdex)
    fractionalPart = fracdex - integerPart
    integerBase = dec2base(integerPart, base)
    if fractionalPart > 0:
        fractionalBase = ''
        while fractionalPart > 0 and len(fractionalBase) < 10:  # Limit to 10 digits for precision
            fractionalPart = fractionalPart * base
            digit = int(fractionalPart)
            fractionalBase = fractionalBase + dec2base(digit, base)
            fractionalPart = fractionalPart - digit
        if fractionalPart > 0:
            warnings.warn('Fractional part truncated to 10 digits for precision.')
        fracbase = integerBase + '.' + fractionalBase
    else:
        fracbase = integerBase
    return fracbase
