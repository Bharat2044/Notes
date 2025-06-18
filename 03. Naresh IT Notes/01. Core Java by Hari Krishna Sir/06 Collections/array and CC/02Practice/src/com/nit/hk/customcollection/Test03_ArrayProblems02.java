package com.nit.hk.customcollection;

/*
 * Array problems
 * ==============
 * 	1. Array is homogeneous, it can not store different type of objects/values
 * 		//solution: create array by using j.l.Object class
 * 
 * 	2. Array is fixed in length and size, we can not store objects/values beyond its 
 *     its length and once we store a object/value we can not remove
 *     
 *  3. Array does not implement any data structure, so it does not have
 *      inbuilt methods to perform different operations on array elements
 *      like searching, sorting, removing, inserting etc..
 *  
 *  4. It can not store objects/values in different formats
 *  	it can store objects/values on in indexed format
 *      but it can not store objects/values in key=value pair format
 *      
 *      								key			value
 *      								=================
 *        0     1    2    3				eno			7279
 *       7279  H K  NIT  Java			ename		H K
 *       								institute	NIT
 *       							    teaches		Java
 *       
 *  5. It can not store objects/values in different order
 *  	array by default can store objects/values in insertion order only
 *      array does not support storing objects/values in 
 *      	FIFO, LIFO, RIO, SO, SEQOR, HCOR
 *          
 */

public class Test03_ArrayProblems02 {
	
	public static void main(String[] args) {
		//Size problem - we cannot store objects beyond its capacity
		//and we can not remove objects once we store objects 
//
//		Object[] oa = new Object[5];
//		oa[0] = new Student();
//		oa[1] = new Faculty();
//		oa[2] = new Admin();
//		oa[3] = new Bike();
//		oa[4] = new Lion();
//		
//		for(Object obj : oa) {
//			System.out.println(obj);
//		}
		
		//oa[5] = new Object();
		
		//Solution: There is not automated solution to this problem
		//we must write code to solve this problem by follow "Growable Array" algorithm
		
		NITCollection col = new NITCollection();
		System.out.println("capacity: " + col.capacity());
		System.out.println("size    : " + col.size());
		System.out.println("eles    : " + col);
		
//		col.add(new Student());	System.out.println(col);	
//		col.add(new Student()); System.out.println(col);
//		col.add(new Student()); System.out.println(col);
//		col.add(new Student()); System.out.println(col);
//		col.add(new Student()); System.out.println(col);
//		col.add(new Student()); System.out.println(col);
//		col.add(new Student()); System.out.println(col);
//		col.add(new Student()); System.out.println(col);
//		col.add(new Student()); System.out.println(col);
//		col.add(new Student()); System.out.println(col);

		col.add("a");	System.out.println(col);	
		col.add("b"); 	System.out.println(col);
		col.add(5); 	System.out.println(col);
		col.add(6.7); 	System.out.println(col);
		col.add('e'); 	System.out.println(col);
		col.add(true); 	System.out.println(col);
		col.add("a"); 	System.out.println(col);
		col.add(5); 	System.out.println(col);
		col.add(null); 	System.out.println(col);
		col.add(10); 	System.out.println(col);
	
		System.out.println("\ncapacity: " + col.capacity());
		System.out.println("size    : " + col.size());
		System.out.println("eles    : " + col);
		
		col.add(null); System.out.println(col);
		col.add(new A(5, 6)); System.out.println(col);

		System.out.println("\ncapacity: " + col.capacity());
		System.out.println("size    : " + col.size());
		System.out.println("eles    : " + col);
			
	}
	
}








