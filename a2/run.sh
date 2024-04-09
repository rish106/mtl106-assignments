#!/bin/sh

g++ -o main main.cpp && \
    ./main < "$1"
