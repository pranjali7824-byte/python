import time
import datetime
import os

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(f"Current time: {current_time}", end="\r")

        if current_time == alarm_time:
            print("\n⏰ Wake up! Alarm ringing!")

            # Sound (works on Windows)
            for _ in range(5):
                print('\a')  # beep sound
                time.sleep(1)

            break

        time.sleep(1)


def main():
    alarm_time = input("Enter alarm time (HH:MM): ")
    set_alarm(alarm_time)


if __name__ == "__main__":
    main()
