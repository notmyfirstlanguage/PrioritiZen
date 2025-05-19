import math
import dateparser

def score_importance(level):
    importance_scores = {
        "BIG PROBLEM": 4,
        "VERY SAD": 4,
        "REAL TROUBLE": 3,
        "SAD": 3,
        "SOME TROUBLE": 2,
        "KINDA SAD": 2,
        "TOTALLY FINE": 1
    }
    return importance_scores.get(level, 1)

def score_urgency(level, deadline=None):
    if level == "Emergency":
        return 4
    elif level in ["Someone actively waiting", "Someone passively waiting"]:
        return 2.5 if "actively" in level else 2
    elif level == "No one waiting":
        return 1
    elif deadline:
        parsed_date = dateparser.parse(deadline)
        if parsed_date:
            minutes_until_deadline = (parsed_date - datetime.now()).total_seconds() / 60
            return max(2, min(3.99, 4 - math.log2((minutes_until_deadline + 1) / 1440)))
    return 1

def score_aversiveness(level):
    aversiveness_scores = {
        "I’d actually enjoy it!": 1,
        "It’s fine": 2,
        "I really don’t wanna": 3,
        "NOOOOOO!": 4
    }
    return aversiveness_scores.get(level, 2)
