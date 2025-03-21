"""
def hamming(n):
    if n==1:
        return 1
    my_dict ={2:2,3:3,5:5}
    smallest=5
    for a in range (2,n+1):
        smallest = min(my_dict.values())
        for key in my_dict:
            if(my_dict[key]==smallest):
                my_dict[key] += key
        print(my_dict)
        print(smallest)
    return smallest
"""
def hamming(n):
    hamming_numbers = [1]
    i2 = i3 = i5 = 0

    while len(hamming_numbers) < n:
        next_hamming = min(hamming_numbers[i2] * 2, hamming_numbers[i3] * 3, hamming_numbers[i5] * 5)
        hamming_numbers.append(next_hamming)

        if next_hamming == hamming_numbers[i2] * 2:
            i2 += 1
        if next_hamming == hamming_numbers[i3] * 3:
            i3 += 1
        if next_hamming == hamming_numbers[i5] * 5:
            i5 += 1

    return hamming_numbers[-1]