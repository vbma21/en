"""
English Learning App - Backend Module
Модернизированный код для использования в Android приложении
"""

import random
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class Word:
    """Модель для хранения пары слов с системой весов"""
    english: str
    russian: str
    id: int
    weight: float = 1.0  # Вес слова (1.0 = нормальный, >1.0 = часто ошибаюсь, <1.0 = хорошо знаю)
    correct_count: int = 0  # Количество правильных ответов
    incorrect_count: int = 0  # Количество неправильных ответов
    
    def to_dict(self) -> Dict:
        return asdict(self)


class WordDatabase:
    """Управление базой данных слов"""
    
    def __init__(self):
        self.words: List[Word] = []
        self._init_words()
    
    def _init_words(self) -> None:
        """Инициализация базы слов"""
        words_data = [
            ("mayonnaise", "майонез"),
            ("to handle", "справляться"),
            ("enough", "достаточно"),
            ("remember", "помнить"),
            ("professor", "профессор"),
            ("philosophy", "философия"),
            ("items", "предметы, вещи"),
            ("in front of", "напротив"),
            ("wordlessly", "молча"),
            ("empty", "пустая"),
            ("to fill", "заполнить"),
            ("he then asked the students if the jar was full", "он спросил студентов заполнена ли банка"),
            ("agree", "соглашаться"),
            ("disagree", "не соглашаться"),
            ("the box of pebbles", "коробка с галькой"),
            ("poured into", "насыпать"),
            ("to shook", "встряхнуть"),
            ("area, space, room", "пространство, место"),
            ("pick up", "доставать, срывать"),
            ("everything else", "все остальное"),
            ("once more", "еще раз"),
            ("respond", "отвечать"),
            ("an unanimous yes", "единогласное «да»"),
            ("produce", "производить"),
            ("from under the table", "из под стола"),
            ("the entire contents", "всё содержимое"),
            ("entire", "всё"),
            ("effectively filling the empty space", "эффективно заполняя всё пространство"),
            ("laugh", "смеяться"),
            ("to laugh at", "смеяться над кем-либо"),
            ("laughter subsided", "смех стих"),
            ("recognize", "осознавать"),
            ("represent", "представлять"),
            ("passions", "увлечения"),
            ("remain", "оставаться"),
            ("your life would still be full", "ваша жизнь будет все еще полной"),
            ("matter", "значит"),
            ("the sand is everything else", "песок - все остальное"),
            ("small stuff", "мелочи, ерунда"),
            ("continue", "продолжить"),
            ("the same goes for life", "то же самое можно сказать о жизни"),
            ("to spend on", "тратить на что-либо"),
            ("pay attention to", "обратить внимание"),
            ("critical to your happiness", "важные для вашего счастья"),
            ("take time", "найдите время"),
            ("to get medical checkups", "пройти медосмотр"),
            ("to clean the house", "убираться в доме"),
            ("to fix the disposal", "выбросить мусор"),
            ("take care of", "забота о чем-либо"),
            ("set your priorities", "расставить приоритеты"),
            ("the rest is just sand", "остальное - просто песок"),
            ("careful", "осторожный"),
            ("careless", "беззаботный"),
            ("raise a hand", "поднимать руку"),
            ("rise", "подняться самому"),
            ("inquire", "спрашивать"),
            ("I'm glad", "я рад"),
            ("it just goes to", "просто показать"),
            ("no matter how full your life may seem", "неважно насколько полной может казаться ваша жизнь"),
            ("a couple of cups of coffee", "пара чашек кофе"),
            ("to roll into the open areas", "заполнить свободное пространство"),
            ("interesting enough", "достаточно интересно"),
            ("rather interesting", "довольно интересно"),
            ("this book is interesting enough", "эта книга достаточно интересная"),
            ("this book is rather interesting", "эта книга довольно интересная"),
        ]
        
        for idx, (english, russian) in enumerate(words_data, 1):
            self.words.append(Word(english=english, russian=russian, id=idx))
    
    def get_all_words(self) -> List[Word]:
        """Получить все слова"""
        return self.words
    
    def get_weighted_random_word(self) -> Optional[Word]:
        """Получить случайное слово на основе весов (часто ошибаемые чаще появляются)"""
        if not self.words:
            return None
        
        # Создаем список весов
        weights = [word.weight for word in self.words]
        total_weight = sum(weights)
        
        if total_weight == 0:
            return random.choice(self.words)
        
        # Нормализуем веса
        normalized_weights = [w / total_weight for w in weights]
        
        # Выбираем слово на основе нормализованных весов
        return random.choices(self.words, weights=normalized_weights, k=1)[0]
    
    def get_word_by_id(self, word_id: int) -> Optional[Word]:
        """Получить слово по ID"""
        for word in self.words:
            if word.id == word_id:
                return word
        return None
    
    def get_words_count(self) -> int:
        """Получить количество слов"""
        return len(self.words)
    
    def mark_word_correct(self, word_id: int) -> None:
        """Пометить слово как правильно отвеченное (уменьшить вес)"""
        word = self.get_word_by_id(word_id)
        if word:
            word.correct_count += 1
            # Уменьшаем вес, но не ниже 0.5
            word.weight = max(0.5, word.weight - 0.1)
    
    def mark_word_incorrect(self, word_id: int) -> None:
        """Пометить слово как неправильно отвеченное (увеличить вес)"""
        word = self.get_word_by_id(word_id)
        if word:
            word.incorrect_count += 1
            # Увеличиваем вес, но не выше 3.0
            word.weight = min(3.0, word.weight + 0.2)
    
    def get_most_problematic_words(self, limit: int = 5) -> List[Dict]:
        """Получить слова, на которых чаще всего ошибаемся"""
        # Фильтруем слова с хотя бы одной ошибкой
        problematic = [w for w in self.words if w.incorrect_count > 0]
        
        # Сортируем по количеству ошибок и весу
        problematic.sort(
            key=lambda w: (w.incorrect_count, w.weight),
            reverse=True
        )
        
        return [
            {
                "english": w.english,
                "russian": w.russian,
                "incorrect_count": w.incorrect_count,
                "correct_count": w.correct_count,
                "weight": round(w.weight, 2),
                "error_rate": round(w.incorrect_count / (w.correct_count + w.incorrect_count) * 100, 1) if (w.correct_count + w.incorrect_count) > 0 else 0
            }
            for w in problematic[:limit]
        ]


