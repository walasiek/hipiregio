from dataclasses import dataclass, field
from typing import List
from hipiregio.rc.rc_utils import get_text_id_from_full_id


@dataclass
class RCTextReference:
    full_id: str
    chapter: str
    start_fragment: str
    end_fragment: str
    open_license: bool
    reference: str


@dataclass
class RCText:
    full_id: str
    text_id: str = field(init=False)
    content: str
    reference: RCTextReference

    def __post_init__(self):
        self.text_id = get_text_id_from_full_id(self.full_id)


@dataclass
class RCQuestion:
    text_id: str
    question: str
    options: List[str]
    correct: int


class RCInputData:
    """
    Data for Reading Comprehension test.
    """

    def __init__(self, culture):
        self.culture = culture
        self.text_id_to_texts = dict()
        self.questions = []

    def add_text(self, text: RCText):
        self.text_id_to_texts[text.text_id] = text

    def add_question(self, question: RCQuestion):
        if question.text_id not in self.text_id_to_texts:
            raise Exception(f"Invalid file with questions! Unknown text_id = {question.text_id}")
        self.questions.append(question)

    def get_content_for_question(self, question: RCQuestion) -> str:
        return self.text_id_to_texts[question.text_id].content

    def create_prompt_for_question(self, question_index: int) -> str:
        # TODO trywialne (placeholder)
        question = self.questions[question_index]
        content = self.get_content_for_question(question)
        prompt = "W kolejnej wiadomości zostaną podane 'tekst', 'pytanie' oraz 'opcje'. Po dokładnym przeczytaniu i zrozumieniu tekstu wybierz najbardziej odpowiednią odpowiedź na pytanie spośród czterech opcji. Odpowiedz bezpośrednio numerem opcji.\n"


        prompt += f"Tekst: {content}\n\n"

        prompt += f"Pytanie: {question.question}\n\n"

        prompt += "Opcje:\n"

        for index, option in enumerate(question.options):
            prompt += f"{index+1}. {option}\n"
        return prompt

    def to_dict(self):
        result = {
            "questions": [],
        }

        for question in self.questions:
            entry = {
                'content': self.text_id_to_texts[question.text_id].content,
                'question': question.question,
                'options': question.options,
                'correct': question.correct
            }
            result['questions'].append(entry)
        return result
