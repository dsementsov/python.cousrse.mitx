



test_tuple = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples (t) :
    '''
    Returns tuple with every other element in a tuple
    Parameters:
    arg1 (tuple)
    Returns:
    a tuple with every other element
    ''' 
    odd_tuple = ()
    for i in range(len(t)):
        if i%2 == 0:
            odd_tuple += (t[i],) 
    return (odd_tuple)

output = oddTuples(test_tuple)

print (output)




def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    sum = 0
    for key in aDict.keys():
        for element in aDict[key]:
            sum += element
    return sum

