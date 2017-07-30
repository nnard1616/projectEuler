cmake_minimum_required(VERSION 3.2 FATAL_ERROR)
project(project_euler VERSION 0.1 LANGUAGES CXX)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ")
set(CMAKE_CXX_STANDARD 14)

include(GNUInstallDirs)



#~ enable_testing()
add_subdirectory(problems)
add_subdirectory(common)
add_subdirectory(main_app)
























#~ cmake_minimum_required(VERSION 2.8)

#~ project(projectEuler)
#~ set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}  -std=c++14")
#~ #-larmadillo
#~ include_directories(${PROJECT_SOURCE_DIR})
#~ include_directories(${CMAKE_BINARY_DIR})

#~ add_definitions("-Wall -Wextra ")

#~ add_subdirectory(common)
#~ add_subdirectory(problems/p103)
#~ add_subdirectory(problems/p105)
#~ add_subdirectory(problems/p106)

#~ file(GLOB apps_source "apps/*.cpp")
#~ list(SORT apps_source)

#~ set(exec_dependencies common p103 p105 p106)

#~ message(STATUS "\n   Applications: ")
#~ foreach(app_src_file ${apps_source})
    #~ get_filename_component(app_base ${app_src_file} NAME_WE)
    #~ message(STATUS "Adding application ${app_base}")
    #~ add_executable(${app_base} ${app_src_file})
    #~ target_link_libraries(${app_base} ${exec_dependencies})
#~ endforeach(app_src_file)

