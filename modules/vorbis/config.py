def can_build(env):
    return True #env.module_check_dependencies("vorbis", ["ogg"])

def get_name():
    return 'vorbis'

def configure(env):
    pass


def get_doc_classes():
    return [
        "AudioStreamOGGVorbis",
        "AudioStreamPlaybackOGGVorbis",
    ]


def get_doc_path():
    return "doc_classes"
