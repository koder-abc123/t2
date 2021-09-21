def can_build(env):
    return False#env["tools"] and not env["disable_3d"]


def configure(env):
    pass

def get_name():
    return 'gltf'

def get_doc_classes():
    return [
        "EditorSceneImporterGLTF",
        "GLTFAccessor",
        "GLTFAnimation",
        "GLTFBufferView",
        "GLTFCamera",
        "GLTFDocument",
        "GLTFLight",
        "GLTFMesh",
        "GLTFNode",
        "GLTFSkeleton",
        "GLTFSkin",
        "GLTFSpecGloss",
        "GLTFState",
        "GLTFTexture",
    ]


def get_doc_path():
    return "doc_classes"
