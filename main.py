from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# Discord網頁登入頁面URL
discord_url = "https://discord.com/login"

# Discord帳號
username = "chi200706@gmail.com"

# 從pwd.txt讀取密碼
pwd_txt_path = 'pwd.txt'
if os.path.isfile(pwd_txt_path):
  f = open(pwd_txt_path, 'r')
  password = f.read()
  f.close()

# 目標朋友名稱
target_friend_name = "路過騎士"

# 訊息內容
message_content = "哈囉你好啊"

# 初始化網頁驅動
driver = webdriver.Chrome()
driver.get(discord_url)

# 等待網頁載入
time.sleep(3)

email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")
email_input.send_keys(username)
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

# 登入後等待一段時間，確保頁面載入完成
time.sleep(10) # 預留時間做些簡易的點擊

# 找所有好友
friend_list = driver.find_element(By.XPATH, "//div[text()='所有']")
friend_list.click()

# 等待所有好友列表彈出並搜尋特定好友
time.sleep(5)
search_bar = driver.find_element(By.XPATH, "//input[@placeholder='搜尋']")
search_bar.send_keys(target_friend_name)

# 等待搜尋結果出現
time.sleep(5)

# 點擊目標好友
friend = driver.find_element(By.XPATH, f"//span[text()='{target_friend_name}']")
friend.click()

# 等待訊息視窗載入
time.sleep(5)

# 找到訊息輸入框，輸入訊息並送出
message_input = driver.find_element(By.XPATH, "//div[@data-slate-node='element']")
message_input.send_keys(message_content)
message_input.send_keys(Keys.ENTER)

# 等待訊息發送完成
time.sleep(2)

# 關閉網頁
driver.quit()
