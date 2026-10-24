            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        return quantity


def build_portfolio():
    """Collect holdings; repeated stock symbols are combined."""
    portfolio = {}

    while True:
        symbol = get_stock_symbol()
        if symbol is None:
            break

        quantity = get_positive_quantity(symbol)
        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.")

    return portfolio


def build_summary(portfolio):
    """Return a formatted summary and the calculated total value."""
    lines = [
        f"{'Stock':<10}{'Quantity':>10}{'Price (USD)':>16}{'Value (USD)':>16}",
        "-" * 52,
    ]
    total = 0.0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        lines.append(
            f"{symbol:<10}{quantity:>10,}${price:>15,.2f}${value:>15,.2f}"
        )

    lines.extend([
        "-" * 52,
        f"{'Total investment:':<26}${total:,.2f} {CURRENCY}",
    ])

    return "\n".join(lines), total


def ask_yes_no(prompt):
    """Return True for yes and False for no; reprompt on invalid input."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter y/yes or n/no.")


def save_summary(summary_text):
    """Save the current summary, replacing any previous summary."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with OUTPUT_FILE.open("w", encoding="utf-8") as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write(f"Generated on: {timestamp}\n")
            file.write(f"Currency: {CURRENCY}\n\n")
            file.write(summary_text)
            file.write("\n")
    except OSError as error:
        print(f"Could not save the summary: {error}")
        return False

    print(f"Summary saved to '{OUTPUT_FILE.resolve()}'.")
    return True


def main():
    """Run the stock portfolio tracker."""
    print("=" * 36)
    print("STOCK PORTFOLIO TRACKER")
    print("=" * 36)
    print("Sample prices only — not live market data.")

    show_available_stocks()
    portfolio = build_portfolio()

    if not portfolio:
        print("\nNo stocks were entered. Nothing to summarize.")
        return

    summary_text, total = build_summary(portfolio)

    print("\nYOUR PORTFOLIO")
    print(summary_text)
    print(f"\nNumber of distinct stocks: {len(portfolio)}")
    print(f"Total investment value: ${total:,.2f} {CURRENCY}")

    if ask_yes_no("\nSave this summary to a text file? (y/n): "):
        save_summary(summary_text)

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram closed. Goodbye!")
