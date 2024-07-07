import curses, pytube
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
    #yt.bypass_age_gate()
    sprint(yt.initial_data['contents']
           ['twoColumnWatchNextResults']
           ['results']['results']
           ['contents'][0]
           ['videoPrimaryInfoRenderer']
           ['videoActions']['menuRenderer']
           ['topLevelButtons'][0]
           ['segmentedLikeDislikeButtonViewModel']
           ['likeButtonViewModel']['likeButtonViewModel']
           ['toggleButtonViewModel']['toggleButtonViewModel']
           ['defaultButtonViewModel']['buttonViewModel']
           ['title']
           ,"Likes",x=1,y=2)
    sprint("Author:",yt.author,x=1,y=3)
    sprint("Publish Date:",yt.publish_date,x=1,y=4)
    stdscr.refresh()

curses.endwin()