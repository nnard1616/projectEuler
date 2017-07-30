#include <problems/p102.hpp>

// Use Heron's formula for the area of a triangle given the lengths a,b,c of the
// sides A = sqrt s*(s-a)*(s-b)*(s-c) where s is the semiperimeter 0.5*(a+b+c).
// Apply Heron's formula to the whole triangle. Apply Heron's formula to the 3
// triangles formed by the origin and each of the 3 pairs of points. The origin
// is in the interior if the area of the whole triangle equals the sum of the
// areas of the 3 triangles.

// I actually used matrix determinants to calculate areas, but same general
// principle.
namespace problems
{
  int p102()
  {
    std::ifstream infile("../../cppSolutions/problems/txt/p102_triangles.txt");
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
    double triArea = std::abs(arma::det(tri)) / 2;
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
