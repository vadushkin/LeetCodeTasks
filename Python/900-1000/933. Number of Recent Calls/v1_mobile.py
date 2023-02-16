class RecentCounter:

    def init(self):

        self.s = []

    def ping(self, t: int) -> int:

        while self.s and t - self.s[0] > 3000:

            self.s.pop(0)

        self.s.append(t)

        return len(self.s)
