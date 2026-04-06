import requests
from datetime import datetime
from typing import Dict, Optional

def get_currency_rates() -> Optional[Dict]:
    """
    Получает актуальные курсы мировых валют к рублю
    Использует бесплатный API от exchangerate-api.com
    """
    try:
        # Список популярных валют
        currencies = ["USD", "EUR", "GBP", "JPY", "CNY", "CHF", "CAD", "AUD", "NZD", "SEK", "NOK", "DKK", "INR", "BRL", "MXN", "ZAR"]
        
        url = "https://api.exchangerate-api.com/v4/latest/RUB"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        rates = data.get("rates", {})
        
        # Фильтруем только нужные нам валюты
        filtered_rates = {curr: rates[curr] for curr in currencies if curr in rates}
        
        # Форматируем и выводим результат
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        
        print("=" * 60)
        print(f"Курсы валют к рублю ({timestamp})")
        print("=" * 60)
        print(f"{'Валюта':<10} {'Курс (за 1 единицу)':<20} {'Тренд'}")
        print("-" * 60)
        
        for curr, rate in sorted(filtered_rates.items()):
            # Форматируем курс в зависимости от его размера
            if rate >= 1:
                rate_str = f"₽ {rate:.2f}"
            else:
                rate_str = f"₽ {rate:.4f}"
            
            print(f"{curr:<10} {rate_str:<20} 📊")
        
        print("=" * 60)
        
        return filtered_rates
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при получении данных: {e}")
        return None
    except (ValueError, KeyError) as e:
        print(f"❌ Ошибка при обработке данных: {e}")
        return None


def get_currency_info() -> None:
    """
    Выводит детальную информацию о курсах с расчётами
    """
    try:
        url = "https://api.exchangerate-api.com/v4/latest/RUB"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        rates = data.get("rates", {})
        
        # Основные валюты для расчёта
        main_currencies = {
            "USD": "Доллар США",
            "EUR": "Евро",
            "GBP": "Британский фунт",
            "JPY": "Японская йена"
        }
        
        print("\n" + "=" * 60)
        print("РАСЧЁТЫ ДЛЯ ОСНОВНЫХ ВАЛЮТ")
        print("=" * 60)
        
        for code, name in main_currencies.items():
            if code in rates:
                rate = rates[code]
                print(f"\n{name} ({code}):")
                print(f"  1 {code} = ₽ {rate:.2f}")
                print(f"  100 {code} = ₽ {rate * 100:,.2f}")
                print(f"  1000 {code} = ₽ {rate * 1000:,.2f}")
                print(f"  1 ₽ = {1/rate:.6f} {code}")
        
        print("\n" + "=" * 60)
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")


if __name__ == "__main__":
    print("\n🌍 МОНИТОРИНГ КУРСОВ ВАЛЮТ\n")
    
    # Получаем и выводим курсы
    rates = get_currency_rates()
    
    # Выводим детальную информацию если данные получены
    if rates:
        get_currency_info()
    
    print("\n✅ Данные получены с exchangerate-api.com")
