from sonar_sweep_part_1 import *

def main():
    reports = read_inputs("input.txt")
    ctr = 0
    previous = 0

    for i in range(len(reports)):
        total = sum(reports[i:i+3])
        if total > previous and i != 0:
            ctr+=1
        previous = total
    print(ctr)

main()
