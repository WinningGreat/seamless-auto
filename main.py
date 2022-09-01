# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
proxyList = [
    "51.38.131.145:8080",
    "130.41.55.190:8080",
    "182.90.224.115:3128",
    "58.17.24.162:9091",
    "66.94.113.79:3128",
    "103.231.78.36:80",
    "45.169.162.1:3128",
    "150.136.246.57:80",
    "140.227.211.47:8080",
    "208.52.157.113:5555",
    "223.62.53.140:3128",
    ""
]

# proxyDriver = webdriver.Chrome('/Users/winnieg/Downloads/chromedriver')

# proxyDriver.get("https://www.freeproxylists.net/")

# proxyDataTable = proxyDriver.find_element(By.CLASS_NAME, "DataGrid")

# proxyIds = proxyDataTable.find_elements(By.TAG_NAME, 'td')

# print(proxyIds[1].text)


for proxy in proxyList:


    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy)

    driver = webdriver.Chrome('/Users/winnieg/Downloads/chromedriver', chrome_options=chrome_options)
    # driver.get("https://seamlesshr.com/refer-and-earn-a/?utm_campaign=Refer+and+Earn&utm_source=linkedin&utm_medium=paid&hsa_acc=504014782&hsa_cam=612444133&hsa_grp=201147844&hsa_ad=183818734&hsa_net=linkedin&hsa_ver=3")
    driver.get("https://webhook.site/fccec302-143a-4e0d-9300-a7a1fd608bf1")

    driver.close()
    time.sleep(3)



# cookieButton = driver.find_element(By.CLASS_NAME, 'ekit-btn-wraper')
# cookieButton.click()
# print(cookieButton)
# actions = ActionChains(driver)
# fake = Faker()
# fake_name = fake.name().split(" ")
# first_name = fake_name[0]
# last_name = fake_name[1]
# inputDict = {"firstname": first_name , "lastname": last_name, "email": "{}{}@{}".format(first_name, last_name, random.choice(["gmail.com", "yahoo.com", "outlook.com", "icloud.com"])), "company": fake.company(), "phone": "080{}".format("".join([str(random.randint(i, 9)) for i in range(0,9)])),
             
#              }

# selectDict = {"what_best_describes_you_":random.choice(["Customer/User", "Business Consultant", "HR Professional", "Affiliate Marketer", "Self-Employed"]),
# "have_you_sold_or_used_an_enterprise_saas_product_before": random.choice(["Yes", "No"])
#               }

# for key, value in inputDict.items():
#     element = driver.find_element(By.CSS_SELECTOR, 'input[name="{}"]'.format(key))
#     try:
#         actions.move_to_element(element).perform()
#     except Exception as e:
#         print(e)
#     element.send_keys(value)

# for key, value in selectDict.items():
#     element = driver.find_element(By.CSS_SELECTOR, 'select[name="{}"]'.format(key))
#     try:
#         actions.move_to_element(element).perform()
#     except Exception as e:
#         print(e)
#     Select(element).select_by_value(value)

# print("I don pass")

# time.sleep(3)
# checkBoxElement = driver.find_element(By.CSS_SELECTOR,'input[name="i_consent_to_the_terms_and_conditions"]')

# checkBoxElement.click()

# radioElement = random.choice(driver.find_elements(By.CSS_SELECTOR,'input[name="are_you_a_public_servant_"]'))

# radioElement.click()

# submitElement = random.choice(driver.find_elements(By.CSS_SELECTOR,'input[type="submit"]'))

# submitElement.click()





# driver.close()
