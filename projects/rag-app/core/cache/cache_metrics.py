class CacheMetrics:
    def __init__(self):
        self.hits = 0
        self.misses = 0
        self.total_time_saved = 0.0

    def record_hit(self, time_saved: float):
        self.hits += 1
        self.total_time_saved += time_saved

    def record_miss(self):
        self.misses += 1

    def get_hit_rate(self) -> float:
        total = self.hits + self.misses
        if total == 0:
            return 0.0
        return (self.hits / total) * 100.0
