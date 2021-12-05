from giant_squid_part_1 import *

def bingo(nums, boards):
    winning_boards = []
    for n in nums:
        for x in range(len(boards)):
            for y in range(len(boards[x])):
                for z in range(len(boards[x][y])):
                    if boards[x][y][z] == n:
                        boards[x][y][z]+="T"
                    if has_winning_row(boards[x][y]) or has_winning_column(boards[x]):
                        winning_boards.append([boards[x], n])
                        boards[x] = [['*' for _ in range(5)] for _ in range(5)]

    compute_final_score(winning_boards[-1][0], winning_boards[-1][-1])

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
