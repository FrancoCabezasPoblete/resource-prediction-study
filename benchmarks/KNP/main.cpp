// OR-Tools solution to the Knapsack problem. https://developers.google.com/optimization/pack/knapsack#c++_4
#include <algorithm>
#include <cstdint>
#include <iterator>
#include <numeric>
#include <sstream>
#include <vector>

#include "ortools/algorithms/knapsack_solver.h"

namespace operations_research {
void RunKnapsackExample() {
  // Instantiate the solver.
  KnapsackSolver solver(
      KnapsackSolver::KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
      "KnapsackExample");
  // knapPI_11_20_1000_100
  std::vector<int64_t> values = {
      384,
      57,
      768,
      399,
      228,
      640,
      456,
      399,
      256,
      342,
      1152,
      57,
      171,
      399,
      384,
      896,
      285,
      513,
      342,
      171};

  std::vector<std::vector<int64_t>> weights = {{
      183,
      178,
      366,
      1246,
      712,
      305,
      1424,
      1246,
      122,
      1068,
      549,
      178,
      534,
      1246,
      183,
      427,
      890,
      1602,
      1068,
      534}};

  std::vector<int64_t> capacities = {8242};

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
  operations_research::RunKnapsackExample();
  return EXIT_SUCCESS;
}