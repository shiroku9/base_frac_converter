from fracbase2dex import fracbase2dex
from fracdex2base import fracdex2base


def fracbase2base(fracbase, fromBase, toBase):
    if not isinstance(fracbase, str):
        raise ValueError('Input must be a string representing a number in the specified base.')
    d = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:fromBase]
    if not all(c in d + '.' for c in fracbase):
        raise ValueError('Input must contain only valid digits for the specified base.')
    if fracbase.count('.') > 1:
        raise ValueError('Input must contain at most one decimal point.')
    fracdex = fracbase2dex(fracbase, fromBase)
    return fracdex2base(fracdex, toBase)
