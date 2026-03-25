# 🚀 Platform Integrations Guide

Video Creator Agent теперь поддерживает **автоматизацию социальных сетей** через официальные API!

## ✨ Возможности

### 🔗 Управление аккаунтами
- Добавление нескольких аккаунтов на каждой платформе
- Безопасное хранение токенов доступа
- Управление через agent.py

### 📤 Автоматический постинг
- Публикация видео на TikTok, Instagram, YouTube
- Массовый постинг на несколько платформ одновременно
- Планирование публикаций

### 📊 Аналитика
- Просмотр статистики (views, likes, comments)
- Сравнение показателей на разных платформах
- Отслеживание вовлеченности

### 🔥 Поиск трендов
- Автоматический поиск вирусных хештегов
- Анализ трендов по нишам
- Интеграция с веб-поиском

---

## 📋 Поддерживаемые платформы

| Платформа | Статус API | Возможности |
|-----------|-----------|-------------|
| **TikTok** | ✅ Поддерживается | Постинг, аналитика, тренды |
| **Instagram** | ✅ Поддерживается | Reels, аналитика |
| **YouTube** | ✅ Поддерживается | Shorts, аналитика |
| **Xiaohongshu** | ⚠️ Ограниченно | Только руководства |

---

## 🚀 Быстрый старт

### 1. Добавление аккаунта

```bash
python agent.py
```

Затем в агенте:
```
Добавь аккаунт TikTok с username @mychannel и account_id 123456
```

Или через функцию:
```python
from platform_integrations import add_social_account

result = add_social_account(
    platform="tiktok",
    username="mychannel",
    account_id="123456",
    access_token="your_oauth_token"
)
```

### 2. Список аккаунтов

```
Покажи все мои аккаунты
```

### 3. Постинг видео

```
Опубликуй video.mp4 на TikTok с описанием "Привет, мир!"
```

### 4. Получение аналитики

```
Покажи аналитику TikTok
```

---

## 🔐 Настройка API доступа

### TikTok API

1. **Регистрация приложения**
   - Перейдите: https://developers.tiktok.com/
   - Создайте приложение
   - Получите `client_key` и `client_secret`

2. **OAuth 2.0_flow**
   ```python
   # Перенаправьте пользователя на:
   auth_url = f"https://open.tiktokapis.com/v2/authorize/?client_key={CLIENT_KEY}&scope=user.info.basic,video.upload&response_type=code&redirect_uri={REDIRECT_URI}"

   # Получите код и обменяйте на токен:
   token_response = requests.post("https://open.tiktokapis.com/v2/oauth/token/", {
       "client_key": CLIENT_KEY,
       "client_secret": CLIENT_SECRET,
       "code": auth_code,
       "grant_type": "authorization_code"
   })

   access_token = token_response.json()["access_token"]
   open_id = token_response.json()["open_id"]
   ```

3. **Добавление аккаунта**
   ```python
   add_social_account(
       platform="tiktok",
       username="mychannel",
       account_id=open_id,
       access_token=access_token
   )
   ```

### Instagram Graph API

1. **Meta Apps**
   - https://developers.facebook.com/apps/
   - Создайте приложение
   - Добавьте Instagram Graph API
   - Получите токен доступа

2. **Разрешения**
   - `instagram_basic`, `instagram_content_publish`, `instagram_manage_insights`

3. **Добавление аккаунта**
   ```python
   add_social_account(
       platform="instagram",
       username="mychannel",
       account_id=instagram_user_id,
       access_token=access_token
   )
   ```

### YouTube Data API v3

1. **Google Cloud Console**
   - https://console.cloud.google.com/
   - Создайте проект
   - Включите YouTube Data API v3
   - Создайте OAuth 2.0 credentials

2. **OAuth Scope**
   ```
   https://www.googleapis.com/auth/youtube.upload
   ```

3. **Добавление аккаунта**
   ```python
   add_social_account(
       platform="youtube",
       username="mychannel",
       account_id=channel_id,
       access_token=oauth_token
   )
   ```

---

## 🛠️ Доступные функции

### add_social_account
Добавить аккаунт социальной сети.

**Параметры:**
- `platform` (обяз): tiktok, instagram, youtube, xiaohongshu
- `username` (обяз): Имя пользователя
- `account_id` (обяз): Уникальный ID аккаунта
- `access_token` (опц): OAuth токен доступа
- `api_key` (опц): API ключ (альтернатива токену)

**Пример:**
```python
add_social_account(
    platform="tiktok",
    username="creator123",
    account_id="789456123",
    access_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
)
```

### list_social_accounts
Показать все настроенные аккаунты.

**Пример:**
```python
accounts = list_social_accounts()
# Вывод:
# 📋 Configured Accounts:
#
# 🎯 TIKTOK
#   ✅ @creator123 (Creator Channel)
#   ✅ @fitness_pro (Fitness Pro)
#
# 🎯 INSTAGRAM
#   ✅ @lifestyle_daily (Lifestyle Daily)
```

### post_to_platforms
Опубликовать видео на платформе.

**Параметры:**
- `platform` (обяз): tiktok, instagram, youtube
- `video_path` (обяз): Путь к видеофайлу
- `caption` (обяз): Описание видео
- `username` (опц): Конкретный аккаунт (если не указано - на все)

**Пример:**
```python
# Опубликовать на один аккаунт
post_to_platforms(
    platform="tiktok",
    video_path="videos/my_video.mp4",
    caption="Мой новый вирусный видео! #viral #fyp",
    username="creator123"
)

# Опубликовать на все аккаунты платформы
post_to_platforms(
    platform="instagram",
    video_path="videos/reel.mp4",
    caption="Новый рилс! #reels #explore"
)
```

