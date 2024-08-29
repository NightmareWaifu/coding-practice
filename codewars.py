#because they didn't have go :/
#formatting rules - 2 new lines between everything 4 new lines between kyu
#comment the name of the problem below the function / at the start of the solution

#8kyu




#7kyu


#Clothes size number converter
def size_to_number(size):
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


#English beggars
def beggars(values, n):
    
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


#Parse bank account number
def parse_bank_account(bank_account):
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


#Nearly flatten a messy array
def near_flatten(nested):
    
    return check_nested(nested,[])

def check_nested(array, lowest_level):
    #where lowest_level contains all of the lowest-level arrays
    for item in array:
        if type(item) == list:
            check_nested(item, lowest_level)
        else:
            lowest_level.append(array)
            break

    return sorted(lowest_level)


#Number of Letters of Numbers
def numbers_of_letters(n):
    return numbers_of_letters_data(n, [])
    
def numbers_of_letters_data(n, path):
    numbers_letters = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    letters = ""
    for num in str(n):
        letters = letters + numbers_letters[int(num)]
    
    path.append(letters)
    if n == len(letters):
        return path
    
    letter_value = len(letters)
    
    return numbers_of_letters_data(letter_value, path)


#5kyu

#A Chain adding function
class CustomIntFunc(int):
    def __call__(self, a):
        return CustomIntFunc(self + a)
def add(n):
    #refer to https://stackoverflow.com/questions/39038358/function-chaining-in-python
    
    return CustomIntFunc(n)
#4kyu
#3kyu
#2kyu
#1kyu


if __name__ == "__main__":
    #stuff
    #beggars([1,2,3,4,5],1)

    #print(size_to_number("xl"))

    # print(parse_bank_account(   ' _  _     _  _     _  _  _  _  _ \n'
    #                             '|_ |_   || ||_   | _||_ |_| _||_|\n'
    #                             '|_| _|  ||_||_|  ||_  _| _||_ |_|\n'))

    #print(near_flatten([[1,2,3],[[4,5],[[6],[7,8]]]]))
    #print(check_nested([[[1],[2,3]],[4,5]],[]))

    print(numbers_of_letters(1))
