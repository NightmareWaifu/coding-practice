#because they didn't have go :/
 

#8ku
#7kyu
#6kyu
def beggars(values, n):
    #English beggars
    if n == 0:
        return []
    print(f"Values: {values} - n: {n}")

    #dictionary maybe? then have begger: array format

    beggar_sum = []
    for i in range(n):
        beggar_sum.append(0)
    beggar = 0
    for offer in values:
        #internal timer, reset once more than n
        if beggar>n-1:
            beggar = 0
        print(f'Beggar: {beggar}')
        beggar_sum[beggar] = beggar_sum[beggar] + offer

        beggar+=1
    #return an array length n-1 (take home of each beggar 1 to n)
    print(beggar_sum)
    return beggar_sum

#5kyu
#4kyu
#3kyu
#2kyu
#1kyu


if __name__ == "__main__":
    #stuff
    beggars([1,2,3,4,5],1)