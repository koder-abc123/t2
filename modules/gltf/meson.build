_module_gltf_srcs = files(run_command(globber, '*.cpp').stdout().split('\n'))
lib_module_gltf = library('module_gltf', _module_gltf_srcs, dependencies: [DEP_GODOT_ALL])

DEP_MODULE_GLTF = declare_dependency(link_with: lib_module_gltf)

MODULE_DEPENDENCIES += DEP_MODULE_GLTF
