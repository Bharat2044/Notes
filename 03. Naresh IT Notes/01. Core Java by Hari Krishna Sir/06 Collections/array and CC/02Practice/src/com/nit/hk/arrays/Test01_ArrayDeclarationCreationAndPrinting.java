package com.nit.hk.arrays;

import java.util.Arrays;

/*
 * 1. What is an array?
 *    - an array is a referenced data type, it is an object
 *    - an array is a collection same type of variables created in continuous 
 *      memory location
 * 2. Why an array?
 * 		- It is used for storing multiple values or multiple objects of similar type
 *       in continuation memory locations with single name.
 *       
 * 3. How can we create array?
 * 		- by using data type either by using PDT or RDT
 *        based on the type of values or the type of objects
 *        we need to store in this array
 *        
 *      - For example 
 *      	- for storing integers we must create  	array by using int data type 
 *      	- for storing names we must create  	array by using String data type 
 *      	- for storing Student objects we must create  	array by using Student class name
 *      
 * 4. Syntax to create array?
 *		- we have three ways to create an array object
 *		  for storing multiple values or multiple objects
 *		
 *			DT[] arrayVarName = new DT[size];
 *			DT[] arrayVarName = {v1/o1, v2/o2, v3/o3, ......};
 *			DT[] arrayVarName = new DT[]{v1/o1, v2/o2, v3/o3, ......};
 *
 *		For example:
 *			- int[] ia1 = new int[5]; 
 *				- new int[] array object is created with 5 locations with 
 *                default values 0 because the internal locations are of int type 
 *
 *			- int[] ia2 = {3, 4, 5, 6, 7}; 
 *				- new int[] array object is created with 5 locations with 
 *				  given values 3, 4, 5, 6, 7  
 *
 *			- int[] ia3 = new int[]{3, 4, 5}; 
 *				- new int[] array object is created with 3 locations
 *                because we have mentioned 3 values in {} 
 *              - these three locations are initialized with the given values  3, 4, 5  
 * 
 *
 * 5. There ways of creating array object and their differences?
 * 
 * 		- Case #1: We know only the type of values and the number of values to store
 *  			   we do not know the actual values to store, those values are coming
 *                 into program at runtime, means program execution time, then we must
 *                 create array object by using new kw and size syntax 
 *                 	 
 *  	- Case #2: We know the type of values and the number of values to store
 *  			   also know the actual values to store at development time itself,
 *  				then we must create array object by using { } with values 
 *  
 *  	- Case #3: we need to create an array object with values without variable declaration
 *  			   either for passing it as an argument to a method or to a constructor
 *                    or  for returning from a method then we must create array object 
 *                    by using new kw and { } with values
 *  
 * 5. Difference between array declaration and array creation?
 * 		- just creating new variable for storing array object is called array declaration
 * 		- creating memory locations by using new keywords for storing multiple values is called array creation
 *  
 * 6. Difference between array declaration and array creation?
 * 		- in array declaration memory location are not created and we can not store any values
 * 		- in array creation memory locations are created and we can store values
 * 
 * 7. How to read and display array values[statically and dynamically]
 * 		1. arrayVariableName[index]
 * 		2. for loop with index and length as condition value 	(1.0v)
 * 		3. java.lang.Arrays.toString(arrayObject)  				(1.2v)
 * 		4. for each loop  						  				(5v)
 * 		5. stream api											(8v)
 * 
 * 	- Rule:  index>0 && <length else we will get AIOOBE
 * 
 * 8. what are the different operations we can do on array object?
 * 		1. declaring an array
 * 		2. creating an array
 * 		3. initializing array object
 * 		4. reading array object values
 * 		5. modifying array object values
 * 
 * 9. Developing a program to initialize array with dynamic values 
 * 
 * 10. Developing a program to pass and return array object with dynamic values
 * 
 * 11. all types of array objects common type -> Object[] and Object
 * 
 * 12. Developing overloaded, loosely coupled and runtime polymorphic methods for
 * 		passing array objects as argument, reading and display their elements
 * 
 * 13. Difference between array object creation with primitive and referenced type
 * 
 * 14. Develop a program to create an array object to store Student class objects
 * 	   with three different students details. You must show array object creation 
 *     with Student type in all three syntaxes.
 * 
 */
public class Test01_ArrayDeclarationCreationAndPrinting {
	public static void main(String[] args) {
		
		//1. array declaration [array varaible creation]
		int[] ia;  //it is just a variable declaration for storing int[] object
		
		//System.out.println(ia); //error because it not an object, it is just a variable
		
		//2. array object creation
		ia = new int[5]; //int[] array object creation with 5 locationss
						//for storing 5 integers
		
		//3. reading array values
		System.out.println(ia);
		System.out.println();		
	/*
	  //static code
		System.out.println(ia[0]);
		System.out.println(ia[1]);
		System.out.println(ia[2]);
		System.out.println(ia[3]);
		System.out.println(ia[4]);
		//System.out.println(ia[5]); Rule: [index>=0 and <length]
	
		//still it is static code
		for(int i=0; i<5; i++) {
			System.out.println(ia[i]);
		}
	*/	
		
		//dynamic code to read all values from an array
		for(int i=0; i<ia.length; i++) {  //1.0v
			System.out.println(ia[i]);
		}
		
		System.out.println(Arrays.toString(ia)); //1.2v
		
		for(int value : ia) {  //1.5v- for each loop			
			System.out.print(value + " ");
		}
		System.out.println();
		
		//8v stream api and method reference
		Arrays.stream(ia).forEach((value) -> System.out.print(value+ " "));
		
		
		System.out.println();
		
		//initializing array object
		ia[0] = 3;
		ia[1] = 4;
		ia[2] = 5;
		ia[3] = 6;
		ia[4] = 7;
		
		//display(ia);
		System.out.println(Arrays.toString(ia));
		
		//modifying array object values
		ia[2] = 12;
		ia[3] = ia[0] - ia[2];
		
		//display(ia);
		System.out.println(Arrays.toString(ia));		
	}
	
	static void display(int[] ia) {
		for(int i=0; i<ia.length; i++) {
			System.out.println(ia[i]);
		}
		System.out.println();
	}
}

