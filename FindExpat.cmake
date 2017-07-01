find_path(EXPAT_INCLUDE_DIR NAMES expat.h PATHS ${CONAN_INCLUDE_DIRS_EXPAT})
find_library(EXPAT_LIBRARY NAMES ${CONAN_LIBS_EXPAT} PATHS ${CONAN_LIB_DIRS_EXPAT})

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(Expat DEFAULT_MSG
    EXPAT_INCLUDE_DIR EXPAT_LIBRARY)
