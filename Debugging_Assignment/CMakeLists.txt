cmake_minimum_required(VERSION 3.10)
project(DebugChallenge)
set(CMAKE_CXX_STANDARD 17)
find_package(Eigen3 REQUIRED)
# Create executable
add_executable(debug_challenge main.cpp)

# BUG: Missing target link libraries for Eigen
# target_link_libraries(debug_challenge Eigen3: Eigen)