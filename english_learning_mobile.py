"""
English Learning App - Kivy Mobile UI
Для запуска на Android (через Buildozer)
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp
from english_learning_backend import EnglishLearningApp

# Размер окна для тестирования на компьютере
Window.size = (400, 800)


class EnglishLearningUI(BoxLayout):
    """Главный интерфейс приложения"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(10)
        self.spacing = dp(10)
        
        self.app = EnglishLearningApp()
        self.app.next_word()
        self.show_translation = False
        
        # Заголовок
        self.title_label = Label(
            text="📚 English Learning App",
            font_size='24sp',
            bold=True,
            size_hint_y=0.08
        )
        self.add_widget(self.title_label)
        
        # Метка направления
        self.direction_label = Label(
            text=self.app.get_direction_label(),
            font_size='18sp',
            size_hint_y=0.08,
            color=(0.1, 0.1, 0.1, 1)
        )
        self.add_widget(self.direction_label)
        
        # Секция для слова
        word_box = BoxLayout(orientation='vertical', size_hint_y=0.25, spacing=dp(15))
        
        self.word_label = Label(
            text="Переведите слово:",
            font_size='14sp',
            size_hint_y=0.3
        )
        word_box.add_widget(self.word_label)
        
        self.prompt_word_label = Label(
            text=self.app.get_prompt_word(),
            font_size='32sp',
            bold=True,
            size_hint_y=0.7
        )
        word_box.add_widget(self.prompt_word_label)
        
        self.add_widget(word_box)
        
        # Кнопка для показа ответа
        show_answer_btn = Button(
            text='🔤 Показать ответ',
            size_hint_y=0.08,
            background_color=(0.2, 0.6, 1, 1)
        )
        show_answer_btn.bind(on_press=self.on_show_answer)
        self.add_widget(show_answer_btn)
        
        # Кнопка переключения направления
        switch_box = BoxLayout(size_hint_y=0.1, spacing=dp(10))
        self.toggle_direction_btn = Button(
            text='🔄 Сменить направление',
            background_color=(0.3, 0.5, 0.8, 1)
        )
        self.toggle_direction_btn.bind(on_press=self.on_toggle_direction)
        switch_box.add_widget(self.toggle_direction_btn)
        self.add_widget(switch_box)
        
        # Секция результата
        self.result_label = Label(
            text="",
            font_size='16sp',
            size_hint_y=0.12
        )
        self.add_widget(self.result_label)
        
        # Кнопки: Правильно / Неправильно
        answer_box = BoxLayout(size_hint_y=0.15, spacing=dp(10))
        
        self.correct_btn = Button(
            text='✅ Правильно\nответил',
            size_hint_x=0.5,
            background_color=(0.2, 0.8, 0.2, 1)
        )
        self.correct_btn.bind(on_press=self.on_mark_correct)
        answer_box.add_widget(self.correct_btn)
        
        self.incorrect_btn = Button(
            text='❌ Неправильно\nответил',
            size_hint_x=0.5,
            background_color=(1, 0.2, 0.2, 1)
        )
        self.incorrect_btn.bind(on_press=self.on_mark_incorrect)
        answer_box.add_widget(self.incorrect_btn)
        
        self.add_widget(answer_box)
        
        # Кнопка Далее
        self.next_btn = Button(
            text='➡️ Следующее слово',
            size_hint_y=0.1,
            background_color=(1, 0.6, 0.2, 1)
        )
        self.next_btn.bind(on_press=self.on_next_word)
        self.add_widget(self.next_btn)
        
        # Кнопка Статистика
        self.stats_btn = Button(
            text='📊 Статистика',
            size_hint_y=0.08,
            background_color=(0.8, 0.2, 1, 1)
        )
        self.stats_btn.bind(on_press=self.on_show_statistics)
        self.add_widget(self.stats_btn)
        
        # Обновляем слово
        self.update_word()
    
    def update_word(self):
        """Обновить отображение слова"""
        self.prompt_word_label.text = self.app.get_prompt_word()
        self.direction_label.text = self.app.get_direction_label()
        self.result_label.text = ""
        self.show_translation = False
    
    def on_show_answer(self, instance):
        """Показать ответ"""
        answer = self.app.get_current_answer()
        self.result_label.text = f"🔤 Ответ: {answer}"
        self.result_label.color = (1, 0.8, 0, 1)  # Жёлтый
        self.show_translation = True
    
    def on_mark_correct(self, instance):
        """Отметить как правильный ответ"""
        result = self.app.mark_correct()
        self.result_label.text = "✅ Молодец! Правильно!"
        self.result_label.color = (0.2, 1, 0.2, 1)  # Зелёный
    
    def on_mark_incorrect(self, instance):
        """Отметить как неправильный ответ"""
        result = self.app.mark_incorrect()
        self.result_label.text = f"❌ Неправильно\nПравильный ответ: {self.app.get_current_answer()}"
        self.result_label.color = (1, 0.3, 0.3, 1)  # Красный
    
    def on_toggle_direction(self, instance):
        """Переключить направление перевода"""
        self.app.toggle_direction()
        self.update_word()
        self.result_label.text = f"🔄 Направление: {self.app.get_direction_label()}"
        self.result_label.color = (0.2, 0.6, 1, 1)
    
    def on_next_word(self, instance):
        """Перейти к следующему слову"""
        self.app.next_word()
        self.update_word()
    
    def on_show_statistics(self, instance):
        """Показать статистику"""
        stats = self.app.get_stats()['session_stats']
        problematic = stats.get('problematic_words', [])
        
        # Форматируем топ ошибок
        problematic_text = "Слова, на которых вы чаще всего ошибаетесь:\n" + "=" * 40 + "\n"
        if problematic:
            for i, word in enumerate(problematic, 1):
                problematic_text += f"{i}. {word['english']}\n   ({word['russian']})\n   ❌ Ошибок: {word['incorrect_count']}, ✅ Правильно: {word['correct_count']}\n   Вероятность ошибки: {word['error_rate']}%\n\n"
        else:
            problematic_text += "Пока нет ошибок! Продолжайте в том же духе! 🎉"
        
        stat_text = f"""
📊 СТАТИСТИКА СЕССИИ
{'=' * 40}
✅ Правильных ответов: {stats['correct']}
❌ Неправильных ответов: {stats['incorrect']}
📝 Всего ответов: {stats['total']}
🎯 Точность: {stats['accuracy']}%
⏱️  Время сессии: {str(stats['session_duration']).split('.')[0]}

{problematic_text}
"""
        self.show_popup("📊 Статистика", stat_text)
    
    def show_popup(self, title, message):
        """Показать всплывающее окно"""
        content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Используем ScrollView для длинного текста
        scroll = ScrollView(size_hint_y=0.9)
        label = Label(
            text=message,
            size_hint_y=None,
            markup=True
        )
        label.bind(texture_size=label.setter('size'))
        scroll.add_widget(label)
        content.add_widget(scroll)
        
        close_btn = Button(text='Закрыть', size_hint_y=0.1)
        
        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.9, 0.7)
        )
        
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        
        popup.open()


class EnglishLearningApp_Kivy(App):
    """Главный класс Kivy приложения"""
    
    def build(self):
        self.title = "English Learning App"
        return EnglishLearningUI()


if __name__ == '__main__':
    app = EnglishLearningApp_Kivy()
    app.run()
