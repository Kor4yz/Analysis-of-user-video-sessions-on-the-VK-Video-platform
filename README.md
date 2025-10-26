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


---

## 📬 Автор
**Денис Морозов**  
📧 Kor4yz@yandex.ru · [GitHub](https://github.com/Kor4yz) · [Telegram](https://t.me/kor4yz)
