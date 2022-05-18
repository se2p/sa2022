# Generated from SimpleProgram.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,15,90,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,
        2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,
        6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,4,11,71,8,11,11,11,
        12,11,72,1,12,1,12,5,12,77,8,12,10,12,12,12,80,9,12,1,13,1,13,1,
        14,4,14,85,8,14,11,14,12,14,86,1,14,1,14,0,0,15,1,1,3,2,5,3,7,4,
        9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,1,0,
        3,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,
        13,32,32,92,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,
        1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,
        1,0,0,0,1,31,1,0,0,0,3,34,1,0,0,0,5,40,1,0,0,0,7,44,1,0,0,0,9,47,
        1,0,0,0,11,52,1,0,0,0,13,58,1,0,0,0,15,61,1,0,0,0,17,63,1,0,0,0,
        19,65,1,0,0,0,21,67,1,0,0,0,23,70,1,0,0,0,25,74,1,0,0,0,27,81,1,
        0,0,0,29,84,1,0,0,0,31,32,5,58,0,0,32,33,5,61,0,0,33,2,1,0,0,0,34,
        35,5,98,0,0,35,36,5,101,0,0,36,37,5,103,0,0,37,38,5,105,0,0,38,39,
        5,110,0,0,39,4,1,0,0,0,40,41,5,101,0,0,41,42,5,110,0,0,42,43,5,100,
        0,0,43,6,1,0,0,0,44,45,5,105,0,0,45,46,5,102,0,0,46,8,1,0,0,0,47,
        48,5,116,0,0,48,49,5,104,0,0,49,50,5,101,0,0,50,51,5,110,0,0,51,
        10,1,0,0,0,52,53,5,119,0,0,53,54,5,104,0,0,54,55,5,105,0,0,55,56,
        5,108,0,0,56,57,5,101,0,0,57,12,1,0,0,0,58,59,5,100,0,0,59,60,5,
        111,0,0,60,14,1,0,0,0,61,62,5,43,0,0,62,16,1,0,0,0,63,64,5,45,0,
        0,64,18,1,0,0,0,65,66,5,62,0,0,66,20,1,0,0,0,67,68,5,59,0,0,68,22,
        1,0,0,0,69,71,3,27,13,0,70,69,1,0,0,0,71,72,1,0,0,0,72,70,1,0,0,
        0,72,73,1,0,0,0,73,24,1,0,0,0,74,78,7,0,0,0,75,77,7,1,0,0,76,75,
        1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,26,1,0,0,0,
        80,78,1,0,0,0,81,82,2,48,57,0,82,28,1,0,0,0,83,85,7,2,0,0,84,83,
        1,0,0,0,85,86,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,
        88,89,6,14,0,0,89,30,1,0,0,0,4,0,72,78,86,1,6,0,0
    ]

class SimpleProgramLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    Number = 12
    Identifier = 13
    Digit = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'begin'", "'end'", "'if'", "'then'", "'while'", "'do'", 
            "'+'", "'-'", "'>'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "Number", "Identifier", "Digit", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "Number", "Identifier", 
                  "Digit", "WS" ]

    grammarFileName = "SimpleProgram.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


