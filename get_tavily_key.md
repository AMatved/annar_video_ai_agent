# 🔑 Получение правильного API ключа Tavily

## Проблема:

Ваш ключ `tvly-tvly-dev-...` не работает (401 Unauthorized).

## Решение:

### Шаг 1: Получить production ключ

1. Откройте: https://tavily.com/
2. Нажмите **"Get Started Free"** или **"Sign Up"**
3. Зарегистрируйтесь (бесплатно)
4. Перейдите в: https://tavily.com/home/api-key
5. **Скопируйте API ключ**

⚠️ **ВАЖНО:** Production ключ начинается с `tvly-` (НЕ `tvly-dev-`)

Пример правильного ключа:
```
tvly-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

### Шаг 2: Авторизоваться с новым ключом

```bash
# Способ 1: Через команду
export PATH="C:\Users\User\AppData\Roaming\Python\Python313\Scripts:$PATH"
tvly login --api-key tvly-ВАШ_НОВЫЙ_КЛЮЧ

# Способ 2: Через переменную окружения
export TAVILY_API_KEY="tvly-ВАШ_НОВЫЙ_КЛЮЧ"
```

### Шаг 3: Протестировать

```bash
tvly search "TikTok trends 2025" --max-results 3 --json
```

---

## 💡 Альтернатива: Использовать ваш бесплатный поиск

У вас **УЖЕ ЕСТЬ** рабочий бесплатный поиск в `mcp_tools.py`:

```bash
python agent.py "Найди тренды TikTok и создай идеи"
```

**Преимущества:**
- ✅ БЕСПЛАТНО (без ограничений)
- ✅ Уже работает
- ✅ Никаких API ключей не нужно

**Недостатки:**
- ⚠️ Медленнее (~35 сек vs ~5 сек)
- ⚠️ DuckDuckGo вместо Tavily

---

## 🎯 Рекомендация:

1. **Для тестов сейчас:** Используйте ваш бесплатный поиск в agent.py
2. **Для production:** Получите production Tavily ключ

**Получить ключ:** https://tavily.com/home/api-key

---

## ✅ Что уже работает:

```bash
# Ваш бесплатный поиск (работает!)
cd C:\Users\User\video_creator_agent
python agent.py "Найди тренды TikTok"
```

**Tavily Skills будут работать** после получения production ключа!

---

Хотите использовать бесплатный поиск или получить production Tavily ключ? 🚀
