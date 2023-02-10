# (0,0) 90,40
# (60,-),(-,60)
# from icecream import ic


# 两个杯子现在有多少水，两个杯子的容量
def successors(x, y, X, Y):
    """
    这里面存放的是可以走的下一步是啥
    """
    return {
        (x, 0): '倒空y',
        (0, y): '倒空x',
        (x + y - Y, Y) if x + y >= Y else (0, x + y): 'x倒入y中',
        (X, x + y - X) if y + x >= X else (x + y, 0): 'y倒入x中',
        (X, y): '装满x',
        (x, Y): '装满y'

    }


if __name__ == '__main__':
    # 定义容量
    capacity1, capacity2 = 90, 40
    # 定义初始化
    paths = [[('init', (0, 0))]]
    goal = 60
    # 防止陷入死循环
    explored = set()
    while paths:
        path = paths.pop(0)
        frontier = path[-1]
        (x, y) = frontier[-1]
        for state, action in successors(x, y, capacity1, capacity2).items():
            # ic(frontier, state, action)
            print(frontier, state, action)
            new_path = path + [(action, state)]

            if goal in state:
                print("************************************************************************")
                print(new_path)
                exit()
            else:
                paths.append(new_path)

            explored.add(state)

    print(explored)
