# Problem: 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Finds the length of the longest substring without repeating characters.

        :type s: str
        :rtype: int
        """
        # This dictionary stores the most recent index of each character encountered.
        # Format: {character: last_seen_index}
        char_map = {}
        
        # 'left' is the starting index of the current sliding window.
        left = 0
        
        # 'max_length' stores the maximum length found so far.
        max_length = 0

        # 'right' is the ending index of the current sliding window.
        # We iterate through the string, expanding the window to the right.
        for right, char in enumerate(s):
            # Check if the current character is already in our window.
            # We also check if its last seen index (char_map[char]) is
            # on or after the start of our current window ('left').
            if char in char_map and char_map[char] >= left:
                # If it is, we have a duplicate in the current window.
                # To fix this, we shrink the window by moving the 'left' pointer
                # to the position right after the previous occurrence of this character.
                left = char_map[char] + 1
            
            # Update the last seen index of the current character to its new position.
            char_map[char] = right
            
            # Calculate the length of the current valid window.
            current_length = right - left + 1
            
            # Update the overall maximum length if the current window is longer.
            max_length = max(max_length, current_length)
            
        return max_length
        