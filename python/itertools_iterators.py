# https://www.interviewbit.com/problems/itertools-terminating-iterators/
import itertools as it
import operator as op
def main():
    arr1 = [2, 1, 3, 4, 1]
    arr2 = [1, 2, 4]
    arr3 = [10, 3, 4, 3, 5, 6, 32, 11]
    
    # make a new arr4 which include all the elements in order first of arr1 then arr2 and then arr3
    # Write your code here
    arr4 = list(it.chain(arr1,arr2,arr3))
    
    print(arr4)
    
    # using accumulate(), store the successive muliplication of elements of arr4 in a new list arr5
    arr5 = list(it.accumulate(arr4, op.mul))
    
    print(arr5)
    
    return 0

if __name__ == '__main__':
    main()
    
#  Output
# [2, 1, 3, 4, 1, 1, 2, 4, 10, 3, 4, 3, 5, 6, 32, 11]
# [2, 2, 6, 24, 24, 24, 48, 192, 1920, 5760, 23040, 69120, 345600, 2073600, 66355200, 729907200]


