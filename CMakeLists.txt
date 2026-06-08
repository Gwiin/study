cmake_minimum_required(VERSION 3.10)
project(study)

set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD 17)

include(ExternalProject)

set(PICO_BOARD "pico2_w" CACHE STRING "Target Raspberry Pi Pico board")

string(REPLACE " " "_" ATMEGA128_GENERATOR_TAG "${CMAKE_GENERATOR}")
set(ATMEGA128_BINARY_DIR "${CMAKE_BINARY_DIR}/atmega128-build-${ATMEGA128_GENERATOR_TAG}")
string(REPLACE " " "_" PICO_GENERATOR_TAG "${CMAKE_GENERATOR}")
set(PICO_BINARY_DIR "${CMAKE_BINARY_DIR}/pico-build-${PICO_GENERATOR_TAG}")

add_subdirectory(c/basics/part3)
add_subdirectory(c/basics/part4/carSerial)
add_subdirectory(c/basics/part4/myRandom)
add_subdirectory(c/basics/part4/baseballGame)
add_subdirectory(c/basics/part5/date)
add_subdirectory(c/basics/part5/twoDouble)
add_subdirectory(c/basics/part6/scoreProcess)
add_subdirectory(c/ds/stack/myStack1)
add_subdirectory(c/ds/stack/myStack2)
add_subdirectory(c/ds/stack/myStack3)
add_subdirectory(c/ds/stack/myStack4)
add_subdirectory(c/ds/queue/myQueue1)
add_subdirectory(c/ds/queue/myQueue3)
add_subdirectory(c/projects/bowlingGame)
add_subdirectory(opencv)

ExternalProject_Add(pico_project
	SOURCE_DIR ${CMAKE_SOURCE_DIR}/embedded/pico
	BINARY_DIR ${PICO_BINARY_DIR}
	CMAKE_GENERATOR ${CMAKE_GENERATOR}
	BUILD_ALWAYS 1
	CMAKE_ARGS
		-DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
		-DCMAKE_EXPORT_COMPILE_COMMANDS=ON
		-DPICO_BOARD=${PICO_BOARD}
		-DPICO_SDK_PATH=${CMAKE_SOURCE_DIR}/embedded/pico/deps/pico-sdk
	INSTALL_COMMAND ""
)

ExternalProject_Add_Step(pico_project sync_compile_commands
	COMMAND ${CMAKE_COMMAND} -E copy_if_different
		${PICO_BINARY_DIR}/compile_commands.json
		${CMAKE_SOURCE_DIR}/embedded/pico/compile_commands.json
	DEPENDEES build
	ALWAYS 1
	COMMENT "Syncing Pico compile_commands.json for IDE support"
)

ExternalProject_Add(atmega128_project
	SOURCE_DIR ${CMAKE_SOURCE_DIR}/embedded/atmega128
	BINARY_DIR ${ATMEGA128_BINARY_DIR}
	CMAKE_GENERATOR ${CMAKE_GENERATOR}
	BUILD_ALWAYS 1
	CMAKE_ARGS
		-DCMAKE_TOOLCHAIN_FILE=${CMAKE_SOURCE_DIR}/embedded/atmega128/avr-toolchain.cmake
		-DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE}
		-DCMAKE_EXPORT_COMPILE_COMMANDS=ON
	INSTALL_COMMAND ""
)

ExternalProject_Add_Step(atmega128_project sync_compile_commands
	COMMAND ${CMAKE_COMMAND} -E copy_if_different
		${ATMEGA128_BINARY_DIR}/compile_commands.json
		${CMAKE_SOURCE_DIR}/embedded/atmega128/compile_commands.json
	DEPENDEES configure
	ALWAYS 1
	COMMENT "Syncing AVR compile_commands.json for IDE support"
)
