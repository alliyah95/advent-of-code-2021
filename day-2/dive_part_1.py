def read_inputs(file_name):
    input_file = open(file_name, "r")
    plan = [p for p in input_file]
    return plan

def main():
    plan = read_inputs("input.txt")
    h_pos = 0
    depth = 0

    for p in plan:
        x_val = int([c for c in p if c.isdigit()][0])

        if "forward" in p:
            h_pos+=x_val
        elif "down" in p:
            depth+=x_val
        else:
            depth-=x_val
    
    print(h_pos * depth)

if __name__ == "__main__":
    main()
