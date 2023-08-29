
import pyshorteners

def shorten_url(url):
    
    s = pyshorteners.Shortener()
    
    short_url = s.tinyurl.short(url)
    
    return short_url

if __name__ == "__main__":
    
    long_url = input("Enter the URL to shorten: ")
    
    shortened_url = shorten_url(long_url)
    
    print("Shortened URL:", shortened_url)
