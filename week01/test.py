def get_middle(s):
    return s[int(len(s)/2)] if len(s) % 2 !=0 else s[int(len(s)/2)-1:int(len(s)/2)+1]


def find_missing_letter(chars):
    a = [ord(i) for i in sorted(chars)]
    for i in range(len(a)):
        if  a[i+1] - a[i] != 1:
            return a[i]+1

def digital_root(n):
    print(map(int,str(n)))
    return n if n < 10 else digital_root(sum([int(i) for i in str(abs(n))]))

numbers = "2 4 7 8 10"
def iq_test(numbers):
    numbers = [int(i) % 2 == 0 for i in numbers.split()]
    return numbers.index(True) + 1 if numbers.count(True) < numbers.count(False) else numbers.index(False) + 1

def high(x):
    aa = [sum(s) for s in [[ord(j)-96 for j in i] for i in x.split()]]
    return x.split()[aa.index(max(aa))]

# likes([]) # must be "no one likes this"
# likes(["Peter"]) # must be "Peter likes this"
# likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
# likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
# likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

def likes(names):
    # dict_t = {0:'no one likes this',
    #           1:f'{names[0]} likes this',
    #           2:f'{names[0]} and {names[1]} like this',
    #           3:f'{names[0]}, {names[1]} and {names[2]} like this',
    #           4:f'{names[0]}, {names[1]} and {len(names)-2} others like this'}
    if len(names) > 3:
        return f'{names[0]}, {names[1]} and {len(names)-2} others like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    else:
        return 'no one likes this'



# likes([])

# print(sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

def max_sequence(arr):
    return sum(sorted(list(set(arr))))

# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def getRealChild(listA):
    realChildList = []
    for i in range(0, len(listA) - 1):
        for j in range(i + 1, len(listA)):
            realChildList.append(listA[i:j])
    return realChildList

