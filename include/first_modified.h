#pragma once
#include "include.h"

void first_modified()
{
    std::cout << "Задание - 1 - с модифицированным методом ньютона\n";

    std::vector<std::complex<double>> roots = {3,
                                               std::complex<double>(-0.5, sqrt(3) / 2),
                                               std::complex<double>(-0.5, -sqrt(3) / 2)};
    std::vector<int> root_count = {2, 1, 1};
    std::vector<std::complex<double>> starts = {2,
                                                std::complex<double>(1, 1),
                                                std::complex<double>(1, -1)};
    for (int i = 0; i < roots.size(); i++)
    {
        std::cout << "\n------------\n";
        std::ofstream fout("mod_first_root_" + std::to_string(i) + ".txt");
        auto Res = mod_newton(starts[i], roots[i], root_count[i], fout);
        std::cout << std::setprecision(8);
        std::cout << "Для начального приближения: " + std::to_string(starts[i].real()) + " + i" + std::to_string(starts[i].imag()) + '\n';
        std::cout << "Найден корень: " + std::to_string(Res.real()) + " + i" + std::to_string(Res.imag()) + '\n';
        std::cout << "Данные о сходимости записаны в файл: mod_first_root_" + std::to_string(i);
    }
}