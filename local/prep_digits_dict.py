#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from prep_dict import PrepDict

reload(sys)
sys.setdefaultencoding('utf8')

__author__ = "Jose Molina"


class PrepDigitsDict(object):

    @staticmethod
    def make_extra_questions_txt():
        """
        This file contains additional (dec-tree) questions about stress and tones.
        """
        s = ""
        with open('dict/extra_questions.txt', 'w') as f:
            f.write(s)

    @staticmethod
    def make_lexicon_txt():
        """
        This file has pronunciation dictionary.
        formatted: word phone1 phone2 ...
        For words with multiple pronunciations, repeat entries on separate lines.
        This file also should contains any pronunciation symbols for silences
        """
        s = "ONE W AH N\nTWO T UW\nTHREE TH R IY\nFOUR F OW R\nFIVE F AY V\n" +\
            "SIX S IH K S\nSEVEN S EH V AX N\nEIGHT EY T\nNINE N AY N\n" + \
            "ZERO Z IY R OW\nOH OW\n<SIL> SIL\n"
        with open('dict/lexicon.txt', 'w') as f:
            f.write(s)

    @staticmethod
    def make_lexicon_words_txt():
        """
        Same as lexicon.txt, except this file only contains non-silence symbols
        """
        s = "ONE W AH N\nTWO T UW\nTHREE TH R IY\nFOUR F OW R\nFIVE F AY V\n" +\
            "SIX S IH K S\nSEVEN S EH V AX N\nEIGHT EY T\nNINE N AY N\n" + \
            "ZERO Z IY R OW\nOH OW\n"
        with open('dict/lexicon_words.txt', 'w') as f:
            f.write(s)

    @staticmethod
    def make_nonsilence_phones_txt():
        """
        This file® has all symbols representing all phones used in words.
        If a phone can have variations depending on its context,
        you can list up the variances horizontally.
        (This variation is NOT an allophone.)
        These variations should be handled as additional questions
        when building decision trees.
        """
        s = "AH\nAY\nAX\nEH\nEY\nF\nIH\nIY\nK\nN\nOW\nR\nS\nT\nTH\nUW\nV\nW\nZ\n"
        with open('dict/nonsilence_phones.txt', 'w') as f:
            f.write(s)

    @staticmethod
    def make_silence_phones_txt():
        """
        This files has all symbols representing non-word sounds.
        Silence, noise, laughter, etc.
        silence_phones.txt and nonsilence_phones.txt SHOULD be mutually exclusive.
        """
        s = "SIL\n"
        with open('dict/silence_phones.txt', 'w') as f:
            f.write(s)

    @staticmethod
    def make_optional_silence_txt():
        """
        This files has symbols for optional (at the end of every word) silence.
        Usually, only silence.
        """
        s = "SIL\n"
        with open('dict/optional_silence.txt', 'w') as f:
            f.write(s)

PrepDict.register(PrepDigitsDict)

PrepDigitsDict.make_extra_questions_txt()
PrepDigitsDict.make_lexicon_txt()
PrepDigitsDict.make_lexicon_words_txt()
PrepDigitsDict.make_nonsilence_phones_txt()
PrepDigitsDict.make_silence_phones_txt()
PrepDigitsDict.make_optional_silence_txt()
