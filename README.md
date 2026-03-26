# 🛡️ Edge-AI Auditor: Autonomous Local Budget Monitoring

![Python](https://img.shields.io/badge/Python-3.10-blue)
![AI Model](https://img.shields.io/badge/Model-Gemma--3--4B-orange)
![Hardware](https://img.shields.io/badge/GPU-RTX_3060_Optimized-green)

**Edge-AI Auditor** — це гібридна аналітична система для автоматичного виявлення корупційних аномалій у місцевих бюджетах України. Система працює 100% локально на споживчому обладнанні (Edge Computing) без передачі чутливих даних в інтернет.

## 🚀 Основні можливості
* **Математична фільтрація (Z-Score):** Миттєвий пошук аномальних транзакцій у великих CSV/Excel масивах (Threshold > 3.0).
* **Локальний LLM-Аналіз:** Використання оптимізованої моделі `google/gemma-3-4b` для семантичного аналізу знайдених аномалій.
* **Повна конфіденційність:** Жодних запитів до хмарних API (OpenAI/Claude). Захист від витоку державної таємниці (Air-gapped ready).

## ⚙️ Як це працює
1. Скрипт завантажує таблицю `budget.csv`.
2. Алгоритм знаходить нетипові сплески витрат.
3. Локальний сервер LM Studio (через OpenAI API формат на `localhost`) генерує професійний звіт слідчого-аудитора за 5 секунд.

## 💻 Інструкція з запуску
1. Встановіть [LM Studio](https://lmstudio.ai/) та завантажте модель Gemma 3 4B.
2. Увімкніть **Local Server** на порту `1234`.
3. Встановіть залежності: `pip install pandas numpy openai`.
4. Запустіть скрипт: `python auditor.py`.

*Розроблено в рамках дослідження продуктивності SLM на архітектурі NVIDIA Ampere.*