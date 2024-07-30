# Three Sum

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.


## Examples:
|Input|OUtput|Explanation|
------|------|-----------|
`nums = [-1,0,1,2,-1,-4]`|`[[-1,-1,2],[-1,0,1]]`|nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.<br>nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.<br>nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.<br>The distinct triplets are [-1,0,1] and [-1,-1,2].<br>Notice that the order of the output and the order of the triplets does not matter.|
`nums = [0,1,1]`|`[]`|`The only possible triplet does not sum up to 0.`|
 nums = `[0,0,0]`|`[[0,0,0]]`|`The only possible triplet sums up to 0.`

## Difficulty:

`medium`

## Learning Objectives:

+ Array
+ Two Pointers
+ Sorting



## Link:

[problem on leetcode](https://leetcode.com/problems/3sum/)
