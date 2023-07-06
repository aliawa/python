filename = "sample.txt"
with open(filename) as diary_file:
    n = 1
    for line in diary_file:
        print(n, line.rstrip("\n"))
        n += 1
