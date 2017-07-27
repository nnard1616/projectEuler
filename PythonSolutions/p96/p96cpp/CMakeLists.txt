cmake_minimum_required(VERSION 2.8)

project(p96cpp)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

include_directories(${PROJECT_SOURCE_DIR})
include_directories(${CMAKE_BINARY_DIR})

add_definitions("-Wall -Wextra")

file(GLOB mainSources "*.cpp" "Sources/*.cpp")
file(GLOB headerFiles "Headers/*.hpp")
add_custom_target(Headers SOURCES ${headerFiles})

list(SORT mainSources)
list(SORT headerFiles)
add_executable(${PROJECT_NAME} ${mainSources})
