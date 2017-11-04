from conans import ConanFile, CMake, tools

class ExpatConan(ConanFile):
    """ This recipe requires conan 0.25.1 at least"""

    name = "Expat"
    version = "2.2.5"
    description = "Recipe for Expat library"
    license = "MIT/X Consortium license. Check file COPYING of the library"
    url = "https://github.com/ZaMaZaN4iK/conan-expat"
    source_url = "https://github.com/libexpat/libexpat"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports = ['FindExpat.cmake', 'patches/*']

    def source(self):
        base_url = "https://github.com/libexpat/libexpat/archive"
        zip_name = "R_2_2_5.zip"
        tools.download("%s/%s" % (base_url, zip_name), "libexpat")
        tools.unzip("libexpat")

    def build(self):
        tools.patch(base_path = "libexpat-R_2_2_5", patch_file="patches/useConanFileAndIncreaseCMakeVersion.patch")

        cmake = CMake(self, parallel=True)

        cmake_args = { "BUILD_doc" : "OFF",
                       "BUILD_examples" : "OFF",
                       "BUILD_shared" : self.options.shared,
                       "BUILD_tests" : "OFF",
                       "BUILD_tools" : "OFF",
                       "CMAKE_DEBUG_POSTFIX": "d",
                       "CMAKE_POSITION_INDEPENDENT_CODE": "ON",
                     }

        cmake.configure(source_dir="../libexpat-R_2_2_5/expat", build_dir="build", defs=cmake_args)
        cmake.build(target="install")

    def package(self):
        self.copy("FindExpat.cmake", ".", ".")

    def package_info(self):
        if self.settings.build_type == "Debug":
            self.cpp_info.libs = ["expatd"]
        else:
            self.cpp_info.libs = ["expat"]
        if not self.options.shared:
            self.cpp_info.defines = ["XML_STATIC"]

    def configure(self):
        del self.settings.compiler.libcxx
