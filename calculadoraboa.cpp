#include <iostream>
using namespace std;

    float soma(float a, float b){
        return a + b;
    }
    float subtracao(float a, float b){
        return a - b;
    }
    float multiplicacao(float a, float b){
        return a * b;
    }
    float divisao(float a, float b){
        if(b != 0){
            return a / b;
        }else{
            cout << "Erro: Divisão por zero" << endl;
            return 0;
        }
    }

int main (){
    float num1, num2;
    char operacao;
    char continuar;
    do {
        cout << "Digite a operação (+, -, *, /,): ";
        cin >> operacao;
        cout << "Digite o primeiro numero: ";
        cin >> num1;
        cout << "Digite o segundo numero: ";
        cin >> num2;

         switch (operacao)
         {
         case '+':
             cout << soma(num1, num2) << endl;
            break;
        case '-':
             cout << subtracao(num1, num2) << endl;
            break;
        case '*':
             cout << multiplicacao(num1, num2) << endl;
            break;
        case '/':
             cout << divisao(num1, num2) << endl;
            break;
         
         default:
            cout << "Operação inválida!" << endl;
            break;
         }

         cout << "Deseja continuar o programa? (s/n): ";
         cin >> continuar;

    }while(continuar == 's' || continuar == 'S');
    cout << "Saindo do programa." << endl;
    return 0;
}