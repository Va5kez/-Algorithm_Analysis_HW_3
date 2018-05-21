import sys
#from Max_Point.maxpoint import MaxPoint
from Universal_Hashing.universal_hashing import hashing

def main():
    print "Universal Hashing\n"
    array = [1,2,3,4,5,6,7,8,9,10,11,12] #Max 20
    print array
    prime = hashing(array)
    print prime
    print "\nMax Point"


if __name__ == "__main__":
    main()
