#!/bin/sh

rm -rf ./2021CS10581.zip ./2021CS10581
mkdir -p 2021CS10581
cp ./main.cpp ./run.sh ./2021CS10581
zip -r 2021CS10581 2021CS10581/
rm -rf 2021CS10581/
