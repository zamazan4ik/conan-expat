from conans import ConanFile, tools, CMake
import os, sys
#import multiprocessing

class ExpatConan(ConanFile):
    name = "Expat"
    version = "2.2.0"
    settings = "os", "compiler", "build_type", "arch"
    url="https://github.com/piponazo/conan-expat"
    FOLDER_NAME = "expat_%s" % version.replace(".", "_")
    license="GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007"

    def source(self):
        tarball = 'expat-2.2.0.tar.bz2'
        url='http://downloads.sourceforge.net/project/expat/expat/2.2.0/expat-2.2.0.tar.bz2'
        self.output.info("Downloading %s..." % url)
        tools.download(url, tarball)
        tools.unzip(tarball, ".")
        os.remove(tarball)

    def build(self):
        os.rename('expat-2.2.0', 'expat')
        cmake = CMake(self.settings)
        cmake_options = []
        cmake_options.append("CMAKE_INSTALL_PREFIX=installFolder")
        #n_cores = multiprocessing.cpu_count()
        n_cores = 12
        options = " -D".join(cmake_options)

        conf_command = 'cd expat && cmake . %s -D%s' % (cmake.command_line, options)
        self.output.warn(conf_command)
        self.run(conf_command)
        self.run("cd expat && cmake --build . %s -- -j%s" % (cmake.build_config, n_cores))
        self.run("cd expat && cmake --build . --target install")

    def package(self):
        self.copy("*.h",   dst="include", src="expat/installFolder/include")
        self.copy("*.so*", dst="lib",     src="expat/installFolder/lib")

    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        self.cpp_info.libs = ['expat']  # The libs to link against
        self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
        self.cpp_info.resdirs = ['res']  # Directories where resources, data, etc can be found
