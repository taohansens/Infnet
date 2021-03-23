import subprocess


def open_notepad(file_name):
    program_name = "notepad.exe"
    subprocess.Popen([program_name, file_name])


def main():
    file = input("Digite o nome do arquivo .txt: ")
    open_notepad(file)


if __name__ == "__main__":
    main()
