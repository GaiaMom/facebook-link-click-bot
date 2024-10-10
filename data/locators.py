from selenium.webdriver.common.by import By

class BasePageLocators:
    DIALOG_CONTAINER = (By.CSS_SELECTOR, 'div[role="dialog"]')
    A_ELEMENT = (By.CSS_SELECTOR, 'a[rel="nofollow noreferrer"]')

class ArticlePageLocators:
    POST_TAG = (By.TAG_NAME, "shreddit-post")
    ADD_COMMENT_SEC = (By.TAG_NAME, "comment-composer-host")
    COMMENT_EDIT_AREA = (By.TAG_NAME, "shreddit-composer")
    UPVOTE_BTN = (By.CSS_SELECTOR, "button[upvote]")
    DOWNVOTE_BTN = (By.CSS_SELECTOR, "button[downvote]")