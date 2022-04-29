import curses
import time
import sys
import pigpio

pi2 = pigpio.pi() # Connect

def ESC():
    # wait half a second
    time.sleep(1)
    pi2.set_servo_pulsewidth(13,1500)
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    try:
            char = screen.getch()
            if char == ord('q'):
                pi2.stop()
                pi2.set_servo_pulsewidth(13, 1500)

            elif char == curses.KEY_UP:
                pi2.set_servo_pulsewidth(13, 1570)
                print('up')

            elif char == curses.KEY_DOWN:
                pi2.set_servo_pulsewidth(13, 1350)
                print('down')

       #     elif char == curses.KEY_RIGHT:
       #         pi2.set_servo_pulsewidth(13,1550)
       #         print('right')

       #     elif char == curses.KEY_LEFT:
       #         pi2.set_servo_pulsewidth(13,1550)
       #         print('left')

            elif char == ord('s'):
                pi2.set_servo_pulsewidth(13, 1500)
                print('stop')
            time.sleep(20)
    finally:
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        pi2.set_servo_pulsewidth(13, 1500)
    pi2.stop()

ESC()
