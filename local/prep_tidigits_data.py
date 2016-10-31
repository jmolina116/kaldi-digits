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
        transcript = basename
        transcript = transcript.replace('a', '')
        transcript = transcript.replace('b', '')
        transcript = transcript.replace('1', 'ONE ')
        transcript = transcript.replace('2', 'TWO ')
        transcript = transcript.replace('3', 'THREE ')
        transcript = transcript.replace('4', 'FOUR ')
        transcript = transcript.replace('5', 'FIVE ')
        transcript = transcript.replace('6', 'SIX ')
        transcript = transcript.replace('7', 'SEVEN ')
        transcript = transcript.replace('8', 'EIGHT ')
        transcript = transcript.replace('9', 'NINE ')
        transcript = transcript.replace('z', 'ZERO ')
        transcript = transcript.replace('o', 'OH ')
        transcript = transcript[:-1]
        spk_id = get_spk_id(filename)
        results.append("{} {}".format(spk_id + '_' + basename, transcript))
    return '\n'.join(sorted(results))


def get_spk_id(filename):
    paths = filename.split(os.sep)
    age = 'a' if paths[-5] == 'adults' else 'c'
    sex = 'm' if paths[-3] == 'boy' or paths[-3] == 'man' else 'f'
    return age + sex + paths[-2]


def wav_scp(filenames):
    results = []
    for filename in filenames:
        basename = filename.split(os.sep)[-1].split('.')[0]
        spk_id = get_spk_id(filename)
        f = '$KALDI_ROOT/tools/sph2pipe_v2.5/sph2pipe -f wav ' + filename + ' |'
        results.append("{} {}".format(spk_id + '_' + basename, f))
    return "\n".join(results)


def utt2spk(filenames):
    results = []
    for filename in filenames:
        paths = filename.split(os.sep)
        basename = paths[-1].split('.')[0]
        spk_id = get_spk_id(filename)
        results.append("{} {}".format(spk_id + '_' + basename, spk_id))
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
