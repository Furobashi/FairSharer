def fair_sharer(values=list, num_iterations=int, share=0.1)->list:
    """Runs num_iterations.
In each iteration the highest value in "values" gives a fraction (share)
to both the left and right neighbor. The leftmost field is considered
the neightbor of the rightmost field.
Examples:
fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
Args
values:
1D array of values (list or numpy array)
num_iteration:
Integer to set the number of iterations
"""
    for _ in range(num_iterations):

        #searching for the highest value in the list
        max_val = max(values)

        #getting the index of the highest value
        max_index = values.index(max_val)
        
        #calculating the share of the highest value, which will be passed on
        sharing = max_val*share

        last_indx = len(values)-1

        if max_index == 0: 
            values[last_indx] += sharing
        else:
            values[max_index-1] += sharing        

        if max_index == last_indx:
            values[0] += share
        else:
            values[max_index+1] += sharing
        

        #subtracting the shares from the highest value
        values[max_index] -= 2*sharing

    #returning new list with adjusted values    
    return values

print(fair_sharer([0, 1000, 800, 0], 1))
print(fair_sharer([0, 1000, 800, 0], 2))
print(fair_sharer([0, 1000, 800, 0], 3))
