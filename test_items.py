import pytest
from selenium import webdriver
import time

def test_find_card_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    time.sleep(30)
    
    url=browser.current_url.split('/')
    langUrl=url[3]
    print("URL -- ",url,'\nlangUrl -- ',langUrl)
    button=browser.find_element_by_css_selector("#add_to_basket_form > button")
    print('Button text -- ',button.text)
    assert button , "BUTTON NOT FOUND !!!"
    
    if 'fr' in langUrl:
        assert button.text=='Ajouter au panier', 'The text is not in France or does not match'
    if 'en' in langUrl:
        assert button.text=='Add to basket', 'The text is not in English or does not match'
    if 'ru' in langUrl:
        assert button.text=='Добавить в корзину', 'The text is not in Russian or does not match'
    if 'es' in langUrl:
        assert button.text=='Añadir al carrito', 'The text is not in Spanish or does not match'

    
    
#pytest --browser_name=chrome --language=fr -s -v test_items.py
