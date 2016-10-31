import urllib2
from collections import defaultdict
from bs4 import BeautifulSoup, SoupStrainer


def find_duplicates(links):
    # Default value of the hash table will be a zero integer value.
    video_count = defaultdict(int)
    celeb_count = defaultdict(int)
    channel_count = defaultdict(int)

    VIDEO_DUP_THRESHOLD = 1
    # Every celebrity link comes in a pair (image and text).
    CELEB_DUP_THRESHOLD = 2
    # Every channel link comes in a pair (image and text).
    CHANNEL_DUP_THRESHOLD = 2

    for link in links:
        href = link.get("href")
        if not href:
            continue
        if "/videos/" in href:
            # The second argument of the split method means to split once,
            # therefore the end result will only have two parts.
            _, video = href.split("/videos/", 1)
            video_count[video] += 1
        elif "/celebrities/" in href:
            _, celeb = href.split("/celebrities/", 1)
            celeb_count[celeb] += 1
        elif "/tv/" in href:
            _, channel = href.split("/tv/", 1)
            channel_count[channel] += 1

    # Print content if its occurrence count is above the duplicate threshold.
    for video in video_count:
        if video_count[video] > VIDEO_DUP_THRESHOLD:
            print "Likely duplicate video:", video
    for celeb in celeb_count:
        if celeb_count[celeb] > CELEB_DUP_THRESHOLD:
            print "Likely duplicate celebrity:", celeb
    for channel in channel_count:
        if channel_count[channel] > CHANNEL_DUP_THRESHOLD:
            print "Likely duplicate channel:", channel


if __name__ == "__main__":
    SITE = "http://www.viki.com"
    HEADER = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11' \
                      '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

    request = urllib2.Request(SITE, headers=HEADER)
    response = urllib2.urlopen(request)
    find_duplicates(BeautifulSoup(response, "html.parser",
                                  parse_only=SoupStrainer('a')))
