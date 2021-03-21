
class Pos(object):
    def __init__(self, x, y, path):
        self.x = x
        self.y = y
        self.path = path

    def __str__(self):
        return self.path


def up(node):
    return Pos(node.x - 1, node.y, node.path + 'U')


def down(node):
    return Pos(node.x + 1, node.y, node.path + 'D')


def left(node):
    return Pos(node.x, node.y - 1, node.path + 'L')


def right(node):
    return Pos(node.x, node.y + 1, node.path + 'R')


if __name__ == '__main__':
    m = 0 # 列
    n = 0 # 行
    visited = set() #记录来过的地方
    map_int = [] # 地图数组
    queen = [] # 队列
    with open('./maze', mode='r', encoding='utf-8') as fp:
        #读取数据
        data = fp.readlines()
        for line in data:
            map_int.append(list(line.strip()))
        m = len(map_int)
        n = len(map_int[0])
        # 新建一个结点 坐标0,0 起始位置 此时 path=''
        pos = Pos(0, 0, '')
        # 此时的queen 装入 起点
        queen.append(pos)
        # 当 还有路可走
        while len(queen) != 0:
            # 当前移动的结点
            move_node = queen[0]
            # 这条路出队 开始尝试这条路的走法
            queen.pop(0)
            # 当前坐标表示为 
            move_str = (move_node.x,move_node.y)
            print(move_node)
            for q,i in enumerate(queen):
                print(q,i)
            #如果这地方没有来过
            if move_str not in visited:
                #加入集合 代表来过
                visited.add(move_str)
                #如果 达到了终点直接退出
                if move_node.x == m - 1 and move_node.y == n - 1:
                    print(move_node)
                    print(len(move_node.__str__()))
                    break
                # 如果 可以向下走 并且不在最下面
                if move_node.x < m - 1 and map_int[move_node.x + 1][move_node.y] == '0':
                    queen.append(down(move_node))
                # 如果可以向左走 并且不在最左边
                if move_node.y > 0 and map_int[move_node.x][move_node.y - 1] == '0':
                    queen.append(left(move_node))
                        # 如果可以向右走 并且不在最右边
                if move_node.y < n - 1 and map_int[move_node.x][move_node.y + 1] == '0':
                    queen.append(right(move_node))
                        # 如果可以向上走 并且不在最上边
                if move_node.x > 0 and map_int[move_node.x - 1][move_node.y] == '0':
                    queen.append(up(move_node))
        
