#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>

using namespace std;

struct Board {
	int nums[5][5];
	int markers[5][5];
	Board(ifstream&);
	void markBoard(int num);
	bool checkWin();
	int score();
};

void readNums(ifstream&, vector<int>&); //reads in the input for game play
void readBoards(ifstream&, vector<Board>&);
void markBoards(int, vector<Board>&);
int checkBoards(vector<Board>);

int main(int argc, char *argv[]) {
	
	//open file from command line args
	string filename = argv[1];
	ifstream fin;
	fin.open(filename);

	//get game input
	vector<int> nums;
	readNums(fin, nums);

	
	//get array of boards
	vector<Board> boards;
	readBoards(fin, boards);

	fin.close();

	//play game
	for (int i =0; i < nums.size(); i++){
		markBoards(nums[i], boards);
		int cb = -1;
		if (i>=4)
			cb = checkBoards(boards);
		if (cb != -1){
			cout<<cb*nums[i]<<endl;
			return 0;
		}
	}

	return 0;
}

void readNums(ifstream &fin, vector<int> &nums) {
	string line;
	string num;
	
	fin>>line;
	stringstream ss(line);

	while(getline(ss, num, ',')){
		nums.push_back(stoi(num));
	}	
}

void readBoards(ifstream &fin, vector<Board> &boards){
	while(!fin.eof()){
		Board b(fin);
		boards.push_back(b);
	}
	boards.pop_back(); //extra one getting read in? \n?
}

Board::Board(ifstream &fin){
	int num;
	for (int i = 0; i<5; i++){
		for (int j = 0; j<5; j++){
			fin>>num;
			nums[i][j] = num;
			markers[i][j] = 0;
		}
	}
}

void markBoards(int num, vector<Board> &b){
	for (int i = 0; i<b.size(); i++){
		b[i].markBoard(num); 
	}
}

int checkBoards(vector<Board> b) {
	for (int i=0; i<b.size(); i++){
		if (b[i].checkWin()){
			return b[i].score();
		}		
	}
	return -1;
}

void Board::markBoard(int num) { //Could be faster if marking and chekcing are combined
	for (int i = 0; i<5; i++) {
		for (int j = 0; j<5; j++) {
			if (nums[i][j] == num)
				markers[i][j] = 1; //should check here. oops dont wanna remake functions. 
		}
	}
}	

bool Board::checkWin(){
	
	//check horizontal
	for (int i =0; i<5; i++){
		int sum = 0;
		for (int j = 0; j<5; j++){
			sum += markers[i][j];
		}
		if (sum == 5)
			return true;
	}

	//check vertical
	for (int j =0; j<5; j++){
		int sum = 0;
		for (int i = 0; i<5; i++){
			sum += markers[i][j];
		}
		if (sum == 5)
			return true;
	}
	return false;
}

int Board::score(){
	int score = 0;
	for (int i = 0; i<5; i++){
		for(int j = 0; j<5; j++){
			if (!markers[i][j])
				score += nums[i][j];
		}
	}
	return score;
}
