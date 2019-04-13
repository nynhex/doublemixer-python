# Python 3 library and CLI to "double mix" your Bitcoin

Mixes using two mixers, so if one of the two is insecure, hacked, or a honeypot, your identity should still be safe.

The first mixer knows your output address, the second knows the first mixer's input address and sends funds accordingly.

## Installation

* `pip3 install doublemixer || pip install doublemixer`

## Usage

* `doublemixer mix --currency bitcoin --address 1a....`

# Licence

[Unlicense/Public domain](LICENSE.txt)
