import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def start_webdriver(initial_url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Активирует безоконный режим
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        r"C:\Programming\task_sender_bot\chromedriver.exe", options=options)
    driver.get(initial_url)
    return driver


def checker(last_tasks, key_words, driver):
    """Возвращает ссылку и заголовок  заданий, в названии или зголовках которых присутствуют ключевые слова"""

    driver.refresh()

    tasks = []
    wait = WebDriverWait(driver, 500)

    teg_containers = driver.find_elements_by_xpath(
        '//*[contains(@class, "tags tags_short")]')

    for a in range(1, 26):
        heading = driver.find_element_by_xpath(f'//*[@id="tasks_list"]/li[{a}]/article/div/header/div[1]/a')
        tags = driver.find_element_by_xpath(f'//*[@id="tasks_list"]/li[{a}]/article/div/div/ul')
        for word in key_words:
            if not (f'{heading.text}\n {heading.get_attribute("href")}' in last_tasks) \
                    and (word in heading.text or word in tags.text):
                tasks.append(f'{heading.text}\n {heading.get_attribute("href")}')
                break
    return tasks


"""    for a in range(0, 25):
        for word in key_words:
            if (word in teg_containers[a].text or word in headings[a].text) and not (headings[a].text in last_tasks):
                tasks.append(f'{headings[a].text}\n {headings[a].get_attribute("href")}')
    return tasks
    //*[@id="tasks_list"]/li[24]/article/div/header/div[1]/a
    //*[@id="tasks_list"]/li[1]/article/div/header/div[1]
//*[@id="tasks_list"]/li[25]/article/div/header/div[1]/a
//*[@id="tasks_list"]/li[25]/article/div/header/div[1]
////*[@id="tasks_list"]/li[24]/article/div/div/ul
//*[@id="tasks_list"]/li[24]/article/div/header/div[1]
//*[@id="tasks_list"]/li[24]/article/div/div/ul"""
