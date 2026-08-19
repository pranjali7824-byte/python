from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust if days or months are negative
    if days < 0:
        months -= 1
        days += 30  # approximate

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def main():
    print("🎂 Age Calculator")

    dob_input = input("Enter your DOB (YYYY-MM-DD): ")

    try:
        birth_date = datetime.strptime(dob_input, "%Y-%m-%d")
        years, months, days = calculate_age(birth_date)

        print(f"\nYou are {years} years, {months} months, and {days} days old.")

    except:
        print("❌ Invalid date format! Use YYYY-MM-DD.")


if __name__ == "__main__":
    main()
