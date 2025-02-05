import re


def get_text_id_from_full_id(full_id: str) -> str:
    text_id = re.sub(r"_[a-z][a-z]-[A-Z]{2,4}$", "", full_id)
    return text_id


def create_full_id(text_id: str, culture: str) -> str:
    return f"{text_id}_{culture}"


def is_full_id_from_given_culture(full_id: str, culture: str) -> bool:
    return full_id.endswith(f"_{culture}")
