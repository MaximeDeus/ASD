# -*- coding: utf-8 -*-

"""
:mod:`sorting` module : sorting functions module for quicksort assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr> , Maxime DEROISSART`_

:date: 2017, january
"""

import copy
import random
import generate
import test
import sys

cpt=0  #global comparaison counter

def merge (t1,t2, cmp):
    """
    Given two sorted list, creates a fresh sorted list.
    
    :param t1: A list of objects
    :type t1: list
    :param t2: A list of objects
    :type t1: list
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A fresh list, sorted.
    :rtype: list
    
    .. note::
    
       time complexity of merge is :math:`O(n_1+n_2)` with
       :math:`n_1` and :math:`n_2` resp. the length of *t1* and *t2*

    """
    n1 = len(t1)
    n2 = len(t2)
    t = [ 0 for i in range(0,n1+n2)]
    i = j = k = 0
    while i < n1 and j < n2:
        if cmp(t1[i],t2[j]) < 0:
            t[k] = t1[i]
            i = i + 1
        else:
            t[k] = t2[j]
            j = j + 1
        k = k + 1
    while i < n1:
        t[k] = t1[i]
        i = i + 1
        k = k + 1
    while j < n2:
        t[k] = t2[j]
        j = j + 1
        k = k + 1
    return t


