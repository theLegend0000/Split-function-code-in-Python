def split(st,sep):
    lst=[]      #initializing a list
    word=''   #initializing an empty word

    for i in st:    # running a loop in the string 'st'

        if i != sep:    #checking if 'i' is not equal to the separator 'sep'
            word+=i  #if the above condition is True then i will be added to the 'word' string
        else:
            lst.append(word)    # if the above condition is false this will append the 'word' into the list 'lst'
            word=''                 #Emptying the 'word' for new 'word'

    lst.append(word)            # Since the last word won't be appended to the list therefore appending it in the end
    return lst                        # returning the list 'lst'

name = 'Man is Impatient'
separator = ' '

l = split(name,separator)
print(l)
