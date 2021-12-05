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
                    if has_winning_row(boards[x][y]) or has_winning_column(boards[x]):
                        compute_final_score(boards[x], n)
                                 
def has_winning_row(row):
    return all("T" in r for r in row)

def has_winning_column(board):
    col_num = 0
    col = []
    for i in range(len(board)):
        for b in board:
            col.append(b[i])
        if len(col) == len(board):
            if all("T" in c for c in col):
                return True
            else:
                col = []
                col_num+=1
    return False

def compute_final_score(winning_board, winning_num):
    total = 0
    for row in winning_board:
        for r in row:
            if "T" not in r:
                total+=int(r)
    print(total*int(winning_num))
    exit()

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

if __name__ == "__main__":    
    main()
