# 给出一个区间的集合，请合并所有重叠的区间。 
# 
#  
# 
#  示例 1: 
# 
#  输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2: 
# 
#  输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。 
# 
#  
# 
#  提示： 
# 
#  
#  intervals[i][0] <= intervals[i][1] 
#  
#  Related Topics 排序 数组 
#  👍 724 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        result = []
        # 先排序,降低复杂度
        intervals = sorted(intervals, key=lambda x: x[0])
        # 左边界
        left = intervals[0][0]
        # 右边界
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if right >= intervals[i][0]:
                right = max(right, intervals[i][1])
            else:
                result.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
        result.append([left, right])
        return result
# leetcode submit region end(Prohibit modification and deletion)
