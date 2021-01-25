# TIML | Home Buch Bot 
[![Build version](https://img.shields.io/badge/version-0.9-red)]()
[![Python version](https://img.shields.io/badge/Python-3.8-green)]()

**Рабочий прототип - https://t.me/homebuchbot**

### Домашний бот бухгалтер. 
Бот помогает вести личный журнал доходов и расходов. Легкий в использовании, быстро настраиваемый и только самое необходимое. 

- Гибкая настройка категорий
- Автоподсчет суммы по категориям
- Необходимые экспресс отчеты


### Установка и запуск личного бота:
*В качестве базы данных, бот использует Postgresql.*

1. Создать виртуальное окружуние: 
    
    ```
    python -m venv env
    ```

2. Клонировать репозиторий:
   
   ```
   git clone https://github.com/acecrosser/timl_bot.git
   ```

3. Установить зависимости из файла `requirements.txt`

    ```
    python pip install -r requirements.txt
    ```

4. Создать файл `.env` где указать следующие данные:
    ```
    BOT_TOKEN=Ваш токен бота из botfatcher
    ADMIN_ID=Ваш ID 

    DBNAME=Имя БД
    USER=Пользователь БД
    PASSWORD=Пароль пользователя БД
    ```

5. Запустить файл connect.py из папки `data/dbase/` для создания таблиц в БД:

    ```
    python connect.py
    >>> БД успешна создана
    ```

6. Запустить Бота:
    
    ```
    python app.py
    ```

   