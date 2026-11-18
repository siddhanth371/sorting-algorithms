
# n=int(input("enter the number of elements:"))
# arr=[]
# for i in range(1,n):
#     ele=int(input("enter the element:"))
#     arr.append(ele)
# print(arr)


def selection_sort(nums):
    # Traverse through all array elements
    for i in range(len(nums)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

nums = [5, 7, 4, 8, 1, 6, 9, 2]
selection_sort(nums)
print(nums)

#for descending order
nums=[2,4,7,8,6,1,2]
n=len(nums)
for i in range(0,n):
    max_index=i
    for j in range(i+1,n):
        if(nums[j]>nums[max_index]):
            max_index=j
    nums[i],nums[max_index]=nums[max_index],nums[i]
print(nums)