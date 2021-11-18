import random
import copy


class Game:
    def __init__(self):
        self.board = [
            ["o", "x", "o"],
            ["o", "x", "o"],
            ["x", "", ""]]

    def computerSelect(self,nboard):
        randomList = self.open_tiles(nboard)
        computerDecision = random.randrange(len(randomList))
        updateRow = computerDecision // 3
        updateCol = computerDecision % 3
        nboard[updateRow][updateCol] = 'o'

    def isTerminal(self, nboard):
        return self.open_tiles(nboard) == []

    def putTitle(self, position, nboard, player):
        temp_board = copy.deepcopy(nboard)
        updateRow = position // 3
        updateCol = position % 3
        temp_board[updateRow][updateCol] = player
        return copy.deepcopy(temp_board)

    def state(self, nboard, player):
        flag = False
        print("in the state", nboard, player)
        print((nboard[0][1] == nboard[1][1] == nboard[2][1]))
        for i in range(len(nboard)):
            for j in range(len(nboard[0])):
                if nboard[i][j] == '':
                    flag = True
        one = nboard[0][0]
        two = nboard[0][1]
        three = nboard[0][2]
        four = nboard[1][0]
        five = nboard[1][1]
        six = nboard[1][2]
        seven = nboard[2][0]
        eight = nboard[2][1]
        nine = nboard[2][2]
        if (one == two == three) or (four == five == six) or (seven == eight == nine) or \
                (one == four == seven) or (two == five == eight) or (three == six == nine) or \
                (one == five == nine) or (three == five == seven):
            print("------")
            if player == 'o':
                return -10
            else:
                print("-------1")
                return 10
        elif flag:
            print("-------------1")
            return 1
        else:
            return 0
    def setTitle(self, position, nboard):
        temp_board = copy.deepcopy(nboard)
        updateRow = position // 3
        updateCol = position % 3
        temp_board[updateRow][updateCol] = ''
        return copy.deepcopy(temp_board)

    def open_tiles(self, nboard):
        openTitlesList = []
        for i in range(0, 3):
            for j in range(0, 3):
                if nboard[i][j] == '':
                    openTitlesList.append(i * 3 + j)
        return openTitlesList

    # def backtracking(self, board):
    #     list = []
    #     for i in range (len(board)):
    #         for j in range (len(board[0])):
    #             if board[i][j] == '':
    #                 path = []
    #                 gird = copy.deepcopy(board)
    #                 list.append(self.dfs(gird, i, j, path, 'x'))
    #     return list
    #
    #
    # def dfs(self, grid, i , j, path, player):
    #     if self.isTerminal(grid):
    #         return path
    #     reward = self.state(grid, player)
    #     if reward == -10 or reward == 10:
    #         path.append(grid, reward)
    #         return path
    #
    #     if player == 'x':
    #         player = 'o'
    #     else:
    #         player = 'x'
    #     temp_grid = copy.deepcopy(grid)
    #     for n in self.open_tiles(grid):
    #
    def AiPath(self, newboard):
        gird = copy.deepcopy(newboard)
        allThePath = []

        def backtrack(grid, path, player, n):
            print("start-------", n, grid)
            if self.isTerminal(grid):
                # print(path)
                path.append([grid, 0])
                allThePath.append(path)
                return
            reward = self.state(grid, player)
            print("get reward: ---", reward)
            if reward == -10 or reward == 10:
                # print(path)
                path.append([grid, reward])
                allThePath.append(path)
                return
            if player == 'x':
                player = 'o'
            else:
                player = 'x'
            # print(self.open_tiles(grid))
            print("starting play")
            size = self.open_tiles(grid)
            for n in size:
                # print(n)
                nextStepGrid = self.putTitle(n, grid, player)
                reward = self.state(nextStepGrid, player)
                path.append([nextStepGrid, reward])
                backtrack(nextStepGrid, path, player, n + 1)
                grid = self.setTitle(n, nextStepGrid)
                path.pop()

        backtrack(gird, [], 'o', 0)
        return allThePath

    def play(self):
        nboard = copy.deepcopy(self.board)
        self.computerSelect(nboard)
        return nboard


if __name__ == '__main__':
    GameRunner = Game()
    board = GameRunner.play()
    print("starting board:", board)
    board = GameRunner.AiPath(board)

    print(board)
    # print("-----------------")
    # for k in board:
    #     print("-----------")
    #     print(k[0])
    #     print(k[1])
    #     print("------------")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
