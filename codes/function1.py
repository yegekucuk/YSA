def helper(liste):
    # [3,4] -> [[3],[4]]
    return [[x] for x in liste]

def create_sublists(input_list, window_size):
    """
    Shifting a window through a list
    Window's size is determined by the window_size variable 
    
    For example, if window size is 2:
    ["I","like","hiking","and","biking"]
    
    OUTPUT1[0] -> ['I', 'like', 'hiking']
    OUTPUT1[1] -> ['like', 'hiking', 'and']
    OUTPUT2[0] -> and
    OUTPUT2[1] -> biking
    
    """
    output1 = [input_list[i:i+window_size] for i in range(len(input_list)-window_size+1)]
    output2 = input_list[window_size:]

    # Removing the last combination for output1, because the last combination has no output.
    output1.pop(-1)

    return output1, output2

import numpy as np
def toInt(window:np.array):
    """
    This function converts dtype = "float32" array to dtype="int8" array,
    It gets the highest number and makes it 1, others 0
    As Dense layer is creating outputs in float32 type, this function seemed to be necessary. 
    """
    window = window.tolist()
    maximum = max(window)
    for i,j in enumerate(window):
        if j == maximum:
            window[i] = 1
        else:
            window[i] = 0
    window = np.asarray(window, dtype="int8")
    return window
