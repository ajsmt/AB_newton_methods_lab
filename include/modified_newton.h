#pragma once
#include "include.h"

std::complex<double> mod_root_step(std::complex<double> x, int root_count)
{
    return x - (double)root_count * f(x) / df(x);
}

std::complex<double> mod_newton(std::complex<double> x, std::complex<double> root, int root_count, std::ostream &out, double eps = 1e-6, int steps = 100, int step = 1)
{
    out << "k ,\t|xk - x|\n";
    for (int i = 0; i <= steps; i += step)
    {
        out << i << ",\t" << std::abs(x - root) << '\n';
        std::complex<double> x_ = x;
        x = mod_root_step(x, root_count);
        if (std::abs(x - x_) <= eps)
            break;
    }
    return x;
}
