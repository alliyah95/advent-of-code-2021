from binary_diagnostic_part_1 import *

def calculate(report, r_type):
    ctr = [0,0]
    for i in range(len(report[0])-1):
        for r in report:
            ctr[int(r[i])]+=1
        report = filter_reports(report, i, ctr, r_type)
        if len(report) == 1:
            return report[0]
        ctr = [0,0]

def filter_reports(report, ind, ctr, r_type):
    val = {"ogr":"1", "csr":"0"}
    if equally_common(ctr):
        return [r for r in report if r[ind] == val[r_type]]
    compare = str(ctr.index(max(ctr))) if r_type == "ogr" else str(ctr.index(min(ctr)))
    return [r for r in report if r[ind] == compare]

def equally_common(ctr):
    return all(n==ctr[0] for n in ctr)

def main():
    report = read_inputs("input.txt")
    ogr = int(calculate(report, "ogr"), 2)
    csr = int(calculate(report, "csr"), 2)
    print(ogr * csr)

main()
