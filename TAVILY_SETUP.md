# 🔍 Tavily MCP Setup Guide

## Проблема

Ваш Tavily MCP сервер требует API ключ для работы. Без него веб-поиск не будет functioning.

## ✅ Решение 1: Получить бесплатный API ключ Tavily (Рекомендуется)

### Шаг 1: Регистрация на Tavily

1. Откройте: https://tavily.com/
2. Нажмите **"Get Started Free"** или **"Sign Up"**
3. Зарегистрируйтесь (бесплатно - до 1000 запросов/месяц)

### Шаг 2: Получить API ключ

1. После регистрации войдите в аккаунт
2. Перейдите в: https://tavily.com/home/api-key
3. Скопируйте ваш API ключ

### Шаг 3: Добавить в .env файл

Откройте `.env` и добавьте:

```bash
TAVILY_API_KEY=tvly-ваш_ключ_здесь
```

### Шаг 4: Использовать встроенный Tavily клиент

Вместо использования внешнего MCP сервера, используйте встроенный:

```python
# В mcp_tools.py используйте прямой Tavily API
import requests

def tavily_search_direct(query: str, max_results: int = 10) -> str:
    """Direct Tavily API call"""
    api_key = os.environ.get("TAVILY_API_KEY")

    if not api_key:
        return "❌ TAVILY_API_KEY not set"

    response = requests.post(
        "https://api.tavily.com/search",
        json={
            "api_key": api_key,
            "query": query,
            "max_results": max_results
        }
    )

    return response.json()
```

---

## 🔄 Решение 2: Использовать другой MCP сервер (альтернатива)

### Вариант A: Brave Search MCP (бесплатный)

```json
{
  "mcpServers": {
    "brave-search": {
      "type": "sse",
      "url": "https://mcp.brave.search/prefix"
    }
  }
}
```

### Вариант B: Использовать DuckDuckGo (без API ключа)

Создайте простой поиск через DuckDuckGo:

```python
# Добавьте в mcp_tools.py
from duckduckgo_search import DDGS

def duckduckgo_search(query: str, max_results: int = 10) -> str:
    """Free web search using DuckDuckGo"""
    ddgs = DDGS()
    results = ddgs.text(query, max_results=max_results)

    output = []
    for result in results:
        output.append(f"Title: {result['title']}")
        output.append(f"URL: {result['link']}")
        output.append(f"Snippet: {result['body']}\n")

    return "\n".join(output)
```

Установка:
```bash
pip install duckduckgo-search
```

---

## 🚀 Решение 3: Агент БЕЗ веб-поиска (текущее состояние)

Ваш агент **УЖЕ РАБОТАЕТ** с 18 встроенными инструментами:

### ✅ Доступные функции:

```bash
# Идеи
python agent.py "Сохрани идею: утренняя рутина"

# Скрипты
python agent.py "Создай скрипт о продуктивности"

# Заголовки
python agent.py "Сгенерируй 5 вирусных заголовков"

# Хештеги
python agent.py "Покажи трендовые хештеги для TikTok"

# Проекты
python agent.py "Создай проект Мой влог"
```

### ⚠️ Не работает:
- Веб-поиск актуальных трендов (нужен API ключ)

---

## 📊 Текущий статус

| Функция | Статус |
|---------|--------|
| 18 встроенных инструментов | ✅ Работает |
| MCP Server (агент как сервис) | ✅ Работает |
| Веб-поиск через Tavily | ❌ Нужен API ключ |
| Claude Desktop интеграция | ✅ Работает |

---

## 🎯 Рекомендация

**Быстрое решение:**

1. **Получите бесплатный API ключ** на Tavily (5 минут):
   - https://tavily.com/
   - Бесплатно: 1000 запросов/месяц

2. **Или используйте DuckDuckGo** (полностью бесплатно):
   ```bash
   pip install duckduckgo-search
   ```

3. **Или продолжайте без веб-поиска**:
   - Агент всё равно мощный!
   - Использует встроенную базу знаний

---

## 🔧 Быстрый тест

**Проверить работу агента:**
```bash
cd C:\Users\User\video_creator_agent

# Тест 1: Базовые функции
python agent.py "Создай 5 вирусных заголовков"

# Тест 2: Идеи
python agent.py "Сохрани идею для TikTok про фитнес"

# Тест 3: Скрипты
python agent.py "Напиши скрипт 30 секунд о продуктивности"
```

**Всё работает!** ✅

Веб-поиск - это дополнительная функция, а не обязательная.
