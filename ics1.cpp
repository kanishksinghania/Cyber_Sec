#include<iostream>
#include<string>
#include<bits/stdc++.h>

using namespace std;

void en(string text, int r) {
    int n = text.length();
    char arr[n + 1];
    strcpy(arr, text.c_str());
    char result[r][n];
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = ' ';
        }
    }
    int row = 0; 
    bool down = true; 

    for (int i = 0; i < n; i++) {
        result[row][i] = arr[i];
        if (row == 0) {
            down = true;
        } else if (row == r - 1) {
            down = false;
        }
        if (down) {
            row++;
        } else {
            row--;
        }
    }
    cout << "Rail Fence Cipher Matrix:" << endl;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < n; j++) {
            if (result[i][j] != ' ') {
                cout << result[i][j];
            }
        }
    }
    cout << endl;
}
void dp(string ciphertext, int r) {
    int n = ciphertext.length();
    char arr[n + 1];
    strcpy(arr, ciphertext.c_str());
    char result[r][n];

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < n; j++) {
            result[i][j] = ' ';
        }
    }

    int row = 0;
    bool down = true;
    for (int i = 0; i < n; i++) {
        result[row][i] = ' '; 
        if (row == 0) {
            down = true;
        } else if (row == r - 1) {
            down = false;
        }
        if (down) {
            row++;
        } else {
            row--;
        }
    }
    int index = 0;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < n; j++) {
            if (result[i][j] == '*') {
                result[i][j] = arr[index++];
            }
        }
    }
    cout << "Decrypted Message: ";
    row = 0;
    down = true;

    for (int i = 0; i < n; i++) {
        cout << result[row][i];
        if (row == 0) {
            down = true;
        } else if (row == r - 1) {
            down = false;
        }
        if (down) {
            row++;
        } else {
            row--;
        }
    }

    cout << endl;
}


int main() {
    string pt; 
    string ct;
    int key;
    int ch;
    cout<<"What do you want to perform in Rail Fence Cipher: \n";
    cout<<"1) Encryption\n2) Decryption\n";
    cin>>ch;
    switch(ch) {
        case 1:
            cout<<"Enter the plaintext: ";
            cin>>pt;
            cout<<"Enter the key: ";
            cin>>key;
            cout<<"The Encrypted message is: \n";
            en(pt,key);
            break;
        case 2:
            cout<<"Enter the ciphertext: ";
            cin>>ct;
            cout<<"Enter the key: ";
            cin>>key;
            cout<<"The Decrypted message is: \n";
            dp(ct,key);
            break;
    }

}

