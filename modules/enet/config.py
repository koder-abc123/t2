def get_name() -> str:
    return 'enet'

def can_build(env: dict) -> bool:
    return True


def get_doc_classes() -> [str]:
    return [
        "ENetMultiplayerPeer",
        "ENetConnection",
        "ENetPacketPeer",
    ]


def get_doc_path() -> str:
    return "doc_classes"
