# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 
# 
#  
# 
#  示例： 
# 
#  s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
#  
# 
#  
# 
#  提示：你可以假定该字符串只包含小写字母。 
#  Related Topics 哈希表 字符串 
#  👍 291 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        data = [0] * 26
        for i in s:
            data[ord(i) - 97] += 1
        for i in s:
            if data[ord(i) - 97] == 1:
                return s.index(i)
        return -1


# leetcode submit region end(Prohibit modification and deletion)
"""
遍历两次

第一次遍历字符串，统计所有字母出现的个数
第二次遍历字符串，取出第一个总数为1的字母，然后返回下标
或者也可以遍历统计数组，获得到下标最小的总数为1的字符返回
"""
