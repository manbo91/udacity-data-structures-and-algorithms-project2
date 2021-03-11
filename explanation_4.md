# Problem 4: Active Directory

Worst-case time-complexity is **_O(gn)_**.

The time-complexity for this program is **_O(gn)_** because we have to check all the groups' users.

the n is the number of users in a group.

g = groups, n = users in a group

Worst-case space-complexity is **_O(g)_**.

This program only accesses lists (groups, users) and compares.
But, when accessing a group, it takes up space in memory to the call stack.
