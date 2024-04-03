# Sign language translator model
Эта модель предназначена для перевода языка жестов в буквы по американской системе.

## Окружение
Для начала склонируйте проект и настройте окружение
```bash
git clone https://github.com/Maksim-Kotenkov/Sign-language-translator
cd Sign-language-translator
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## Запуск проекта
Датасеты для обучения не лежат в репозитории, поэтому прочтите README в папке data и сформируйте датасет.
Обучение можно запустить командой:
```bash
python3 train.py
```
