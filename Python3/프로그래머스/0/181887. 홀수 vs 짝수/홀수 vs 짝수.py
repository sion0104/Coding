def solution(num_list):
    odd_sum, even_sum = 0, 0
    for i in range(0, len(num_list)):
        if i % 2 == 0:
            odd_sum += num_list[i]
        else:
            even_sum += num_list[i]
            
    return max(odd_sum, even_sum)