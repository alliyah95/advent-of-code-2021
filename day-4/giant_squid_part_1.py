def read_file(file_name):
    input_file = open(file_name, "r")
    return input_file.read().split("\n")


def bingo(nums, boards):
    for n in nums:
        for x in range(len(boards)):
            for y in range(len(boards[x])):
                for z in range(len(boards[x][y])):
                    if boards[x][y][z] == n:
                        boards[x][y][z]+="T"
                    if winning_row(boards[x][y]):
                        pass
                    elif winning_column(boards[x]):
                        pass
                                 

def winning_row(row):
    return all("T" in b for b in row)

def winning_column(board):
    col = []
    for i in range(len(board)):
        for j in range(board[i]):


def main():
    puzzle = read_file("input.txt")
    nums = puzzle[0].split(",")
    boards = []
    indiv_boards = []

    for p in puzzle[1:]:
        if p == "":
            continue
        indiv_boards.append(p.split())
        if len(indiv_boards) == 5:
            boards.append(indiv_boards)
            indiv_boards = []
    
    bingo(nums, boards)
    
main()