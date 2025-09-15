# 🐍 LeetCode-Python

Welcome to **LeetCode-Python**!  
This repository contains my **daily solutions** to LeetCode problems, solved in **Python**.  

## 📌 Why This Repo?
- To build a **habit of daily problem-solving**.  
- To strengthen **data structures & algorithms**.  
- To prepare for **coding interviews** at top tech companies.  
- To track personal growth and share solutions with the community.  

## 🚀 Why Python?
- **Readable & concise** → focus more on logic than syntax.  
- **Huge standard library** → quick utilities for math, strings, etc.  
- **Widely used in interviews** → most companies accept Python solutions.  

## 🔥 Daily Motivation
> *“Small progress every day adds up to big results.”*  
Coding daily isn’t just about solving problems — it’s about training your mind to think logically, consistently, and confidently.  

## 🏗️ Repository Structure
leetcode-python/
│── Easy/
│── Medium/
│── Hard/
│── README.md

Each folder will have solutions with clean code and comments.  

## ✨ Example
```python
# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
