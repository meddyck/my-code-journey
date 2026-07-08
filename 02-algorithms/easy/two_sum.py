"""
PROBLEM: Two Sum (LeetCode #1)
-------------------------------------------------------------------
Given an array of integers `nums` and an integer `target`, return 
indices of the two numbers such that they add up to `target`.
-------------------------------------------------------------------
"""

def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
    """
    APPROACH 1: Brute Force (Nested Loops)
    - Checks every possible pair using two loops.
    
    Time Complexity  : O(N^2) -> Very slow as the number of elements increases.
    Space Complexity : O(1)   -> Uses no additional memory.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hashmap(nums: list[int], target: int) -> list[int]:
    """
    APPROACH 2: Hash Map / Dictionary (Optimized Solution)
    - Stores numbers and their indices in a dictionary to find the needed 
      complement in O(1) time.
    
    Time Complexity  : O(N) -> Traverses the array only once.
    Space Complexity : O(N) -> Uses extra memory for the Hash Map.
    """
    
    # -------------------------------------------------------------------------
    # CODE EXPLANATIONS & KEY CONCEPTS:
    #
    # 1. `seen = {}`: 
    #    A Hash Map (dictionary) to store visited numbers and their indices 
    #    in the format `{number: index}`. Acts like leaving a memo note.
    #
    # 2. `enumerate(nums)`: 
    #    Loop helper that gives both the index (`current_index`) and 
    #    the value (`num`) at the same time.
    #
    # 3. `complement = target - num`: 
    #    Calculates the required matching value to reach the target. 
    #    (If Target = 9 and current number = 2, complement is 7).
    #
    # 4. `if complement in seen`: 
    #    Checks if the needed matching number was already recorded in our map.
    #
    # 5. `seen[num] = current_index`: 
    #    If the complement is not found, records the current number and its index 
    #    so future iterations can use it as a complement.
    # -------------------------------------------------------------------------
    
    seen = {}  # {number: index}
    
    for current_index, num in enumerate(nums):
        complement = target - num  # Calculate the required matching number
        
        # Check if the needed complement was already recorded in our map
        if complement in seen:
            return [seen[complement], current_index]
            
        # Record the current number and index for future iterations
        seen[num] = current_index
        
    return []


# =====================================================================
# TEST CASES / EDGE CASES
# =====================================================================
if __name__ == "__main__":
    print("--- Testing Two Sum Solutions ---")
    
    # Test 1: Standard Case
    nums1, target1 = [2, 7, 11, 15], 9
    assert two_sum_hashmap(nums1, target1) == [0, 1]
    print("✓ Test 1 Passed (Standard Case)")

    # Test 2: Negative Numbers
    nums2, target2 = [-3, 4, 3, 90], 0
    assert two_sum_hashmap(nums2, target2) == [0, 2]
    print("✓ Test 2 Passed (Negative Numbers)")

    # Test 3: Duplicate Values
    nums3, target3 = [3, 3], 6
    assert two_sum_hashmap(nums3, target3) == [0, 1]
    print("✓ Test 3 Passed (Duplicate Values)")

    print("\nAll test cases passed successfully!")
