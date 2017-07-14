cmake_minimum_required(VERSION 2.8)

project(projectEuler)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -larmadillo -std=c++11")
#-larmadillo
include_directories(${PROJECT_SOURCE_DIR})
include_directories(${CMAKE_BINARY_DIR})

add_definitions("-Wall -Wextra ")

add_subdirectory(common)
add_subdirectory("problems/p102")

file(GLOB apps_source "apps/*.cpp")
list(SORT apps_source)

set(exec_dependencies common p102)

message(STATUS "\n   Applications: ")
foreach(app_src_file ${apps_source})
    get_filename_component(app_base ${app_src_file} NAME_WE)
    message(STATUS "Adding application ${app_base}")
    add_executable(${app_base} ${app_src_file})
    target_link_libraries(${app_base} ${exec_dependencies})
endforeach(app_src_file)

