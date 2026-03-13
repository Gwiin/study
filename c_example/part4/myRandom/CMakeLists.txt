
cmake_minimum_required(VERSION 3.10)
project(myRandom)

set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD 17)


include_directories(${CMAKE_CURRENT_LIST_DIR}) #설명 : 현재 CMakeLists.txt 파일이 있는 디렉토리를 포함 디렉토리로 추가합니다. 이렇게 하면 해당 디렉토리에 있는 헤더 파일들을 소스 파일에서 사용할 수 있게 됩니다.
add_executable(myRandom main.c myRandom.c)
