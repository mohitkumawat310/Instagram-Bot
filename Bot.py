from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import time
def loginAndSeacrh():
    chromedriver = "C:\Python\chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://instagram.com")
    time.sleep(3)

    username = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(1) > div > label > input")
    username.send_keys("mohitkumawat310")
    password = driver.find_element_by_css_selector("#loginForm > div > div:nth-child(2) > div > label > input")
    password.send_keys("Enter Your Password")

    # hit enter to login
    password.send_keys(Keys.ENTER)

    time.sleep(8)

    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()

    time.sleep(5)

    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

    search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys("#uiux")

    time.sleep(5)
    search.send_keys(Keys.ENTER)
    search.send_keys(Keys.ENTER)
    # like and comment post
    likecommentpost(driver)


def likecommentpost(driver):
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]").click()
    while True:
        time.sleep(2)
        # post = driver.find_element_by_xpath("/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]")
        # actionChains = ActionChains(driver)
        # actionChains.double_click(post).perform()
        # select comment input
        driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button").click()
        driver.find_element_by_css_selector(".Ypffh").click()
        comment = driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
        time.sleep(2)
        comment.send_keys("Nice Post and I am a Bot")
        time.sleep(2)
        comment.send_keys(Keys.ENTER)
        time.sleep(4)
        # next post
        driver.find_element_by_css_selector("._65Bje").click()


if __name__ == "__main__":
    loginAndSeacrh()
