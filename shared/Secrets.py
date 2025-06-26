from urllib.parse import quote

MYSQL_URI = (
    f"mysql+asyncmy://"
    f"{quote('endless_arcade')}:"
    f"{quote('mysql@endless_arcade@angel-bhindi@6i5bsT1L1ElxAmkyQv4tIoWiVxcdGRH4jaJXPKs8ZsLPD3aqUwk6nllngXmCCk8XjvAXSXopKDU4nFOlNacN3hmh8PKHy0RFeM0J')}@/"
    f"{quote('heavenly')}"
    f"?unix_socket=/var/run/mysqld/mysqld.sock"
)

REDIS_PASSWORD = "redis@root@angel-bhindi@9NfplTGVg00LYbQ8Ja2ynU1COjCwI0k50g64qIu3c02vYlXsOGmBfB4yQkMkOTPwSXXhSmDTncJC7fewWf4YjGDZOTkoi8QtFhf"

BOT_TOKEN = "MTM4NzY4Nzc0Mjg3NTYzNTczMw.GnFDl4.apDxTzc9CTL6xnJ7M_L0lVkepZsGzczJYt8wD4"

