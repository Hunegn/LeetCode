class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.max = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr < len(self.history):
            self.history[self.curr] = url
        else:
            self.history.append(url)
        self.max = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.max, self.curr + steps)
        return self.history[self.curr]
