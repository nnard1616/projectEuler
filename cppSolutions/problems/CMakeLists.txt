project(problem_solutions VERSION 0.1 LANGUAGES CXX)

file(GLOB lib_source "./source/*.cpp")

add_library(problems ${lib_source})


# Define headers for this library. PUBLIC headers are used for
# compiling the library, and will be added to consumers' build
# paths.
target_include_directories(problems PUBLIC 
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
  PRIVATE source) #why do i need this?
  
# If we have compiler requirements for this library, list them here
target_compile_features(problems
  PUBLIC cxx_auto_type
  PRIVATE cxx_variadic_templates)
  
  


  # Depend on a library that we defined in the top-level file
target_link_libraries(problems common)
    #~ boost
    #~ MyOtherLibrary)
     
# 'make install' to the correct locations (provided by GNUInstallDirs).
install(TARGETS problems EXPORT problemsConfig
    ARCHIVE  DESTINATION ${CMAKE_INSTALL_LIBDIR}
    LIBRARY  DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME  DESTINATION ${CMAKE_INSTALL_BINDIR})  # This is for Windows
install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

# This makes the project importable from the install directory
# Put config file in per-project dir (name MUST match), can also
# just go into 'cmake'.
install(EXPORT problemsConfig DESTINATION share/problems/cmake) #where is the share directory?


export(TARGETS problems FILE problemsConfig.cmake)

# Every library has unit tests, of course
#~ add_executable(testlib
    #~ test/testlib.cpp)

#~ target_link_libraries(testlib
    #~ lib)

#~ add_test(testlib testlib)
