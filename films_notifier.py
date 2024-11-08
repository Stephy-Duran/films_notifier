import smtplib
import ssl
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

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
        print(f'ERROR: The city {
              city} is not in the list, please check if is a valid city')

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
load_dotenv()

port = 465  # For SSL
password = os.getenv("EMAIL_PASSWORD", "password")
smtp_server = "smtp.gmail.com"

sender_email = "testmailcode016@gmail.com"
receiver_email = "testmailcode016+receiver@gmail.com"

context = ssl.create_default_context()


def send_email(city, msg):
    ''' Method that sends an email with the movies available '''
    parsed_msg = f"""\
Subject: Movies available in {city}

The movies available in {city} are:
{msg}
""".encode("utf-8")

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login("testmailcode016@gmail.com", password)
        server.sendmail(sender_email, receiver_email, parsed_msg)


def send_mutliple_emails(targets):
    ''' Send an email to multiple targets '''

    plain_msg = """\
Thank you for attending our event.

If you have any questions, feel free to contact us."""

    html_msg = """\
<html>
    <body>
        <p>Thank you for attending our event.</p>
        <p>If you have any questions, feel free to contact us.</p>
    </body>
</html>
"""

    message = MIMEMultipart("alternative")
    message["Subject"] = "Send email to multiple targets and HTML"
    message["From"] = sender_email
    message["To"] = ", ".join(targets)

    part1 = MIMEText(plain_msg, "plain")
    part2 = MIMEText(html_msg, "html")

    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login("testmailcode016@gmail.com", password)
        server.sendmail(sender_email, targets, message.as_string())
# Email sender Section End


if __name__ == "__main__":
    city = "Medellín"
    movies_txt = collect_movies(city)
    send_email(city, movies_txt)
    driver.quit()

    # target_emails = []
    # send_mutliple_emails(target_emails)
