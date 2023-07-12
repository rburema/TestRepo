#include <iostream>
#include <ranges>
#include <string_view>
#include <vector>

class A
{
public:
    int z;
};

int main()
{
    using namespace std::literals;

    const auto bits = { "https:"sv, "//"sv, "cppreference"sv, "."sv, "com"sv };
    for (char const c : bits | std::views::join)
        std::cout << c;
    std::cout << '\n';

    const std::vector<std::vector<int>> v{ { 1, 2 }, { 3, 4, 5 }, { 6 }, { 7, 8, 9 } };
    const std::vector<std::vector<std::vector<int>>> w{ v, v, v };

    auto jv = std::ranges::join_view(w);
    for (auto const e : jv)
    {
        std::cout << '\n';
        for (auto const ee : e)
        {
            A.z = ee;
            std::cout << A.z << ' ';
        }
    }
    std::cout << '\n';
}
