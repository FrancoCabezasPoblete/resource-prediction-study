cmake_minimum_required(VERSION 3.14)
project(benchmarks VERSION 1.0)

set(CMAKE_PREFIX_PATH "/opt/ortools")
find_package(ortools CONFIG REQUIRED)

add_executable(knp KNP/main.cpp)
target_link_libraries(knp ortools::ortools)
add_executable(n_queens N_QUEENS/main.cpp)
target_link_libraries(n_queens ortools::ortools)
add_executable(tsp TSP/main.cpp)
target_link_libraries(tsp ortools::ortools)