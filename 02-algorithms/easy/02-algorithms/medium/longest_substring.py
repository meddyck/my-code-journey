"""
PROBLEM: Longest Substring Without Repeating Characters (LeetCode #3)
-------------------------------------------------------------------
Given a string `s`, find the length of the longest substring 
without repeating characters.

Example: s = "abcabcbb" -> Output: 3 (The answer is "abc")
-------------------------------------------------------------------
"""

def length_of_longest_substring(s: str) -> int:
    """
    APPROACH: Sliding Window + Hash Map
    - We use two pointers (`left` and `right`) to represent an expandable/contractable 
      "window" (box) over the string.
    
    PERFORMANCE / TIME COMPLEXITY:
    - Time Complexity: O(N) -> Linear Time!
      What is O(N)? It means the execution time grows directly in proportion to the 
      length of the input string (N). We pass through the string only once using a 
      single loop, making it very fast and efficient compared to O(N^2) nested loops.
      
    - Space Complexity: O(K) -> K is the number of unique characters stored in the map.
    """
    
    # -------------------------------------------------------------------------
    # CODE EXPLANATIONS & KEY CONCEPTS:
    #
    # 1. `char_map = {}`: 
    #    Acts like a memo note or notebook. Stores the last seen index of each 
    #    character in the format `{character: last_seen_index}`.
    #
    # 2. `left = 0` & `right`: 
    #    `right` expands the right boundary of our window in every iteration.
    #    `left` is the starting boundary of our valid (non-repeating) window.
    #
    # 3. `if char in char_map and char_map[char] >= left`:
    #    Checks if the current character was seen before AND is INSIDE our current window.
    #
    #    --> WHAT HAPPENS ON CONSECUTIVE DUPLICATES (e.g., s = "abcc")?
    #        When we reach the second 'c' at index 3:
    #        1. We detect that 'c' was already seen at index 2.
    #        2. We instantly jump `left` past the old 'c': `left = 2 + 1 = 3`.
    #        3. The window shrinks to just the new 'c' (`"c"`), resetting the window.
    #
    # 4. `left = char_map[char] + 1`:
    #    Moves the left boundary right after the duplicate character's old position 
    #    to kick the duplicate out of our active window.
    #
    # 5. `right - left + 1`:
    #    Calculates the current width/length of our active valid window.
    # -------------------------------------------------------------------------
    
    char_map = {}  # {character: last_seen_index}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        # If the character is a duplicate and falls inside the current window
        if char in char_map and char_map[char] >= left:
            # Move `left` boundary right after the previous occurrence
            left = char_map[char] + 1
        
        # Record/update the character's last seen index
        char_map[char] = right
        
        # Calculate current window size and update the maximum length found so far
        max_length = max(max_length, right - left + 1)

    return max_length


# =====================================================================
# TEST CASES / EDGE CASES
# =====================================================================
if __name__ == "__main__":
    print("--- Testing Longest Substring Solution ---")

    # Test 1: Standard Case ("abcabcbb" -> "abc" length 3)
    assert length_of_longest_substring("abcabcbb") == 3
    print("✓ Test 1 Passed (Standard Case)")

    # Test 2: Consecutive Duplicates ("abcc" -> "abc" length 3)
    assert length_of_longest_substring("abcc") == 3
    print("✓ Test 2 Passed (Consecutive Duplicates)")

    # Test 3: All Same Characters ("bbbbb" -> "b" length 1)
    assert length_of_longest_substring("bbbbb") == 1
    print("✓ Test 3 Passed (All Same Characters)")

    # Test 4: Subsequence in middle ("pwwkew" -> "wke" length 3)
    assert length_of_longest_substring("pwwkew") == 3
    print("✓ Test 4 Passed (Overlapping Characters)")

    # Test 5: Empty String ("" -> 0)
    assert length_of_longest_substring("") == 0
    print("✓ Test 5 Passed (Empty String)")

    print("\nAll test cases passed successfully!")
