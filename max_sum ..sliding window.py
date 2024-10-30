def max_sum(nums,k):
    current_sum=sum(nums[:k])
    max_sum=current_sum
    i=k
    while i<len(nums):
        current_sum+=nums[i]-nums[i-k]
        max_sum=max(max_sum,current_sum)
        i+=1
    return max_sum
nums=[2,4,8,1,6,9,0,5]
k=3
result =max_sum(nums,k)
print(result)