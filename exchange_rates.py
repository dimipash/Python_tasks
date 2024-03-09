class ExchangeRates:
    """
        The ExchangeRates class represents a collection of exchange rates. It has a constructor that takes a dictionary
        or a list of tuples representing the exchange rates. It has a __getattr__ method that allows for dynamic
        attribute access based on the exchange rates. The __getattr__ method supports accessing the exchange rate for
        a given currency, or a function to convert between currencies. The ExchangeRates class has a _exchange method
        that calculates the exchange rate between two currencies. The _exchange method is called by the __getattr__
        method when a conversion function is accessed. The ExchangeRates class does not check the types of the
        arguments, so you should ensure they are correct before creating an ExchangeRates object. If they are not,
        this class may raise a TypeError or ValueError.
    """

    def __init__(self, rates):
        if isinstance(rates, dict):
            self.rates = rates
        elif isinstance(rates, list) and all((isinstance(t, tuple) for t in rates)):
            self.rates = {k: v for k, v in rates}
        else:
            raise TypeError("Rates must be a dict or list of tuples")

    def __getattr__(self, name):
        if name in self.rates.keys():
            return self.rates[name]

        change = name.split("_")
        if len(change) != 3:
            raise AttributeError("Unsupported action called")

        name, c1, c2 = change
        if name != 'change':
            raise AttributeError("Unsupported action called")

        r1 = self.rates.get(c1, None)
        r2 = self.rates.get(c2, None)

        if not r1 or not r2:
            raise AttributeError("Incorrect currencies")

        try:
            return lambda v: self._exchange(r1, r2, v)
        except:
            raise AttributeError("Unsupported action called")

    def _exchange(self, r1, r2, v):
        if not isinstance(v, (int, float)):
            raise ValueError(f"Currency to change should be int or float, {type(v)} given")

        return r1 / r2 * v


rates_dict = {"usd": 1.75, "euro": 1.95, "gbp": 2.9, 'lv': 1}
rates = ExchangeRates(rates_dict)
print(rates.usd)
print(rates.change_lv_usd(1.5))
print(rates.change_euro_usd(100))
print(rates.change_usd_euro(100))
