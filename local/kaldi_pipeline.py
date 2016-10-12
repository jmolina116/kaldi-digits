#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import subprocess
import sys
from abc import ABCMeta, abstractmethod
from os.path import join as pjoin

reload(sys)
sys.setdefaultencoding('utf8')

__author__ = "YOURNAME"


class KaldiPipeline(object):
    """
    This is an abstract class for a Kaldi training-deciding pipeline.
    It also has some useful doctrings and helper methods. 
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        # assumes all the scripts are in a dir under the project root e.g. local
        self.ROOT_PATH = os.sep.join(os.path.realpath(__file__).split(os.sep)[:-2])
        self.paths = {'root': self.ROOT_PATH}

    def read_path_defs(self, json_path):
        # read paths
        return {k: self.expand_path(v)
                for k, v in json.load(open(self.expand_path(json_path))).iteritems()}

    def expand_path(self, final_dest):
        return pjoin(self.ROOT_PATH, final_dest)

    @abstractmethod
    def run_all(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_train_data(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_test_data(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_dict(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_lm(self):
        raise NotImplementedError

    @staticmethod
    def run_kaldi_script(cmd_path, *req_args, **options):
        cmd = [cmd_path]
        for k, v in options.iteritems():
            cmd.append('--' + k.replace('_', '-'))
            if v is not None:
                cmd.append(v)
        cmd.extend(req_args)
        print cmd
        subprocess.check_call(cmd)

    def prepare_lang(self, dict_src_path, oov_symbol, tmp_path, lang_path,
                     position_dependent_phones=True):
        """
        An example implementation of wrapping a Kaldi script.
        Using this docstring for taking notes on a particular cmd arg structure
        might be a good idea for later use or code documentation.
        """
        self.run_kaldi_script('utils/prepare_lang.sh',
                              [dict_src_path, oov_symbol, tmp_path, lang_path],
                              {"position_dependent_phones":
                                   str(position_dependent_phones).lower()})

    def extract_mfcc(self, *paths, **options):
        """
        Another example to wrap a Kaldi script
        The documentation is is highly recommended in this implementation,
        since later users can't help looking for the original script to figure out.

        Below is copied from the original script
        =====
        echo "Usage: $0 [options] <data-dir> [<log-dir> [<mfcc-dir>] ]";
        echo "e.g.: $0 data/train exp/make_mfcc/train mfcc"
        echo "Note: <log-dir> defaults to <data-dir>/log, and <mfccdir> defaults to <data-dir>/data"
        echo "Options: "
        echo "  --mfcc-config <config-file>                      # config passed to compute-mfcc-feats "
        echo "  --nj <nj>                                        # number of parallel jobs"
        echo "  --cmd (utils/run.pl|utils/queue.pl <queue opts>) # how to run jobs."
        echo "  --write-utt2num-frames <true|false>     # If true, write utt2num_frames file."

        """
        self.run_kaldi_script("steps/make_mfcc.sh", paths, options)

    def compute_cmvn_stats(self, data_path, log_path, feat_path):
        """
        A bad example of not having documentation.
        But at least this keep the original arg structures.
        And the original is simple enough not to have any options
        (which is not necessarily true if you look into the original).
        """
        self.run_kaldi_script("steps/compute_cmvn_stats.sh",
                              [data_path, log_path, feat_path])


