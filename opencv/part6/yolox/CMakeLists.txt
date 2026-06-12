cmake_minimum_required(VERSION 3.22)
set(project_name "opencv_zoo_object_detection_yolox")

PROJECT (${project_name})

set(OPENCV_VERSION "4.5.0")
set(OPENCV_INSTALLATION_PATH "" CACHE PATH "Where to look for OpenCV installation")
find_package(OpenCV ${OPENCV_VERSION} REQUIRED HINTS ${OPENCV_INSTALLATION_PATH})
# Find OpenCV, you may need to set OpenCV_DIR variable
# to the absolute path to the directory containing OpenCVConfig.cmake file
# via the command line or GUI

# If the package has been found, several variables will
# be set, you can find the full list with descriptions
# in the OpenCVConfig.cmake file.
# Print some message showing some of them
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

# Declare the executable targets built from your sources
add_executable(${project_name} demo.cpp)
add_executable(yolox_cpu demo1.cpp)

# Link your application with OpenCV libraries
target_link_libraries(${project_name} PRIVATE ${OpenCV_LIBS})
target_link_libraries(yolox_cpu PRIVATE ${OpenCV_LIBS})
