#!/usr/bin/python3

__version__ = '0.0.2'

import logging
import random

import aaargh
import bitmix
import foxmixer
import privcoin
import pyqrcode

from . import validate


cli = aaargh.App()

logging.basicConfig(level=logging.WARNING)


def random_mixers(count=2):
    """
    Returns a list of mixers with the same mixing API.

    Order will be random as well.
    """
    return random.sample([bitmix, privcoin, foxmixer], count)


def mix(currency, output_address):
    """
    currency must be one of: bitcoin
    output_address is destination for double mixed coins.
    """
    validate.currency(currency)
    mixers = random_mixers()
    mix_1 = mixers[0].mix(currency=currency,
                          output_address=output_address)
    final_mix_address = mix_1['address']
    mix_2 = mixers[1].mix(currency=currency,
                          output_address=final_mix_address)
    return mix_2['address']


@cli.cmd(name='mix')
@cli.cmd_arg('--currency', type=str, required=True)
@cli.cmd_arg('--output_address', type=str, required=True)
def _mix_terminal(currency, output_address):
    """
    currency must be one of: bitcoin
    output_address is destination for double mixed coins.

    Unfortunately, not an easy way to share code with mix().
    """
    validate.currency(currency)

    mixers = random_mixers()
    mix_1 = mixers[0].mix(currency=currency,
                          output_address=output_address)
    final_mix_address = mix_1['address']
    mix_2 = mixers[1].mix(currency=currency,
                          output_address=final_mix_address)

    mix_1_letter = mixers[0].letter_of_guarantee(mix_1['id'])
    mix_2_letter = mixers[1].letter_of_guarantee(mix_2['id'])
    send_to_address = mix_2['address']

    msg = 'Letter of guarantee for first mix: \n\n{}\n\n'\
          'Letter of guarantee for final mix: \n\n{}\n\n'\
          '{}\n'\
          '{}\n'
    uri = '{}:{}'.format(currency, send_to_address)
    qr = pyqrcode.create(uri).terminal(module_color='black',
                                       background='white',
                                       quiet_zone=1)
    output = msg.format(mix_2_letter, mix_1_letter, qr, uri)

    return output


def main():
    output = cli.run()
    if output is True:
        exit(0)
    elif output is False:
        exit(1)
    else:
        print(output)
        exit(0)


if __name__ == '__main__':
    main
