def solution(inputArray):
        if(1 <= len(inputArray) <= 10):
            lenght_list = []
            for i in range(len(inputArray)):
                if(1 <= len(inputArray[i]) <= 10):
                    pass
                else:
                    return
            for i in range(len(inputArray)):
                lenght_list.append(len(inputArray[i]))
            
            max_value = max(lenght_list)
            max_indices = [i for i, x in enumerate(lenght_list) if x == max_value]
            
            longest_strings = []
            
            for i in max_indices:
                longest_strings.append(inputArray[i])
            return longest_strings


def solution(s1, s2):
    sum = 0
    def letter_occurances(string):
        letter_dict = dict()
        for letter in string:
            letter_dict[letter] = 0
        for letter in string:
            letter_dict[letter] += 1
        return letter_dict
    
    s1_letters = letter_occurances(s1)
    s2_letters = letter_occurances(s2)
    
    if(len(s1_letters) < len(s2_letters)):
        for letter in s1_letters:
            if(letter in s2_letters):
                if(s1_letters[letter] < s2_letters[letter]):
                    sum += s1_letters[letter]
                else:
                    sum += s2_letters[letter]
    else:
        for letter in s2_letters:
            if(letter in s1_letters):
                if(s1_letters[letter] < s2_letters[letter]):
                    sum += s1_letters[letter]
                else:
                    sum += s2_letters[letter]
    return sum



def solution(n):
    if(10 <= n <= 10**6):
        ticket_number_list = [int(x) for x in str(n)]
        half_length = int(len(ticket_number_list) /2)
        first_half_sum = sum(ticket_number_list[:half_length])
        second_half_sum = sum(ticket_number_list[half_length:])
        if(first_half_sum == second_half_sum):
            return True
        else:
            return False

def solution(a):
    tree_indices = []
    non_trees = []
    for i in range(len(a)):
        if(a[i] == -1):
            tree_indices.append(i)
        else:
            non_trees.append(a[i])
            
    sorted_non_trees = sorted(non_trees)
    
    for i in range(len(a)):
        if i not in tree_indices:
            a[i] = sorted_non_trees.pop(0)
    return a
    
    
def solution(inputString):
    reverse_string = list(inputString)
    start = []
    end = []
    for index, value in enumerate(inputString):
        if value == "(":
            start.append(index)
        if value == ")":
            end.append(index)
            start_index = start.pop()
            end_index = end.pop()
            reverse_string[start_index:end_index] = reverse_string[start_index:end_index][::-1]
    reverse_string = (filter(lambda a: a!=")" and a!="(", reverse_string))
    
    return ''.join(reverse_string)
    


