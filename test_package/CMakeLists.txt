project(PackageTest C)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Expat REQUIRED)

message("EXPAT_LIBRARY: ${EXPAT_LIBRARY}")
message("EXPAT_INCLUDE_DIR: ${EXPAT_INCLUDE_DIR}")

add_executable(example example.c)
target_link_libraries(example ${EXPAT_LIBRARY})
target_compile_definitions(example PRIVATE "-DXML_STATIC")
