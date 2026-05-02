from abc import ABC, abstractmethod

class Currency(ABC):
    def __init__(self, code, buy_rate, sell_rate, commission_percent = 0):
        self._code = code
        self._buy_rate = buy_rate
        self._sell_rate = sell_rate
        self._commission_percent = commission_percent

    @property
    def code(self):
        return self._code

    def _adjust_rate_for_amount(self, rate, amount):
        if amount > 5000:
            return rate * 0.99
        elif amount >1000:
            return rate * 0.995
        return rate

    def apply_commission(self, value):
        commision_value = value * (self._commission_percent / 100)
        return value + commision_value, commision_value

    @abstractmethod
    def description(self):
        pass

class EUR(Currency):
    def description(self):
        return "EUR"

class USD(Currency):
    def description(self):
        return "USD"

class GBP(Currency):
    def description(self):
        return "GBP"

class UAH(Currency):
    def description(self):
        return "UAH"

class PLN(Currency):
    def description(self):
        return "PLN"

class Exchange():
    def __init__(self):
        self._currencies = {}
        self._history = {}

    def add_currency(self, currency: Currency):
        self._currencies[currency.code] = currency

    def get_currency_codes(self):
        return list(self._currencies.keys())

    def get_history(self):
        return list(self._history)