import curses, pytube, requests
stdscr = curses.initscr()
curses.noecho()


def sprint(*string,x=0,y=0):
    try:
        stdscr.addstr(y,x," ".join(list(map(str,string))))
    except:
      pass

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

while True:
    yt = pytube.YouTube(url)
    sprint("Video:", yt.title,x=0,y=0)
    sprint(yt.views,"Views",x=1,y=1)
    sprint("Author:",yt.author,x=1,y=2)
    sprint("Publish Date:",yt.publish_date,x=1,y=3)
    stdscr.refresh()

curses.endwin()