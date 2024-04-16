arr = [12,9,23,17,25,19,4,8,21,34,26,17,19,14,27,22,15,7,2,14,5,18,24]

size = len(arr)
print(size)

k = 3
curr_sum =0
maxi_sum = 0
j = 0
for i in range(0,size):
    curr_sum = curr_sum +arr[i]
    
    while i-j+1 >k:
        curr_sum = curr_sum -arr[j]
        j = j+1
    
    
    if i-j+1 ==k:
       if curr_sum >maxi_sum:
           maxi_sum = curr_sum
    
print(maxi_sum)
    
    