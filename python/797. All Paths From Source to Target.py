class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(graph,0,[],res)
        return res

    def dfs(self,graph, pos, temp, res):
        if pos==len(graph)-1:
            temp+=[pos]
            res.append(temp)
            return
        for i in graph[pos]:
            self.dfs(graph,i,temp+[pos],res)
if __name__ == '__main__':
    a=Solution()
    print(a.allPathsSourceTarget([[1,2], [3], [3], []] ))
