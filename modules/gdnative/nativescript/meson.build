module_gdnative_srcs += files(run_command(globber, '*.cpp').stdout().split('\n'))

if PLATFORM == 'linuxbsd' or PLATFORM == 'iphone'
    module_gdnative_link_args += ['-rdynamic']
endif
