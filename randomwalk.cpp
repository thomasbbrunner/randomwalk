
#include <array>
#include <random>
#include <iostream>

int main(int, char const **)
{
    // configuration
    constexpr unsigned int iterations = 1000;
    constexpr std::array<unsigned int, 2> space_size{
        100,
        100};
    constexpr unsigned int space_dims = space_size.size();

    std::mt19937 rand_engine(1234);
    std::uniform_int_distribution<unsigned int> rand_dist_space_dims(0, space_dims);
    std::uniform_int_distribution<unsigned int> rand_dist_0_2(0, 2);

    // array with coordinate history
    std::array<std::array<unsigned int, space_dims>, iterations> coords{0};

    // starting coordinates
    for (unsigned int i; i < space_dims; i++)
    {
        std::uniform_int_distribution<unsigned int> rand_dist_space_size(0, space_size.at(i));
        coords.at(0).at(i) = rand_dist_space_size(rand_engine);
    }

    // borders (format {x_min, y_min} and {x_max, y_max})
    std::array<unsigned int, space_dims> min_coords{0};
    std::array<unsigned int, space_dims> max_coords = space_size;
    for (auto &&max_coord : max_coords)
    {
        max_coord -= 1;
    }

    // new coordinates
    std::array<std::array<int, space_dims>, 2> new_coords{0};

    return 0;
}
