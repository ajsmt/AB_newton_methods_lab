#pragma once
#include "include.h"

double f1(double x, double y, double c)
{
    return std::pow(x - c, 2) + std::pow(y, 2) - 1;
}

double f2(double x, double y, double c)
{
    return std::pow(x, 2) + std::pow(y - c, 2) - 100;
}

double error(double x, double y, double c)
{
    return std::sqrt(std::pow(f1(x, y, c), 2) + std::pow(f2(x, y, c), 2));
}

bool system_step(double &x, double &y, double c)
{
    std::vector<std::vector<double>> J(2, std::vector<double>(2));
    J[0][0] = 2 * (x - c);
    J[0][1] = 2 * y;
    J[1][0] = 2 * x;
    J[1][1] = 2 * (y - c);

    double D = J[0][0] * J[1][1] - J[0][1] * J[1][0];
    if (std::abs(D) <= 1e-10)
        return false;

    double A = f1(x, y, c);
    double B = f2(x, y, c);

    x += ((-A * J[1][1] + B * J[0][1]) / D);
    y += ((A * J[1][0] - B * J[0][0]) / D);

    return true;
}

bool newton_system(double &x, double &y, double c, std::ostream &out, double eps = 1e-10, int iters = 100)
{
    out << "k,\terror\n";

    for (int i = 0; i < iters; i++)
    {
        double Error = error(x, y, c);
        out << i << ",\t" << Error << '\n';

        if (std::abs(Error) <= eps)
            return true;

        if (system_step(x, y, c) == false)
            return false;
    }

    return false;
}

std::vector<std::pair<double, double>> Find_all_system_roots(double c, double step = 0.5, double eps = 1e-10)
{
    double A_1 = std::max(c - 1.0, -10.0);
    double A_2 = std::min(c + 1.0, 10.0);
    double B_1 = std::max(-1.0, c - 10.0);
    double B_2 = std::min(1.0, c + 10.0);

    std::vector<std::pair<double, double>> All_roots;

    for (double x = A_1; x <= A_2; x += step)
    {
        for (double y = B_1; y <= B_2; y += step)
        {
            double root_x = x;
            double root_y = y;

            std::ostringstream data;

            bool is_root = newton_system(root_x, root_y, c, data);

            if (!is_root)
                continue;

            if (std::abs(error(root_x, root_y, c)) > eps)
                continue;

            bool flag = true;
            for (auto [X, Y] : All_roots)
            {
                if (std::abs(X - root_x) <= 1e-4 && std::abs(Y - root_y) <= 1e-4)
                {
                    flag = false;
                    break;
                }
            }

            if (!flag)
                continue;

            All_roots.push_back({root_x, root_y});
            std::ofstream fout("system_" + std::to_string(c) + "_" + std::to_string(All_roots.size()) + ".txt");
            fout << data.str();
        }
    }
    return All_roots;
}