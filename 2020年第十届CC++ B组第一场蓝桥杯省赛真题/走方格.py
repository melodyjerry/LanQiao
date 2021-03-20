n,m=map(int,input().split())
##设 dp[i][j] 这个二维数组的意思为
##第 i 行 第 j 列 的格子 有n种方案
##那么,显而易见的是 如果要走到那个格子,他只能从左或者上走到
##所以走到那个格子的走法是他们的和
##即
##dp[i][j]=dp[i-1][j]+dp[i][j-1]
##但是注意到 第0行和第0列有且仅有一种走法,那么全部设置为1

dp=[[1 for col in range(m)] for row in range(n)]
print(dp)
def nextstep(i,j):
    #终止条件
    if i==n or j==m:
        return
    else:
        #判断
        print(i,j)
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
        nextstep(i+(1 if i!=n else 0),j)
        nextstep(i,j+(1 if j!=m else 0))
nextstep(1,1)
for i in range(n):
    print(*dp[i])
