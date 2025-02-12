def send_email(message, recipient, sender="university.help@gmail.com"):
    # Проверка email адресов
    def is_valid_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    # Проверка отправки некорректному получателю
    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return  # Отмена функции, если адреса некорректны

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return  # Отмена функции при попытке отправить письмо самому себе

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


# Результат
send_email("Привет!", "vasyok1337@gmail.com")  # Письмо должно быть успешно отправлено
send_email("Привет!", "kolyn_chik.34@mail.ru",
           sender="university.info@gmail.com")  # Письмо должно быть успешно отправлено нестандартному отправителю
send_email("Привет!", "university.help@gmail.com",
           sender="university.help@gmail.com")  # Нельзя отправить письмо самому себе
send_email("Привет!", "fun_link@network.uk",
           sender="university.help@gmail.com")  # Невозможно отправить письмо (некорректный адрес)
