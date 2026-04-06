# 📚 English Learning App - Документация

## Обзор проекта

Модернизированное приложение для изучения английских слов с поддержкой:
- 🖥️ Консольное приложение
- 📱 Мобильное приложение (Kivy)
- 🌐 REST API (Flask)
- 📦 Android приложение (через Buildozer)

---

## 📁 Структура файлов

```
.
├── english_learning_backend.py    # Основная бизнес-логика
├── english_learning_api.py        # REST API для мобильных приложений
├── english_learning_mobile.py     # Kivy интерфейс для мобильных устройств
├── buildozer.spec                 # Конфигурация для сборки APK
├── requirements.txt               # Python зависимости
└── README.md                      # Эта документация
```

---

## 🚀 Быстрый старт

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Запуск консольного приложения

```bash
python english_learning_backend.py
```

### 3. Запуск мобильного интерфейса (Kivy)

```bash
python english_learning_mobile.py
```

### 4. Запуск REST API

```bash
python english_learning_api.py
```

API будет доступен по адресу: `http://localhost:5000`

---

## 💻 Использование API

### Endpoints

#### Проверка здоровья API
```
GET /api/health
```
**Ответ:**
```json
{
  "status": "OK",
  "message": "English Learning API is running"
}
```

#### Получить следующее слово
```
GET /api/word/next
```
**Ответ:**
```json
{
  "success": true,
  "data": {
    "word_id": 1,
    "english": "mayonnaise",
    "statistics": {
      "correct": 0,
      "incorrect": 0,
      "total": 0,
      "accuracy": 0.0
    }
  }
}
```

#### Показать ответ
```
GET /api/word/show-answer
```
**Ответ:**
```json
{
  "success": true,
  "data": {
    "answer": "майонез"
  }
}
```

#### Проверить ответ пользователя
```
POST /api/word/check-answer
Content-Type: application/json

{
  "translation": "майонез"
}
```
**Ответ:**
```json
{
  "success": true,
  "data": {
    "is_correct": true,
    "correct_answer": "майонез",
    "statistics": {
      "correct": 1,
      "incorrect": 0,
      "total": 1,
      "accuracy": 100.0
    }
  }
}
```

#### Получить статистику
```
GET /api/statistics
```

#### Сбросить сессию
```
POST /api/session/reset
```

#### Получить список всех слов
```
GET /api/words/list
```

---

## 📱 Создание Android приложения

### Предварительные требования

1. **Java JDK 11 или выше**
   ```bash
   java -version
   ```

2. **Android SDK** (установить через Android Studio)
   - Минимальный API уровень: 21
   - Целевой API уровень: 31+

3. **Buildozer**
   ```bash
   pip install buildozer
   ```

4. **Зависимости (Linux/Ubuntu)**
   ```bash
   sudo apt-get update
   sudo apt-get install -y \
     build-essential \
     git \
     python3 \
     python3-dev \
     libffi-dev \
     libssl-dev \
     openjdk-11-jdk \
     libncurses5 \
     virtualenv
   ```

### Сборка APK

1. **Подготовка проекта**
   ```bash
   buildozer android debug
   ```

2. **Установка на устройство**
   ```bash
   adb install -r bin/englishlearning-1.0-debug.apk
   ```

3. **�из версия**
   ```bash
   buildozer android release
   ```

---

## 🏗️ Архитектура приложения

### Backend (`english_learning_backend.py`)

**Классы:**

1. **`Word`** - Модель данных для слова
   - `english: str` - Английское слово
   - `russian: str` - Русский перевод
   - `id: int` - Уникальный ID

2. **`WordDatabase`** - Управление базой слов
   - `get_all_words()` - Получить все слова
   - `get_random_word()` - Получить случайное слово
   - `get_word_by_id(word_id)` - Получить слово по ID

3. **`LearningSession`** - Управление сессией обучения
   - `start_new_word()` - Начать новое слово
   - `check_answer(user_translation)` - Проверить ответ
   - `get_statistics()` - Получить статистику сессии

4. **`EnglishLearningApp`** - Главный класс приложения
   - `next_word()` - Перейти к следующему слову
   - `show_answer()` - Показать ответ
   - `submit_answer(translation)` - Отправить ответ
   - `get_stats()` - Получить общую статистику

### REST API (`english_learning_api.py`)

Использует **Flask** с поддержкой CORS для обработки HTTP запросов от мобильных приложений.

### Мобильный UI (`english_learning_mobile.py`)

Использует **Kivy** для создания нативного мобильного интерфейса.

---

## 🎯 Использование с другими фреймворками

### React Native

Используйте REST API для подключения к приложению:

```javascript
// Получить следующее слово
fetch('http://your-api-server/api/word/next')
  .then(res => res.json())
  .then(data => console.log(data));

// Проверить ответ
fetch('http://your-api-server/api/word/check-answer', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ translation: 'майонез' })
});
```

### Flutter

```dart
final response = await http.get(
  Uri.parse('http://your-api-server/api/word/next'),
);
```

---

## 📊 Статистика и метрики

Приложение отслеживает:
- ✅ Количество правильных ответов
- ❌ Количество неправильных ответов
- 🎯 Процент точности
- ⏱️ Время проведённое на обучение
- 📝 Всего обработано слов

---

## ⚙️ Конфигурация

### Добавление новых слов

Редактируйте метод `_init_words()` в классе `WordDatabase`:

```python
def _init_words(self) -> None:
    words_data = [
        ("new_english_word", "новое русское слово"),
        # ... добавьте новые пары
    ]
```

### Изменение параметров API

В файле `english_learning_api.py`:

```python
if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',  # Доступен со всех IP
        port=5000        # Порт
    )
```

---

## 🐛 Решение проблем

### Ошибка: "No module named 'kivy'"
```bash
pip install kivy
```

### Ошибка: "No module named 'flask'"
```bash
pip install flask flask-cors
```

### Ошибка при сборке APK
1. Убедитесь, что установлены все зависимости
2. Используйте Python 3.9 или выше
3. Используйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

### Медленное подключение к API
- Убедитесь, что сервер запущен
- Проверьте сетевое соединение
- Используйте локальный IP адрес вместо `localhost`

---

## 📈 Возможные улучшения

- [ ] Добавить базу данных (SQLite/PostgreSQL)
- [ ] Реализовать систему уровней сложности
- [ ] Добавить синхронизацию между устройствами
- [ ] Реализовать систему рейтинга
- [ ] Добавить озвучку слов
- [ ] Реализовать категории слов
- [ ] Добавить режим мультиплеера
- [ ] Создать веб-версию (React/Vue)

---

## 📝 Лицензия

Open Source - свободно используйте в своих проектах

---

## 👨‍💻 Поддержка

Для вопросов и предложений откройте Issue на GitHub.

---

**Версия:** 1.0.0  
**Последнее обновление:** 2026-04-04
