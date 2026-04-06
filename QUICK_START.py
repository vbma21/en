"""
English Learning App - Quick Start Guide
Быстрая инструкция по запуску компонентов
"""

# ============================================================
# 📚 ENGLISH LEARNING APP - БЫСТРЫЙ ЗАПУСК
# ============================================================

"""

🎯 ВЫШАГОВАЯ ИНСТРУКЦИЯ:

─────────────────────────────────────────────────────────────

1️⃣  УСТАНОВКА ЗАВИСИМОСТЕЙ
    
    Откройте терминал и выполните:
    
    pip install -r requirements.txt
    
    Это установит:
    - Kivy       (фреймворк для мобильного UI)
    - Flask      (для REST API)
    - Requests   (для HTTP запросов)

─────────────────────────────────────────────────────────────

2️⃣  ВЫБОР РЕЖИМА РАБОТЫ

    А) КОНСОЛЬНОЕ ПРИЛОЖЕНИЕ (простой вариант)
    ─────────────────────────────────────
       python english_learning_backend.py
    
       Используется:
       - Для тестирования
       - Как справочник
       - Обучение в консоли

    ───────────────────────────────────────

    Б) МОБИЛЬНОЕ ПРИЛОЖЕНИЕ (Kivy UI)
    ─────────────────────────────────────
       python english_learning_mobile.py
    
       Используется:
       - На компьютере (тестирование)
       - На Android (после сборки через Buildozer)
       - Красивый графический интерфейс

    ───────────────────────────────────────

    В) REST API СЕРВЕР (для интеграции)
    ─────────────────────────────────────
       python english_learning_api.py
    
       API запустится на: http://localhost:5000
       
       Используется:
       - Для создания своего мобильного приложения
       - Интеграция с React Native, Flutter и т.д.
       - Сервер для веб-приложения

─────────────────────────────────────────────────────────────

3️⃣  ТЕСТИРОВАНИЕ API

    В отдельном терминале выполните:
    
    # Интерактивный режим
    python examples_and_tests.py interactive
    
    # Быстрый тест всех endpoints
    python examples_and_tests.py test
    
    # Примеры curl команд
    python examples_and_tests.py curl

─────────────────────────────────────────────────────────────

4️⃣  СОЗДАНИЕ ANDROID ПРИЛОЖЕНИЯ

    🔧 Требования:
    ─────────────
    - Python 3.9+
    - Java JDK 11+
    - Android SDK
    - Buildozer
    
    📦 Установка Buildozer:
    ═══════════════════════
    pip install buildozer
    
    🏗️  Сборка APK:
    ════════════════
    buildozer android debug
    
    Выходной файл: bin/englishlearning-1.0-debug.apk
    
    📱 Установка на смартфон:
    ═════════════════════════
    adb install -r bin/englishlearning-1.0-debug.apk

─────────────────────────────────────────────────────════════

📁 СТРУКТУРА ФАЙЛОВ:

    english_learning_backend.py   ← Основная логика приложения
    │
    ├─→ english_learning_api.py   ← REST API (Flask сервер)
    │
    ├─→ english_learning_mobile.py ← UI для мобильных (Kivy)
    │
    ├─→ examples_and_tests.py     ← Примеры и тесты
    │
    ├─→ buildozer.spec           ← Конфиг для Android сборки
    │
    ├─→ requirements.txt          ← Python зависимости
    │
    └─→ README.md                ← Подробная документация

─────────────────────────────────────────────────────────────

🎮 РЕКОМЕНДУЕМЫЕ ВАРИАНТЫ ИСПОЛЬЗОВАНИЯ:

    ✅ Для начинающих:
       → Запустить консольное приложение
       → python english_learning_backend.py

    ✅ Для тестирования UI:
       → Запустить Kivy приложение
       → python english_learning_mobile.py

    ✅ Для создания своего приложения:
       → Запустить REST API
       → python english_learning_api.py
       → Использовать endpoints для своего фронтенда

    ✅ Для Android:
       → Следовать гайду "СОЗДАНИЕ ANDROID ПРИЛОЖЕНИЯ"
       → buildozer android debug

─────────────────────────────────────────────────────────────

🌐 API ENDPOINTS (когда запущен Flask сервер):

    GET  /api/health              ← Проверка статуса
    GET  /api/word/next           ← Следующее слово
    GET  /api/word/show-answer    ← Показать ответ
    POST /api/word/check-answer   ← Проверить ответ
    GET  /api/statistics          ← Статистика
    POST /api/session/reset       ← Сбросить сессию
    GET  /api/words/list          ← Все слова

─────────────────────────────────────────────────────────────

🐛 ЕСЛИ ПОЯВИЛАСЬ ОШИБКА:

    "ModuleNotFoundError: No module named 'kivy'"
    → pip install kivy
    
    "ModuleNotFoundError: No module named 'flask'"
    → pip install flask flask-cors
    
    "Connection refused" (при запуске API тестов)
    → Убедитесь, что запущен: python english_learning_api.py
    
    "Buildozer not found"
    → pip install buildozer

─────────────────────────────────────────────────────────────

💡 СОВЕТЫ:

    1. Используйте виртуальное окружение:
       python -m venv venv
       source venv/bin/activate  # Linux/Mac
       venv\\Scripts\\activate    # Windows

    2. Для Android разработки смотрите полную документацию:
       README.md

    3. Добавьте свои слова в english_learning_backend.py

    4. Кастомизируйте интерфейс в english_learning_mobile.py

─────────────────────────────────────────────────────────────

🚀 ПОЛЕЗНЫЕ КОМАНДЫ:

    # Просмотр логов API
    python english_learning_api.py 2>&1 | tee api.log
    
    # Проверка синтаксиса
    python -m py_compile english_learning_backend.py
    
    # Форматирование кода
    pip install black
    black *.py
    
    # Проверка типов (Type Checking)
    pip install mypy
    mypy *.py

─────────────────────────────────────────────────────────────

📚 ДОПОЛНИТЕЛЬНЫЕ РЕСУРСЫ:

    Kivy Documentation:    https://kivy.org/doc/stable/
    Flask Documentation:   https://flask.palletsprojects.com/
    Buildozer Guide:       https://buildozer.readthedocs.io/
    Android Development:   https://developer.android.com/

─────────────────────────────────────────────────────────────

✨ ГОТОВО! 

Теперь вы можете выбрать подходящий режим и начать использование!

═════════════════════════════════════════════════════════════

"""

# ============================================================
# БЫСТРЫЙ ТЕСТ - убедитесь что всё работает
# ============================================================

if __name__ == "__main__":
    print(__doc__)
    
    print("\n" + "=" * 60)
    print("✅ ПРОВЕРКА ЗАВИСИМОСТЕЙ")
    print("=" * 60 + "\n")
    
    dependencies = {
        'kivy': 'Kivy (мобильный UI)',
        'flask': 'Flask (REST API)',
        'requests': 'Requests (HTTP клиент)'
    }
    
    for module, description in dependencies.items():
        try:
            __import__(module)
            print(f"✅ {description:<30} установлен")
        except ImportError:
            print(f"❌ {description:<30} НЕ установлен")
            print(f"   Установите с помощью: pip install {module}")
    
    print("\n" + "=" * 60)
    print("📝 ДЛЯ НАЧАЛА РАБОТЫ ВЫПОЛНИТЕ:")
    print("=" * 60)
    print("""
    1. Консольное приложение:
       python english_learning_backend.py
    
    2. Мобильное приложение:
       python english_learning_mobile.py
    
    3. REST API сервер:
       python english_learning_api.py
    """)
