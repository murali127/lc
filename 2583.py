import collections

class Solution(object):
    def kthLargestLevelSum(self, root, k):
        if not root:
            return -1
        
        queue = collections.deque([root])
        level_sums = []
        
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level_sums.append(level_sum)
        
        if len(level_sums) < k:
            return -1
        
        level_sums.sort(reverse=True)
        return level_sums[k - 1]
