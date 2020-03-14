import sys

def char_map(str1, str2):
    dict = {}

    # if the string length is not equal, return false
    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)):
        # check if char is in dictionary 
        # and if already a differnt value exists return false
        if str1[i] in dict:
            if dict[str1[i]] != str2[i]:
                return False
        else:
            dict[str1[i]] = str2[i]
    return True

if __name__ == '__main__':
    result = char_map(sys.argv[1], sys.argv[2])
    print(result)