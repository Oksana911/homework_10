import json


def candidates_load(path):
    """
    Загружаем данные кандидатов
    """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

def format_candidate(candidates_list):
    """
    Форматируем данные кандидатов из списка в формат:
    Имя кандидата -
    Позиция кандидата
    Навыки через запятую
    """
    candidates = "<pre>"
    for candidate in candidates_list:
        name = candidate["name"]
        position = candidate["position"]
        skills = candidate["skills"]
        candidates += (
                f"Имя кандидата - {name}\n"
                f"Позиция кандидата - {position}\n"
                f"Навыки - {skills}\n\n"
        )

    return candidates + "<pre>"