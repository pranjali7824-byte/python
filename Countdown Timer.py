import time

def countdown(t):
    while t:
        minutes, seconds = divmod(t, 60)
        timer = f"{minutes:02d}:{seconds:02d}"
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("\n⏰ Time's up!")

    # Optional beep (works on some systems)
    print('\a')


def main():
    print("⏳ Countdown Timer")

    try:
        seconds = int(input("Enter time in seconds: "))
        countdown(seconds)
    except:
        print("❌ Please enter a valid number!")


if __name__ == "__main__":
    main()
