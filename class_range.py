class Range:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def contains(self, n):
        return self.start <= n < self.end

    def overlaps(self, r):
        return not (self.end <= r.start or r.end <= self.start)

    def merge(self, r):
        if self.overlaps(r):
            self.start = min(self.start, r.start)
            self.end = max(self.end, r.end)
            return True
        return False

    def __str__(self):
        return f"[{self.start}, {self.end}]"


r1 = Range(1, 3)
r2 = Range(2, 5)
if r1.merge(r2):
    print(r1)
