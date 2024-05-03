#include <iostream>
using namespace std;
int main(){
    float numero1;
    float numero2;
    int operacion;
    float resultado;
    cout << "Que tal Voy A ser tu calculadora con 2 numeros \n dame el primer numero: \n";
    cin >> numero1;
    cout << "dame el segundo numero: \n";
    cin >> numero2;
    cout << "dime que operacion quieres hacer? \n 1 => suma\n 2 => resta\n 3 => multicacion\n 4 => division\n";
    cin >> operacion;
    if (operacion == 1)
    {
        resultado = numero1 + numero2;
        cout << "El resultado de la suma es: ";
        cout << resultado;
    }else if (operacion == 2){
        resultado = numero1 - numero2;
        cout << "El resultado de la resta es: ";
        cout << resultado;
    }else if (operacion == 3){
        resultado = numero1 * numero2;
        cout << "El resultado de la multiplicacion es: ";
        cout << resultado;
    }else if (operacion == 4){
        resultado = numero1 / numero2;
        cout << "El resultado de la division es: ";
        cout << resultado;
    }else
    {
        cout << "Losiento No Tengo Esa Opcion";
    }
    
    
return 0;

}