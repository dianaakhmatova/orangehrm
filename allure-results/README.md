# 📊 Allure Reports

Автотесты сохраняют результаты в папку `allure-results/`, которая используется для построения отчётов.

Пример команды генерации отчёта:
```bash
pytest --alluredir=allure-results/
allure serve allure-results/
```