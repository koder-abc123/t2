_module_theora_srcs = files(run_command(globber, '*.cpp').stdout().split('\n'))
lib_module_theora = library('module_theora', _module_theora_srcs,
    dependencies: [DEP_GODOT_ALL, DEP_LIBTHEORA, DEP_LIBOGG, DEP_LIBVORBIS]
)

DEP_MODULE_THEORA = declare_dependency(link_with: lib_module_theora)

MODULE_DEPENDENCIES += DEP_MODULE_THEORA
