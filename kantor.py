from abc import ABC, abstractmethod

class Currency(ABC):
    @abstractmethod
    def verify_banknote(self, banknote):
        pass
    @abstractmethod
    def adjust_rate(self):
        pass

class RateCurrency(Currency):
    def __init__(self, code, rate, commission = 0.0):
        self.code = code
        self.rate = rate
        self.commission = commission

    def verify_banknote(self, banknote):
        print(f"{self.code}: standard check")
        return True

    def apply_commission(self, value):
        return value * (1 + self.commission/100)

    def to_pln(self, amount):
        self.adjust_rate()
        value = amount * self.rate
        return self.apply_commission(value)

    def from_pln(self, amount):
        value = amount / self.rate
        return self.apply_commission(value)

    def convert_to(self, other, amount, banknote):
        print(f"Current rate {self.code}: {self.rate}")
        print("\nVerifying banknote...")

        if not self.verify_banknote(banknote):
            print("Banknote is fake")
            print("Exchange prohibited")
            return None

        print("Banknote is genuine")
        print("\nAdjusting rate...")
        self.adjust_rate()
        print(f"New rate {self.code}: {self.rate}")
        pln_value = amount * self.rate
        result = other.from_pln(pln_value)
        return result

class USD(RateCurrency):
    def __init__(self):
        super().__init__("USD", rate=4.0, commission=2)

    def verify_banknote(self, banknote):
        self.check_texture(banknote)
        self.check_microprint(banknote)
        return banknote.get("real", False)

    def check_texture(self, banknote):
        print("USD: checking relief printing")

    def check_microprint(self, banknote):
        print("USD: checking microprint")

    def adjust_rate(self):
        print("USD: rate is strengthening")
        self.rate += 0.10

class EUR(RateCurrency):
    def __init__(self):
        super().__init__("EUR", rate=4.5, commission=1.5)

    def verify_banknote(self, banknote):
        self.check_color_shift(banknote)
        self.check_pattern(banknote)
        return banknote.get("real", False)

    def check_color_shift(self, banknote):
        print("EUR: checking color shift")

    def check_pattern(self, banknote):
        print("EUR: checking geometric pattern")

    def adjust_rate(self):
        print("EUR: rate is weakening")
        self.rate -= 0.05

class UAH(RateCurrency):
    def __init__(self):
        super().__init__("UAH", rate=0.1, commission=0)

    def verify_banknote(self, banknote):
        self.check_uv(banknote)
        self.check_ir(banknote)
        return banknote.get("real", False)

    def check_uv(self, banknote):
        print("UAH: checking ultraviolet")

    def check_ir(self, banknote):
        print("UAH: checking infrared security")

    def adjust_rate(self):
        print("UAH: sharp fluctuation")
        self.rate *= 1.15

class PLN(RateCurrency):
    def __init__(self):
        super().__init__("PLN", rate=1, commission=0.5)

    def verify_banknote(self, banknote):
        self.check_watermark(banknote)
        self.check_security_thread(banknote)
        return banknote.get("real", False)

    def check_watermark(self, banknote):
        print("PLN: checking watermark")

    def check_security_thread(self, banknote):
        print("PLN: checking security thread")

    def adjust_rate(self):
        print("USD: Rate is stable")
        rate = self.rate

class GBP(RateCurrency):
    def __init__(self):
        super().__init__("GBP", rate=5.2, commission=2.5)

    def verify_banknote(self, banknote):
        self.check_hologram(banknote)
        self.check_polymer(banknote)
        return banknote.get("real", False)

    def check_hologram(self, banknote):
        print("GBP: checking hologram")

    def check_polymer(self, banknote):
        print("GBP: checking polymer base")

    def adjust_rate(self):
        print("GBP: rate is strengthening")
        self.rate += 0.17

def update_currency(currency):
    print(f"\nUpdating rate for {currency.code}")
    currency.adjust_rate()
    print(f"New rate: {currency.rate}")

usd = USD()
eur = EUR()
uah = UAH()
pln = PLN()
gbp = GBP()

real_note = {"real": True}
fake_note = {"real": False}

print("\n========== CONVERTING USD → EUR ==========")

result1 = usd.convert_to(eur, 100, real_note)

if result1:
    print("USD → EUR:", result1)

print("\n========== CONVERTING EUR → UAH ==========")

result2 = eur.convert_to(uah, 200, fake_note)

if result2:
    print("EUR → UAH:", result2)