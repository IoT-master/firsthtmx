from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional

app = FastAPI()

templates = Jinja2Templates(directory="templates")

set_of_qa = [
    {
        "q": "While you might like both, choose only one category as your preference (btw, Rosé wine are produced from red grapes)?",
        "a": ["Red", "White"],
    },
    {
        "q": "From the below options, which is your preferred weather?",
        "a": [
            "Love a coolness to the air along with the sun, thank you!",
            "No extremes please, keep it mild for me both day and night.",
            "Enjoy having winter weather, break out the chilly temps!",
            "Warm both day and night…free me of cool weather altogether!",
            "Love the heat of summer but with cool nights, please!",
        ],
    },
    {
        "q": "If cultural norms or temperature were not a concern, which would be your preference?",
        "a": [
            "1. Bare naked and fancy free.",
            "2. Simply a thin layer, like a shirt, shorts or robe.",
            "3. Several layers of clothing. ",
            "4. Only undies simply to be discrete.",
            "5. Layered in beautiful attire, because that’s just you!",
        ],
    },
]


@app.get("/question", response_class=HTMLResponse)
async def get_survey_question(request: Request):
    question = {"area": "My Question"}
    answer = {"area": "My Answer"}
    context = {"request": request, "question": question, "answer": answer}
    return templates.TemplateResponse("survey.html", context)
