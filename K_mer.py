#!/usr/bin/env python3
#-*- coding:utf-8 -*-                        
# Filename:K-mer.py                       
# Author:Qian Zhou                           
# Email:zhouqian@hust.edu.cn                   
# Date:2019/8/13                                  
# Filename:K-mer.py                          
# Description:
import sys
filename = sys.argv[2]
fo1 = open(filename,"r")
Text = "".join(fo1.read().splitlines())
fo1.close()
k = int(sys.argv[1])
def FrequencyMap(Text,k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for i in range(n - k +1):
            if Text[i:i+k] == Pattern:
                freq[Pattern] += 1
    return freq
def FrequencySeq(Text,k):
    freq = FrequencyMap(Text,k)
    m = max(freq.values())
    sub_freq = {key : value for key,value in freq.items() if value == m}
    seq = list(sub_freq.keys())
    return seq
def OutputFile(Text,k):
    outfile = open("k_mer.txt","w")
    seq = FrequencySeq(Text,k)
    for elem in seq:
        outfile.write(elem)
        outfile.write("\n")
    outfile.close()
    return outfile
OutputFile(Text,k)









