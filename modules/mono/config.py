def get_name() -> str:
    return 'mono'

def can_build(env: dict) -> bool:
    supported_platforms = ["windows", "osx", "linuxbsd",
                           "server", "android", "haiku", "javascript", "iphone"]
    return env.platform in supported_platforms


# def configure(env):
#     platform = env["platform"]

#     if platform not in supported_platforms:
#         raise RuntimeError("This module does not currently support building for this platform")

#     env.use_ptrcall = True
#     env.add_module_version_string("mono")

#     from SCons.Script import BoolVariable, PathVariable, Variables, Help

#     default_mono_static = platform in ["iphone", "javascript"]
#     default_mono_bundles_zlib = platform in ["javascript"]

#     envvars = Variables()
#     envvars.Add(
#         PathVariable(
#             "mono_prefix",
#             "Path to the Mono installation directory for the target platform and architecture",
#             "",
#             PathVariable.PathAccept,
#         )
#     )
#     envvars.Add(BoolVariable("mono_static", "Statically link Mono", default_mono_static))
#     envvars.Add(BoolVariable("mono_glue", "Build with the Mono glue sources", True))
#     envvars.Add(BoolVariable("build_cil", "Build C# solutions", True))
#     envvars.Add(
#         BoolVariable("copy_mono_root", "Make a copy of the Mono installation directory to bundle with the editor", True)
#     )

#     # TODO: It would be great if this could be detected automatically instead
#     envvars.Add(
#         BoolVariable(
#             "mono_bundles_zlib", "Specify if the Mono runtime was built with bundled zlib", default_mono_bundles_zlib
#         )
#     )

#     envvars.Update(env)
#     Help(envvars.GenerateHelpText(env))

#     if env["mono_bundles_zlib"]:
#         # Mono may come with zlib bundled for WASM or on newer version when built with MinGW.
#         print("This Mono runtime comes with zlib bundled. Disabling 'builtin_zlib'...")
#         env["builtin_zlib"] = False
#         thirdparty_zlib_dir = "#thirdparty/zlib/"
#         env.Prepend(CPPPATH=[thirdparty_zlib_dir])


def get_doc_classes() -> [str]:
    return [
        "CSharpScript",
        "GodotSharp",
    ]


def get_doc_path() -> str:
    return "doc_classes"
