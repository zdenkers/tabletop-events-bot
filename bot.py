from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import re
import os
import random
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://tabletop.events/account?redirect_after=/conventions/dragonsteel-2024/badgetypes/general-admission-badge6")
time.sleep(3)
with open('./log', 'a') as log_file:
    log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} page_loaded\n")
    log_file.flush()
    os.fsync(log_file.fileno())
    username_element = driver.find_element(By.ID, 'login')
    username_element.send_keys('username goes here')
    log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} entering username\n")
    log_file.flush()
    os.fsync(log_file.fileno())
    password_element = driver.find_element(By.ID, 'password')
    password_element.send_keys('password goes here')
    log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} entering password\n")
    log_file.flush()
    os.fsync(log_file.fileno())
    log_in_button = driver.find_element(By.XPATH, "//input[@value='Log In']")
    log_in_button.click()
    log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} logging in\n")
    log_file.flush()
    os.fsync(log_file.fileno())
    should_continue = True
    while should_continue:
        time.sleep(random.randrange(8,12))
        availability = driver.find_element(By.XPATH, "//div//b[text()='Availability:']/..")
        pattern = "^Availability:(\b|[^0-1]*)([2-9]\d*|[1-9]\d+)"
        log_file.write(f"{availability.text}\n")
        log_file.flush()
        os.fsync(log_file.fileno())
        if re.match(pattern, availability.text, re.IGNORECASE):
            log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} found tickets\n")
            log_file.flush()
            os.fsync(log_file.fileno())
            should_continue = False
        else:
            driver.refresh()
            log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} no tickets found trying again\n")
            log_file.flush()
            os.fsync(log_file.fileno())

    add_to_cart_button = driver.find_element(By.XPATH, "//button[@ng-click='add_to_cart()']")
    add_to_cart_button.click()
    log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} first ticket added to cart\n")
    log_file.flush()
    os.fsync(log_file.fileno())
    time.sleep(3)
    firstname = driver.find_element(By.ID, 'firstname')
    firstname.send_keys('second ticket first name')
    lastname = driver.find_element(By.ID, 'lastname')
    lastname.send_keys('second ticket last name')
    add_to_cart_button = driver.find_element(By.XPATH, "//button[@ng-click='add_to_cart()']")
    add_to_cart_button.click()
    log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} second ticket added to cart\n")
    log_file.flush()
    os.fsync(log_file.fileno())
    time.sleep(3)
    checkout_button = driver.find_element(By.XPATH, "//a[text()='Checkout']")
    checkout_button.click()
    log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} entering checkout\n")
    log_file.flush()
    os.fsync(log_file.fileno())

    time.sleep(10)
    card_select = Select(driver.find_element(By.ID, "stripe_card_id"))
    card_select.select_by_index(1) # select the index of the stored credit card you want to use 1 is first not 0
    log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} card selected\n")
    log_file.flush()
    os.fsync(log_file.fileno())
    billing_input = driver.find_element(By.ID, "stripe_postal_code")
    billing_input.send_keys('zip code')
    log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} postal code entered\n")
    log_file.flush()
    os.fsync(log_file.fileno())

    place_order_button = driver.find_element(By.XPATH, "//button[@ng-click='pay_via_stripe($event);']")
    place_order_button.click()

    log_file.write(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')} order placed\n")
    log_file.flush()
    os.fsync(log_file.fileno())


driver.close()