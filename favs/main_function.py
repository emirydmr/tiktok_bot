def main(VIDEO_URL):
    import os
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
    import random
    from fake_useragent import UserAgent
    user_agent = UserAgent(platforms="pc").random
    views_sent = 0
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent}")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disables logging
        
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1200, 1200)
    driver.get('https://vipto.de/')
    print('[!] Solve the captcha...')

    #captcha solving time
    time.sleep(5)
    
    #view button
    driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[6]/div/button').click()
    time.sleep(2)
    
    #input link
    driver.find_element(By.XPATH, '/html/body/div[10]/div/form/div/input').send_keys(VIDEO_URL)
    time.sleep(2)
    
    
    
    while True:
        try:
            #press search
            driver.find_element(By.XPATH, '/html/body/div[10]/div/form/div/div/button').click()
            time.sleep(2)
            # Clicks the "Send Views" button.
            driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div[1]/div/form/button').click()
        except:
            waiting_time = random.randint(10,20)
            time.sleep(waiting_time)
            print(f"buttons not found/ waiting another {waiting_time} seconds")
            