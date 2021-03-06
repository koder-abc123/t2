def get_name() -> str:
    return 'visual_script'


def can_build(env: dict) -> bool:
    return True


def get_doc_classes() -> [str]:
    return [
        "VisualScriptBasicTypeConstant",
        "VisualScriptBuiltinFunc",
        "VisualScriptClassConstant",
        "VisualScriptComment",
        "VisualScriptComposeArray",
        "VisualScriptCondition",
        "VisualScriptConstant",
        "VisualScriptConstructor",
        "VisualScriptCustomNode",
        "VisualScriptDeconstruct",
        "VisualScriptEditor",
        "VisualScriptEmitSignal",
        "VisualScriptEngineSingleton",
        "VisualScriptExpression",
        "VisualScriptFunctionCall",
        "VisualScriptFunctionState",
        "VisualScriptFunction",
        "VisualScriptGlobalConstant",
        "VisualScriptIndexGet",
        "VisualScriptIndexSet",
        "VisualScriptInputAction",
        "VisualScriptIterator",
        "VisualScriptLists",
        "VisualScriptLocalVarSet",
        "VisualScriptLocalVar",
        "VisualScriptMathConstant",
        "VisualScriptNode",
        "VisualScriptOperator",
        "VisualScriptPreload",
        "VisualScriptPropertyGet",
        "VisualScriptPropertySet",
        "VisualScriptResourcePath",
        "VisualScriptReturn",
        "VisualScriptSceneNode",
        "VisualScriptSceneTree",
        "VisualScriptSelect",
        "VisualScriptSelf",
        "VisualScriptSequence",
        "VisualScriptSubCall",
        "VisualScriptSwitch",
        "VisualScriptTypeCast",
        "VisualScriptVariableGet",
        "VisualScriptVariableSet",
        "VisualScriptWhile",
        "VisualScript",
        "VisualScriptYieldSignal",
        "VisualScriptYield",
    ]


def get_doc_path() -> str:
    return "doc_classes"
