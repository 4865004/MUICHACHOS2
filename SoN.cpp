#include <iostream>
using namespace std;
int main(){
    
    char condicion;
    bool resultado;
    cout << "Escribe S o N para Cambiar una variable: ";
    cin >> condicion;
    if (condicion == 's'){
        resultado = true;
        cout << "La variable es: ";
        cout << resultado;
    }else if (condicion == 'n')
    {
        resultado == false;
        cout << "La variable es: ";
        cout << resultado;
    }else
    {
        cout << "Losiento no se que pusiste";
    }
      
    return 0;
}