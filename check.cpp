#include <iostream>
#include <string>
using namespace std;

const int MAX_STUDENTS = 20;

// this function will calculate the result of the student
int calculateResult(int midExamResult, int finalExamResult) {
    return midExamResult + finalExamResult;
}

 char determineGrade(int result) {
    if (result >= 90) {
        return 'A';
    } else if (result >= 80) {
        return 'B';
    } else if (result >= 60) {
        return 'C';
    } else if (result >= 50) {
        return 'D';
    } else {
        return 'F';
    }
}


void displayStudentInfo(string names[], int midExamResults[], int finalExamResults[], int results[], char grades[], int size) {
    cout << "------- Student Information -------" << endl;
    cout << "| Name | Mid-Exam | Final Exam | Result | Grade |" << endl;
    cout << "-------+-----------+--------------+--------+-------+" << endl;
    for (int i = 0; i < size; i++) {
        cout << "| " << names[i] << " | ";
        cout << midExamResults[i] << " | ";
        cout << finalExamResults[i] << " | ";
        cout << results[i] << " | ";
        cout << grades[i] << " |" << endl;
    }
    cout << "-------+-----------+--------------+--------+-------+" << endl;
}

void findHighestLowest(string names[], int results[], char grades[], int size) {
    int highestResult = results[0];
    int lowestResult = results[0];
    int highestIndex = 0;
    int lowestIndex = 0;

    for (int i = 1; i < size; i++) {
        if (results[i] > highestResult) {
            highestResult = results[i];
            highestIndex = i;
        } else if (results[i] < lowestResult) {
            lowestResult = results[i];
            lowestIndex = i;
        }
    }

    cout << "\nStudent with Highest Result: " << names[highestIndex] << " (" << highestResult << ", " << grades[highestIndex] << ")" << endl;
    cout << "Student with Lowest Result: " << names[lowestIndex] << " (" << lowestResult << ", " << grades[lowestIndex] << ")" << endl;
}
int main() {
    string names[MAX_STUDENTS];
    int midExamResults[MAX_STUDENTS];
    int finalExamResults[MAX_STUDENTS];
    int results[MAX_STUDENTS];
    char grades[MAX_STUDENTS];
    int numStudents;

    cout << "Enter the number of students (maximum of " << MAX_STUDENTS << "): ";
    cin >> numStudents;

    if (numStudents > MAX_STUDENTS) {
        cout << "Error: Maximum student capacity reached." << endl;
        return 1;
    }

    // Input student data
    for (int i = 0; i < numStudents; i++) {
        cout << "\nEnter details for student " << i + 1 << ":" << endl;
        cout << "Name: ";
        cin >> names[i];
        cout << "Mid-Exam Result: ";
        cin >> midExamResults[i];
        cout << "Final Exam Result: ";
        cin >> finalExamResults[i];
    }

    // Calculate results and grades
    for (int i = 0; i < numStudents; i++) {
        results[i] = calculateResult(midExamResults[i], finalExamResults[i]);
        grades[i] = determineGrade(results[i]);
    }

    // Display student information table
    displayStudentInfo(names, midExamResults, finalExamResults, results, grades, numStudents);

    // Find highest and lowest results
    findHighestLowest(names, results, grades, numStudents);

    return 0;
}