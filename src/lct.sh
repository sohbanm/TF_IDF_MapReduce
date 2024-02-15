#!/bin/bash

WCDIR=/home/letter
STREAMINGJAR=share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar

printf "TF MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                        \
    -files   $WCDIR/TF_Map.py,$WCDIR/TF_Reduce.py \
    -mapper  $WCDIR/TF_Map.py                      \
    -reducer $WCDIR/TF_Reduce.py                   \
    -input   Gutenberg/'*'                          \
    -output  TF_out

printf "\nIDF MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                            \
    -files   $WCDIR/IDF_Map.py,$WCDIR/IDF_Reduce.py \
    -mapper  $WCDIR/IDF_Map.py                        \
    -reducer $WCDIR/IDF_Reduce.py                     \
    -input   TF_out/'*'                                   \
    -output  IDF_out

printf "\nTF-IDF MAP-REDUCE\n\n"
bin/hadoop jar $STREAMINGJAR                            \
    -files   $WCDIR/TF_IDF_Map.py,$WCDIR/TF_IDF_Reduce.py \
    -mapper  $WCDIR/TF_IDF_Map.py                        \
    -reducer $WCDIR/TF_IDF_Reduce.py                     \
    -input   TF_out/'*',IDF_out/'*'                                   \
    -output  output
