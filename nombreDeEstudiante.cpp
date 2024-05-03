#include <iostream>
using namespace std;

int main(){
    string nombreEstudiante;
    cout << "Oye dime el nombre de un estudiante" << endl;
    getline(cin, nombreEstudiante, '\n');
    cout << "Hola " << nombreEstudiante << endl;
    return 0;
}