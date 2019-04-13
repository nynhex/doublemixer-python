#!/usr/bin/python3

__version__ = '0.0.1'

import logging

import aaargh
import bitmix
import privcoin

from . import validate


cli = aaargh.App()

logging.basicConfig(level=logging.WARNING)


def mix(currency, output_address):
    """
    currency must be one of: bitcoin
    output_address is destination for double mixed coins.
    """
    validate.currency(currency)
    privcoin_output = privcoin.mix(currency=currency,
                                   output_address=output_address)
    final_mix_address = privcoin_output['address']
    bitmix_output = bitmix.mix(currency=currency,
                               output_address=final_mix_address)
    return bitmix_output['input_address']


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

    privcoin_output = privcoin.mix(currency=currency,
                                   output_address=output_address)
    final_mix_address = privcoin_output['address']
    bitcode = privcoin_output['bitcode']

    privcoin_letter = privcoin.letter_of_guarantee(bitcode)

    # Terminal output
    bitmix_output = bitmix._mix_terminal(currency=currency,
                                         output_address=final_mix_address)

    msg = 'Final mix bitcode: {}\nFinal mix guarantee:\n{}\n{}'
    output = msg.format(bitcode, privcoin_letter, bitmix_output)

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
