# -*- coding: utf-8 -*-

import listiterator as list

def print_with_iterator (l):
    """
    Print elements of a list using an iterator.
    
    :param l: The list to be printed
    :type l: dict
    """
    l_iterator=list.get_listiterator(l)
    while list.hasNext(l_iterator):
        print(list.next(l_iterator))
    return None
        

def print_with_iterator_reverse (l):
    """
    Print elements of a list using an iterator in reverse order.
    
    :param l: The list to be printed
    :type l: dict
    """
    l_iterator=list.get_listiterator(l)
    while list.hasNext(l_iterator):
        list.next(l_iterator)
    while list.hasPrevious(l_iterator):
         print(list.previous(l_iterator))
    return None
    
def print_with_iterator_reverse_bis (l):
    """
    Print elements of a list using an iterator in reverse order.
    
    :param l: The list to be printed
    :type l: dict
    """
    l_iterator=list.get_listiterator(l,from_the_end = True)
    while list.hasPrevious(l_iterator):
        print(list.previous(l_iterator))
    return None

def ordering_insert (l, v):
    """
    Add *v* to list *l* such that *l* is kept ordered.
    
    :param l: An ordered list.
    :type l: dict
    :param v: The value to be inserted.
    :type v: same as elements of *l*
    """
    if list.is_empty(l):
        cons(l,v)
        Found = True
    else:
        Found = False
        it=list.get_listiterator(l)
        while list.hasNext(it) and not Found:
            if v<=list.next(it):
               list.previous(it)
               list.add(it,v)
               Found = True
    if not Found:
        list.add(it,v)
    return None
    
        
    

if __name__ == "__main__":
    l = list.empty_list ()
    for i in reversed(range(1,5)):
        list.cons(l,i)
        
    list.print_list(l);

    print("test 0 : impression renversee")
    list.print_list(l,reverse=True)

    print("test 1 : impression avec iterateurs")
    print_with_iterator(l)
    print_with_iterator_reverse(l)

    print("test 2 : insertion avant le 3eme element")
    it = list.get_listiterator (l)
    print(list.next(it))
    print(list.next(it))
    list.add(it,23)
    assert(list.previous(it) == 23)
    print_with_iterator(l)
    print_with_iterator_reverse(l)

    print("test 3 : insertion apres le dernier element")
    it = list.get_listiterator (l)
    while (list.hasNext(it)):
        list.next(it)
    list.add(it,45)
    assert(list.previous(it) == 45)
    l=list.set_head_tail(it)
    print_with_iterator(l)
    print_with_iterator_reverse(l)

    print("test 4 : insertion avant le premier element")
    it = list.get_listiterator (l)
    list.add(it,0)
    assert(list.previous(it) == 0)
    l=list.set_head_tail(it)
    print_with_iterator(l)
    print_with_iterator_reverse(l)

    print("test 5 : insertion avant le dernier element avec l'iterateur placé en fin")
    it = list.get_listiterator (l,True)
    list.previous(it)
    list.add(it,445)
    assert(list.previous(it) == 445)
    print_with_iterator(l)
    print_with_iterator_reverse(l)

    print("test 6 : affichage à l'envers avec l'itérateur placé en fin")
    print_with_iterator_reverse_bis(l)

    print("test 7 : ajout après le dernier élément")
    it = list.get_listiterator (l,True)
    list.add(it,5)
    assert(list.previous(it) == 5)
    l=list.set_head_tail(it)
    print_with_iterator(l)
    print_with_iterator_reverse(l)
        
    print("test 8 : inserer trié, à vous d'écrire ce test")
    l = list.empty_list ()
    for i in reversed(range(2,10,2)):
        list.cons(l,i)
    it = list.get_listiterator (l)
    ordering_insert(l,5)
    ordering_insert(l,9)
    ordering_insert(l,1)
    l=list.set_head_tail(it)    
    print_with_iterator(l)
    print_with_iterator_reverse(l)
    

    print("test 9 : suppression en tete")
    l = list.empty_list ()
    for i in reversed(range(1,5)):
        list.cons(l,i)
    it = list.get_listiterator (l)
    list.remove(it)
    l=list.set_head_tail(it)  
    print_with_iterator(l)
    print_with_iterator_reverse(l)
    

    print("test 10 : suppression en queue")
    l = list.empty_list ()
    for i in reversed(range(1,5)):
        list.cons(l,i)
    it = list.get_listiterator (l,True)
    list.previous(it)
    list.remove(it)
    l=list.set_head_tail(it)  
    print_with_iterator(l)
    print_with_iterator_reverse(l)
    
    
    
