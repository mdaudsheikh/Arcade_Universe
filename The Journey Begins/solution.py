def solution(param1, param2):
    if(-1000 <= param1 <= 1000 or -1000 <= param1 <= 1000):
        return param1 + param2
    else:
        False

def solution(year):
    if(1 <= year <= 2005):
        if(year%100 == 0):
            return (year//100)
        else:
            return (year//100 +1)


def solution(inputString):
    
    string_reverse = ""
    
    if(1 <= len(inputString) <= 10**5):
        for i in range(len(inputString)):
            string_reverse += inputString[len(inputString) - i -1]

        if(string_reverse == inputString):
            return True
        else:
            return False
