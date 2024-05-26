"""Write a Python function that takes a list of integers as input and returns the length of the longest increasing subsequence. The subsequence does not need to be contiguous, but the elements must be in increasing order.

def longest_increasing_subsequence_length(nums):
    # Implement the algorithm to find the length of the longest increasing subsequence
    pass

# Example Usage
nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = longest_increasing_subsequence_length(nums)
print(f"The length of the longest increasing subsequence is: {result}")"""


def lognest_sub(ls: list) -> int:
    l = len(ls)
    max_sub = 1

    for i in range(l):
        sub = 1
        currnet = ls[i]
        for j in range(i+1, l):
            if (currnet < ls[j]):
                currnet = ls[j]
                sub += 1
        if(sub> max_sub): 
            max_sub = sub
    return max_sub


if __name__ == "__main__":
    nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    max_nr = lognest_sub(nums)
    print(f"max_nr: {max_nr}")


