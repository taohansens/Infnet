def reverse(file):
    textfile = open(file, "r", encoding="utf-8")
    lines = textfile.readlines()
    for line in reversed(lines):
        print(line[::-1])


def main():
    filename = "q04.txt"
    reverse(filename)


if __name__ == "__main__":
    main()