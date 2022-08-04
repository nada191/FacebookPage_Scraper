import re

import requests
from selenium.webdriver.common.by import By


def check_page_exists(name: str) -> bool:
    """ Check if a facebook page exists or not using the facebook graph.
    Args:
        name (str):  name of the facebook page.
    Returns:
        bool: True if the page exists.
              False otherwise.
    """

    url = "https://graph.facebook.com/" + name
    response = requests.get(url)

    if response.text.find("Unsupported get request") == -1:
        return True
    else:
        return False

def get_posted_time(post):
    """ Scrap the posted time of the current post.
    Returns:
        str : the posted time of the current post.
    """

    element = post.find_element(By.CSS_SELECTOR, "a.gpro0wi8.b1v8xokw")
    return element.get_attribute('innerText')


def get_text(post):
    """ Scrap the text of the current post.
    Returns:
        object: str if the post contain a text description.
                None if the post doesn't contain a text. (Only images/video/pdf ...)
    """
    try:
        div_text = post.find_element(By.CSS_SELECTOR, '[data-ad-comet-preview]')
        text = div_text.get_attribute('innerText')
    except:
        text = None
    return text

def get_shares_comments(post):
    """ Scrap the shares and comments of the current post.
    Returns:
        int: the number of shares of the current post.
        int: the number of comments of the current post.
    """

    elements = post.find_elements(By.CSS_SELECTOR, "div.gtad4xkn")
    shares = "0"
    comments = "0"
    for element in elements:
        text = element.get_attribute("innerText")
        if "Shares" in text:
            shares = re.findall("\d+", text)[0]

        if "Comments" in text:
            comments = re.findall("\d+", text)[0]

    return shares, comments


def get_reactions(post):
    """ Scrap the reactions of the current post.
    Returns:
        int: the number of reactions of the current post.
    """
    reactions = 0
    try:
        total_reactions = post.find_element(By.CSS_SELECTOR, 'span.ltmttdrg.gjzvkazv')
        reactions = total_reactions.get_attribute("innerText")
    except Exception as e:
        print(e)
    return reactions

def get_images(post):
    """ Scrap all the images of the current post.
    Returns:
        list(str): links of all images of the current post.
    """

    list_of_images = []
    elements = post.find_elements(By.CSS_SELECTOR, 'div.do00u71z.ni8dbmo4.stjgntxs.l9j0dhe7 img.i09qtzwb')
    for element in elements:
        list_of_images.append(element.get_attribute('src'))
    return list_of_images

def get_link_video(post):
    """ Scrap the video of the current post.
    Returns:
        object: str: link of the video if the post contain a video.
                None if the post doesn't contain any video.
    """
    try:
        div_text = post.find_element(By.CSS_SELECTOR, "[aria-label='Enlarge']")
        text = div_text.get_attribute('href')
        text = text[:text.rfind("/")]
    except:
        text = None
    return text