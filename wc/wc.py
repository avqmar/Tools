#!/Users/aviralkumar/opt/anaconda3/envs/practice/bin/python
import argparse
import os
import sys


def c(file):
    return os.stat(file).st_size
    
def l(file):
    with open(file,'r') as f:
        lines = f.readlines()
    return len(lines)

def w(file):
    word_count = 0
    with open(file,'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('\t','')
            line = line.replace('\n','')
            line = line.split(' ')
            line_filter = [i for i in line if i!='']
            word_count = word_count + len(line_filter)
        
    return word_count

def m(file):
    with open(file, 'rb') as file:
        content = file.read()
        char_count = len(content.decode('utf-8'))
    return char_count
        
def main():
    
    parser = argparse.ArgumentParser(description='Count w, ch, l etc.')
    parser.add_argument('filename',nargs='?',default=None)
    parser.add_argument('-c')
    parser.add_argument('-l')
    parser.add_argument('-w')
    parser.add_argument('-m')
    args = parser.parse_args()

    if args.filename:
               
        print(c(args.filename),l(args.filename), w(args.filename),args.filename)
    
    if args.c:
        
        print(c(args.c),args.c)

    if args.l:
        
        print(l(args.l),args.l)

    if args.w:
        
        print(w(args.w),args.w)

    if args.m:
        char_count = m(args.m)
        print(char_count,args.m)
    
main()