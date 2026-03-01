#pragma once
#include "include.h"

std::complex<double> f(std::complex<double> x)
{
    return std::pow(x, 4) - 5.0 * std::pow(x, 3) + 4.0 * std::pow(x, 2) + 3.0 * x + 9.0;
}

std::complex<double> df(std::complex<double> x)
{
    return 4.0 * std::pow(x, 3) - 15.0 * std::pow(x, 2) + 8.0 * x + 3.0;
}

std::complex<double> root_step(std::complex<double> x)
{
    return x - f(x) / df(x);
}

std::vector<std::complex<double>> find_all_roots(double eps = 1e-3, double step = 0.5, double A = 4, double B = 4)
{
    std::vector<std::complex<double>> roots;
    for (double Re = -A; Re <= A; Re += step)
    {
        for (double Im = -B; Im <= B; Im += step)
        {
            std::complex<double> x(Re, Im);
            std::complex<double> x_1 = root_step(x);
            int iters = 50;
            int iter = 0;
            while (std::abs(x - x_1) > eps && iter < iters)
            {
                x = x_1;
                x_1 = root_step(x);
                iter++;
            }

            if (iter == iters)
                continue;

            if (std::abs(f(x_1)) > eps)
                continue;

            if (std::isnan(f(x_1).imag()) || std::isnan(f(x_1).real()))
                continue;

            bool flag = true;
            for (auto &r : roots)
            {
                if (std::abs(r - x_1) <= eps)
                {
                    flag = false;
                    break;
                }
            }
            if (flag)
                roots.push_back(x_1);
        }
    }
    return roots;
}

std::complex<double> newton(std::complex<double> x, std::complex<double> root, std::ostream &out, double eps = 1e-6, int steps = 100, int step = 1)
{
    out << "k ,\t|xk - x|\n";
    for (int i = 0; i <= steps; i += step)
    {
        out << i << ",\t" << std::abs(x - root) << '\n';
        std::complex<double> x_ = x;
        x = root_step(x);
        if (std::abs(x - x_) <= eps)
            break;
    }
    return x;
}
