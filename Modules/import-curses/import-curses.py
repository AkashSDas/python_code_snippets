# ###### import curses ######

# =================================
# Run each code block separately
# =================================
import time
import curses

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# stdscr.addstr(y, x, String)
stdscr.addstr(5, 5, "Hello")
stdscr.refresh() 
# Just implement all previous operations, update screen with latest update
time.sleep(3)

curses.echo()
curses.nocbreak()
stdscr.keypad(False)

curses.endwin()

def main(stdscr):
  curses.curs_set(0) # it stops blinking of cursor
  stdscr.addstr(5, 5, "Hello")
  stdscr.refresh()
  time.sleep(3)

curses.wrapper(main)
# =================================
import curses
import time

def main(stdscr):
  curses.curs_set(0)
  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)
               #   number is the identifier

  h, w = stdscr.getmaxyx()
  text = "Hello World"
  x = w//2 - len(text)//2
  y = h//2

  stdscr.attron(curses.color_pair(1))
  stdscr.addstr(y, x, text)
  stdscr.attroff(curses.color_pair(1))

  stdscr.refresh()
  time.sleep(3)


curses.wrapper(main)
# =================================
import time
import curses

def main(stdscr):
  curses.curs_set(0)

  while 1:
    key = stdscr.getch()

    stdscr.clear()

    if key == curses.KEY_UP:
      stdscr.addstr(0, 0, "you pressed up key")
    elif key == curses.KEY_DOWN:
      stdscr.addstr(0, 0, "you pressed down key")
    elif key == curses.KEY_ENTER or key in [10, 13]:
      stdscr.addstr(0, 0, "you pressed enter key")

    stdscr.refresh()

curses.wrapper(main)
# =================================
import time
import curses

menu = ['Home', 'Play', 'Scoreboard', 'Exit']

def print_menu(stdscr, selected_row_idx):
  stdscr.clear()

  h, w = stdscr.getmaxyx()

  for idx, row in enumerate(menu):
    x = w//2 - len(row)//2
    y = h//2 - len(menu)//2 + idx
    if idx == selected_row_idx:
      stdscr.attron(curses.color_pair(1))
      stdscr.addstr(y, x, row)
      stdscr.attroff(curses.color_pair(1))
    else:
      stdscr.addstr(y, x, row)

  stdscr.refresh()

def main(stdscr):
  curses.curs_set(0)
  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

  current_row_idx = 0

  print_menu(stdscr, current_row_idx)

  while 1:
    key = stdscr.getch()

    stdscr.clear()

    if key == curses.KEY_UP and current_row_idx > 0:
      current_row_idx -= 1
    elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
      current_row_idx += 1
    elif key == curses.KEY_ENTER or key in [10, 13]:
      stdscr.addstr(0, 0, f"You pressed {menu[current_row_idx]}")
      stdscr.refresh()
      stdscr.getch()
      if current_row_idx == len(menu) - 1:
        break

    print_menu(stdscr, current_row_idx)
    stdscr.refresh()

curses.wrapper(main)
# =================================
import curses
    
def main(stdscr):
  curses.curs_set(0)
  curses.mousemask(1) # detects mouse click

  key = stdscr.getch()

  if key == curses.KEY_MOUSE:

    #click = curses.getmouse()
    #stdscr.addstr(0, 0, str(click))
    #stdscr.refresh()

    # same work is done in other way

    _, x, y, _, _ = curses.getmouse()
    stdscr.addstr(0, 0, f'{y} {x}')
    stdscr.refresh()

  stdscr.getch()

curses.wrapper(main)
# =================================
import curses
    
def main(stdscr):
  curses.curs_set(0)
  curses.mousemask(1) 
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
  curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)

  stdscr.addstr(0, 0, 'Hello!')

  stdscr.addstr(1, 0, 'Red')
  stdscr.addstr(2, 0, 'Green')

  while 1:
    stdscr.refresh()
    key = stdscr.getch()

    if key == curses.KEY_MOUSE:
      _, x, y, _, _ = curses.getmouse()

      if y == 1 and x in range(3):
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(0, 0, 'Hello!')
        stdscr.attroff(curses.color_pair(1))
      elif y == 2 and x in range(5):
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(0, 0, 'Hello!')
        stdscr.attroff(curses.color_pair(2))
      elif key == 27:
        break

curses.wrapper(main)
