// OR-Tools solution to the Knapsack problem. https://developers.google.com/optimization/pack/knapsack#c++_4
#include <algorithm>
#include <cstdint>
#include <iterator>
#include <numeric>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

#include "ortools/algorithms/knapsack_solver.h"

namespace operations_research {
void RunKnapsackExample(const std::string& filename) {
  // Instantiate the solver.
  KnapsackSolver solver(
    KnapsackSolver::KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
    "KnapsackExample");
  
  std::ifstream file(filename);
  if (!file) {
    std::cerr << "No se pudo abrir el archivo." << std::endl;
    return;
  }
  std::string line;
  std::vector<int64_t> values;
  std::vector<std::vector<int64_t>> weights(1);
  std::vector<int64_t> capacities;
  // knapPI_11_20_1000_100
  while (std::getline(file, line)) {
    if (line.rfind("z ", 0) == 0) {
      std::istringstream iss(line.substr(2));
      int64_t capacity;
      iss >> capacity;
      capacities.push_back(capacity);
      continue;
    }

    if (line.find("knapPI") != std::string::npos || line.find("n ") != std::string::npos || 
      line.find("c ") != std::string::npos || line.find("time ") != std::string::npos) {
      continue;
    }

    std::istringstream iss(line);
    std::string part;
    int counter = 0;
    int64_t value, weight;

    while (std::getline(iss, part, ',')) {
      int64_t number = std::stoll(part);
      if (counter == 1) {
        value = number;
      } else if (counter == 2) {
        weight = number;
      }
      counter++;
    }

    values.push_back(value);
    weights[0].push_back(weight);
  }
  
  solver.Init(values, weights, capacities);
  int64_t computed_value = solver.Solve();

  // Print solution
  std::vector<int> packed_items;
  for (std::size_t i = 0; i < values.size(); ++i) {
    if (solver.BestSolutionContains(i)) packed_items.push_back(i);
  }
  std::ostringstream packed_items_ss;
  std::copy(packed_items.begin(), packed_items.end() - 1,
            std::ostream_iterator<int>(packed_items_ss, ", "));
  packed_items_ss << packed_items.back();

  std::vector<int64_t> packed_weights;
  packed_weights.reserve(packed_items.size());
  for (const auto& it : packed_items) {
    packed_weights.push_back(weights[0][it]);
  }
  std::ostringstream packed_weights_ss;
  std::copy(packed_weights.begin(), packed_weights.end() - 1,
            std::ostream_iterator<int>(packed_weights_ss, ", "));
  packed_weights_ss << packed_weights.back();

  int64_t total_weights =
      std::accumulate(packed_weights.begin(), packed_weights.end(), int64_t{0});

  //LOG(INFO) << "Total value: " << computed_value;
  //LOG(INFO) << "Packed items: {" << packed_items_ss.str() << "}";
  //LOG(INFO) << "Total weight: " << total_weights;
  //LOG(INFO) << "Packed weights: {" << packed_weights_ss.str() << "}";
}
}  // namespace operations_research

int main(int argc, char** argv) {
  if (argc != 2) {
    std::cerr << "Use: " << argv[0] << " <filename>" << std::endl;
    return EXIT_FAILURE;
  }
  operations_research::RunKnapsackExample(argv[1]);
  return EXIT_SUCCESS;
}