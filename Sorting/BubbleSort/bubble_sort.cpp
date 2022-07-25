
// Implementing bubble sort using pointers
// 25 Jul 2022


#include <iostream>
#include <algorithm>
#include <cassert>


struct BubbleSort{


  void bubble_sort(int* ptr_2_start, int length){


    while (!std::is_sorted(ptr_2_start, ptr_2_start+length)){
      
      for(int i=0;i<(length-1);i++){

	// Swap the values if true
	if(*(ptr_2_start+i) > *(ptr_2_start+i+1)){

	  int temp_holder = *(ptr_2_start+i);
	  *(ptr_2_start+i) = *(ptr_2_start+i+1);
	  *(ptr_2_start+i+1) = temp_holder;

	}
      }
    }
  }


  void print_array(int* list_start, int length){
    
    
    for(int i=0;i<length;i++){
      std::cout << *(list_start+i) << " " ;
      
    }
    std::cout << "\n";
  }

  void Tests(){
    
    std::cout << "Test 1...";
    int numbers1[10] = {-2,4,-54,23,98,0,93,34,987,123};
    int* ptr1 = numbers1;
    this->bubble_sort(ptr1, 10);
    assert(std::is_sorted(ptr1,ptr1+10));
    std::cout << "passed \n";

    std::cout << "Test 2...";
    int numbers2[5] = {1,1,90,91,90};
    int* ptr2 = numbers2;
    this->bubble_sort(ptr2,5);
    assert(std::is_sorted(ptr2,ptr2+5));
    std::cout << "passed \n";
  }

  
};



int main(){

  int numbers[10] = {1,4,5,2,3,9,8,6,7,0};
  
  int length_of_array = sizeof(numbers) / sizeof(numbers[0]);

  int* start = numbers;
  
  BubbleSort BS;

  BS.bubble_sort(numbers,length_of_array);
  BS.print_array(start, length_of_array);

  BS.Tests();
}
