def binary_search_k(nums, k: int) -> tuple:
    lower_bound = 0
    upper_bound = len(nums)
    i=lower_bound

    while lower_bound < upper_bound:
        i = (lower_bound + upper_bound)//2
        print(i)
        if nums[i] == k:
            return nums[i],i, k 
        elif nums[i] > k:
            upper_bound = i -1
        elif nums[i] < k:
            lower_bound = i + 1



def main():
    nums = []
    nums.extend(range(400))
    print(binary_search_k(nums,8))

if __name__ == "__main__":
    main()