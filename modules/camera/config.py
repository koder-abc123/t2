def get_name() -> str:
    return 'camera'

def can_build(env: dict) -> bool:
    supported_platforms = ['osx', 'windows']
    return env.platform in supported_platforms
