import unittest
import sys
import base64
import hashlib
import datetime
from Crypto.Cipher import AES
import os

# Author Christian Seely

# Usage: python utests.py password.
# Note: This script is meant for internal testing and you will be able to run it

# Import all the problem solutions so they can be called.
importCommands = list(map(lambda m : 'from {0} import *'.format(m), [m[:-3] for m in os.listdir(os.path.dirname(os.path.abspath(__file__))) if m.startswith('Problem')]))
list(map(exec, importCommands))


class PythonPeulerAnswersTest(unittest.TestCase):

    oEncryptedAns = {
        'problemOne' : b'WEAH7jOgTrV4o+0hQJxxXUXu7OswKS84AAs0qwnkm7P+yJz+/fcXkdhhALLa4wGP',
        'problemTwo' : b'0rAp7RtfQ23ZZNIPLnFe2iVny+KbLjBSWHWcETOr6KFmrSmcPBsyfkvIEMMoBJAY',
        'problemThree' : b'efGG+/lBZFwe7H8miIiiFcep9uKSCM0Rf/Ii61qJdmlmE601r/17j56JgrrLDPyo',
        'problemFour' : b'tPX0pDGGYN/O9rI4/QQiWljwLImDRPZt3jd25KtvU377ToMnHwYrmgC+016TSlkS',
        'problemFive' : b'bz/ugRmEWTf0/6LQGvsMNtDi/Yf086j3JFBzSunEqBAWpM5q19kecDI05iOmhNmu',
        'problemSix' : b'GspLuQY9GHhZWQYx299Azoj4dCwvYSvPbPlWF27cZMJ6miGx9TMoXESTujvlaMKn',
        'problemSeven' : b'H7ruRioC4la64oFgu1nlP/9NQKxTUbA8sjDJ6tC4r5aaHQoFFz6HkMoyvhXAN/B7',
        'problemEight' : b'I52sbA/32iULVxOo2azEpj3UBKihphlWxBikgNPD1twvGfAlgWl+nOXtRUN77HjY',
        'problemNine' : b'HHLQAWElDEK5NEJSeUXdm1MzYyoMwYU5NnRU0oaV7qx0h05xEJKMzEzQ3gnItgxS',
        'problemTen' : b'SQhUIi27SSzJS/BfZcHeQw81rZKcTfvpNGK9Sq9bY3/DmXoZebPoprN1I27zgfKi',
        'problemEleven' : b'jUrg0SmnsQVPciby0Bl4RJ2CV0kF/01qlfB9bZAAovPC2zVTRsXxbE7YHRhuc0LX',
        'problemTwelve' : b'0kdNTC8+QG4DD7SoEWLT1sCbCFXB5yLQ0lLu/8lTUBB2nurynxvzU5NNfMboyuTy',
        'problemThirteen' : b'lJvLYfX0WloQxchzGQsoDere9FKJijiRZi3VMS1+S+ZYE2siNnxhFXjiqkraUY0e',
        'problemFourteen' : b'it/cuUwhqwBLtyczDJiokNX9jp89gfFFUZm9X9jwIwFwJO45knkX0TGvEm5vcCUn',
        'problemFifteen' : b'3cpW+XUwqnVB2SmNtAUwGu+4ttUbONj0pTe9HQfgm+TDjKbtIeXValIlKzHP3idU',
        'problemSixteen' : b'VWUqWgnjE04ppTGTam0j2n4kbAJ8UCg5o4bO2rVi363lTUdOUhFbbqB11LE99rTc',
        'problemSeventeen' : b'/heSLLaQHHsdbdbcEfAixHusxg0ZCQA1cnxiOWsBDWku6ICP2CArOJO3uRKBd095',
        'problemNineteen' : b'6sgsTpfowIE5WE06QsZGAHNXK14Iy4Uvb7Hcouu8hO8Eybd1ebaq41e9qZ1Oy3FP',
        'problemTwenty' : b'nYQyJeDfy3sJDDhcGVAUE6nTt30XERCH9iM6PrUDrSJscy3OOTw8GgS8gjsMHVsB',
        'problemTwentyOne' : b'GwXYi6DCNmAAcMexAvy6tcuxIQ9UiWbjIXDnsT6KDwhpwhcbL1Ny1YfeAvDW8N0r',
        'problemTwentyTwo' : b'wmfaAQRC5/O5FARqal2TOoQYScX1VROvuU/73SHB9o9HoZjsURkB3/tBXLo3sERe',
        'problemTwentyFour' : b'8OfqY4RPBrA6hFBrf50G939KKqX++pYYF9tdhoRdQwNePRaZHX7jUynoUNNOxoC8',
        'problemTwentyFive' : b'LdyrQdbBCS8Jloumt7vzp/jXHU1/bbnIOAr/y7jHstrOOoE9b3IMfrNANQ8tzU4P',
        'problemThirty' : b'vdic1NUhlBX+vxwxFDwWQ0Wvovc8MrzmQD511/chwAuQI3IjVDWKN4gWXBeq20dW',
        'problemThirtyFour' : b's07hN0dE67aAQNeCxKyQSC5jdMlZumOEq7n5WLWh4fDGRdWISJlPobRw3eAYEY1M',
        'problemFortyEight' : b'm2s+Hm4QzcTVOJa4suZDMAqd/I/P8EuHF/KYL65kSH5/z36ob63qChC3YeLyvQQj',
    }
    oAns = {}
    PASSWORD = ''

    def decrypt(self, bText, bKey):
        oUp = lambda x : x[:-ord(x[len(x)-1:])]
        sEText = base64.b64decode(bText)
        oCipher = AES.new(bKey, AES.MODE_CBC, sEText[:AES.block_size])
        return oUp(oCipher.decrypt(sEText[AES.block_size:])).decode('utf-8')

    @classmethod
    def setUpClass(cls):
        # Sanity check.
        sCheck = b'ZR+Z4qfaNKk81ZLtpZGibFRsqawy4MVDkEFnWFXnVQNL28iJDoZFDtc3bT6twacP'
        bKey = hashlib.sha256(cls.PASSWORD.encode()).digest()
        assert('check' == cls.decrypt(cls,sCheck,bKey))
        cls.oAns = {k: cls.decrypt(cls,v, bKey).replace("'",'') for k, v in cls.oEncryptedAns.items()}


    def analyzeTest(self, sMethodName, fExpected):
        oTs = datetime.datetime.now()
        fResult = float(globals()[sMethodName]())
        oTe = datetime.datetime.now()
        print("{0} {1}. Time: {2} ms".format(sMethodName, 'Passed' if fResult == fExpected else 'Failed', int((oTe - oTs).total_seconds() * 1000)))
        assert(fResult == fExpected)

    def testAll(self):
        for (sMySolutionMethod, sExpected) in self.oAns.items():
            self.analyzeTest(sMySolutionMethod, float(sExpected))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        PythonPeulerAnswersTest.PASSWORD = str(sys.argv.pop())
    else:
        raise RuntimeError("A password must be provided to run these unit tests.")
    unittest.main()