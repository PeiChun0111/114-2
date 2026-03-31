import numpy as np

class ScoreAnalyzer:
    def __init__(self, scores):
        # Convert input list to NumPy array
        self.scores = np.array(scores)

    def max_per_student(self):
        # Max score for each student (row-wise)
        return np.max(self.scores, axis=1)

    def avg_per_subject(self):
        # Average score for each subject (column-wise)
        return np.mean(self.scores, axis=0)

N, M = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(N)]

analyzer = ScoreAnalyzer(scores)

max_scores = analyzer.max_per_student()
avg_scores = analyzer.avg_per_subject()

print(*max_scores)
print(*[f"{x:.1f}" for x in avg_scores])