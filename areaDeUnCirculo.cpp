#include <iostream>

using namespace std;

int main(){
    float radio;
    float pi = 3.14;
    cout << "Que tal, voy a calcular el area de un circulo \n";
    cout << "Ingresa el radio: ";
    cin >> radio;
    cout << "El area es: " << pi * (radio*radio) << endl;
    return 0;
}