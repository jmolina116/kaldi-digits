#! /usr/bin/env python

import os
import os.path
import sys

__author__ = "Jose Molina"

path = sys.argv[1]
output = sys.argv[2]

files = [os.path.join(root, f) for root, dirs, files in os.walk(path)
         for f in files if f.endswith('.wav')]


def text(filenames):
    results = []
    for filename in filenames:
        basename = filename.split(os.sep)[-1].split('.')[0]
        transcript = basename.split('_')[0]
        transcript = transcript.replace('1', 'ONE ')
        transcript = transcript.replace('2', 'TWO ')
        transcript = transcript.replace('3', 'THREE ')
        transcript = transcript.replace('4', 'FOUR ')
        transcript = transcript.replace('5', 'FIVE ')
        transcript = transcript.replace('6', 'SIX ')
        transcript = transcript.replace('7', 'SEVEN ')
        transcript = transcript.replace('8', 'EIGHT ')
        transcript = transcript.replace('9', 'NINE ')
        transcript = transcript.replace('0', 'ZERO ')
        transcript = transcript[:-1]
        results.append("{} {}".format('amja_' + basename, transcript))
    return '\n'.join(sorted(results))


def wav_scp(filenames):
    results = []
    for filename in filenames:
        basename = filename.split(os.sep)[-1].split('.')[0]
        results.append("{} {}".format('amja_' + basename, filename))
    return "\n".join(results)


def utt2spk(filenames):
    results = []
    for filename in filenames:
        basename = filename.split(os.sep)[-1].split('.')[0]
        results.append("{} {}".format('amja_' + basename, 'amja'))
    return "\n".join(results)


def spk2utt():
    os.system('utils/utt2spk_to_spk2utt.pl ' +
              'data/' + output + '/utt2spk > ' +
              'data/' + output + '/spk2utt')


with open('data/' + output + '/text', 'w') as f:
    f.write(text(files))

with open('data/' + output + '/wav.scp', 'w') as f:
    f.write(wav_scp(files))

with open('data/' + output + '/utt2spk', 'w') as f:
    f.write(utt2spk(files))

spk2utt()
