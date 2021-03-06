#CXX = clang 
CC=gcc
CFLAGS=-ggdb -Wall 
CXX=g++
CXXFLAGES=-ggdb -std=c++11 -Wall -lstdc++
SRCS=
OBJS=$(SRCS:.cpp=.o)
LD=
TARGET=out

PHONY=all lib cobj runc runpy clean

all: lib cobj
	$(CC) $(CFLAGS) test.o -L. -lhello -o test

lib: hello.c hello.h
	$(CC) $(CFLAGS) hello.c -fPIC -shared -o libhello.so

cobj: test.c
	$(CC) $(CFLAGS) -c test.c -o test.o

runc: all
	env LD_LIBRARY_PATH=. ./test

runpy: lib
	env LD_LIBRARY_PATH=. LIBHELLO=./libhello.so python tryso.py

clean:
	rm -rf libhello.so test test.o

