"""
    给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
    两个相邻元素间的距离为 1 。


    示例 1：
        输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
        输出：[[0,0,0],[0,1,0],[0,0,0]]

    示例 2：
        输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
        输出：[[0,0,0],[0,1,0],[1,2,1]]
"""

from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        pass

print(Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))