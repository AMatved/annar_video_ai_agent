# 🎉 Tavily Skills установлены!

## ✅ Что уже сделано:

1. ✅ Установлены **7 Tavily Skills** в `~\.agents\skills\`
2. ✅ Установлен **Tavily CLI** (tvly)

## ⚠️ Что нужно сделать:

### Шаг 1: Добавить tvly в PATH

**Временное решение** (для текущей сессии):
```bash
export PATH="C:\Users\User\AppData\Roaming\Python\Python313\Scripts:$PATH"
```

**Постоянное решение** (Windows):
1. Откройте: **Система → О системе → Дополнительные параметры системы**
2. Нажмите: **Переменные среды**
3. В **Path** добавьте: `C:\Users\User\AppData\Roaming\Python\Python313\Scripts`
4. Перезапустите терминал

### Шаг 2: Получить API ключ Tavily

1. Откройте: https://tavily.com/
2. Зарегистрируйтесь (бесплатно)
3. Получите API ключ: https://tavily.com/home/api-key
4. **Бесплатно:** 1000 запросов/месяц

### Шаг 3: Авторизоваться

```bash
tvly login
# Введите ваш API ключ
```

---

## 🚀 Как использовать Tavily Skills

### В Claude Code (сейчас):

```
Ты: "Используй tavily-search для поиска трендов TikTok"
Я: → Автоматически вызову skill → Поиск через Tavily → Верну результаты
```

### Примеры использования:

```bash
# Поиск
tvly search "TikTok trends 2025" --json

# Извлечение контента
tvly extract https://example.com --json

# Глубокое исследование
tvly research "AI trends 2025" --json

# Краулинг сайта
tvly crawl https://example.com --max-pages 10 --json
```

---

## 📊 Доступные Skills:

| Skill | Описание | Команда |
|-------|----------|---------|
| **tavily-search** | Поиск в интернете | `tvly search` |
| **tavily-extract** | Извлечение контента | `tvly extract` |
| **tavily-research** | Глубокое исследование | `tvly research` |
| **tavily-crawl** | Краулинг сайтов | `tvly crawl` |
| **tavily-map** | Картирование сайта | `tvly map` |
| **tavily-cli** | CLI интерфейс | `tvly` |
| **tavily-best-practices** | Лучшие практики | - |

---

## 💡 Важно:

**Сейчас Skills работают, но НУЖЕН API ключ:**

1. Без API ключа: Skills не будут работать
2. С API ключом: Полноценный поиск в интернете

**Получить API ключ:** https://tavily.com/home/api-key

**Авторизация:**
```bash
tvly login
```

---

## 🎯 Что дальше?

После авторизации вы можете:

1. **Использовать в Claude Code:**
   ```
   "Найди актуальные тренды через tavily-search"
   ```

2. **Использовать в командной строке:**
   ```bash
   tvly search "TikTok trends" --json
   ```

3. **Комбинировать с вашим агентом:**
   - Ваш агент: DuckDuckGo (бесплатно)
   - Tavily Skills: Быстрый поиск (нужен API ключ)

---

## ⚡ Quick Start (после получения API ключа):

```bash
# 1. Авторизуйтесь
tvly login

# 2. Протестируйте
tvly search "TikTok trends 2025" --json

# 3. Используйте в Claude Code
# Просто скажите: "Используй tavily-search для поиска..."
```

---

**🎉 Skills готовы! Осталось только получить API ключ и авторизоваться!**

Получите ключ здесь: https://tavily.com/home/api-key
