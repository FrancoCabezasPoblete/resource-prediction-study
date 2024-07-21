#include <cmath>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

#include "ortools/constraint_solver/routing.h"
#include "ortools/constraint_solver/routing_enums.pb.h"
#include "ortools/constraint_solver/routing_index_manager.h"
#include "ortools/constraint_solver/routing_parameters.h"

namespace operations_research {
struct DataModel {
    //rat783.tsp
    const std::vector<std::vector<int>> locations;
    const int num_vehicles = 1;
    const RoutingIndexManager::NodeIndex depot{0};
};

// @brief Generate distance matrix.
std::vector<std::vector<int64_t>> ComputeEuclideanDistanceMatrix(
    const std::vector<std::vector<int>>& locations
) {
    std::vector<std::vector<int64_t>> distances = std::vector<std::vector<int64_t>>(
        locations.size(),
        std::vector<int64_t>(locations.size(),
        int64_t{0})
    );
    for (int from_node = 0; from_node < locations.size(); from_node++) {
        for (int to_node = 0; to_node < locations.size(); to_node++) {
            if (from_node != to_node)
            distances[from_node][to_node] = static_cast<int64_t>(
                std::hypot(
                    (locations[to_node][0] - locations[from_node][0]),
                    (locations[to_node][1] - locations[from_node][1])
                )
            );
        }
    }
    return distances;
}

/*
//! @brief Print the solution
//! @param[in] manager Index manager used.
//! @param[in] routing Routing solver used.
//! @param[in] solution Solution found by the solver.
void PrintSolution(
    const RoutingIndexManager& manager,
    const RoutingModel& routing, const Assignment& solution
) {
    LOG(INFO) << "Objective: " << solution.ObjectiveValue();
    // Inspect solution.
    int64_t index = routing.Start(0);
    //LOG(INFO) << "Route:";
    int64_t distance{0};
    std::stringstream route;
    while (!routing.IsEnd(index)) {
        route << manager.IndexToNode(index).value() << " -> ";
        const int64_t previous_index = index;
        index = solution.Value(routing.NextVar(index));
        distance += routing.GetArcCostForVehicle(previous_index, index, int64_t{0});
    }
    LOG(INFO) << route.str() << manager.IndexToNode(index).value();
    LOG(INFO) << "Route distance: " << distance << "miles";
    LOG(INFO) << "";
    LOG(INFO) << "Advanced usage:";
    LOG(INFO) << "Problem solved in " << routing.solver()->wall_time() << "ms";
}
*/

void Tsp(const std::string& filename) {
    std::ifstream file(filename);
	if (!file) {
		std::cerr << "No se pudo abrir el archivo." << std::endl;
		return;
	}

    std::string line;
    std::vector<std::vector<int>> locations;

    while (std::getline(file, line)) {
        if (line.rfind("NODE_COORD_SECTION", 0) == 0)
            break;
    }
    while (std::getline(file, line)) {
        if (line.rfind("EOF", 0) == 0) {
            break;
        }
        std::istringstream iss(line);
        int index, x, y;
        iss >> index >> x >> y;
        locations.push_back({x, y});
    }

    // Instantiate the data problem.
    DataModel data = {locations};

    // Create Routing Index Manager
    RoutingIndexManager manager(data.locations.size(), data.num_vehicles, data.depot);

    // Create Routing Model.
    RoutingModel routing(manager);

    const auto distance_matrix = ComputeEuclideanDistanceMatrix(data.locations);
    const int transit_callback_index = routing.RegisterTransitCallback(
        [&distance_matrix, &manager](const int64_t from_index,const int64_t to_index) -> int64_t {
            // Convert from routing variable Index to distance matrix NodeIndex.
            const int from_node = manager.IndexToNode(from_index).value();
            const int to_node = manager.IndexToNode(to_index).value();
            return distance_matrix[from_node][to_node];
        }
    );

    // Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index);

    // Setting first solution heuristic.
    RoutingSearchParameters searchParameters = DefaultRoutingSearchParameters();
    searchParameters.set_first_solution_strategy(
        FirstSolutionStrategy::AUTOMATIC
        //FirstSolutionStrategy::PATH_CHEAPEST_ARC
    );

    // Solve the problem.
    const Assignment* solution = routing.SolveWithParameters(searchParameters);

    // Print solution on console.
    //PrintSolution(manager, routing, *solution);
    }
}  // namespace operations_research

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Use: " << argv[0] << " <filename>" << std::endl;
        return EXIT_FAILURE;
    }
    operations_research::Tsp(argv[1]);
    return EXIT_SUCCESS;
}