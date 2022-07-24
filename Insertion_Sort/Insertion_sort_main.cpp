
// Implementing Insertion sort using pointers
// 24Jul2022


#include <iostream>
#include <algorithm>
#include <cassert>



class InsertionSort{

public:
  
  void insertion_sort(int* ptr_2_start, int length){

    
    for(int i=1;i<length;i++)
      {
	int curr_spot = i;
	if( *(ptr_2_start+i) < *(ptr_2_start+i-1))
	  {
	    
	    while(*(ptr_2_start+curr_spot) < *(ptr_2_start+curr_spot-1))
	      {
		
		//this->print_array(ptr_2_start, length);
		int temp_holder = *(ptr_2_start+curr_spot-1);
		
		*(ptr_2_start+curr_spot-1) = *(ptr_2_start+curr_spot);
		*(ptr_2_start+curr_spot) = temp_holder;

		curr_spot -= 1;
		
		if(curr_spot < 1)
		  {
		    break;
		  }
		
	      }
	  }
      }
    //this->print_array(ptr_2_start,length);


  }

  
  void print_array(int* list_start, int length){
    
    
    for(int i=0;i<length;i++){
      std::cout << *(list_start+i) << " " ;
      
    }
    std::cout << "\n";
  }


  
  void Tests(){

    

    int arr1[10] = {78, 34, 35, 6, 34, 56, 3, 56, 2, 4};
    int* arr1_start = arr1;
    std::cout << "Test 1... ";
    this->insertion_sort(arr1_start, 10);
    assert(std::is_sorted(arr1, arr1 + 10));
    std::cout << "passed" << std::endl;

    int arr2[10] = {1,-9,90,56,9888,90,59,1,2,34};
    int* arr2_start = arr2;
    std::cout << "Test 2...";
    this->insertion_sort(arr2_start, 10);
    assert(std::is_sorted(arr2,arr2+10));
    std::cout << "passed" << std::endl;
    

  }

  
};






int main(){


  int numbers[] = {5,9,-1,3,4,6,6,-30,2};
  
  
  int length_of_array = sizeof(numbers) / sizeof(numbers[0]);

  int* address;

  address = numbers;

  InsertionSort IS;

  IS.insertion_sort(address, length_of_array);

  IS.Tests();

}
