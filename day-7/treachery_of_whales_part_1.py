def determine_least_fuel(h_positions):
    least = 9999999999
    total_fuel = 0

    for pos in h_positions:
        for pos2 in h_positions:
            total_fuel += abs(pos-pos2)
        if total_fuel < least:
            least = total_fuel
        total_fuel = 0
    return least

def read_inputs(file_name):
    with open(file_name, "r") as input_file:
        return [int(f) for f in input_file.read().split(",")]

def main():
    print(determine_least_fuel(read_inputs("input.txt")))

if __name__ == "__main__":
    main()
