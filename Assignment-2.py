def frozen_set(str1,str2):
    fset = frozenset(str1)
    print(fset.difference(str2))# char not in both set
    print(fset.intersection(str2))# char which is available on both set
    print(fset.symmetric_difference(str2))# unique chars
    print(fset.union(str2))# all unique chars from both sets
    print(fset.issubset(str2)) # check if set one is subset of set two
    print(fset.issuperset(str2)) # check if set one is superset of set two

def index_step(lst):
    print(lst[::-1]) # list in reverse order
    print(lst[::2]) # list skipped by every two item


if __name__ == "__main__": 
    vowels = ('a', 'e', 'i', 'o', 'u')
    string = ("teachnook")
    frozen_set(string,vowels)
    index_step(string)
