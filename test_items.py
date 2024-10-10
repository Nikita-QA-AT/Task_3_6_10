import pytest
import time
import math
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


    


def test_dolshna_bit_knopka_dobavl_v_korziny(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(5)
    print()
    
    button_add_to_basket = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button_add_to_basket is not None, "Кнопка добавления в корзину не найдена"

