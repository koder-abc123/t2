_module_stb_vorbis_srcs = files(run_command(globber, '*.cpp').stdout().split('\n'))

lib_module_stb_vorbis = library('module_stb_vorbis',
    _module_stb_vorbis_srcs,
    include_directories: '../../thirdparty/libogg',
    dependencies: [DEP_GODOT_ALL]
)

DEP_MODULE_STB_VORBIS = declare_dependency(link_with: lib_module_stb_vorbis)

MODULE_DEPENDENCIES += DEP_MODULE_STB_VORBIS
