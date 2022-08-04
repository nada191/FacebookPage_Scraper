import time
from random import randint

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def get_full_path(name: str) -> str:
    """ Get the full URL of a facebook page.
    Args:
        name (str): the name of the facebook page.
    Returns:
        'str' : full URL of a facebook page.
    """
    return "https://facebook.com/{}".format(name)

def get_name(driver):
    """ Get the name of the actual facebook page opened by the driver
    Args:
        driver (selenium.webdriver.Chrome):
    Returns:
        str : a string containing the page name.
    """
    name = driver.find_element(By.TAG_NAME, "strong").get_attribute("textContent")
    return name

def close_error_popup(driver):
    """ Close the popup that appears when starting to scroll down.
    Notes: The pop-up appears with some facebook pages ex:"TED", "www.foot24.tn" ...
            and doesn't appear with others "santetunisie.rns.tn" ...
    Args:
        driver (selenium.webdriver.Chrome):
    Raises:
        WebDriverException: If the popup exist but the DOM is updated.
        ex : if the driver can't find the pop-up.
    """
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label=Close]")))
        driver.find_element(By.CSS_SELECTOR, "[aria-label=Close]").click()

    except WebDriverException as e:
        try:
            time.sleep(5)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label=Close]")))
            driver.find_element(By.CSS_SELECTOR, "[aria-label=Close]").click()
        except WebDriverException as e:
            pass

    except Exception as ex:
        pass
        print("error at close_error_popup method : {}".format(ex))

def scroll_down_first(driver):
    """ Move to the middle of the page to see if the pop-up appears for the current page.
    Args:
        driver (selenium.webdriver.Chrome):
    """
    body = driver.find_element(By.CSS_SELECTOR, "body")
    for _ in range(6):#randint(5, 6))
        body.send_keys(Keys.PAGE_UP)
    for _ in range(8):
        body.send_keys(Keys.PAGE_DOWN)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def check_timeout(start_time, current_time, timeout):
    """ Check if the scraper reached the timeout for scraping or not.
    Args:
        start_time (): Time when we start the scraping.
        current_time (): Actual time.
        timeout (int): Maximum time for scraping.
    Returns:
        bool: False if timeout reached. True otherwise.
    """
    return (current_time - start_time) > timeout


def scroll_to_bottom(driver, timeout):
    """ Scroll to the bottom of the current page opened by the driver.
    Args:
        driver ():
        timeout (int): Maximum time for scraping.
    Returns:
        bool : True if we reached the bottom of the page before timeout
                False if we reached the timeout.
    """
    old_position = 0
    new_position = None
    end_position = 0
    start_time = time.time()
    body = driver.find_element(By.CSS_SELECTOR, "body")

    while new_position != old_position and not check_timeout(start_time, time.time(), timeout):
        # Get old scroll position
        old_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(1)
        driver.execute_script((
            "var scrollingElement = (document.scrollingElement ||"
            " document.body);scrollingElement.scrollTop ="
            " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))

        if end_position != new_position:
            for _ in range(randint(5, 6)):
                body.send_keys(Keys.PAGE_UP)
        end_position = new_position
    if new_position == old_position:
        return True
    else:
        return False