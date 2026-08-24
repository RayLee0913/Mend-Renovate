def move(
    keyboard: str,
    x: int,
    y: int,
) -> tuple[int, int]:
    if keyboard == "up":
        y += 1
    elif keyboard == "down":
        y -= 1
    elif keyboard == "left":
        x -= 1
    elif keyboard == "right":
        x += 1
    else:
        print(f"Unknown keyboard input: {keyboard}")

    return x, y


def main() -> None:
    x = 0
    y = 0

    print("Keyboard controls: up, down, left, right, status, quit")

    while True:
        keyboard = input("Keyboard input: ").strip().lower()

        if keyboard == "quit":
            print("Exit")
            break

        if keyboard == "status":
            print(f"Position: ({x}, {y})")
            continue

        x, y = move(keyboard, x, y)
        print(f"Position: ({x}, {y})")


if __name__ == "__main__":
    main()
