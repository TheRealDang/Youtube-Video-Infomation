import curses, pytube
stdscr = curses.initscr()
curses.noecho()

ry = 0

def sprint(*string,x=0,y=0):
    try:
        stdscr.addstr(y-ry,x," ".join(list(map(str,string))))
    except:
      pass

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def get_description(yt):
    for n in range(6):
        try:
            description =  yt.initial_data["engagementPanels"][n]["engagementPanelSectionListRenderer"]["content"]["structuredDescriptionContentRenderer"]["items"][1]["expandableVideoDescriptionBodyRenderer"]["attributedDescriptionBodyText"]["content"]            
            return description
        except:
            continue
    return False


while True:
    if '' == curses.KEY_UP:
        if ry != 0:
            ry -= 1
    if '' == curses.KEY_DOWN:
        ry += 1
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
    sprint("Description:\n",get_description(yt=yt),x=1,y=4)
    stdscr.refresh()

curses.endwin()