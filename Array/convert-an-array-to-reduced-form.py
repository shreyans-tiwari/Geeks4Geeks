"""
Given an array with N distinct elements, convert the given array to a reduced form
where all elements are in range from 0 to N-1. The order of elements is same, i.e.,
0 is placed in place of smallest element, 1 is placed for second smallest element,
and N-1 is placed for the largest element.

Note: You don't have to return anything. You just have to change the given array.
"""

def convert(self,arr, n):
	    a = arr[:];
	    a.sort();
	    m_a = {};
	    r = 0
	    for i in a:
	        if i not in m_a:
	            m_a[i] = r
	            r += 1
	   
	    for i in range(len(arr)):
	        arr[i] = m_a[arr[i]]
