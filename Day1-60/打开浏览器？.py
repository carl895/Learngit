# 打开chrome
driver = webdriver.Chrome(chrome_driver, options=option)
driver.get('https://www.baidu.com/')
# 最大化谷歌
driver.maximize_window()
time.sleep(1)
