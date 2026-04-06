"""
English Learning App - Примеры использования и тесты
"""

import requests
import json
from typing import Dict

# Базовый URL API (измените на свой сервер)
BASE_URL = "http://localhost:5000"


class APITester:
    """Класс для тестирования API"""
    
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
    
    def test_health(self) -> bool:
        """Проверить доступность API"""
        try:
            response = self.session.get(f"{self.base_url}/api/health")
            print(f"✅ Health Check: {response.json()}")
            return response.status_code == 200
        except Exception as e:
            print(f"❌ Health Check Error: {e}")
            return False
    
    def get_next_word(self) -> Dict:
        """Получить следующее слово"""
        try:
            response = self.session.get(f"{self.base_url}/api/word/next")
            data = response.json()
            print(f"📚 New Word: {data['data']['english']}")
            return data
        except Exception as e:
            print(f"❌ Error: {e}")
            return {}
    
    def show_answer(self) -> str:
        """Показать ответ"""
        try:
            response = self.session.get(f"{self.base_url}/api/word/show-answer")
            data = response.json()
            answer = data['data']['answer']
            print(f"🔤 Answer: {answer}")
            return answer
        except Exception as e:
            print(f"❌ Error: {e}")
            return ""
    
    def check_answer(self, translation: str) -> Dict:
        """Проверить ответ пользователя"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/word/check-answer",
                json={"translation": translation},
                headers={"Content-Type": "application/json"}
            )
            data = response.json()
            
            if data['data']['is_correct']:
                print(f"✅ Correct! Answer was: {data['data']['correct_answer']}")
            else:
                print(f"❌ Wrong! Answer was: {data['data']['correct_answer']}")
            
            return data
        except Exception as e:
            print(f"❌ Error: {e}")
            return {}
    
    def get_statistics(self) -> Dict:
        """Получить статистику"""
        try:
            response = self.session.get(f"{self.base_url}/api/statistics")
            stats = response.json()['data']['session_stats']
            
            print("\n📊 STATISTICS:")
            print(f"   ✅ Correct: {stats['correct']}")
            print(f"   ❌ Incorrect: {stats['incorrect']}")
            print(f"   📝 Total: {stats['total']}")
            print(f"   🎯 Accuracy: {stats['accuracy']}%")
            print(f"   ⏱️  Duration: {stats['session_duration']}\n")
            
            return stats
        except Exception as e:
            print(f"❌ Error: {e}")
            return {}
    
    def reset_session(self) -> bool:
        """Сбросить сессию"""
        try:
            response = self.session.post(f"{self.base_url}/api/session/reset")
            print(f"🔄 Session Reset: {response.json()['message']}")
            return response.status_code == 200
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def get_all_words(self) -> Dict:
        """Получить список всех слов"""
        try:
            response = self.session.get(f"{self.base_url}/api/words/list")
            data = response.json()['data']
            print(f"📚 Total words in database: {data['total']}")
            return data
        except Exception as e:
            print(f"❌ Error: {e}")
            return {}


def interactive_session():
    """Интерактивная сессия обучения"""
    print("\n" + "=" * 60)
    print("🎓 ENGLISH LEARNING - INTERACTIVE SESSION")
    print("=" * 60 + "\n")
    
    tester = APITester()
    
    # Проверка доступности API
    if not tester.test_health():
        print("❌ API is not available. Make sure the server is running.")
        print("Run: python english_learning_api.py")
        return
    
    print("\n" + "=" * 60 + "\n")
    
    # Основной цикл
    while True:
        # Получить новое слово
        tester.get_next_word()
        
        while True:
            user_input = input(
                "\nOptions:\n"
                "1 - Show answer\n"
                "2 - Submit answer\n"
                "3 - Next word\n"
                "4 - Statistics\n"
                "5 - Exit\n"
                "Choice: "
            )
            
            if user_input == "1":
                tester.show_answer()
            
            elif user_input == "2":
                answer = input("Enter translation: ")
                tester.check_answer(answer)
                break
            
            elif user_input == "3":
                break
            
            elif user_input == "4":
                tester.get_statistics()
            
            elif user_input == "5":
                print("\n👋 Goodbye!")
                return
            
            else:
                print("❌ Invalid choice!")


def test_api_endpoints():
    """Тестирование всех API endpoints"""
    print("\n" + "=" * 60)
    print("🧪 API ENDPOINTS TEST")
    print("=" * 60 + "\n")
    
    tester = APITester()
    
    # 1. Health check
    print("1️⃣  Testing health check...")
    tester.test_health()
    
    # 2. Get next word
    print("\n2️⃣  Testing get next word...")
    tester.get_next_word()
    
    # 3. Show answer
    print("\n3️⃣  Testing show answer...")
    tester.show_answer()
    
    # 4. Check correct answer
    print("\n4️⃣  Testing check answer (correct)...")
    # Для этого примера используем простой ответ
    # В реальном приложении нужно получить правильный ответ
    
    # 5. Get statistics
    print("\n5️⃣  Testing statistics...")
    tester.get_statistics()
    
    # 6. Get all words
    print("\n6️⃣  Testing get all words...")
    tester.get_all_words()
    
    # 7. Reset session
    print("\n7️⃣  Testing reset session...")
    tester.reset_session()
    
    print("\n" + "=" * 60)
    print("✅ API TEST COMPLETED")
    print("=" * 60 + "\n")


def example_curl_commands():
    """Примеры команд curl для тестирования API"""
    curl_examples = """
╔════════════════════════════════════════════════════════════════╗
║               CURL COMMAND EXAMPLES                            ║
╚════════════════════════════════════════════════════════════════╝

1️⃣  Health Check:
    curl http://localhost:5000/api/health

2️⃣  Get Next Word:
    curl http://localhost:5000/api/word/next

3️⃣  Show Answer:
    curl http://localhost:5000/api/word/show-answer

4️⃣  Check Answer:
    curl -X POST http://localhost:5000/api/word/check-answer \\
         -H "Content-Type: application/json" \\
         -d '{"translation": "майонез"}'

5️⃣  Get Statistics:
    curl http://localhost:5000/api/statistics

6️⃣  Reset Session:
    curl -X POST http://localhost:5000/api/session/reset

7️⃣  Get All Words:
    curl http://localhost:5000/api/words/list

═════════════════════════════════════════════════════════════════
    """
    print(curl_examples)


if __name__ == "__main__":
    import sys
    
    print("""
╔════════════════════════════════════════════════════════════════╗
║           ENGLISH LEARNING APP - TESTING UTILITY               ║
╚════════════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "test":
            test_api_endpoints()
        elif command == "interactive":
            interactive_session()
        elif command == "curl":
            example_curl_commands()
        else:
            print(f"Unknown command: {command}")
            print("\nAvailable commands:")
            print("  python examples_and_tests.py test          - Test all API endpoints")
            print("  python examples_and_tests.py interactive   - Start interactive session")
            print("  python examples_and_tests.py curl          - Show curl examples")
    else:
        # По умолчанию запускаем интерактивную сессию
        interactive_session()
