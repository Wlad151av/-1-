
k = int(input("Введите число на левой табличке: "))   # to get initial data for calculation
ans = []                                              # empty list creation for correct password generation
for i in range(1,k):                                  # begin to choose numerals from 1 to (k-1)
    for j in range(i+1,k):                                # for each i meaning we check the reat of list
        if k % (i+j) == 0:                              # if there is no rest of division
            ans = ans + list(str(i)+str(j))             # then add the pair to answer
print(''.join(ans))                                     # merging list of digits to answer string