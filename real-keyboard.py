import keyboard


def main() -> None:
    x = 0
    y = 0

    print("Use arrow keys to move. Press Esc to exit.")

    while True:
        event = keyboard.read_event()

        if event.event_type != keyboard.KEY_DOWN:
            continue

        if event.name == "up":
            y += 1
        elif event.name == "down":
            y -= 1
        elif event.name == "left":
            x -= 1
        elif event.name == "right":
            x += 1
        elif event.name == "esc":
            break
        else:
            continue

        print(f"Position: ({x}, {y})")


if __name__ == "__main__":
    main()
