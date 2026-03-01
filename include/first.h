#pragma once
#include "include.h"

void first()
{
    std::cout << "Задание - 1\n";

    std::vector<std::complex<double>> roots = {3,
                                               std::complex<double>(-0.5, sqrt(3) / 2),
                                               std::complex<double>(-0.5, -sqrt(3) / 2)};
    std::vector<std::complex<double>> starts = {2,
                                                std::complex<double>(1, 1),
                                                std::complex<double>(1, -1)};

    std::vector<std::complex<double>> Found_roots = find_all_roots();
    std::cout << "------------\n";
    std::cout << "Все найденные корни: \n";
    for (auto &i : Found_roots)
        std::cout << '(' << i.real() << " + i" << i.imag() << "); \t";
    for (int i = 0; i < roots.size(); i++)
    {
        std::cout << "\n------------\n";
        std::ofstream fout("first_root_" + std::to_string(i) + ".txt");
        auto Res = newton(starts[i], roots[i], fout);
        std::cout << std::setprecision(8);
        std::cout << "Для начального приближения: " + std::to_string(starts[i].real()) + " + i" + std::to_string(starts[i].imag()) + '\n';
        std::cout << "Найден корень: " + std::to_string(Res.real()) + " + i" + std::to_string(Res.imag()) + '\n';
        std::cout << "Данные о сходимости записаны в файл: first_root_" + std::to_string(i);
    }
}