#! /bin/bash
# intended to be run from within current directory

mkdir dict
echo -e "AH\nAY\nAX\nEH\nEY\nF\nIH\nIY\nK\nN\nOW\nR\nS\nT\nTH\nUW\nV\nW\nZ" > dict/nonsilence_phones.txt
echo -e "ONE W AH N\nTWO T UW\nTHREE TH R IY\nFOUR F OW R\nFIVE F AY V\nSIX S IH K S\nSEVEN S EH V AX N\nEIGHT EY T\nNINE N AY N\nZERO Z IY R OW\nOH OW" > dict/lexicon.txt
echo "SIL" > dict/silence_phones.txt
echo "SIL" > dict/optional_silence.txt
cp dict/lexicon.txt dict/lexicon_words.txt
echo "<SIL> SIL" >> dict/lexicon.txt
