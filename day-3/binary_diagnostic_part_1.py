def read_inputs(file_name):
    input_file = open(file_name, "r")
    diagnostic_report = [r for r in input_file]
    return diagnostic_report

def calculate(report):
    data = {0:[0,0], 1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 
    6:[0,0], 7:[0,0], 8:[0,0], 9:[0,0], 10:[0,0], 11:[0,0]}

    for r in report:
        for i in range(len(r)-1):
            data[i][int(r[i])]+=1

    gamma_bin = "".join("0" if data[d][0] > data[d][1] else "1" for d in data)
    epsilon_bin = "".join("0" if data[d][0] < data[d][1] else "1" for d in data)
    return [gamma_bin, epsilon_bin]

def main():
    report = read_inputs("input.txt")
    data = [int(b, 2) for b in calculate(report)]
    print(data[0] * data[1])
    
main()
