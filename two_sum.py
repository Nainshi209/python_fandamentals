 #we are solving a two sum array problem using two pointer approach
#take a array to represent list
arr = [1,2,4,6,10]

# define expected output and target

target = 8

#initilize left pointer 

left = 0

right =  len(arr)-1
#using while loop

while left < right:
    total = arr[left]+arr[right]

    if total == target:
        print("Index position:", left,right)
        print("Index posotion element",arr[left], arr[right])
        print("Targeted sum:", total)
        break

    elif total < target:
        
        left+= 1
    else:
         right-=1