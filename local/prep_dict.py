#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from abc import ABCMeta, abstractmethod

reload(sys)
sys.setdefaultencoding('utf8')

__author__ = "YOURNAME"


class PrepDict(object):
    """
    An abstract preprocessor class for 'lang' part
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_extra_questions_txt(self):
        """
        This file contains additional (dec-tree) questions about stress and tones.
        """
        raise NotImplementedError

    @abstractmethod
    def make_lexicon_txt(self):
        """
        This file has pronunciation dictionary.
        formatted: word phone1 phoen2 ...
        For words with multiple pronunciations, repeat entries on separate lines.
        This file also should contains any pronunciation symbols for silences
        """
        raise NotImplementedError

    @abstractmethod
    def make_lexicon_words_txt(self):
        """
        Same as lexicon.txt, except this file only contains non-silence symbols
        """
        raise NotImplementedError

    @abstractmethod
    def make_nonsilence_phones_txt(self):
        """
        This files has all symbols representing all phones used in words.
        If a phone can have variations depending on its context,
        you can list up the variances horizontally.
        (This variation is NOT an allo-phone.)
        These variations should be handled as additional questions
        when building dicision trees.
        """
        raise NotImplementedError

    @abstractmethod
    def make_silence_phones_txt(self):
        """
        This files has all symbols representing non-word sounds.
        Silence, noise, laughter, etc.
        silence_phones.txt and nonsilence_phones.txt SHOULD be mutually exclusive.
        """
        raise NotImplementedError

    @abstractmethod
    def make_optional_silence_txt(self):
        """
        This files has symbols for optional (at the end of every word) silence.
        Usually, only silence.
        """
        raise NotImplementedError

