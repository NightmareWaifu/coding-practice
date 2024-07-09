#because they didn't have go :/
 

#8ku
#7kyu
def size_to_number(size):
    #Clothes size number converter
    #x can only be used on S and L
    #S,M,L cannot me repeated strings
    #s = 36, m = 38, l = 40, every x is +-2
    if size and str(size[-1]).upper() not in {"S","M","L"}:
        return None
    
    if str(size).upper() == "M":
        return 38
    
    size_extra = str(size).upper().count("X") * 2

    if str(size).upper().replace("X","") == "S":
        return 36-size_extra
    elif str(size).upper().replace("X","") == "L":
        return 40+size_extra
    




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
    #beggars([1,2,3,4,5],1)
    print(size_to_number("xl"))