# Python 3 library and CLI to "double mix" your Bitcoin

Mixes using two mixers, so if one of the two is insecure, hacked, or a honeypot, your identity should still be safe.

The first mixer knows your output address, the second knows the first mixer's input address and sends funds accordingly.

## Installation

* `pip3 install doublemixer || pip install doublemixer`

## Usage

* `doublemixer mix --currency bitcoin --address 1a....`

## Mixers

Randomly selects two of the following mixers:

* [Privcoin](https://github.com/teran-mckinney/privcoin-python)
* [Bitmix](https://github.com/teran-mckinney/bitmix-python)
* [FoxMixer](https://github.com/teran-mckinney/foxmixer-python)

## Screenshot

![doublemixer screenshot](https://pic8.co/sh/opLCYG.png)

# Licence

[Unlicense/Public domain](LICENSE.txt)
