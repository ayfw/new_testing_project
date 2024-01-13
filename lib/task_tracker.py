def task_tracker(text):
    if "#TODO" in text:
        return True
    if text == "":
        raise Exception ("This is an empty string!")
    else:
        return False