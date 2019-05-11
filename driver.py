from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, sys
import platform

# 실행자의 OS 맞는 크롬드라이버 반환
def getChromeDriverPath():
    osType = platform.system()

    if osType == 'Drawin': # type of os is mac
        print('OS TYPE IS',osType)
        return 'chromedriver/mac64_chromedriver'

    elif osType == 'Linux': # type of os is linux
        print('OS TYPE IS',osType)
        return 'chromedriver/linux64_chromedriver'

    elif osType == 'Windows': # type of os is windows
        print('OS TYPE IS',osType)
        return 'chromedriver/win32_chromedriver.exe'
    
    else:
        return 0
    
def createDriver(targetUrl):

    chromeDriverPath = getChromeDriverPath()
    # chromeDriverPath = '.chromedriver/linux64_chromedriver'
    if not(chromeDriverPath):
        print('Failed to check operating system type')
        sys.exit(1) # OS 타입을 확인하지 못하면 프로그램 종료

    options = Options()
    #head less mode
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")
    #for anti head less mode detection
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36") # agent change 
    options.add_argument("lang=ko_KR") 

    # driver setting
    driver = webdriver.Chrome(chrome_options=options, executable_path=chromeDriverPath)
    driver.get(targetUrl)

    # for anti head less mode detection
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});") #num of plugin spoofing
    driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
    driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

    return driver



