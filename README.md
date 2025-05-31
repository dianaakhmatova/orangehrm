# 🧪 OrangeHRM Automated Testing

## 📌 Описание
Автоматизированное тестирование веб-приложения OrangeHRM с использованием Selenium WebDriver, PyTest, Allure и Page Object Model

## ⚙️ Технологии
- Python 3.11
- Selenium WebDriver
- PyTest
- Allure
- Page Object Model (POM)
- CI/CD (планируется через Jenkins или GitHub Actions)

## 📁 Структура проекта
```
orangehrm/
├── tests/         # Тестовые сценарии
├── pages/         # Page Object модели
├── utils/         # Вспомогательные утилиты (настройки, логгеры и т.п.)
├── reports/       # Allure-отчёты
├── screenshots/   # Скриншоты (например, Allure)
├── requirements.txt
└── README.md
```

## ▶️ Как запустить
```bash
pip install -r requirements.txt
pytest --alluredir=reports/
allure serve reports/
```


## 🧑‍💻 Автор
[Diana Akhmatova](https://github.com/dianaakhmatova)
