cmake_minimum_required(VERSION 3.17)

project(ExtremeVoxel)

#add_executable(extreme-voxel main.cpp)
add_executable(extreme-voxel main.cpp /home/gabriele/workspace/glfw/deps/glad_gl.c)

set(GLFW_BUILD_DOCS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_TESTS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)

add_subdirectory(/home/gabriele/workspace/glfw glfw)
target_link_libraries(extreme-voxel glfw)
find_package(OpenGL REQUIRED)
target_link_libraries(extreme-voxel OpenGL::GL)
include_directories(glfw/deps/)
include_directories(/home/gabriele/workspace/glfw/deps/)
