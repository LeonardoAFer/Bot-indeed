from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time
import pyautogui


chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'


chrome_options = Options()
chrome_options.binary_location = chrome_path
chrome_options.add_argument("--start-maximized")  


driver = Chrome(options=chrome_options)


driver.get('https://www.indeed.com/')


driver.implicitly_wait(10)

try:
 
    campo_de_entrada = driver.find_element(By.XPATH, '//input[@placeholder="Cargo, palavras-chave ou empresa"]')


    campo_de_entrada.send_keys("estágio ti")


    campo_de_entrada.send_keys(Keys.ENTER)

 
    time.sleep(5)

    for _ in range(5): 
     
        driver.execute_script("window.scrollBy(0, 400);")
    
        time.sleep(2)

   
        x, y = pyautogui.position()

    
        pyautogui.click(x, y)

      
        time.sleep(2)

        try:
            candidatar_se_button = driver.find_element(By.XPATH, '//button[@id="indeedApplyButton"]')
            candidatar_se_button.click()  

            pyautogui.moveTo(1000, 1000)

  
            while True:
                time.sleep(10) 

        except:
            pass  

finally:

    pass  
