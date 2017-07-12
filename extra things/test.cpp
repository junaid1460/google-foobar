#include<iostream>
#include<stdlib.h>

int randomnumber() {
    srand(time(NULL));
    int number;
    number = rand()%10+1;

    return number;

}
using namespace std;

int main()
{
    int tries = 0;

    while(true) {
        int guess;
        cout << "A random number between 1 and 10 has been chosen. Guess the number:" << endl;
        cin >> guess;

        if(guess>randomnumber()){
            cout << "Your guess is too high!" << endl;
            tries++;
        }

        else if(guess==randomnumber()) {
            cout << "Correct! The number was " << randomnumber() << endl;

        }

        else if(guess<randomnumber()) {
            cout << "Your guess is too low!" << endl;
            tries++;

        }

    }
    return 0;
}

