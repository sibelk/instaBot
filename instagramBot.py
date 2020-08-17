from instUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
class Instagram :
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages:':'en,en_US'})
        
        self.browser = webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    def signIn(self):
        self.browser.get("https://www.instagram.com/?hl=tr")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passInput = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        usernameInput.send_keys(self.username)
        passInput.send_keys(self.password)
        passInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(2)
        followersCount = int(self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute("title"))
        followersLink = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(2)
        print("total followers: ", followersCount)
        followerDialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        newFollowerCount = len(followerDialog.find_elements_by_css_selector("li"))
       
        action = webdriver.ActionChains(self.browser)
        while newFollowerCount < followersCount:
            followerDialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            newFollowerCount = len(followerDialog.find_elements_by_css_selector("li"))
            
           
        followers = followerDialog.find_elements_by_css_selector("li")
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            print(link)
    def followUser(self,username):
          self.browser.get(f"https://www.instagram.com/{self.username}/")
          time.sleep(2)
          followBtn = self.browser.find_element_by_tag_name("button")
          if followBtn.text != "Following":
              followBtn.click()
              time.sleep(1)
          else:
              pass
    def unfollowUser(self,username):
         self.browser.get(f"https://www.instagram.com/{self.username}/")
         time.sleep(2)
         followBtn = self.browser.find_element_by_tag_name("button")
         if followBtn.text == "Following":
              followBtn.click()
              time.sleep(1)
              confirmBtn = self.browser.find_element_by_xpath("//button[text()='Unfollow']").click()
            
         else:
              pass
    def getFollowed(self):
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        time.sleep(2)
        followedCount = int(self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text)
        followedLink = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(2)
        followedDialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        newFollowedCount = len(followedDialog.find_elements_by_css_selector("li"))
        print("total followed: ",followedCount)
        print(" followed: ",newFollowedCount)
        action = webdriver.ActionChains(self.browser)
       
        while newFollowedCount < followedCount:
            followedDialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            
            newFollowedCount = len(followedDialog.find_elements_by_css_selector("li"))

            print(" followed: ",newFollowedCount)
            
            
            
           
        followedList = followedDialog.find_elements_by_css_selector("li")
        for user in followedList:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            print(link)

        
    def usersLikesOfPost(self,post_url):
        pass
    def usersCommentsOfPost(self,post_url):
        pass
    def likePost(self,post_url):
        pass
    def commentPost(self,post_url,comment_text):
        pass
    def listAllPost(self,username):
        pass
    def isFollowing(self,username,followedName):
        pass
    



            


inst = Instagram(username,password)
inst.signIn()
inst.getFollowed()