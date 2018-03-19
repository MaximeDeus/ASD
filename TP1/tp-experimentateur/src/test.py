# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for experiences assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2015, december
"""

import sys
import experience
import sorting

cpt=0

def compare (m1,m2):
    return experience.compare(m1,m2)

# STRATEGY 1
def negative_markers1(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.
    The two lists aren't sorted.

    :param markers: The list of markers
    :type markers: List of String
    :param positive: The list of positive markers
    :type positive: List of String
    :return: The list of negative markers
    :rtype: List of String

    
    """
    global cpt
    negative = [] #initialize result
    for marker in markers:
        found=False #(re)initialize variable
        position=0 #(re)initialize indexation
        while not found and position < len(positive): #while the marker hasn't been found in the list of positives markers  
            if compare(marker,positive[position]) == 0: #if the marker is positive
                found=True
            else:
                position+=1
            cpt+=1 #increase counter
        if not found:
            negative+=[marker] #If the marker isn't positive (so he's negative..)
    return negative #returns the list of negatives markers

# STRATEGY 2
def negative_markers2(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.
    positive list will be sorted (just the copy).

    :param markers: The list of markers
    :type markers: List of String
    :param positive: The list of positive markers
    :type positive: List of String
    :return: The list of negative markers
    :rtype: List of String

    
    """
    global cpt
    negative = []
    positive_sorted=sorting.merge_sort(positive,compare) #sort positive markers's list
    for marker in markers:
        found=False
        position=0
        while not found and position < len(positive_sorted) and compare(marker,positive_sorted[position]) > -1: #If the marker still not been found and at least one positive
                                                                                        #marker remaining isn't strictly greater than the marker
            if compare(marker,positive_sorted[position]) == 0:
                found=True
            else:
                position+=1
            cpt+=1
        if not found:
            negative+=[marker]
    return negative

# STRATEGY 3
def negative_markers3(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.
    The two lists are sorted.

    :param markers: The list of markers
    :type markers: List of String
    :param positive: The list of positive markers
    :type positive: List of String
    :return: The list of negative markers
    :rtype: List of String

    
    """
    global cpt
    negative = []
    positive_sorted=sorting.merge_sort(positive,compare) #sort positive markers's list
    markers_sorted=sorting.merge_sort(markers,compare) #sort markers's list
    position=0 #No reinitialization of the position
    for marker in markers_sorted:
        found=False
        while not found and position < len(positive_sorted) and compare(marker,positive_sorted[position]) > -1: #if m>=p
            if compare(marker,positive_sorted[position]) == 0: #m=p
                found=True
            position+=1
            cpt+=1
        if not found:
            negative+=[marker]
    return negative
        
if __name__ == "__main__":
    p = int(sys.argv[1])
    m = int(sys.argv[2])
    for n in range (10,101,10): #n=10 20 30... 100
       file=open("tp1-"+str(n)+".dat","w") #creates file and open it in write mode
       m=n #Initialize m and p
       p=1
       while p<=m: #Creates the grid of each file
           file.write(str(m)+" "+str(p)+ " ")
           print (m,p, end=" ")
           markers = experience.markers(m)
           positive = experience.experience(p,markers)
           negative_markers1(markers,positive)
           print(cpt, end=" ")
           file.write(str(cpt)+" ")
           cpt = 0
           negative_markers2(markers,positive)
           print(cpt, end=" ")
           file.write(str(cpt)+" ")
           cpt = 0
           negative_markers3(markers,positive)
           print(cpt, end="\n")
           file.write(str(cpt)+"\n")
           cpt = 0
           p+=1
       file.close()

##    print("Markers: %s" % (markers))
##    print("Positive markers: %s" % (positive))

    # test stategy 1
 #   cpt = 0
##    print("Negative markers: %s" % (negative_markers1(markers,positive)))
##    print("Nb. comparisons: %d" % (cpt))

    # test stategy 2
 #   cpt = 0
##    print("Negative markers: %s" % (negative_markers2(markers,positive)))
##    print("Nb. comparisons: %d" % (cpt))
    # test stategy 3
 #   cpt = 0
##    print("Negative markers: %s" % (negative_markers3(markers,positive)))
##    print("Nb. comparisons: %d" % (cpt))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
