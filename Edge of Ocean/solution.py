def solution(inputArray):
    product_list = []
    if(2 <= len(inputArray) <= 10):
        
        for i in range(len(inputArray) -1):
            if(-1000 <= inputArray[i] <= 1000):
                product_list.append(inputArray[i] * inputArray[i+1])
                
        return max(product_list)


def solution(n):
    
    if(n == 1):
        return 1
    return solution(n-1) + (n-1)*4


def solution(statues):
    if (1 <= len(statues) <=10 and 0 <= max(statues) <=20):
        all_statues = []
        min_num_statues = 0
        for i in range(min(statues),max(statues)+1):
            all_statues.append(i)
        for i in range(len(all_statues)):
            if all_statues[i] not in statues:
                min_num_statues +=1
        return min_num_statues

def solution(sequence):
    #Take out the edge cases
    if len(sequence) <= 2:
        return True

    #Set up a new function to see if it's increasing sequence
    def IncreasingSequence(test_sequence):
        if len(test_sequence) == 2:
            if test_sequence[0] < test_sequence[1]:
                return True
        else:
            for i in range(0, len(test_sequence)-1):
                if test_sequence[i] >= test_sequence[i+1]:
                    return False
                else:
                    pass
            return True

    for i in range (0, len(sequence) - 1):
        if sequence[i] >= sequence [i+1]:
            #Either remove the current one or the next one
            test_seq1 = sequence[:i] + sequence[i+1:]
            test_seq2 = sequence[:i+1] + sequence[i+2:]
            if IncreasingSequence(test_seq1) == True:
                return True
            elif IncreasingSequence(test_seq2) == True:
                return True
            else:
                return False

def solution(matrix):
    if(1 <= len(matrix) <=5):
        if(1 <= len(matrix[0]) <=5):
            sum = 0
            for i in range(len(matrix[0])):
                for j in range(len(matrix)):
                    if(0 <= matrix[j][i] <= 10):
                        pass
                    else:
                        return
                        
            for i in range(len(matrix[0])):
                for j in range(len(matrix)):
                    if(matrix[j][i] == 0):
                        break
                    else:
                        sum += matrix[j][i]
            return sum


