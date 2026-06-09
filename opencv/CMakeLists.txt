cmake_minimum_required(VERSION 3.16)
project(opencv_cpp_basic)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)

file(GLOB_RECURSE SOURCES CONFIGURE_DEPENDS
    "${CMAKE_CURRENT_SOURCE_DIR}/part*/*.cpp"
)

foreach(SOURCE IN LISTS SOURCES)
    get_filename_component(EXE_NAME "${SOURCE}" NAME_WE)
    add_executable("${EXE_NAME}" "${SOURCE}")
    target_include_directories("${EXE_NAME}" PRIVATE
        "${CMAKE_CURRENT_SOURCE_DIR}/part1"
    )
    target_link_libraries("${EXE_NAME}" PRIVATE ${OpenCV_LIBS})
endforeach()
