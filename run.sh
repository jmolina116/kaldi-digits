#! /bin/bash
# Author: Jose Molina
# intended to be run from within current directory

source ./path.sh

printf '\n\n\n===== PREPARING DICTIONARY =====\n'
mkdir -p dict
python local/prep_digits_dict.py

printf '\n\n\n===== PREPARING LANG =====\n'
utils/prepare_lang.sh --position-dependent-phones false dict "<SIL>" dict/temp data/lang

printf '\n\n\n===== COMPILING FST =====\n'
$KALDI_ROOT/tools/openfst-1.3.4/bin/fstcompile \
    --isymbols=data/lang/words.txt --osymbols=data/lang/words.txt \
    data/lang/G.txt > data/lang/G.fst

printf '\n\n\n===== TRAIN-DECODE ROUND 1 =====\n'
mkdir -p data/train1
mkdir -p data/test1
printf '\n=== PREPARING DATA ===\n'
python local/prep_tidigits_data.py raw_data/tidigits/data/adults/train train1
python local/prep_tidigits_data.py raw_data/tidigits/data/adults/test test1
utils/fix_data_dir.sh data/train1
utils/fix_data_dir.sh data/test1
printf '\n=== TRAINING ===\n'
steps/make_mfcc.sh --nj 112 data/train1 exp/make_mfcc/train1
steps/compute_cmvn_stats.sh data/train1 exp/make_mfcc/train1
steps/train_mono.sh --nj 112 --cmd utils/run.pl data/train1 data/lang exp/mono1
printf '\n=== LATTICE ===\n'
$KALDI_ROOT/src/fstbin/fstcopy 'ark:gunzip -c exp/mono1/fsts.1.gz|' ark,t:- | head -n 20
printf '\n=== TESTING ===\n'
steps/make_mfcc.sh --nj 113 data/test1 exp/make_mfcc/test1
steps/compute_cmvn_stats.sh data/test1 exp/make_mfcc/test1
printf '\n=== MAKING GRAPHS ===\n'
utils/mkgraph.sh --mono data/lang exp/mono1 exp/mono1/graph
printf '\n=== DECODING & EVALUATING ===\n'
steps/decode.sh --nj 113 exp/mono1/graph data/test1 exp/mono1/decode
steps/get_ctm.sh data/test1 exp/mono1/graph exp/mono1/decode

printf '\n\n\n===== TRAIN-DECODE ROUND 2 =====\n'
mkdir -p data/train2
mkdir -p data/test2
printf '\n=== PREPARING DATA ===\n'
python local/prep_tidigits_data.py raw_data/tidigits/data/adults/train train2
python local/prep_fsdd_data.py raw_data/fsdd_waves/recordings test2
utils/fix_data_dir.sh data/train2
utils/fix_data_dir.sh data/test2
printf '\n=== TRAINING ===\n'
steps/make_mfcc.sh --nj 112 data/train2 exp/make_mfcc/train2
steps/compute_cmvn_stats.sh data/train2 exp/make_mfcc/train2
steps/train_mono.sh --nj 112 --cmd utils/run.pl data/train2 data/lang exp/mono2
printf '\n=== LATTICE ===\n'
$KALDI_ROOT/src/fstbin/fstcopy 'ark:gunzip -c exp/mono2/fsts.1.gz|' ark,t:- | head -n 20
printf '\n=== TESTING ===\n'
steps/make_mfcc.sh --mfcc_config local/mfcc_fsdd.conf --nj 1 data/test2 exp/make_mfcc/test2
steps/compute_cmvn_stats.sh data/test2 exp/make_mfcc/test2
printf '\n=== MAKING GRAPHS ===\n'
utils/mkgraph.sh --mono data/lang exp/mono2 exp/mono2/graph
printf '\n=== DECODING & EVALUATING ===\n'
steps/decode.sh --nj 1 exp/mono2/graph data/test2 exp/mono2/decode
steps/get_ctm.sh data/test2 exp/mono2/graph exp/mono2/decode

printf '\n\n\n===== TRAIN-DECODE ROUND 3 =====\n'
mkdir -p data/train3
mkdir -p data/test3
printf '\n=== PREPARING DATA ===\n'
python local/prep_tidigits_data.py raw_data/tidigits/data/adults train3
python local/prep_tidigits_data.py raw_data/tidigits/data/children/test test3
utils/fix_data_dir.sh data/train3
utils/fix_data_dir.sh data/test3
printf '\n=== TRAINING ===\n'
steps/make_mfcc.sh --nj 225 data/train3 exp/make_mfcc/train3
steps/compute_cmvn_stats.sh data/train3 exp/make_mfcc/train3
steps/train_mono.sh --nj 225 --cmd utils/run.pl data/train3 data/lang exp/mono3
printf '\n=== LATTICE ===\n'
$KALDI_ROOT/src/fstbin/fstcopy 'ark:gunzip -c exp/mono3/fsts.1.gz|' ark,t:- | head -n 20
printf '\n=== TESTING ===\n'
steps/make_mfcc.sh --nj 50 data/test3 exp/make_mfcc/test3
steps/compute_cmvn_stats.sh data/test3 exp/make_mfcc/test3
printf '\n=== MAKING GRAPHS ===\n'
utils/mkgraph.sh --mono data/lang exp/mono3 exp/mono3/graph
printf '\n=== DECODING & EVALUATING ===\n'
steps/decode.sh --nj 50 exp/mono3/graph data/test3 exp/mono3/decode
steps/get_ctm.sh data/test3 exp/mono3/graph exp/mono3/decode
