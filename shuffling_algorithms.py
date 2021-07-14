#python code to demonstrate 
#different ways to shuffle a list

from random import randint

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def modern_shuffle(list_p):
    #index of the last value in the list
    last_index = len(list_p) - 1

    #continue looping until every index has been shuffled 
    while last_index > 0:
        #get random index
        rand_indx = randint(0, last_index)

        #swap last index with random index
        list_p[last_index], list_p[rand_indx] = list_p[rand_indx], list_p[last_index]

        #decrement last index
        last_index -= 1

    return list_p

def fy_shuffle(list_p):
    #iterate through the list backwards
    for cur_indx in range(len(test_list) - 1, 0, -1):
        #get random index that has not been shuffled
        rand_indx = randint(0, cur_indx)

        #swap current index with the random index
        list_p[cur_indx], list_p[rand_indx] = list_p[rand_indx], list_p[cur_indx]
    
    return list_p

#same as fy_shuffle() but iterating forward using the enumerate function
def fy_shuffle_forward(list_p):
    for cur_val, cur_indx in enumerate(list_p):
        rand_indx = randint(0, cur_indx)

        list_p[cur_indx], list_p[rand_indx] = list_p[rand_indx], list_p[cur_indx]
    
    return list_p



print(modern_shuffle(test_list))
print(fy_shuffle(test_list))
print(fy_shuffle_forward(test_list))
