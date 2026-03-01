#pragma once
#include "include.h"

void second()
{
    std::vector<double> C = {0.0, 9.0 / std::sqrt(2), 7.0};

    for (double c : C)
    {
        std::cout << "\n------------\n";
        std::cout << "c: " << c << '\n';
        auto roots = Find_all_system_roots(c);
        std::cout << "Корней: " << roots.size() << '\n';
        for(int i = 0; i < roots.size(); i++){
            std::cout << i << ": (" << roots[i].first << ", " << roots[i].second << ");\n";
        }
        if (roots.empty())
            std::cout << "Корней нет\n";
    }
}