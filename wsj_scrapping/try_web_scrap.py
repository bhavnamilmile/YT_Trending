
from urllib.request import urlopen
#https://cosmocode.io/how-to-connect-selenium-to-an-existing-browser-that-was-opened-manually/

#https://www.wsj.com/search?query=%22Darren%20Wilson%22%3B%20%22Michael%20Brown%22%3B%20%22Ferguson%22&isToggleOn=true&operator=AND&sort=relevance&duration=1y&startDate=2014%2F11%2F01&endDate=2015%2F06%2F30&source=wsjie%2Cwsjsitesrch%2Cwsjpro%2Capfeed&page=20
if __name__ =="__main__":

    ws_url = "https://www.wsj.com/search?query=%22Michael%20Brown%22&isToggleOn=true&operator=AND&sort=relevance&duration=1y&startDate=2014%2F11%2F01&endDate=2015%2F06%2F30&source=wsjie%2Cwsjsitesrch%2Cwsjpro%2Capfeed&page=3"

    openedpage = urlopen(ws_url)
    content = openedpage.read()
    code = bytes.decode("utf-8")
