# Sum of all even number in a list

def sumEven(l1):
    sum = 0
    for i in l1:
        if i%2 == 0:
            sum = sum + i

    return sum

l = list(map(int,input("Enter a list : ").split()))
result = sumEven(l)
print(result)

# Count the number of Vowels

def countVowels(words):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in words:
        if i in vowels:
            count+=1
    return count

w = input("Enter a words :")
resultCount = countVowels(w)
print(resultCount)





def uniqueNums(nums):
    for i in range(0,len(nums)-1):
        if i in nums and nums.count(i) >=2:
            nums.remove(i)    
    return nums
l= [1,1,1,2,2,3,3,4]
uniqueList = uniqueNums(l)
print(uniqueList)                

