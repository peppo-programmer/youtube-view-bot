  
import time;
from selenium import webdriver;


intro = """
      	   ██████╗  ██████╗ ████████╗████████╗███████╗██████╗
      	   ██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
      	   ██████╔╝██║   ██║   ██║      ██║   █████╗  ██████╔╝
      	   ██╔══██╗██║   ██║   ██║      ██║   ██╔══╝  ██╔══██╗
      	   ██████╔╝╚██████╔╝   ██║      ██║   ███████╗██║  ██║
      	   ╚═════╝  ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝

MADE BY LASMOD
"""

print(intro)

#time to refresh page (seconds)
Timer = 270

#youtube link
link = 'https://www.youtube.com/watch?v=wLFn4MGXPWE&t=25s'

#number of views
views = 10000

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
