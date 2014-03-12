import sys


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
