from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# from webdriver_manager.firefox import GeckoDriverManager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# driver = webdriver.Chrome(executable_path="D:\Selenium\BrowserDrivers\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="D:\Selenium\BrowserDrivers\geckodriver.exe")

driver.maximize_window()
driver.get("https://staging.karshare.com/")
print(driver.title)
driver.close()