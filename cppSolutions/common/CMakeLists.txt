project(common_problem_methods VERSION 0.1 LANGUAGES CXX)

file(GLOB lib_source "./source/*.cpp")

add_library(common ${lib_source})


# Define headers for this library. PUBLIC headers are used for
# compiling the library, and will be added to consumers' build
# paths.
target_include_directories(common PUBLIC 
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include> 
  $<INSTALL_INTERFACE:include>
  PRIVATE source) #why do i need this?
  
# If we have compiler requirements for this library, list them here
target_compile_features(common
  PUBLIC cxx_auto_type
  PRIVATE cxx_variadic_templates)
  


#do i need a link here? Common doesn't import anything from 'problems'
  # Depend on a library that we defined in the top-level file
#~ target_link_libraries(lib
    #~ boost
    #~ MyOtherLibrary)
     
# 'make install' to the correct locations (provided by GNUInstallDirs).
install(TARGETS common EXPORT commonConfig
    ARCHIVE  DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY  DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME  DESTINATION ${CMAKE_INSTALL_BINDIR})  # This is for Windows
install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

# This makes the project importable from the install directory
# Put config file in per-project dir (name MUST match), can also
# just go into 'cmake'.
install(EXPORT commonConfig DESTINATION share/common/cmake) #where is the share directory?


export(TARGETS common FILE commonConfig.cmake)

# Every library has unit tests, of course
#~ add_executable(testlib
    #~ test/testlib.cpp)

#~ target_link_libraries(testlib
    #~ lib)

#~ add_test(testlib testlib)













#~ cmake_minimum_required(VERSION 2.8.3)

#~ get_filename_component(dir_name ${CMAKE_CURRENT_LIST_DIR} NAME)

#~ file(GLOB lib_source "*.cpp" "*.h*")
#~ LIST(SORT lib_source)

#~ message(STATUS "Configuring library: ${dir_name}")
#~ add_library(${dir_name} ${lib_source})

#~ set(LIBRARY_INSTALL_PATH ${CMAKE_INSTALL_PREFIX}/lib)
#~ set(HEADER_INSTALL_PATH ${CMAKE_INSTALL_PREFIX}/include)
#~ install(TARGETS ${dir_name} DESTINATION ${LIBRARY_INSTALL_PATH})

