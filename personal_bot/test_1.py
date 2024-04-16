import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.refresh()

    # Get screen dimensions
    screen_height, screen_width = stdscr.getmaxyx()

    # Calculate cell size based on screen width
    cell_width = screen_width // 5

    # Initialize cursor position
    cursor_x = 0

    # Draw the row of cells
    commands = ["Заповнити книгу", "Пошук за іменем", "Переглянути книгу", "Видалити запис", "Вийти"]
    for j, command in enumerate(commands):
        stdscr.addstr(0, j * cell_width, f'{command}', curses.A_REVERSE if j == cursor_x else curses.A_NORMAL)

    # Move cursor to the first cell
    stdscr.move(0, cursor_x * cell_width)

    while True:
        # Get user input
        key = stdscr.getch()

        # Handle arrow keys and Enter key
        if key == curses.KEY_LEFT and cursor_x > 0:
            cursor_x -= 1
        elif key == curses.KEY_RIGHT and cursor_x < 4:
            cursor_x += 1
        elif key in (curses.KEY_ENTER, ord('\n'), ord('\r')):  # Handle Enter key to select cell
            break
        elif key == ord('q'):  # Handle 'q' to quit
            cursor_x = -1
            break

        # Redraw the row with the new cursor position
        for j, command in enumerate(commands):
            stdscr.addstr(0, j * cell_width, f'{command}', curses.A_REVERSE if j == cursor_x else curses.A_NORMAL)

        # Move the cursor to the new position
        stdscr.move(0, cursor_x * cell_width)
        stdscr.refresh()

    # Print the selected cell or a message if 'q' was pressed
    # if cursor_x != -1:
    #     stdscr.addstr(2, 0, f"Ви обрали команду: {commands[cursor_x]}")
    # else:
    #     stdscr.addstr(2, 0, "Ви вийшли без вибору команди")
    #stdscr.getch()  # Wait for a key press before ending
    if cursor_x == 0:
        print("Заповнити книгу")
    if cursor_x == 1:
        print("Пошук за іменем")
    if cursor_x == 2:
        print("Переглянути книгу")
    if cursor_x == 3:
        print("Видалити запис")
    if cursor_x == 4:
        print("Вийти")

# Initialize curses and call main function
curses.wrapper(main)



