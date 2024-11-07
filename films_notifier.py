import smtplib
import ssl

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Installs the ChromeDriver if it is not installed and executes the browser
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()


def wait_for_element(by_selector, selector, timeout=30):
    ''' Method that waits for an element to be clickable '''
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by_selector, selector))
    )


def collect_movies(city):
    ''' Method that collects the movies available in the selected city '''
    driver.get("https://www.cinecolombia.com/")

    # Selects the city
    # wait_for_element(By.CSS_SELECTOR, "#city option")
    cities = driver.find_elements(By.CSS_SELECTOR, "#city option")

    print("\nCities available:")
    for city1 in cities:
        print(city1.text)
    print("\n")

    accept_button = driver.find_element(
        By.CSS_SELECTOR, '.columns.is-multiline .button.is-primary.has-shadow')
    city_found = False

    for option in cities:
        if option.text == city:
            option.click()
            accept_button.click()
            city_found = True
            print(f"The city '{city}' has been selected.")
            break

    if not city_found:
        print(f'ERROR: The city {city} is not in the list, please check if is a valid city')

    # Accepts cookies
    wait_for_element(
        By.CSS_SELECTOR, '.button.is-outlined.has-shadow.is-primary').click()

    # Closes publicity
    # wait_for_element(By.CSS_SELECTOR, '.delete').click()

    # Navigates to billboard section
    wait_for_element(By.CSS_SELECTOR, '.nav-tabs a:first-child').click()

    # Saves films in a list
    css_selector = '[class="columns is-multiline columns--slim"] a'
    wait_for_element(By.CSS_SELECTOR, css_selector)
    movies = driver.find_elements(By.CSS_SELECTOR, css_selector)

    movies_txt = ""

    print("\nMovies available:")
    for movie in movies:
        print(movie.text, end="\n\n")
        movies_txt += movie.text + "\n"

    return movies_txt


# Email sender Section Start
port = 1025
smtp_server = "localhost"  # or can use smtp.gmail.com
sender_email = "sender@automation.com"
receiver_email = "receiver@automation.com"


def send_email(city, msg):
    ''' Method that sends an email with the movies available '''
    parsed_msg = f"""\
Subject: Movies available in {city}

The movies available in {city} are:
{msg}
""".encode("utf-8")
    with smtplib.SMTP(smtp_server, port) as server:
        server.sendmail(sender_email, receiver_email, parsed_msg)
        print(f"Email sent successfully to {receiver_email}")
# Email sender Section End


if __name__ == "__main__":
    city = "Medellín"
    movies_txt = collect_movies(city)
    send_email(city, movies_txt)
