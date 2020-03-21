def hackerrankInString(s):
    # Complete this function
    shag = 0
    for i in 'hackerrank':
        if i in s[shag:]:
            p = s.index(i,shag) + 1
        else:
            return 'NO'
    return 'YES'

q = int(input())

for q_itr in range(q):
    s = input()
    result = hackerrankInString(s)
    print(result) 

 