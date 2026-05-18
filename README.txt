Project Description: Currency Exchange Simulator
Project Overview
This is a software model of a currency exchange office, written in Python.
 The program can handle several currencies (Dollar, Euro, Hryvnia, Zloty, and British Pound)
  and processes the entire exchange operation, from verifying the banknote to dispensing the funds.

What the system can do:

Verify banknote authenticity: Before conducting an exchange, the system checks the banknote.
Each currency has its own unique security features (Dollars are checked for microprinting,
Hryvnias under ultraviolet light, Pounds by holograms, etc.). If a banknote is fake, the exchange
is canceled.

Convert via a base currency: All exchanges between any two currencies (for example, USD to EUR)
are routed through a central base currency — the Polish Zloty (PLN).

Account for commissions and rate fluctuations: Each currency has its own set
commission fee. Additionally, before every exchange, the exchange rate is automatically adjusted
(for example, the Dollar might strengthen, while the Euro might weaken).