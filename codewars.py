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

def parse_bank_account(bank_account):
    #example input
    # text":              '    _  _     _  _  _  _  _ \n'+
    #                     '  | _| _||_||_ |_   ||_||_|\n'+
    #                     '  ||_  _|  | _||_|  ||_| _|\n'

    #maybe break down to try and get the nunbers individually first
    #all numbers are 3 chars
    #lets try to get the numbers individually first
    list_of_nums = ['  ', ' _', ' _', '  ', ' _', ' _', ' _', ' _', ' _', '  |', ' _|', ' _|', '|_|', '|_ ', '|_ ', '  |', '|_|', '|_|', '  |', '|_ ', ' _|', '  |', ' _|', '|_|', '  |', '|_|', ' _|']
    #formula is 0 +28 + 28
    row_one = []
    row_two = []
    row_three = []

    row_length = int(len(bank_account)/3)
    for i in range(0,row_length-1,3):
        #+28 
        row_one.append(bank_account[i:(i+2)])
        row_two.append(bank_account[i+row_length:(i+3)+row_length])
        row_three.append(bank_account[i+(row_length*2):(i+3)+(row_length*2)])


    print(row_one)
    print(row_two)
    print(row_three)
    bank_account_number = []

    new_row_length = int(row_length/3)
    for index in range(0,new_row_length):
        for num in range(0,9):
            if row_one[index] == list_of_nums[num] and row_two[index] == list_of_nums[num+9] and row_three[index] == list_of_nums[num+18]:
                bank_account_number.append(str(num+1))
                print("Number added:",num+1)
                break
            elif row_one[index] == " _" and row_two[index] == "| |" and row_three[index] == "|_|":
                bank_account_number.append(str(0))
                print("Number added: 0")
                break
            else:
                print("NOT FOUND")
                
    
    print(bank_account_number)
    return int(''.join(bank_account_number))
#5kyu
#4kyu
#3kyu
#2kyu
#1kyu


if __name__ == "__main__":
    #stuff
    #beggars([1,2,3,4,5],1)
    #print(size_to_number("xl"))
    print(parse_bank_account(   ' _  _     _  _     _  _  _  _  _ \n'
                                '|_ |_   || ||_   | _||_ |_| _||_|\n'
                                '|_| _|  ||_||_|  ||_  _| _||_ |_|\n'))

