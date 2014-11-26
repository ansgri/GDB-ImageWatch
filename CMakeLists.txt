cmake_minimum_required(VERSION 2.8)

find_package(OpenCV REQUIRED)
if (OpenCV_FOUND)
	message("OpenCV found in  ${OpenCV_INCLUDE_LIST}\n")
endif (OpenCV_FOUND)

if (NOT OpenCV_FOUND)
	message(FATAL_ERROR "OpenCV is required" )
endif(NOT OpenCV_FOUND)

add_executable(main test.cpp)
target_link_libraries(main ${OpenCV_LIBS})
