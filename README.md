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
