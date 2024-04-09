#include <iostream>
#include <cmath>
#include <iomanip>
#include <ios>

using namespace std;

typedef long double ld;

const ld PI = 4 * atan(1);

ld a[7][7], b[7][7];
ld v[7], u[7];
int t_req;
ld t_0, t_1, t_2;
ld alpha, my_beta, my_gamma, rho, epsilon;

ld vaccination(int t) {
    if (t < t_0) {
        return 0.0;
    } else {
        return alpha * (t - t_0);
    }
}

ld social_distancing(int t) {
    if (t < t_1 || t > t_2) {
        return my_beta;
    } else {
        return my_gamma * my_beta;
    }
}

void update_matrix(int t) {

    // vaccination
    ld old_sum = a[0][0] + a[0][1];
    b[0][5] = vaccination(t);
    b[0][0] = ((1 - b[0][5]) * a[0][0]) / old_sum;
    b[0][1] = ((1 - b[0][5]) * a[0][1]) / old_sum;

    // social distancing
    ld sd_factor = social_distancing(t);
    old_sum = a[1][2] + a[1][3];
    b[1][2] = a[1][2] * (sd_factor / old_sum);
    b[1][3] = a[1][3] * (sd_factor / old_sum);

    // seasonal variation
    ld difference = epsilon * sin(2.0 * PI * (ld)t / 365.0);
    b[0][1] += difference;
    b[0][0] -= difference;

    // update A
    a[0][0] = b[0][0];
    a[0][1] = b[0][1];
    a[0][5] = b[0][5];
    a[1][2] = b[1][2];
    a[1][3] = b[1][3];

}

void update_population() {

    ld P_EI = a[1][2] + a[1][3];
    u[0] += a[5][0] * v[5] - ((a[0][1] + a[0][5]) * v[0]);
    u[1] += a[0][1] * v[0] - P_EI * v[1];
    u[2] += rho * P_EI * v[1] - ((a[2][4] + a[2][6]) * v[2]);
    u[3] += (1.0 - rho) * P_EI * v[1] - ((a[3][4] + a[3][6]) * v[3]);
    u[4] += a[2][4] * v[2] + a[3][4] * v[3];
    u[5] += a[0][5] * v[0] - a[5][0] * v[5];
    u[6] += a[2][6] * v[2] + a[3][6] * v[3];

    for (int i = 0; i < 7; i++) {
        v[i] = u[i];
    }

}

void get_input() {

    for (int i = 0; i < 7; i++) {
        for (int j = 0; j < 7; j++) {
            cin >> a[i][j];
            b[i][j] = a[i][j];
        }
    }
    cin >> t_0 >> t_1 >> t_2;
    cin >> alpha >> my_gamma >> rho >> epsilon;
    cin >> t_req;

}

void initialise_terms() {

    my_beta = a[1][2] + a[1][3];

    v[0] = u[0] = 1.0;
    for (int i = 1; i < 7; i++) {
        v[i] = u[i] = 0.0;
    }

}

int main() {

    get_input();

    initialise_terms();

    for (int t = 1; t <= t_req; t++) {
        update_population();
        update_matrix(t);
    }

    cout << fixed << setprecision(20);
    for (int i = 0; i < 7; i++) {
        cout << v[i] << " \n"[i == 6];
    }

}
