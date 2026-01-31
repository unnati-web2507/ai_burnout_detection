"""
AI Burnout Detection - Prototype Model
"""

def predict_burnout(stress_level, sleep_hours, work_hours):
    if stress_level >= 7 and sleep_hours < 6:
        return "High Burnout Risk"
    elif stress_level >= 5:
        return "Medium Burnout Risk"
    else:
        return "Low Burnout Risk"

if __name__ == "__main__":
    print(predict_burnout(8, 5, 10))
