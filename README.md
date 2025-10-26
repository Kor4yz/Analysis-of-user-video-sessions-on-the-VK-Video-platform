# Анализ видеосессий VK Видео  |  EDA → инсайты → рекомендации
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ZykbZZXAXpsL4L23zqEr1y9f_eD8gnN8?usp=sharing)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Kor4yz/Analysis-of-user-video-sessions-on-the-VK-Video-platform/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://github.com/Kor4yz/Analysis-of-user-video-sessions-on-the-VK-Video-platform/blob/main/vk.py)
## Задача
Однодневный срез пользовательских видеосессий: очистка, EDA, источники трафика, вовлечённость по платформам, рекомендации.

## Стек
Python (pandas, numpy, matplotlib, seaborn), Jupyter/Colab, SQL

## Данные (словари полей)
| Поле | Описание |
|---|---|
| user_id | идентификатор пользователя |
| platform | android / ios |
| video_id | идентификатор ролика |
| video_owner_id | владелец контента |
| src | источник перехода (video_for_you, video_search, …) |
| total_view_time | время просмотра, сек |
Нули и сверхдлинные сессии отсекаются (99-й перцентиль).

## Результаты (Executive summary)

- **Очистка данных.** 4 503 записей → удалено 2 551 (56.6%) с `total_view_time ≤ 0`; срез по 99-му перцентилю → **1 932** валидных сессий.
- **Длина сессий.** max **6 486 c** (~1.8 ч); **mean 255 c** (~4.25 м); **median 3 c** → доминируют короткие сессии, нужен «хук» в первые 30 c.
- **Платформы.** Android: **267** осознанных просмотров vs iOS: **112**; но iOS удерживает дольше (**mean 349 c** vs **216 c**).
- **Охват.** Уникальные пользователи: Android **1 295**, iOS **548**.
- **Источники.** По объёму лидируют **video_for_you** и **video_search**; по удержанию — **video_playlist**, **video_my_history**, **video_my_bookmarks**.
- **Контент.** Топ-видео `1524754758426`: **15.9 ч** суммарно; топ по среднему `1524760890996`: **30.4 мин**.
- **Распределение.** ~**80%** сеансов короче 30 c, ~**85%** — короче 5 мин.


Материалы

Отчёт (PDF): reports/VK.pdf

Ноутбук: notebooks/VK.py

Результаты (основные графики)
## Результаты (примеры графиков)

<p align="center">
  <img src="reports/img/Распределение_времени_просмотра.png" width="46%" />
  <img src="reports/img/Распределение_уникальных_видео_на_пользователя.png" width="46%" />
</p>
<p align="center">
  <img src="reports/img/Топ_10_видео_по_среднему_времени_просмотра.png" width="46%" />
  <img src="reports/img/Топ_10_видео_по_суммарному_времени_просмотра.png" width="46%" />
</p>

## Что делаем дальше

**A. Продуктовые гипотезы (приоритет P1)**
1) *Hook 0–30 c*: усилим первые 30 c (динамичные превью, сильный титул/обложка).
2) *Промо персональных источников*: чаще предлагать **video_playlist** / **video_my_history** (глубокие сессии).
3) *Android удержание*: оптимизировать UX автоперехода/автовоспроизведения.

**Метрики успеха**
- Retained-30s ↑, Median session length ↑, Avg session length ↑, % sessions >5 min ↑.

**B. Эксперименты (P1–P2)**
- **A/B**: новый преролл/обложки vs текущие; целевая страница с бустом персональных источников.
- **Рекомендательная подмешка**: 1 слот «из *my_history*» в ленте *for_you*.

**C. Техника и данные (P0)**
- Устранить нулевые `total_view_time`: проверить логирование старт/стоп.
- Обязательная фильтрация <=0 и >p99 в пайплайне.


---

## 📬 Автор
**Денис Морозов**  
📧 Kor4yz@yandex.ru · [GitHub](https://github.com/Kor4yz) · [Telegram](https://t.me/kor4yz)
