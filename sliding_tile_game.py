
class Board:
    size = 5

    def __init__(self, position, grid):
        assert len(grid) == Board.size
        assert len(grid[0]) == Board.size
        assert 0 <= position[0] < Board.size
        assert 0 <= position[1] < Board.size

        self.pos = position
        self.grid = grid

    def __str__(self):
     out = f'Position: {self.pos}\n'

     for row in self.grid:
        tiles = []
        for tile in row:
            if tile == 0:
                tiles.append('\033[91m' + f'{tile:3}' + '\033[0m')
            else:
                tiles.append(f'{tile:3}')

        out += ' '.join(tiles) + '\n'

     return out

    def clone(self):
        cPos = self.pos[0], self.pos[1]
        cGrid = [[self.grid[i][j] for j in range(self.size)]
                 for i in range(self.size)]
        return Board(cPos, cGrid)

    def __eq__(self, other):
        if self.pos != other.pos:
            return False

        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] != other.grid[i][j]:
                    return False
        return True

    def moveUp(self):
        i, j = self.pos
        if i >= 1:
            st = self.clone()
            st.grid[i][j], st.grid[i-1][j] = (
                st.grid[i-1][j], st.grid[i][j])
            st.pos = (i-1, j)
            return st
        return None

    def moveDown(self):
        i, j = self.pos
        if i + 1 < self.size:
            st = self.clone()
            st.grid[i][j], st.grid[i+1][j] = (
                st.grid[i+1][j], st.grid[i][j])
            st.pos = (i+1, j)
            return st
        return None

    def moveRight(self):
        i, j = self.pos
        if j + 1 < self.size:
            st = self.clone()
            st.grid[i][j], st.grid[i][j+1] = (
                st.grid[i][j+1], st.grid[i][j])
            st.pos = (i, j+1)
            return st
        return None

    def moveLeft(self):
        i, j = self.pos
        if j >= 1:
            st = self.clone()
            st.grid[i][j], st.grid[i][j-1] = (
                st.grid[i][j-1], st.grid[i][j])
            st.pos = (i, j-1)
            return st
        return None

    def moves(self):
        i, j = self.pos

        if i + 1 < self.size:
            yield self.moveDown()

        if i >= 1:
            yield self.moveUp()

        if j + 1 < self.size:
            yield self.moveRight()

        if j >= 1:
            yield self.moveLeft()

    def tPos(self, tile):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == tile:
                    return (i, j)
        return None

    def mDist(self, other):
        result = 0
        for t in range(1, self.size**2):
            p1 = self.tPos(t)
            p2 = other.tPos(t)
            if p1 is not None and p2 is not None:
                result += abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        return result



def tester():
    grid = [
        [14, 3, 21, 8, 1],
        [19, 6, 12, 24, 4],
        [10, 17, 2, 15, 0],
        [23, 9, 5, 18, 13],
        [7, 22, 11, 16, 20]
    ]

    st = Board((2, 4), grid)

    print("Original board:")
    print(st)

    print("Possible next states:")
    for next_state in st.moves():
        print(next_state)
        print("Manhattan distance:", next_state.mDist(st))


if __name__ == '__main__':
    tester()
