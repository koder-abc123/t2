_module_csg_srcs = files(run_command(globber, '*.cpp').stdout().split('\n'))
_lib_module_csg = library('module_csg',
                _module_csg_srcs,
                gdivirtuals_gen,
                dependencies: DEP_GODOT_ALL)

DEP_MODULE_CSG = declare_dependency(link_with: _lib_module_csg)

MODULE_DEPENDENCIES += DEP_MODULE_CSG
