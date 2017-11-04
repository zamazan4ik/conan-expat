cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(SKIP_RPATH)

if (UNIX)
    set(CMAKE_BUILD_WITH_INSTALL_RPATH ON)
    if (APPLE)
        set(CMAKE_INSTALL_RPATH "@executable_path/../lib")
    else ()
        set(CMAKE_INSTALL_RPATH "$ORIGIN/../lib")
    endif ()
endif ()

find_package(Expat REQUIRED)

add_executable(example example.c)
target_link_libraries(example ${EXPAT_LIBRARY})
target_compile_definitions(example PRIVATE "-DXML_STATIC")
