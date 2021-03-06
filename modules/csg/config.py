def get_name() -> str:
    return 'csg'

def can_build(env):
    return True

def configure(env):
    pass

def get_doc_classes():
    return [
        "CSGBox3D",
        "CSGCombiner3D",
        "CSGCylinder3D",
        "CSGMesh3D",
        "CSGPolygon3D",
        "CSGPrimitive3D",
        "CSGShape3D",
        "CSGSphere3D",
        "CSGTorus3D",
    ]


def get_doc_path():
    return "doc_classes"
