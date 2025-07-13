import os

def start_local_shell():
    os.system("python main.py")

def start_container():
    os.system("docker run -it --rm -p 9222:9222 --name nimbus-browser nimbus-chrome")

if __name__ == "__main__":
    print("Nimbus Launcher")
    print("1. Local Shell")
    print("2. Cloud Container")

    choice = input("Choose mode: ")

    if choice == "1":
        start_local_shell()
    elif choice == "2":
        start_container()
    else:
        print("Invalid choice.")
