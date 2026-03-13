# sudo apt install cmake
# sudo apt install build-essential
# sudo apt install gdb

# cmakelists.txt를 다시 저장해야한다.
cmake_minimum_required(VERSION 3.10)
project(study)

set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD 17)

# add_executable(add add.c)

file(GLOB EXECUTABLES "${CMAKE_CURRENT_LIST_DIR}/*.c") # CMakeLists.txt가 있는 디렉토리에서 .c 파일을 모두 찾아서 EXECUTABLES 변수에 저장

foreach(EXECUTABLE ${EXECUTABLES}) # EXECUTABLES 변수에 저장된 각 .c 파일에 대해 반복
    get_filename_component(EXE_NAME ${EXECUTABLE} NAME_WE) #string에서 확장자 제거
    add_executable(${EXE_NAME} ${EXECUTABLE}) # .c 파일을 컴파일하여 실행 파일 생성
endforeach()

