#!/usr/bin/env bash

DAY="$1"

DAY_PY="day${DAY}.py"
DAY_INPUT="input$DAY"
DAYDIR="day$DAY"

mkdir $DAYDIR
touch $DAYDIR/$DAY_INPUT
touch $DAYDIR/testinput
cp newday.py $DAYDIR/$DAY_PY
