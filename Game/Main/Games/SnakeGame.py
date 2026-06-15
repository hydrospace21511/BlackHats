import curses
import random


def snake_game():
    death = False

    def main(stdscr):
        nonlocal death
                            #corbrinha
        curses.curs_set(0)
        stdscr.nodelay(True)
        stdscr.timeout(100)

        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_GREEN, -1)

        color = curses.color_pair(1)

        size, leng = 20, 40

        snake = [
            [size // 2, leng // 2],
            [size // 2, leng // 2 - 1],
            [size // 2, leng // 2 - 2]
        ]

        direction = curses.KEY_RIGHT

        food = [
            random.randint(1, size - 2),
            random.randint(1, leng - 2)
        ]

        while True:
            stdscr.clear()

            for x in range(leng):
                stdscr.addch(0, x, "═", color)
                stdscr.addch(size - 1, x, "═", color)

            for y in range(size):
                stdscr.addch(y, 0, "║", color)
                stdscr.addch(y, leng - 1, "║", color)

            stdscr.addch(0, 0, "╔", color)
            stdscr.addch(0, leng - 1, "╗", color)
            stdscr.addch(size - 1, 0, "╚", color)
            stdscr.addch(size - 1, leng - 1, "╝", color)

            stdscr.addch(food[0], food[1], "*", color)

            for segment in snake:
                stdscr.addch(segment[0], segment[1], "O", color)

            key = stdscr.getch()

            if key == curses.KEY_UP and direction != curses.KEY_DOWN:
                direction = curses.KEY_UP
            elif key == curses.KEY_DOWN and direction != curses.KEY_UP:
                direction = curses.KEY_DOWN
            elif key == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
                direction = curses.KEY_LEFT
            elif key == curses.KEY_RIGHT and direction != curses.KEY_LEFT:
                direction = curses.KEY_RIGHT

            head = snake[0][:]

            if direction == curses.KEY_UP:
                head[0] -= 1
            elif direction == curses.KEY_DOWN:
                head[0] += 1
            elif direction == curses.KEY_LEFT:
                head[1] -= 1
            elif direction == curses.KEY_RIGHT:
                head[1] += 1

            if (
                head[0] in (0, size - 1)
                or head[1] in (0, leng - 1)
                or head in snake
            ):
                death = True
                break

            snake.insert(0, head)

            if head == food:
                while True:
                    new = [
                        random.randint(1, size - 2),
                        random.randint(1, leng - 2)
                    ]
                    if new not in snake:
                        food = new
                        break
            else:
                snake.pop()

            stdscr.refresh()

    curses.wrapper(main)
    return death


if __name__ == "__main__":
    death = snake_game()
    