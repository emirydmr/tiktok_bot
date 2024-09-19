def main():
    import os
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
    import random
    from fake_useragent import UserAgent

    urls = tiktok_links = [line.strip() for line in open("../video_urls.txt", "r").readlines()]
    
    user_agent = UserAgent(platforms="pc").random
    views_sent = 0
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={user_agent}")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disables logging
        
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1200, 1200)
    driver.get('https://vipto.de/')
    captcha = driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/form/div/div/img")
    if captcha:
        print("captcha detected")
    while captcha:
        try:
            driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[6]/div/button').click()
        except NoSuchElementException:
            print("captcha still present")
            time.sleep(2)
        except:
            print("captcha passed")
            captcha = False
    #captcha solving time
    time.sleep(0.5)
    
    #view button
    #driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/div/div[6]/div/button').click()
    time.sleep(2)
    while True:
        try:
            #input link
            random_url_index = random.randint(0,urls.__len__()-1)
            random_url = urls[random_url_index]
            driver.find_element(By.XPATH, '/html/body/div[10]/div/form/div/input').send_keys(random_url)
            print(f"URL at index: {random_url_index} was placed")
            time.sleep(2)
            #press search
            driver.find_element(By.XPATH, '/html/body/div[10]/div/form/div/div/button').click()
            time.sleep(2)
            # Clicks the "Send Views" button.
            driver.find_element(By.XPATH, '/html/body/div[10]/div/div/div[1]/div/form/button').click()
        except Exception as error:
            waiting_time = random.randint(10,20)
            time.sleep(waiting_time)
            print(f"buttons not found/ waiting another {waiting_time} seconds")

if __name__ == "__main__":
    main()
    