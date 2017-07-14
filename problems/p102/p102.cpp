#include "p102.hpp"

namespace p102
{
  int p102()
  {
    std::ifstream infile("../problems/p102/p102_triangles.txt");
    mat tri(3, 3);
    string line;
    vector<mat> triangles;
    int x1, y1, x2, y2, x3, y3;

    while (getline(infile, line))
    {
      vector<string> points = common::split(line, ',');
      x1 = std::stoi(points[0]);
      y1 = std::stoi(points[1]);
      x2 = std::stoi(points[2]);
      y2 = std::stoi(points[3]);
      x3 = std::stoi(points[4]);
      y3 = std::stoi(points[5]);

      // clang-format off
      tri << x1 << y1 << 1 << endr
          << x2 << y2 << 1 << endr
          << x3 << y3 << 1 << endr;

      // clang-format on
      triangles.push_back(tri);
    }
    infile.close();

    int origins = 0;
    for (auto it = triangles.begin(); it != triangles.end(); ++it)
      if (contains_origin(*it))
        origins++;
    return origins;
  }

  bool contains_origin(mat tri)
  {
    double triArea = arma::det(tri) / 2;
    mat oriTri(3, 3);
    double oriTriArea = 0;
    for (int i = 0; i != 3; ++i)
    {
      oriTri = tri;
      oriTri(i, 0) = 0;
      oriTri(i, 1) = 0;
      oriTriArea += std::abs(arma::det(oriTri)) / 2;
    }
    if (triArea == oriTriArea)
      return true;
    return false;
  }
}
