def get_name() -> str:
    return 'regex'

def can_build(env: dict) -> bool:
    return True

def get_doc_classes() -> [str]:
    return [
        "RegEx",
        "RegExMatch",
    ]


def get_doc_path() -> str:
    return "doc_classes"
