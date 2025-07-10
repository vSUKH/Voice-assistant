import curses 
from curses import wrapper
import queue
import time

puzzle =[
    ["#", "o", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "x", "#"]
]
def print_puzzle (puzzle,stdscr,path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(puzzle):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i,j*2,"x",RED)
            else:
                stdscr.addstr(i,j*2, value, BLUE)

def find_start(puzzle,start):
    for i, row in enumerate(puzzle):
        for j, value in enumerate(row):
            if value == start:
                return i,j
    return None

def find_path(puzzle,stdscr):
    start = "o"
    end = "x"
    start_pos = find_start(puzzle, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_puzzle(puzzle, stdscr, path)
        time.sleep(2)
        stdscr.refresh()

        if puzzle[row][col] == end:
            return path
        
        neighbors = find_neighors(puzzle,row,col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
        r, c = neighbor
        if puzzle[r][c]=="#":
            continue
        
        new_path = path + [neighbor]
        q.path((neighbor, new_path))
        visited.add(neighbor)

def find_neighors(puzzle, row , col):
    neighbors = []

    if row > 0: #up
        neighbors.append((row - 1,col))
    if row + 1 < len (puzzle):  #DOWN
        neighbors.append((row + 1,col))
    if col > 0: #LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len (puzzle[0]):  #RIGHT
        neighbors.append((row,col +1))

    return neighbors

def main (stdsrc):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(puzzle, stdsrc)
    stdsrc.getch()
    
wrapper(main)