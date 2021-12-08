def count_lanternfish(lanternfish_list):
    for i in range(80):
        for j in range(len(lanternfish_list)):
            if lanternfish_list[j] == 0:
                lanternfish_list[j] = 6
                lanternfish_list.append(8)
            else:
                lanternfish_list[j] -= 1
    return len(lanternfish_list)

def read_inputs(file_name):
    with open(file_name, "r") as input_file:
        return [int(f) for f in input_file.read().split(",")]

def main():
    print(count_lanternfish(read_inputs("input.txt")))

if __name__ == "__main__":
    main()
