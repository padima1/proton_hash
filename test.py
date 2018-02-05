import proton_hash
from binascii import unhexlify, hexlify

import unittest

# Proton block #1
# moo@b1:~/.proton$ protond getblockhash 1
# 00000c8a1ff01bae3f3875c81cb14115429af5744643b34b4ad1cbb7d2d59ca2
# moo@b1:~/.proton$ protond getblock 00000c8a1ff01bae3f3875c81cb14115429af5744643b34b4ad1cbb7d2d59ca2
#{
#  "hash": "00000c8a1ff01bae3f3875c81cb14115429af5744643b34b4ad1cbb7d2d59ca2",
#  "confirmations": 14729,
#  "size": 179,
#  "height": 1,
#  "version": 536870912,
#  "merkleroot": "a0d06cd65fd7feef3b4223cc926ec2b8320a0ddddf8779c6571ce169826dd58f",
#  "tx": [
#    "a0d06cd65fd7feef3b4223cc926ec2b8320a0ddddf8779c6571ce169826dd58f"
# ],
# "time": 1510848001,
#  "mediantime": 1510848001,
#  "nonce": 320604,
#  "bits": "1e0ffff0",
#  "difficulty": 0.000244140625,
#  "chainwork": "0000000000000000000000000000000000000000000000000000000000200020",
#  "previousblockhash": "0000033b01055cf8df90b01a14734cae92f7039b9b0e48887b4e33a469d7bc07",
#  "nextblockhash": "000006413fc948dc46cd4da718b0bf59d2abfa81c06703db56e7642102581e46"
#}


header_hex = ("02000000" +
    "b67a40f3cd5804437a108f105533739c37e6229bc1adcab385140b59fd0f0000" +
    "a71c1aade44bf8425bec0deb611c20b16da3442818ef20489ca1e2512be43eef"
    "814cdb52" +
    "f0ff0f1e" +
    "dbf70100")

best_hash = '434341c0ecf9a2b4eec2644cfadf4d0a07830358aed12d0ed654121dd9070000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_proton_hash(self):
        self.pow_hash = hexlify(proton_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()
