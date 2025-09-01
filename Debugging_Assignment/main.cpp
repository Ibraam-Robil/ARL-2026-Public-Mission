/*
 * AUTOTRONICS RESEARCH LAB - AUTONOMOUS SYSTEMS WORKSHOP
 * SOLO MISSION: DEBUGGING CHALLENGE
 *
 * INSTRUCTIONS:
 * This file contains multiple bugs across different complexity levels.
 * Your task is to fix ALL bugs and make the program compile and run correctly.
 *
 * Bugs:
 * Level 1 (Compilation Issues)
 * Level 2 (Logic Issues)
 * Level 3 (Algorithm Issues)
 *
 * EXPECTED OUTPUTS:
 * When fixed correctly, the program should output specific strings.
 *
 * SUBMISSION REQUIREMENTS:
 * 1. Submit the corrected code
 * 2. Document what each bug was and how you fixed it
 * 3. Explain what research you did and sources you used
 * 4. Explain how the final solution works
 *
 * You may use AI tools and online resources, but you must understand
 * the solution completely as you'll be interviewed about it.
 */

#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <Eigen/Dense>

using namespace std;

string decodeMessage(int values[], int size) {
    string result = "";
    for (int i = 0; i < size; i++) {   
        if (values[i] > 0) {
            result += char(values[i]);
        }
    }
    return result;
}

Eigen::Vector3d applyRotation(double angle, Eigen::Vector3d point) {
    double scl = 0.5;
    Eigen::Matrix3d rotation;
    rotation << cos(angle)-scl,    -sin(angle),     0,  // BUG: Wrong rotation matrix
                    sin(angle), cos(angle)-scl,     0,
                             0,              0, 1-scl;

    // cout << "Rotation Matrix:\n" << rotation * point << endl;

    return rotation * point;

    // CMakeList BUG
}

string extractName(Eigen::Vector3d result) {
    int ascii_vals[3];
    ascii_vals[0] = int(round(abs(result.x())));
    ascii_vals[1] = int(round(abs(result.y())));
    ascii_vals[2] = int(round(abs(result.z())));
    return decodeMessage(ascii_vals, 3);
}

int main() {
    cout << "Autotronics Research Lab - Debug Challenge" << endl;

    cout << "Level 2 Test: ";
    int simple_values[] = {65, 109, 105, 110, 32, 105, 115};
    int length = sizeof(simple_values) / sizeof(simple_values[0]);
    cout << decodeMessage(simple_values, length) << endl;

    cout << "Level 3 Test: ";
    // cout << "Level 3 Test: " << endl;

    Eigen::Vector3d original_point(83.0, 97.0, 100.0);

    double rotation_angle = M_PI / 4.0;   // 45 degrees

    Eigen::Vector3d rotated = applyRotation(rotation_angle, original_point);

    cout << extractName(rotated) << endl;

    return 0;
}