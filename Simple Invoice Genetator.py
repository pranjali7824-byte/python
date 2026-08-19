def generate_invoice():
    print("🧾 SIMPLE INVOICE GENERATOR")

    items = []

    while True:
        name = input("\nEnter item name (or type 'done' to finish): ")
        if name.lower() == "done":
            break

        try:
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))
        except:
            print("❌ Invalid input! Try again.")
            continue

        total = qty * price
        items.append((name, qty, price, total))

    print("\n" + "="*40)
    print("            INVOICE")
    print("="*40)

    grand_total = 0

    for item in items:
        name, qty, price, total = item
        grand_total += total
        print(f"{name} | Qty: {qty} | ₹{price} | Total: ₹{total}")

    print("-"*40)
    print(f"💰 GRAND TOTAL: ₹{grand_total}")
    print("="*40)


def main():
    while True:
        generate_invoice()
        again = input("\nCreate another invoice? (y/n): ").lower()
        if again != "y":
            print("👋 Goodbye!")
            break


if __name__ == "__main__":
    main()
