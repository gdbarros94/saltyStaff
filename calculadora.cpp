#include <iostream>
using namespace std;
int main (){
    int stop = true;
    while(stop){
    int num1, num2;
    char operacao;
    cout << "Digite o primeiro número: ";
    cin >> num1;
    cout << "Digite o segundo número: ";
    cin >> num2;

    cout << "Escolha a operação (+, -, *, /): ";
    cin >> operacao;
    switch (operacao)
    {
    case '+':
        cout << "Resultado: " << num1 + num2 << endl;
        break;
    case '-':
        cout << "Resultado: " << num1 - num2 << endl;
    break;
    case '*':
        cout << "Resultado: " << num1 * num2 << endl;
    break;
    case '/':
        cout << "Resultado: " << num1 / num2 << endl;
    break;
    default:
        cout << "Operação inválida" << endl;
        break;
    }
    int a = 1;
    cout << "Deseja parar o programa? (1 - sim / 2 - não): ";
    cin >> a;
        if(a == 1){
            stop = false;
        }
    }
    return 0;
}