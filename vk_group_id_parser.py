import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


try:
    # CHANGE URL WHICH MUST BE PARSED 
    # OPEN https://vk.com/groups?act=catalog AND ENTER WHAT YOU WANT TO FIND
    # COPY LINK AND PASTE HERE
    url = "https://vk.com/groups?act=catalog&c%5Blike_hints%5D=1&c%5Bper_page%5D=40&c%5Bq%5D=взаимные%20лайки&c%5Bsection%5D=communities"
    chrome_options = Options()
    chrome_options.add_argument("user-data-dir=C:\\Users\\andre\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    chrome_options.add_argument('--window-size=1800,1000')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get(url)
    time.sleep(2)
    # i кол-во прокруток
    for i in range(8):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    groups = driver.find_elements(by = By.CLASS_NAME, value="groups_row")
    print(len(groups))
    groups_links = []
    for i in range(1,len(groups)+1):
        try:
            a = driver.find_element(by = By.XPATH, value=f'//*[@id="results"]/div[{i}]/div[3]/div[1]/a').get_attribute('href')
            print(a)
            groups_links.append(a)
        except:
            pass
    with open("file.txt", "w") as output:
        for line in groups_links:
            output.write(f"{line}\n")
        output.close()

except Exception as e:
    print(e)