def merge_sort (t,cmp):
    """
    A sorting function implementing the merge sort algorithm
    
    :param t: A list of integers
    :type t: list
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :return: A fresh list, sorted.
    :rtype: list
    """
    n = len(t)
    if n <= 1:
        # cas de base
        return copy.deepcopy(t)
    else:
        # cas general
        t1 = merge_sort((t[0:((n-1)//2+1)]),cmp)
        t2 = merge_sort((t[((n-1)//2+1):n]),cmp)
        return merge(t1,t2,cmp)
    

def quicksort (t,cmp,random=True,best=True):
    """
    A sorting function implementing the quicksort algorithm
    
    :param t: A list of integers
    :type t: list
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :param random: if random = True, pivot will be taken randomly from s, if not, \
    the pivot will be the first element of s
    :type random: Bool
    :return: Nothing

    .. note::
       *t* is modified during the sort process

    :Examples:

    >>> l=generate.random_list(10)
    >>> quicksort(l,test.cmp)
    >>> generate.is_sorted(l)
    True

    >>> l=generate.increasing_list(10)
    >>> quicksort(l,test.cmp,random=True,best=False)
    >>> generate.is_sorted(l)
    True
    
    >>> l=generate.decreasing_list(10)
    >>> quicksort(l,test.cmp,random=False,best=False)
    >>> generate.is_sorted(l)
    True
    
    """
    if len(t) <= 1: #if singleton or empty list
        return None
    else:
        t_slice= { 'data': t , 'left' : 0, 'right' : len(t)-1 } #convert list to sliced list
        quicksort_slice (t_slice,cmp,random=random,best=best) #sort the slice
        return None #return the sorted list


def quicksort_slice (s, cmp,random=True,best=True):
    """
    A sorting function implementing the quicksort algorithm
    
    :param s: A slice of a list, that is a dictionary with 3 fields :
              data, left, right representing resp. a list of objects and left
              and right bounds of the slice.
    :type s: dict
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :param random: if random = True, pivot will be taken randomly from s, if not, \
    the pivot will be the first element of s
    :type random: Bool
    :return: Nothing

    :Examples:

    >>> l={"data":[3, 1, 2, 6, 4, 8, 5, 7, 9],"left":0,"right":8}
    >>> quicksort_slice (l,test.cmp)
    >>> l == {'right': 8, 'data': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'left': 0}
    True
    
    """
    ma_liste=s['data']
    size=len(ma_liste)
    left=s['left']
    right=s['right'] #initialize identificators

    if best:
        p=optimal_pivot(s)

    elif random:
        p=random_pivot(s)
    else:
        p=left

    if left == right: #if singleton
        return None     
    else:
##        print("tranche")
##        print(s)
        ma_tranche_1, ma_tranche_2 = partition (s, cmp, p)
##        print(s)
##        print("pivot")
##        print(p)
##        print("compteur")
##        print(cpt)
##        print("tranche1")
##        print(ma_tranche_1)
##        print("tranche2")
##        print(ma_tranche_2)
        
        ma_tranche_1 = quicksort_slice(ma_tranche_1, cmp,random=random,best=best)
        ma_tranche_2 = quicksort_slice(ma_tranche_2, cmp,random=random,best=best)
    return None



def exchange(l,i,j):
    """
    A function who exchange two elements of a list
    :param l: a list
    :type l: list
    :param i: index of the first element
    :type i: int
    :param j: index of the second element
    :type j: int
    :UC: i,j< len l
    """
    l[i],l[j]=l[j],l[i]
    return None


def partition (s, cmp,p):
    """
    Creates two slices from *s* by selecting in the first slice all
    elements being less than the pivot and in the second one all other
    elements.

    :param s: A slice of a list, that is a dictionary with 3 fields :
              data, left, right representing resp. a list of objects and left
              and right bounds of the slice.
    :type s: dict
    :param cmp: A comparison function, returning 0 if a == b, -1 is a < b, 1 if a > b
    :type cmp: function
    :param p: A pivot
    :type p: int
    :return: A couple of slices, the pivot being at the left index of the second slice.
    :rtype: tuple
    :UC: p must be between 0< size of the data-1

    >>> import generate
    >>> def cmp (x,y): 
    ...    if x == y:
    ...       return 0
    ...    elif x < y:
    ...       return -1
    ...    else:
    ...       return 1
    >>> l = generate.random_list(10)
    >>> pivot = l[0]
    >>> p1,p2 = partition({'left':0,'right':len(l)-1,'data':l},test.cmp,0)
    >>> l1 = p1['data'][p1['left']:p1['right']+1]
    >>> l2 = p2['data'][p2['left']:p2['right']+1]
    >>> [e<f for e in l1 for f in l2]
    ... # doctest: +ELLIPSIS
    [True, ..., True]

    """

    global cpt
    
    ma_liste=s['data']
    size=len(ma_liste)
    left=s['left']
    right=s['right'] #initialize identificators
    
    if left==right: #if there is just zero or one element on the list
        return (s,s)
    else:
        pivot=ma_liste[p] #the element in p position of the sliced list
        exchange(ma_liste,p,right) #interchange the pivot with the last element of the sliced list
        j=left #initialize the position of futures exchange
        for i in range (left,right): #browse sliced list without the pivot
            cpt+=1
            if cmp(ma_liste[i],pivot) == -1: #if [i]element < pivot
                exchange(ma_liste,i,j) #Interchange i/j
                j+=1 #element[i] is fixed on position j
        exchange(ma_liste,j,right) #Put the pivot in j position, now he's sorted
        if left == j: #because right can't be -1 on the first slice
            j+=1
        
        ma_tranche_1 = { "data" : ma_liste, "left" : left, "right" : j-1}
        ma_tranche_2 = { "data" : ma_liste, "left" : j, "right" : right} #return two slices, one with elements under pivot's value, the other one with the rest
    return (ma_tranche_1,ma_tranche_2)

def random_pivot (l):
    """
    returns a random index from a sliced list
    :param l: a sliced list
    :type l: dict
    :returns: a random index from a sliced list
    :rtype: int
    """
    
    return random.randint(l['left'],l['right'])

def optimal_pivot (s):

    """
    returns the best index for a sliced list, in order to use quicksort
    :param l: a sliced list
    :type l: dict
    :returns: a the index
    :rtype: int

    :Examples:

    >>> l= {'right': 9, 'data': generate.increasing_list(10), 'left': 0}
    >>> optimal_pivot (l)
    4

    >>> l= {'right': 9, 'data': generate.decreasing_list(10), 'left': 0}
    >>> optimal_pivot (l)
    5
    
    """
#    global cpt Pour l'avant-dernière question

    sum_s=0
    left=s['left']
    right=s['right'] #initialize identificators
    ma_liste=s['data'][left:right+1]
    size=len(ma_liste)
    
    for e in ma_liste:
#        cpt+=1
        sum_s+=e
    sum_s=sum_s//size
    while sum_s not in ma_liste: #a median value can not be on the list, example [7,9] = 8
        sum_s-=1
    return left+ma_liste.index(sum_s) #returns median value's position of the sliced list


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    cpt=0
    n = int(sys.argv[1]) #the number of table
    i=0
    file=open("tp2-finalcpt"+str(n)+".dat","w") #creates file and open it in write mode

    while i<=n: #Creates the grid of each sort
       file.write(str(100)+" "+str(i)+ " ")
       print (100,i, end=" ")
       s = generate.random_list(i) #generate a random list
       quicksort(s, test.cmp,random=False,best=False) #pivot in 1st position
       print(cpt, end=" ")
       file.write(str(cpt)+" ")
       cpt = 0
       s = generate.random_list(i) 
       quicksort(s, test.cmp,random=True,best=False) #random pivot
       print(cpt, end=" ")
       file.write(str(cpt)+" ")
       cpt = 0
       s = generate.random_list(i) 
       quicksort(s, test.cmp) #best pivot
       print(cpt, end="\n ")
       file.write(str(cpt)+"\n ")
       cpt = 0
       i+=1
    file.close()
