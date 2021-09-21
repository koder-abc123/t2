def can_build(env):
    return True

def get_name():
    return 'ogg'

def configure(env):
    pass


def get_doc_classes():
    return [
        "OGGPacketSequence",
        "OGGPacketSequencePlayback",
    ]


def get_doc_path():
    return "doc_classes"
