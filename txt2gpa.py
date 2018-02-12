import sys

def main(argv):
    if len(argv) == 0:
        print "Usage: txt2gpa.py <supplement.txt>"
        sys.exit(2)
    filename = argv[0]
    with open(filename, 'r') as input:
        lines = input.readlines()
        marks = 0
        total = 0
        for line in lines:
            if "End of the list" in line:
                break
            word = line.strip()
            if word == 'excellent':
                marks += 1
                total += 5
            if word == 'good':
                marks += 1
                total += 4
            if word == 'satisfactory':
                marks += 1
                total += 3
        subjs = len(lines) / 4
        gpa = total * 1.0 / marks
        print "File %s: total subjs: %d, total marks: %d, GPA: %f" % (filename, subjs, marks, gpa)
        # print gpa

if __name__ == "__main__":
   main(sys.argv[1:])