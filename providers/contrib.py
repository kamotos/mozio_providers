from moneyed import CURRENCIES as CURRENCIES_DICT

CURRENCIES = [(cur.code, cur.name) for cur in CURRENCIES_DICT.values()]