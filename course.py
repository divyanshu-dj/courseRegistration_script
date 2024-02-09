
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from concurrent.futures import ThreadPoolExecutor
# import time


# def perform_actions(url):

#     driver.execute_script(f"window.open('{url}', '_blank');")
#     driver.switch_to.window(driver.window_handles[-1])
    
#     roll_number_input = driver.find_element("name", "roll_no")
#     roll_number_input.send_keys("2k22/ee/103")
    
#     password_input = driver.find_element("name", "password")
#     password_input.send_keys("hu77ha")
    
#     login_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
#     login_button.click()
    
#     link = driver.find_element(By.XPATH, "//a[contains(@href,'courseRegisteration/6497164af608d957ec3b409a')]")
#     driver.execute_script("arguments[0].click();", link)
    
    


# with ThreadPoolExecutor(max_workers=10) as executor:
#     options = Options()
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    

#     initial_url = "http://reg.exam.dtu.ac.in/student/login"
    

#     for _ in range(3):
#         executor.submit(perform_actions, initial_url)
#         time.sleep(3)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def perform_actions(url):
    driver.execute_script(f"window.open('{url}', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])

    # Wait for the roll number input to be present
    roll_number_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "roll_no"))
    )
    roll_number_input.send_keys("2k22/ee/103")

    # Wait for the password input to be present
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys("hu77ha")

    # Wait for the login button to be clickable
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    login_button.click()

    # Wait for the link to be present
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'courseRegisteration/6497164af608d957ec3b409a')]"))
    )
    driver.execute_script("arguments[0].click();", link)

    # Switch to the new window (if applicable)
    driver.switch_to.window(driver.window_handles[-1])

    register_button_path = "//td[contains(normalize-space(), 'Value Driven Leadership')]/following-sibling::td/form/button[normalize-space()='Register']"

    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, register_button_path))
    )
    # Scroll to the element using ActionChains
    actions = ActionChains(driver)
    actions.move_to_element(register_button).perform()

    register_button.click()

with ThreadPoolExecutor(max_workers=10) as executor:
    initial_url = "http://reg.exam.dtu.ac.in/student/login"

    for _ in range(2):
        executor.submit(perform_actions, initial_url)
        time.sleep(5)


