
cmake_minimum_required(VERSION 3.10)
project(carSerial)

set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD 17)


include_directories(${CMAKE_CURRENT_LIST_DIR}) 
add_executable(carSerial main.c serial.c)
