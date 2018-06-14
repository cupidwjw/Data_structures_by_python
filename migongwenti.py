# -*- coding:utf-8 -*-
#迷宫问题抽象为矩阵问题，python中用二维数组表示
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,1,0,0,0,1,0,0,0,1],
    [1,0,1,0,0,0,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,1,1,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,0,0,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,0,0,1,1,1,0,1,0,1,1,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,0,0,1],
    [1,0,1,0,1,0,1,0,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
#入口
pos = (1,1)
#出口
end = (10,12)

#中心点，加上4个元素，即可得到上下左右4个点
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

#定义一个标记函数，到过的点都标记为2
def mark(maze,pos):                  #给迷宫maze的pos位置标记为2，表示到过了
    maze[pos[0]][pos[1]] = 2
#定义一个测试是否可以尝试的位置，如果为真，则去尝试；假就不去尝试了
def passable(maze,pos):
    # print 'pos:',pos
    return maze[pos[0]][pos[1]] == 0


path_list = []
#递归方式求解
def find_path(maze,pos,end):
    #标记pos点
    mark(maze,pos)                 #标记该位置已到达
    print '%s已到达' %(pos,)
    #判断pos和end是否相等
    if pos == end:                 #如果是出口，返回true
        # print(pos, end=" ")        #返回这个位置
        #相等返回true
        return True
    #如果不等，则继续向下运行
    for i in range(4):
        #下一个节点的位置
        nextp = pos[0]+dirs[i][0],pos[1]+dirs[i][1]
        # print nextp
        #考虑下一个可能方向

        #判断这个点是否可测试
        if passable(maze,nextp):
            #如果可测试，则进行find_path操作，自己调用自己，参数为maze，nextp，end
            #如果能找到，则打印pos
            if find_path(maze,nextp,end):
                print 'path:',pos #为true时候经过的pos；函数内可以访问但不可以修改函数外的变量
                path_list.append(pos)
                return True
    return False
print find_path(maze,pos,end)
path_list.reverse()
print path_list
