# Copyright (C) 2012-2018 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import bitcoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '1.11.0'

class BitcoinMainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\xf9\xbe\xb4\xd9'
    DEFAULT_PORT = 8333
    RPC_PORT = 8332
    DNS_SEEDS = (('bitcoin.sipa.be', 'seed.bitcoin.sipa.be'),
                 ('bluematt.me', 'dnsseed.bluematt.me'),
                 ('dashjr.org', 'dnsseed.bitcoin.dashjr.org'),
                 ('bitcoinstats.com', 'seed.bitcoinstats.com'),
                 ('xf2.org', 'bitseed.xf2.org'),
                 ('bitcoin.jonasschnelli.ch', 'seed.bitcoin.jonasschnelli.ch'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':0,
                       'SCRIPT_ADDR':5,
                       'SECRET_KEY' :128}
    BECH32_HRP = 'bc'

class BitcoinTestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x0b\x11\x09\x07'
    DEFAULT_PORT = 18333
    RPC_PORT = 18332
    DNS_SEEDS = (('testnetbitcoin.jonasschnelli.ch', 'testnet-seed.bitcoin.jonasschnelli.ch'),
                 ('petertodd.org', 'seed.tbtc.petertodd.org'),
                 ('bluematt.me', 'testnet-seed.bluematt.me'),
                 ('bitcoin.schildbach.de', 'testnet-seed.bitcoin.schildbach.de'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'tb'

class BitcoinRegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\xbf\xb5\xda'
    DEFAULT_PORT = 18444
    RPC_PORT = 18443
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'bcrt'

class BitcoinSVMainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\xf9\xbe\xb4\xd9' # ???
    DEFAULT_PORT = 8333 # ??? 
    RPC_PORT = 8332 # ???
    DNS_SEEDS = (('bitcoin.sipa.be', 'seed.bitcoin.sipa.be'), # ???
                 ('bluematt.me', 'dnsseed.bluematt.me'),
                 ('dashjr.org', 'dnsseed.bitcoin.dashjr.org'),
                 ('bitcoinstats.com', 'seed.bitcoinstats.com'),
                 ('xf2.org', 'bitseed.xf2.org'),
                 ('bitcoin.jonasschnelli.ch', 'seed.bitcoin.jonasschnelli.ch'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':0,
                       'SCRIPT_ADDR':5,
                       'SECRET_KEY' :128}
    BECH32_HRP = 'doesnotexist'

class BitcoinSVTestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x0b\x11\x09\x07' # ???
    DEFAULT_PORT = 18333 # ???
    RPC_PORT = 18332 # ???
    DNS_SEEDS = (('testnetbitcoin.jonasschnelli.ch', 'testnet-seed.bitcoin.jonasschnelli.ch'), # ???
                 ('petertodd.org', 'seed.tbtc.petertodd.org'),
                 ('bluematt.me', 'testnet-seed.bluematt.me'),
                 ('bitcoin.schildbach.de', 'testnet-seed.bitcoin.schildbach.de'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'doesnotexist'

class DashMainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\xf9\xbe\xb4\xd9' # Incorrect
    DEFAULT_PORT = 8333 # Irrelevant
    RPC_PORT = 8332 # Irrelevant
    DNS_SEEDS = (('bitcoin.sipa.be', 'seed.bitcoin.sipa.be'), # Irrelevant
                 ('bluematt.me', 'dnsseed.bluematt.me'),
                 ('dashjr.org', 'dnsseed.bitcoin.dashjr.org'),
                 ('bitcoinstats.com', 'seed.bitcoinstats.com'),
                 ('xf2.org', 'bitseed.xf2.org'),
                 ('bitcoin.jonasschnelli.ch', 'seed.bitcoin.jonasschnelli.ch'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':76,
                       'SCRIPT_ADDR':16,
                       'SECRET_KEY' :204}
    BECH32_HRP = 'doesnotexist'

class DashTestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x0b\x11\x09\x07' # Incorrect
    DEFAULT_PORT = 18333 # Irrelevant
    RPC_PORT = 18332 # Irrelevant
    DNS_SEEDS = (('testnetbitcoin.jonasschnelli.ch', 'testnet-seed.bitcoin.jonasschnelli.ch'), # Irrelevant
                 ('petertodd.org', 'seed.tbtc.petertodd.org'),
                 ('bluematt.me', 'testnet-seed.bluematt.me'),
                 ('bitcoin.schildbach.de', 'testnet-seed.bitcoin.schildbach.de'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':140,
                       'SCRIPT_ADDR':19,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'doesnotexist'

class DogecoinMainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\xf9\xbe\xb4\xd9' # Incorrect
    DEFAULT_PORT = 8333 # Irrelevant
    RPC_PORT = 8332 # Irrelevant
    DNS_SEEDS = (('bitcoin.sipa.be', 'seed.bitcoin.sipa.be'), # Irrelevant
                 ('bluematt.me', 'dnsseed.bluematt.me'),
                 ('dashjr.org', 'dnsseed.bitcoin.dashjr.org'),
                 ('bitcoinstats.com', 'seed.bitcoinstats.com'),
                 ('xf2.org', 'bitseed.xf2.org'),
                 ('bitcoin.jonasschnelli.ch', 'seed.bitcoin.jonasschnelli.ch'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':30,
                       'SCRIPT_ADDR':22,
                       'SECRET_KEY' :158}
    BECH32_HRP = 'doesnotexist'

class DogecoinTestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x0b\x11\x09\x07' # Incorrect
    DEFAULT_PORT = 18333 # Irrelevant
    RPC_PORT = 18332 # Irrelevant
    DNS_SEEDS = (('testnetbitcoin.jonasschnelli.ch', 'testnet-seed.bitcoin.jonasschnelli.ch'), # Irrelevant
                 ('petertodd.org', 'seed.tbtc.petertodd.org'),
                 ('bluematt.me', 'testnet-seed.bluematt.me'),
                 ('bitcoin.schildbach.de', 'testnet-seed.bitcoin.schildbach.de'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':113,
                       'SCRIPT_ADDR':196,
                       'SECRET_KEY' :241}
    BECH32_HRP = 'doesnotexist'

class LitecoinMainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\xf9\xbe\xb4\xd9' # Incorrect
    DEFAULT_PORT = 8333 # Irrelevant
    RPC_PORT = 8332 # Irrelevant
    DNS_SEEDS = (('bitcoin.sipa.be', 'seed.bitcoin.sipa.be'), # Irrelevant
                 ('bluematt.me', 'dnsseed.bluematt.me'),
                 ('dashjr.org', 'dnsseed.bitcoin.dashjr.org'),
                 ('bitcoinstats.com', 'seed.bitcoinstats.com'),
                 ('xf2.org', 'bitseed.xf2.org'),
                 ('bitcoin.jonasschnelli.ch', 'seed.bitcoin.jonasschnelli.ch'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':48,
                       'SCRIPT_ADDR':50,
                       'SECRET_KEY' :176}
    BECH32_HRP = 'ltc'

class LitecoinTestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x0b\x11\x09\x07' # Incorrect
    DEFAULT_PORT = 18333 # Irrelevant
    RPC_PORT = 18332 # Irrelevant
    DNS_SEEDS = (('testnetbitcoin.jonasschnelli.ch', 'testnet-seed.bitcoin.jonasschnelli.ch'), # Irrelevant
                 ('petertodd.org', 'seed.tbtc.petertodd.org'),
                 ('bluematt.me', 'testnet-seed.bluematt.me'),
                 ('bitcoin.schildbach.de', 'testnet-seed.bitcoin.schildbach.de'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':111,
                       'SCRIPT_ADDR':58,
                       'SECRET_KEY' :239}
    BECH32_HRP = 'tltc'

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = BitcoinMainParams()
params = BitcoinMainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params

    if name == 'mainnet' or name == 'btc-mainnet':
        bitcoin.core._SelectCoreParams('mainnet')
        params = bitcoin.core.coreparams = BitcoinMainParams()
    elif name == 'testnet' or name == 'btc-testnet':
        bitcoin.core._SelectCoreParams('testnet')
        params = bitcoin.core.coreparams = BitcoinTestNetParams()
    elif name == 'regtest' or name == 'btc-regtest':
        bitcoin.core._SelectCoreParams('regtest')
        params = bitcoin.core.coreparams = BitcoinRegTestParams()
    elif name == 'bsv-mainnet':
        bitcoin.core._SelectCoreParams('mainnet')
        params = bitcoin.core.coreparams = BitcoinSVMainParams()
    elif name == 'bsv-testnet':
        bitcoin.core._SelectCoreParams('testnet')
        params = bitcoin.core.coreparams = BitcoinSVTestNetParams()
    elif name == 'dash-mainnet':
        bitcoin.core._SelectCoreParams('mainnet')
        params = bitcoin.core.coreparams = DashMainParams()
    elif name == 'dash-testnet':
        bitcoin.core._SelectCoreParams('testnet')
        params = bitcoin.core.coreparams = DashTestNetParams()
    elif name == 'doge-mainnet':
        bitcoin.core._SelectCoreParams('mainnet')
        params = bitcoin.core.coreparams = DogecoinMainParams()
    elif name == 'doge-testnet':
        bitcoin.core._SelectCoreParams('testnet')
        params = bitcoin.core.coreparams = DogecoinTestNetParams()
    elif name == 'ltc-mainnet':
        bitcoin.core._SelectCoreParams('mainnet')
        params = bitcoin.core.coreparams = LitecoinMainParams()
    elif name == 'ltc-testnet':
        bitcoin.core._SelectCoreParams('testnet')
        params = bitcoin.core.coreparams = LitecoinTestNetParams()
    else:
        raise ValueError('Unknown chain %r' % name)
