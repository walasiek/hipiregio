import logging
import os
import json
from hipiregio.utils.globals import HIPIREGIO_RC_ROOT_DIR
from hipiregio.rc.rc_input_data import RCInputData, RCTextReference, RCText, RCQuestion
from hipiregio.rc.rc_utils import is_full_id_from_given_culture


class RCRawReader:
    TEXTS_FILENAME = "texts.json"
    QUESTIONS_FILENAME = "questions.json"
    CONTENTS_FILENAME = "texts-content.json"

    """
    Reads raw JSON data stored in HIPIREGIO_DATA_DIR.
    """
    def __init__(self, culture):
        self.culture = culture

    def read_data(self) -> RCInputData:
        input_data = RCInputData(self.culture)
        raw_contents = self._read_raw_contents()
        raw_texts = self._read_raw_texts()
        self._process_raw_texts(input_data, raw_texts, raw_contents)

        raw_questions = self._read_raw_questions()
        self._process_raw_questions(input_data, raw_questions)
        return input_data

    def _read_raw_contents(self):
        fp = os.path.join(HIPIREGIO_RC_ROOT_DIR, self.CONTENTS_FILENAME)
        logging.info("Reading Text Contents from %s", fp)
        raw_data = self._read_raw(fp)
        return raw_data

    def _read_raw_texts(self):
        fp = os.path.join(HIPIREGIO_RC_ROOT_DIR, self.TEXTS_FILENAME)
        logging.info("Reading Text References from %s", fp)
        raw_data = self._read_raw(fp)
        return raw_data

    def _read_raw_questions(self):
        fp = os.path.join(HIPIREGIO_RC_ROOT_DIR, self.QUESTIONS_FILENAME)
        logging.info("Reading Questions from %s", fp)
        raw_data = self._read_raw(fp)
        return raw_data

    def _read_raw(self, fp):
        try:
            with open(fp, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            logging.error(f"Error: File '{fp}' not found!")
            return None
        except json.JSONDecodeError as e:
            logging.error(f"Error: Invalid JSON format in '{fp}'!")
            logging.error(f"   {e.msg} (at line {e.lineno}, column {e.colno})")
            logging.error(f"   Problem near:\n\n{e.doc[max(0, e.pos-20):e.pos+20]}")
            return None

    def _process_raw_texts(self, input_data, raw_texts, raw_contents):
        for full_id, entry in raw_contents.items():
            if is_full_id_from_given_culture(full_id, self.culture):
                reference_entry = raw_texts[full_id]
                reference_entry['full_id'] = full_id
                reference = RCTextReference(**reference_entry)

                content = entry['content']

                text = RCText(
                    full_id=full_id,
                    content=content,
                    reference=reference,
                    )

                input_data.add_text(text)

    def _process_raw_questions(self, input_data, raw_questions):
        for raw_question_entry in raw_questions['questions']:
            question = RCQuestion(**raw_question_entry)
            input_data.add_question(question)