class LearningSession:
    """Управление сессией обучения с системой весов"""
    
    def __init__(self):
        self.current_word: Optional[Word] = None
        self.correct_answers: int = 0
        self.incorrect_answers: int = 0
        self.session_start: datetime = datetime.now()
        self.word_database: WordDatabase = WordDatabase()
    
    def start_new_word(self) -> Optional[Word]:
        """Начать новое слово (выбор на основе весов)"""
        self.current_word = self.word_database.get_weighted_random_word()
        return self.current_word
    
    def mark_correct(self) -> bool:
        """Пометить текущее слово как правильно отвеченное"""
        if not self.current_word:
            return False
        
        self.correct_answers += 1
        self.word_database.mark_word_correct(self.current_word.id)
        return True
    
    def mark_incorrect(self) -> bool:
        """Пометить текущее слово как неправильно отвеченное"""
        if not self.current_word:
            return False
        
        self.incorrect_answers += 1
        self.word_database.mark_word_incorrect(self.current_word.id)
        return True
    
    def get_statistics(self) -> Dict:
        """Получить статистику сессии"""
        total = self.correct_answers + self.incorrect_answers
        accuracy = (self.correct_answers / total * 100) if total > 0 else 0
        
        return {
            "correct": self.correct_answers,
            "incorrect": self.incorrect_answers,
            "total": total,
            "accuracy": round(accuracy, 2),
            "session_duration": str(datetime.now() - self.session_start),
            "problematic_words": self.word_database.get_most_problematic_words(5)
        }
    
    def reset_session(self) -> None:
        """Сбросить сессию"""
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.session_start = datetime.now()


class EnglishLearningApp:
    """Главный класс приложения с системой весов"""
    
    def __init__(self):
        self.session = LearningSession()
        self.direction: str = "en-ru"  # Направление перевода: en-ru или ru-en
    
    def get_current_word_english(self) -> str:
        """Получить английское слово"""
        if self.session.current_word:
            return self.session.current_word.english
        return ""
    
    def get_current_word_russian(self) -> str:
        """Получить русский перевод"""
        if self.session.current_word:
            return self.session.current_word.russian
        return ""
    
    def get_prompt_word(self) -> str:
        """Получить слово, которое отображается пользователю"""
        if not self.session.current_word:
            return ""
        return self.session.current_word.english if self.direction == "en-ru" else self.session.current_word.russian
    
    def get_current_answer(self) -> str:
        """Получить правильный ответ для текущего слова"""
        if not self.session.current_word:
            return ""
        return self.session.current_word.russian if self.direction == "en-ru" else self.session.current_word.english
    
    def get_direction_label(self) -> str:
        """Получить текст для текущего направления"""
        return "Англ → Рус" if self.direction == "en-ru" else "Рус → Англ"
    
    def toggle_direction(self) -> str:
        """Переключить направление перевода"""
        self.direction = "ru-en" if self.direction == "en-ru" else "en-ru"
        return self.direction
    
    def next_word(self) -> Dict:
        """Перейти к следующему слову"""
        word = self.session.start_new_word()
        
        return {
            "word_id": word.id if word else None,
            "prompt": self.get_prompt_word(),
            "direction_label": self.get_direction_label(),
            "statistics": self.session.get_statistics()
        }
    
    def mark_correct(self) -> Dict:
        """Отметить ответ как правильный"""
        self.session.mark_correct()
        
        return {
            "is_correct": True,
            "correct_answer": self.get_current_answer(),
            "statistics": self.session.get_statistics()
        }
    
    def mark_incorrect(self) -> Dict:
        """Отметить ответ как неправильный"""
        self.session.mark_incorrect()
        
        return {
            "is_correct": False,
            "correct_answer": self.get_current_answer(),
            "statistics": self.session.get_statistics()
        }
    
    def get_stats(self) -> Dict:
        """Получить общую статистику"""
        return {
            "total_words": self.session.word_database.get_words_count(),
            "session_stats": self.session.get_statistics()
        }
    
    def reset(self) -> None:
        """Сбросить приложение"""
        self.session.reset_session()


# Для использования как REST API
if __name__ == "__main__":
    # Пример использования в консоли
    app = EnglishLearningApp()
    
    print("=" * 50)
    print("English Learning App (с системой весов)")
    print("=" * 50)
    
    # Начинаем первое слово
    result = app.next_word()
    print(f"\n📚 Слово: {result['english']}")
    print(f"🔤 Перевод: {app.get_current_word_russian()}")
    
    # Пример: правильный ответ
    print("\n✅ Отмечаем как правильный ответ")
    result = app.mark_correct()
    print(f"Статистика: {result['statistics']}")
    
    # Следующее слово
    result = app.next_word()
    print(f"\n📚 Новое слово: {result['english']}")
    
    print("\n✅ Статистика сессии:")
    stats = app.get_stats()
    print(json.dumps(stats, ensure_ascii=False, indent=2))
