def currency(currency):
    valid_currencies = ['bitcoin']
    if currency not in valid_currencies:
        msg = 'currency must be one of: {}'.format(valid_currencies)
        raise ValueError(msg)
    return True
