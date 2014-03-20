import sys

# Problem

# The decimal numeral system is composed of ten digits, which we represent as "0123456789" (the digits in a system are written from lowest to highest). Imagine you have discovered an alien numeral system composed of some number of digits, which may or may not be the same as those used in decimal. For example, if the alien numeral system were represented as "oF8", then the numbers one through ten would be (F, 8, Fo, FF, F8, 8o, 8F, 88, Foo, FoF). We would like to be able to work with numbers in arbitrary alien systems. More generally, we want to be able to convert an arbitrary number that's written in one alien system into a second alien system.

# Input

# The first line of input gives the number of cases, N. N test cases follow. Each case is a line formatted as

# alien_number source_language target_language
# Each language will be represented by a list of its digits, ordered from lowest to highest value. No digit will be repeated in any representation, all digits in the alien number will be present in the source language, and the first digit of the alien number will not be the lowest valued digit of the source language (in other words, the alien numbers have no leading zeroes). Each digit will either be a number 0-9, an uppercase or lowercase letter, or one of the following symbols !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Output

# For each test case, output one line containing "Case #x: " followed by the alien number translated from the source language to the target language.

# Limits

# 1 <= N <= 100.

# Small dataset

# 1 <= num digits in alien_number <= 4,
# 2 <= num digits in source_language <= 16,
# 2 <= num digits in target_language <= 16.

# Large dataset

# 1 <= alien_number (in decimal) <= 1000000000,
# 2 <= num digits in source_language <= 94,
# 2 <= num digits in target_language <= 94.

# Sample

# Input 			Output 
# 4
# 9 0123456789 oF8		Case #1: Foo
# Foo oF8 0123456789		Case #2: 9
# 13 0123456789abcdef 01 	Case #3: 10011
# CODE O!CDE? A?JM!.		Case #4: JAM!

def source_base10(s,hasht):
    snum=[]
    s1=''
    for c in s:
        snum+=str(hasht[c])
        #s1+=str(hasht[c])
    return snum

def base10_to_target(num,base,hasht):
    final=''
    rem=0
    while num !=0:# > base:
        num,rem=divmod(num,base)
        final+=hasht[str(rem)]
    return final[::-1]

def main():
    if (len(sys.argv) <2):
        print "Provide an input file"
        exit(0)
    fpointer=open(sys.argv[1],"r")

    lines=fpointer.readlines()

    fpointer.close()

    fpointer=open(sys.argv[1][:-2]+'out','w+')
    count=1
    for line in lines[1:]:
        input=line.split()
        
        base_source=len(input[1])
        source_numbers={}
        for i,c in enumerate(input[1]):
            source_numbers[c]=i

        target_numbers={}
        base_target=len(input[2])

        for i,c in enumerate(input[2]):
            target_numbers[str(i)]=c

        src_base10_list=source_base10(input[0],source_numbers)
        i=0;
        n=len(src_base10_list)
        srcno_in_base10=0
        while i < n:
            srcno_in_base10+=int(src_base10_list[i])*pow(base_source,n-i-1)
            i+=1
        srcno_targetbase=base10_to_target(srcno_in_base10,base_target,target_numbers)
        print srcno_targetbase

        fpointer.write('Case #'+str(count)+': '+str(srcno_targetbase)+'\n')
        count+=1
        
    fpointer.close()
    
if __name__=='__main__':
    main()
