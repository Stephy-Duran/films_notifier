# films_notifier

Desarrollado con Python 3.10

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la prueba en local, primero se debe arrancar el servidor SMTPD de Python:

```bash
python -m smtpd -c DebuggingServer -n localhost:1025
```

Y después ejecutar el script:

```bash
python films_notifier.py
```

Para ejecutar la prueba con el servidor SMTP de Gmail, se debe configurar el archivo `.env` con las credenciales de la cuenta de Gmail con la estructura:

```bash
EMAIL_PASSWORD=LA_APP_PASSWORD_GENERADA
```

Esta contraseña se puede generar siguiendo los pasos de [Get Access With App Passwords](https://support.google.com/mail/answer/185833?hl=es-419)


## Recursos Utiles
[Send email with Python](https://realpython.com/python-send-email/#getting-started)
[Selenium Python](https://selenium-python.readthedocs.io/)
[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
[Waits in Selenium](https://www.selenium.dev/documentation/webdriver/waits/)
[POM Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
[CSS Selectors](https://flukeout.github.io)
[Get Access With App Passwords](https://support.google.com/mail/answer/185833?hl=es-419)

## Contacto

Para cualquier duda o sugerencia, puedes contactar por Slack a @Stephany.duran o @c.sandoval
