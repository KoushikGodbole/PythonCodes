import operator

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    temp_val = dict()
    i = 0
    size = len(height)
    temp_height = 0
    cont_height = 0
    temp_res = 0
    while (i < size):
        if (height[i] in temp_val):
            temp_val[height[i]] = temp_val[height[i]] + 1
        else:
            if(height[i] > 0):
                temp_val[height[i]] = 1
        temp_height = temp_height + height[i]
        i += 1
    temp_sorted_keys = sorted(temp_val.items(), key=operator.itemgetter(1), reverse=False)
    i = 0
    #while(i < len(temp_sorted_keys)):
      #  temp = temp_val[temp_sorted_keys[i][0]]
        #if(temp >= 2):
        #    cont_height = temp
        #    break;
        #i += 1
    cont_height = temp_sorted_keys[0][0]
    temp_res = cont_height * (size)

    res = temp_res - temp_height
    return res

result = trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(result)