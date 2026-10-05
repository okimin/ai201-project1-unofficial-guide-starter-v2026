def judge(questions,answer,expects,results) -> bool:
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()