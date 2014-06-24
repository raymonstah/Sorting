// Raymond Ho
// A fun sorting algorithm that works by using threads to sleep for a given input time.
// After that sleep time, it will print the numbers, in sorted order.
// Compile with: g++ -std=c++0x sleepsort.cpp -o sleepsort

#include <iostream>
#include <thread>
#include <chrono>
#include <vector>

using namespace std;

void printNum(int n) {
	chrono::milliseconds duration(n * 10);
	this_thread::sleep_for(duration);
	cout << n << endl;
}

int main () {
	vector<int> v =  {9, 0, 4, 2, 5, 2, 8, 5, 1, 6, 3, 7};
	vector<thread> threads;
	for (int i = 0; i < 12; ++i) 
		threads.push_back(thread (printNum, v[i]));
		
	for (auto &i : threads) i.join();

	return 0;
}
