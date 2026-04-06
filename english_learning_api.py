"""
English Learning App - REST API
Для использования с мобильным приложением (React Native, Flutter, Kivy и т.д.)
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from english_learning_backend import EnglishLearningApp
import logging

# Инициализация
app = Flask(__name__)
CORS(app)  # Разрешить запросы с мобильных приложений

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Глобальный экземпляр приложения
learning_app = EnglishLearningApp()


@app.route('/api/health', methods=['GET'])
def health_check():
    """Проверка здоровья API"""
    return jsonify({
        "status": "OK",
        "message": "English Learning API is running"
    }), 200


@app.route('/api/word/next', methods=['GET'])
def get_next_word():
    """Получить следующее слово"""
    try:
        result = learning_app.next_word()
        return jsonify({
            "success": True,
            "data": result
        }), 200
    except Exception as e:
        logger.error(f"Error getting next word: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/word/current', methods=['GET'])
def get_current_word():
    """Получить текущее слово в формате для UI"""
    try:
        return jsonify({
            "success": True,
            "data": {
                "english": learning_app.get_current_word_english(),
                "Russian": learning_app.get_current_word_russian()
            }
        }), 200
    except Exception as e:
        logger.error(f"Error getting current word: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/word/show-answer', methods=['GET'])
def show_answer():
    """Показать ответ"""
    try:
        answer = learning_app.show_answer()
        return jsonify({
            "success": True,
            "data": {
                "answer": answer
            }
        }), 200
    except Exception as e:
        logger.error(f"Error showing answer: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/word/check-answer', methods=['POST'])
def check_answer():
    """Проверить ответ пользователя"""
    try:
        data = request.get_json()
        user_translation = data.get('translation', '')
        
        if not user_translation:
            return jsonify({
                "success": False,
                "error": "Translation is required"
            }), 400
        
        result = learning_app.submit_answer(user_translation)
        return jsonify({
            "success": True,
            "data": result
        }), 200
    except Exception as e:
        logger.error(f"Error checking answer: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    """Получить статистику"""
    try:
        stats = learning_app.get_stats()
        return jsonify({
            "success": True,
            "data": stats
        }), 200
    except Exception as e:
        logger.error(f"Error getting statistics: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/session/reset', methods=['POST'])
def reset_session():
    """Сбросить сессию"""
    try:
        learning_app.reset()
        return jsonify({
            "success": True,
            "message": "Session reset successfully"
        }), 200
    except Exception as e:
        logger.error(f"Error resetting session: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/words/list', methods=['GET'])
def get_all_words():
    """Получить список всех слов"""
    try:
        words = learning_app.session.word_database.get_all_words()
        words_data = [word.to_dict() for word in words]
        
        return jsonify({
            "success": True,
            "data": {
                "total": len(words_data),
                "words": words_data
            }
        }), 200
    except Exception as e:
        logger.error(f"Error getting words list: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Обработчик 404"""
    return jsonify({
        "success": False,
        "error": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Обработчик 500"""
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500


if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("English Learning App - REST API")
    print("=" * 60)
    print("\nAPI доступен по адресу: http://localhost:5000")
    print("\nДоступные endpoints:")
    print("  GET  /api/health              - Проверка здоровья")
    print("  GET  /api/word/next           - Следующее слово")
    print("  GET  /api/word/show-answer    - Показать ответ")
    print("  POST /api/word/check-answer   - Проверить ответ")
    print("  GET  /api/statistics          - Статистика")
    print("  POST /api/session/reset       - Сбросить сессию")
    print("  GET  /api/words/list          - Все слова")
    print("=" * 60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