### get_platform_analytics
Получить аналитику платформы.

**Параметры:**
- `platform` (обяз): tiktok, instagram, youtube
- `username` (опц): Конкретный аккаунт

**Пример:**
```python
get_platform_analytics(platform="tiktok", username="creator123")
# Вывод:
# 📊 Analytics for @creator123 (TIKTOK)
#
# 👁️  Views: 125K
# ❤️  Likes: 8.5K
# 💬 Comments: 342
# 🔄 Shares: 1.2K
#
# 📊 Engagement Rate: 8.3%
```

### get_registration_help
Получить руководство по регистрации и настройке API.

**Параметры:**
- `platform` (обяз): tiktok, instagram, youtube, xiaohongshu

**Пример:**
```python
help_text = get_registration_help("tiktok")
print(help_text)
# Полное руководство по регистрации TikTok аккаунта и настройке API
```

### discover_trending_topics
Найти трендовые хештеги для ниши.

**Параметры:**
- `niche` (обяз): Ниша (fitness, cooking, tech, etc.)
- `platform` (опц): Платформа (default: tiktok)

**Пример:**
```python
discover_trending_topics(niche="fitness", platform="tiktok")
# Вывод:
# 🔥 Trending hashtags for fitness on tiktok:
# #fyp
# #viral
# #trending
# #foryou
# #fitness
# #fitnesstok
# #fitnesslife
```

---

## 📁 Структура файлов

```
video_creator_agent/
├── platform_integrations.py    # Модуль интеграций
├── accounts.json               # Хранилище аккаунтов (создается автоматически)
├── agent.py                    # Агент с поддержкой платформ
└── PLATFORM_INTEGRATIONS.md    # Эта документация
```

### accounts.json формат
```json
[
  {
    "platform": "tiktok",
    "account_id": "789456123",
    "username": "creator123",
    "access_token": "eyJhbGci...",
    "refresh_token": "eyJhbGci...",
    "token_expires": "2024-12-31T23:59:59",
    "api_key": null,
    "display_name": "Creator Channel",
    "is_active": true,
    "created_at": "2024-03-20T10:30:00"
  }
]
```

---

## ⚠️ Важные предупреждения

### Безопасность
- **НИКОГДА** не коммитьте `accounts.json` в git
- Храните токены в зашифрованном виде в production
- Используйте переменные окружения для секретов
- Реализуйте refresh токенов

### Ограничения API
- **TikTok**: Лимиты на постинг в день
- **Instagram**: Требует верификации бизнеса
- **YouTube**: Квота на загрузку видео в день

### Условия использования (ToS)
- Автоматическая регистрация аккаунтов нарушает ToS большинства платформ
- Используйте только **легитимные** аккаунты
- Получите согласие пользователей на OAuth авторизацию
- Соблюдайте правила каждой платформы

---

## 🧪 Тестирование

### Тестирование без реального API
```python
from platform_integrations import AccountManager, Account

manager = AccountManager("test_accounts.json")

# Создайте тестовый аккаунт
test_account = Account(
    platform="tiktok",
    account_id="test_123",
    username="test_user",
    display_name="Test Account"
)

manager.add_account(test_account)
print(manager.list_accounts())
```

### Тестирование с мок данными
```python
from platform_integrations import TikTokClient, Account

account = Account(
    platform="tiktok",
    account_id="test",
    username="test"
)

client = TikTokClient(account)
result = client.post_video(
    video_path="test.mp4",
    caption="Test video"
)
# Вернет мок ответ (не публикует на самом деле)
```

---

## 🔄 Roadmap

- [ ] Планирование постов (schedule_post)
- [ ] Автоматический refresh токенов
- [ ] Массовый постинг на все платформы
- [ ] Расширенная аналитика
- [ ] A/B тестирование заголовков
- [ ] Интеграция с планировщиками контента
- [ ] Поддержка LinkedIn, Twitter/X

---

## 📞 Поддержка

### Документация API
- **TikTok**: https://developers.tiktok.com/doc/
- **Instagram**: https://developers.facebook.com/docs/instagram-api/
- **YouTube**: https://developers.google.com/youtube/v3

### Сообщество
- GitHub Issues: https://github.com/AMatved/annar_video_ai_agent/issues
- Документация: https://github.com/AMatved/annar_video_ai_agent/wiki

---

## 🎯 Примеры использования

### Пример 1: Полный workflow
```bash
# Запустите агента
python agent.py

# В агенте:
> Добавь аккаунт TikTok @myfitness с ID 123456
✅ Account @myfitness (tiktok) added successfully

> Покажи мои аккаунты
📋 Configured Accounts:
🎯 TIKTOK
  ✅ @myfitness (My Fitness Channel)

> Найди тренды для fitness ниши
🔥 Trending hashtags: #fitness #workout #fitfam #gym

> Опубликуй workout.mp4 с описанием "Daily workout! #fitness"
✅ Video posted successfully to TikTok!
```

### Пример 2: Мультипостинг
```python
from platform_integrations import PlatformAutomation

automation = PlatformAutomation()

# Постинг на все платформы
results = automation.post_to_all_platforms(
    video_path="final_video.mp4",
    caption="My new viral video!",
    platforms=["tiktok", "instagram", "youtube"]
)

for platform, result in results.items():
    print(f"{platform}: {result.get('message', result.get('error'))}")
```

### Пример 3: Аналитика всех аккаунтов
```python
from platform_integrations import PlatformAutomation

automation = PlatformAutomation()
analytics = automation.get_all_analytics()

for account, data in analytics.items():
    if data.get("success"):
        print(f"{account}: {data['views']} views")
```

---

**Создано с ❤️ для контент-креаторов**

*Последнее обновление: 2024-03-20*
