import time
from selenium import webdriver

movie_url="https://www.netflix.com/in/title/80230399"
driver=webdriver.Chrome(r'C:\Users\RAHUL\Downloads\chromedriver.exe')   # Selenium chromedriver path
driver.get(movie_url)

print("Movie URL: ",movie_url)
print("Movie Title: Extraction")

description=driver.find_element_by_xpath('//*[@id="section-hero"]/div[1]/div[1]/div[2]/div/div[2]/div[1]')
print("Description:",description.text)

starcast=driver.find_element_by_xpath('//*[@id="section-hero"]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/span[2]')
print("Starcast:",starcast.text)

play_button=driver.find_element_by_xpath('//*[@id="section-additional-videos"]/div[2]/ul/li/div/button')
play_button.click()

time.sleep(3)

try:
    status=driver.find_element_by_css_selector(
            "button[aria-label='Pause']"
        )
    print('Status: Video is playing')
except:
    print('Status: Video is not playing')

input("Press any key to exit!!!")