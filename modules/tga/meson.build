_module_tga_srcs = files(run_command(globber, '*.cpp').stdout().split('\n'))
lib_module_tga = library('module_tga', _module_tga_srcs, dependencies: [DEP_GODOT_ALL])

DEP_MODULE_TGA = declare_dependency(link_with: lib_module_tga)

MODULE_DEPENDENCIES += DEP_MODULE_TGA
