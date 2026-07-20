import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / '.env'

load_dotenv(ENV_PATH)


class PersonalData:
    """Корректные данные для авторизации загружаются из .env"""

    USER_EMAIL = os.getenv('USER_EMAIL')            # Электронная почта
    USER_PASSWORD = os.getenv('USER_PASSWORD')      # Пароль

    @classmethod
    def validate(cls) -> None:
        "Проверка, что данные пользователя загружены. Если None, то тесты не стартуют."
        if not cls.USER_EMAIL or not cls.USER_PASSWORD:
            raise EnvironmentError("Константы логина и пароля не найдены в файле .env"
                                   )


class IncorrectPersonalData:
    """Некорректные данные для авторизации"""

    USER_EMAIL = "test"                             # Электронная почта
    USER_PASSWORD = "test"                          # Пароль


PersonalData.validate()