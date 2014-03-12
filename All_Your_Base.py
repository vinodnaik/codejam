import sys

def find_base(msg):
    #base will be the number of distinctive elements in the string
    base_elements=list(set(msg))
    return len(base_elements)

def final_string(msg,base):
    #hash table for keeping the reference of each occurence of tha character
    hasht={}

    #hash table for referencing numbers if base is greater than 10
    refer_base={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i'}
    
    final=''
    j=0

    #iterate through each character of the input string
    for i in range(len(msg)):
        #set the first character of the o/p string to '1'
        if i==0:
            final+='1'
            hasht[msg[i]]='1'
        else:
            #case where the present elment has appeared before in the string
            if msg[i] in hasht:
                final+=hasht[msg[i]]
            else:
                #if base is greater than 10
                if j>=10:
                    final+=refer_base[j]
                #generic case, keep adding value of j while incrementing it
                else:
                    final+=str(j)
                    hasht[msg[i]]=str(j)

                    #case where first letter of the string repeats some times Ex: wwwwkw
                    if(j==0):
                        j+=2
                    else:
                        j+=1
    return final

def main():

    if len(sys.argv) != 2:
        print "Provide the input file"
        sys.exit(1)
        
    #obtain the list of input strings
    file_handle=open(sys.argv[1],'r')
    input_list= file_handle.read().strip().split('\n')
    file_handle.close()

    #pop the first entry as it denotes the no of entries in the i/p file
    input_list.pop(0)
    #Process the list elements one by one
    i=1
    file_handle=open(sys.argv[1][:-2]+'out','w+')
    
    for message in input_list:
        #determine the least possible base for the number
        base = find_base(message)

        #this fix is needed in the case string consists of one set of elements and our base function returns 1. (Ex : wwwwwww)
        if (base == 1):
            base+=1
            
        final_str=final_string(message,base)

        #convert the output string to base 10 readable
        seconds=int(final_str,base)

        #write to output file
        file_handle.write('Case #'+str(i)+':'+' '+str(seconds)+'\n')

        #print to stdout for debugging
        s='-'*5+'>'
        print message,s,'Base'+str(base),final_str,s,seconds

        #increment i for writing the case no in o/p file
        i+=1
        
    file_handle.close()

if __name__ =='__main__':
    main()
    
