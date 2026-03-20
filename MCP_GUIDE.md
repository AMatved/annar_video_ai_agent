# 🔌 MCP (Model Context Protocol) Guide

## Что такое MCP?

**MCP = Model Context Protocol** - открытый стандарт от Anthropic для подключения AI к внешним данным и инструментам.

---

## 🆚 Сравнение: Ваш агент vs MCP

### Ваш текущий Video Creator Agent:
```
Gradio Web App → agent.py (прямой вызов) → OpenAI API
```
**Проблема:** Всё жёстко связано

### MCP архитектура:
```
MCP Client → MCP Protocol → MCP Server → Data Sources
```
**Преимущество:** Стандарт, переиспользование

---

## 📋 Ключевые понятия:

### **1. MCP Client**
Приложение которое ИСПОЛЬЗУЕТ MCP серверы
- Claude Desktop
- Ваше web-приложение
- Любое AI-приложение

### **2. MCP Server**
Предоставляет инструменты через MCP
- Tavily (поиск)
- Fetch (веб-страницы)
- **Ваш agent.py может стать MCP сервером!**

### **3. MCP Protocol**
Стандартный JSON-RPC формат общения

---

## 🎯 Будущие задания:

### Задание 1: Run tavily MCP service
```bash
npm install -g @tavily/mcp-server
tavily-mcp-server
```

### Задание 2: Выберите другой MCP сервис
- fetch-mcp (веб-страницы)
- filesystem-mcp (файлы)
- postgres-mcp (база данных)

### Задание 3: Запустите несколько MCP сервисов
```
Claude Desktop подключается к:
├── Tavily MCP (поиск)
├── Fetch MCP (веб)
└── Video Creator MCP (ваш агент!)
```

---

## 💡 Связь с вашим проектом:

### Сейчас (OpenAI Functions):
```python
from openai import OpenAI
client = OpenAI()
```

### Если MCP Server:
```python
from mcp import Server
server = Server("video-creator")
@server.tool()
async def save_idea(title: str):
    # Ваша логика
```

---

## Зачем это нужно?

| Без MCP | С MCP |
|---------|-------|
| Только OpenAI | Любые LLM модели |
| Свой протокол | Стандартный протокол |
| Не переиспользуется | Переиспользуется |

---

**Далее: Превратим agent.py в MCP Server! 🚀**
