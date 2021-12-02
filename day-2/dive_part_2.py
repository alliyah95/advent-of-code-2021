from dive_part_1 import *

def main():
    plan = read_inputs("input.txt")
    h_pos = 0
    depth = 0
    aim = 0

    for p in plan:
        x_val = int([c for c in p if c.isdigit()][0])

        if "forward" in p:
            h_pos+=x_val
            depth+=(aim * x_val)
        elif "down" in p:
            aim+=x_val
        else:
            aim-=x_val
    
    print(h_pos * depth)

main()
