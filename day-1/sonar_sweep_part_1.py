def read_inputs(file_name):
    input_file = open(file_name,"r")
    nums = [int(line) for line in input_file]
    return nums

def main():
    reports = read_inputs("input.txt")
    ctr = 0
    previous = reports[0]
    for i in range(len(reports)):
        if reports[i] > previous:
            ctr+=1
        previous = reports[i]
    print(ctr)

if __name__ == "__main__":
    main()
