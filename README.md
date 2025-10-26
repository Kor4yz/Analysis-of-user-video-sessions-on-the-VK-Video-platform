# Анализ видеосессий VK Видео  |  EDA → инсайты → рекомендации

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZykbZZXAXpsL4L23zqEr1y9f_eD8gnN8?usp=sharing)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://github.com/Kor4yz/Analysis-of-user-video-sessions-on-the-VK-Video-platform)
[![CI](https://github.com/Kor4yz/Analysis-of-user-video-sessions-on-the-VK-Video-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/Kor4yz/Analysis-of-user-video-sessions-on-the-VK-Video-platform/actions)

---

## 🎯 Задача
Однодневный срез пользовательских видеосессий на платформе **VK Видео**:  
очистка данных, исследовательский анализ (EDA), определение источников трафика и вовлечённости по платформам, формирование продуктовых рекомендаций.

---

## 🧰 Стек
`Python` (pandas, numpy, matplotlib, seaborn) · `Jupyter/Colab` · `SQL`

---

## 📊 Данные

| Поле | Описание |
|:--|:--|
| `user_id` | идентификатор пользователя |
| `platform` | платформа: android / ios |
| `video_id` | идентификатор ролика |
| `video_owner_id` | владелец контента |
| `src` | источник перехода (video_for_you, video_search, …) |
| `total_view_time` | время просмотра, сек |

Нули и сверхдлинные сессии (> 99-го перцентиля) исключаются при очистке.

---

## 🚀 Быстрый старт

```bash
git clone https://github.com/Kor4yz/Analysis-of-user-video-sessions-on-the-VK-Video-platform.git
cd Analysis-of-user-video-sessions-on-the-VK-Video-platform
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m src.run --input data/raw/video_sessions.csv --out reports/img
```
Или открой Colab-ноутбук и запусти Run all.

📈 Результаты (Executive summary)

Очистка данных. 4 503 записи → удалено 2 551 (56.6 %) с total_view_time ≤ 0; после среза по 99-му перцентилю — 1 932 валидных сессии.

Длина сессий. max = 6 486 с (~1.8 ч) · mean = 255 с (~4.25 м) · median = 3 с → преобладают короткие просмотры, нужен «хук» в первые 30 с.

Платформы. Android — 267 осознанных просмотров vs iOS — 112; но iOS удерживает дольше (349 с vs 216 с).

Охват. Уникальные пользователи: Android — 1 295, iOS — 548.

Источники. По объёму лидеры: video_for_you, video_search; по удержанию — video_playlist, video_my_history, video_my_bookmarks.

Контент. Топ-видео 1524754758426 — 15.9 ч суммарно; по среднему времени 1524760890996 — 30.4 мин.

Распределение. ~ 80 % сеансов < 30 с; ~ 85 % — < 5 мин.
🖼️ Примеры графиков
<p align="center"> 
  <img src="reports/img/Распределение_времени_просмотра.png" width="46%" /> 
  <img src="reports/img/Распределение_уникальных_видео_на_пользователя.png" width="46%" /> 
</p> 
<p align="center"> 
  <img src="reports/img/Топ_10_видео_по_среднему_времени_просмотра.png" width="46%" /> 
  <img src="reports/img/Топ_10_видео_по_суммарному_времени_просмотра.png" width="46%" /> 
</p>

🔍 Что делаем дальше
A. Продуктовые гипотезы (P1)

Hook 0–30 с. Усилить первые 30 с видео (динамичные превью, сильные титулы/обложки).

Продвижение персональных источников. Чаще показывать video_playlist и video_my_history — они дают длинные сессии.

Android удержание. Оптимизировать UX автоперехода/автовоспроизведения.

Метрики успеха

Retained-30s ↑ · Median session length ↑ · Avg session length ↑ · % sessions > 5 min ↑

B. Эксперименты (P1–P2)

A/B: новый преролл или обложки vs текущие.

Рекомендательная подмешка: 1 слот из my_history в ленте for_you.

C. Техника и данные (P0)

Проверить логирование старт/стоп для нулевых total_view_time.

Жёстко фильтровать ≤ 0 и > p99 в ETL-пайплайне.

📂 Материалы

📄 Отчёт (PDF): reports/VK.pdf

📓 Ноутбук (Colab): notebooks/VK.py

💾 SQL-запросы: sql/

🧪 Тесты и скрипты: src/
 · tests/

---

## 📬 Автор
**Денис Морозов**  
📧 Kor4yz@yandex.ru · [GitHub](https://github.com/Kor4yz) · [Telegram](https://t.me/kor4yz)
© 2025 · MIT License
