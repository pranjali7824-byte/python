import time

def stopwatch():
    input("Press ENTER to START the stopwatch...")
    
    start_time = time.time()
    elapsed = 0
    running = True

    print("⏱️ Stopwatch started! Press ENTER to STOP...\n")

    while running:
        try:
            if input() == "":
                running = False
        except:
            pass

        elapsed = time.time() - start_time
        print(f"Time: {elapsed:.2f} sec", end="\r")

    print("\n⏹️ Stopped!")
    print(f"Total Time: {elapsed:.2f} seconds")


def main():
    while True:
        print("\n--- STOPWATCH ---")
        print("1. Start")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            stopwatch()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
