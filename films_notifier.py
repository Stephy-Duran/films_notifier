from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


def wait_for_element(by_selector, selector, timeout=30):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by_selector, selector)))


def collect_movies(city):
    driver.get("https://www.cinecolombia.com/")

    # Selects the city
    # wait_for_element(By.CSS_SELECTOR, "#city option")
    cities = driver.find_elements(By.CSS_SELECTOR, "#city option")

    for city1 in cities:
        print(city1.text)

    accept_button = driver.find_element(By.CSS_SELECTOR, '.columns.is-multiline .button.is-primary.has-shadow')
    city_found = False

    for option in cities:
        if option.text == city:
            option.click()
            accept_button.click()
            city_found = True
            print(f"The city '{city}' has been selected.")
            break

    if not city_found:
        print(f'The city {city} is not in the list, please check if is a valid city')

    # Accepts cookies
    wait_for_element(By.CSS_SELECTOR, '.button.is-outlined.has-shadow.is-primary').click()

    # Closes publicity
    # wait_for_element(By.CSS_SELECTOR, '.delete').click()

    # Navigates to billboard section
    wait_for_element(By.CSS_SELECTOR, '.nav-tabs a:first-child').click()

    # Saves films in a list
    wait_for_element(By.CSS_SELECTOR, '[class="columns is-multiline columns--slim"] a')
    movies = driver.find_elements(By.CSS_SELECTOR, '[class="columns is-multiline columns--slim"] a')

    for movie in movies:
        print(movie.text)


if __name__ == "__main__":
    city = "Medellín"
    collect_movies(city)
    # time.sleep(10)
