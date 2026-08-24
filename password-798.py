def move(
    password: str,
    x: int,
    y: int,
) -> tuple[int, int]:
    if password == "up":
        y += 1
    elif password == "down":
        y -= 1
    elif password == "left":
        x -= 1
    elif password == "right":
        x += 1
    else:
        print(f"Unknown command: {password}")

    return x, y


def main() -> None:
    x = 0
    y = 0

    print("Commands: up, down, left, right, status, quit")

    while True:
        password = input("Keyboard command: ").strip().lower()

        if password == "quit":
            print("Exit")
            break

        if password == "status":
            print(f"Position: ({x}, {y})")
            continue

        x, y = move(password, x, y)
        print(f"Position: ({x}, {y})")


if __name__ == "__main__":
    main()
