from flask import Flask

import utils

app = Flask(__name__)


@app.route("/")
def main_page():
    candidates_list = utils.candidates_load("candidates.json")
    return utils.format_candidate(candidates_list)


@app.route("/candidates/<int:id>")
def candidate_page(id):
    candidates_list = utils.candidates_load("candidates.json")
    for candidate in candidates_list:
        if candidate["id"] == id:
            return (
                f"""<img src = '{candidate["picture"]}'>"""
                f"""{utils.format_candidate([candidate])}"""
            )


@app.route("/skills/<skill>")
def skills_page(skill):
    candidates_list = utils.candidates_load("candidates.json")
    candidates_by_skills = []
    for candidate in candidates_list:
        if skill.lower() in candidate["skills"].lower().split(", "):
            candidates_by_skills.append(candidate)

    return utils.format_candidate(candidates_by_skills)


app.run()
