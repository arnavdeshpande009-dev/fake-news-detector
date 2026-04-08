def grade(output):
    if "prediction" in str(output):
        return 1.0
    return 0.0