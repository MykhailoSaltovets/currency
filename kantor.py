# from abc import ABC, abstractmethod (previous version)

class Currency():
    def __init__(self, code, rate, commission_percent = 0):
        self._code = code
        self.rate = rate
        self.commission_percent = commission_percent

    def adjust_rate(self, amount):
        return self.rate

    def apply_commission(self, value):
        return value * (1 + self.commission_percent/100)

    def to_pln(self, amount):
        rate = self.adjust_rate(amount)
        value = amount * rate
        return self.apply_commission(value)

    def from_pln(self, amount):
        rate = self.apply_commission(amount)
        value = amount / rate
        return self.apply_commission(value)

    def convert_to(self, other, amount):
        pln_value = self.to_pln(amount)
        return other.from_pln(pln_value)

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

    def convert(self, amount, from_code, to_code):
        if from_code = to_code:
            raise ValueError("Currencies are equal")
        if from_code not in self._currencies or to_code not in self._currencies:
            raise ValueError("Currencies not found")
        from_cur = self._currencies[from_code]
        to_cur = self._currencies[to_code]