import pyshorteners

def shorten_url(full_url):
    s = pyshorteners.Shortener()
    try:
        short_url = s.tinyurl.short(full_url)
        return short_url
    except Exception as e:
        return f"Error: {str(e)}"


def expand_url(short_url):
    s = pyshorteners.Shortener()
    try:
        full_url = s.tinyurl.expand(short_url)
        return full_url
    except Exce