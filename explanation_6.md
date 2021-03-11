# Problem 6: Union and Intersection of Two Linked List

## Worst-case time-complexity of `union()` is **_O(n + m)_**.

Because we are iterating the elements from input ListLists(llist1, llist2).

## Worst-case time-complexity of `intersection()` is **_O(n + m)_**.

Because we are iterating the elements from input ListLists(llist1, llist2).

We are storing the count of elements in llist1 in a dict. And if it exists in llist2 as well, it subtracts one count from the dict and appends the value to the new LinkedList.

## The worst-case space-compleixty of `union()` is **_O(n + m)_**.

In the case of `union()`, all elements of llist1 and llist2 are different.

## The worst-case space-complexity of `intersection()` is **_O(n)_**.

In the case of `intersection()`, all elements of llist1 and llist2 are the same.
