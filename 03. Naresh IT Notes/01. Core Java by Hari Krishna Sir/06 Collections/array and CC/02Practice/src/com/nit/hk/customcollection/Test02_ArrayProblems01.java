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

public class Test02_ArrayProblems01 {
	
	public static void main(String[] args) {
		//type problem -we can store only same type or its lesser type values or objects
		
		int[] ia = new int[10];
		ia[0] = 5;
		ia[0] = 'a';
//		ia[0] = 5L;
//		ia[0] = 5.7;
//		ia[0] = true;
//		ia[0] = "a";

		double[] da = new double[10];
		da[0] = 5;
		da[0] = 5L;
		da[0] = 5L;
		da[0] = 5.7;
		da[0] = 'a';
//		da[0] = true;
//		da[0] = "a";

		Student1[] sa = new Student1[10];
		sa[0] = new Student1();
//		sa[0] = new Faculty();
//		sa[0] = new Admin();
//		sa[0] = new Person();

		Person[] pa = new Person[10];
		pa[0] = new Person();
		pa[0] = new Student1();
		pa[0] = new Faculty();
		pa[0] = new Admin();
//		pa[0] = new Lion();
//		pa[0] = new Tiger();
		
		Lion[] la = new Lion[10]; // lion objects
		Tiger[] ta = new Tiger[10]; // tiger objects
		Elephant[] ea = new Elephant[10]; // elephant objects
		
		Animal[] aa = new Animal[10];
		aa[0] = new Lion();
		aa[0] = new Tiger();
		aa[0] = new Elephant();

		Object[] oa = new Object[10];
		oa[0] = new Student1();
		oa[0] = new Lion();
		oa[0] = new Bike();
		
		//How can we solve array type problem?
			//we must choose parent type for storing same type and sub type objects
			
			//for storing all different types of java objects we must choose 
			//java.lang.Object class array.
		
	}
	
}


class Person{ }
class Student1 extends Person{}
class Faculty extends Person{}
class Admin extends Person{}

interface Animal{ }
class Lion implements Animal{ }
class Tiger implements Animal{ }
class Elephant implements Animal{ }

interface Vehicle {}
class Bus implements Vehicle{} 
class Car implements Vehicle{} 
class Bike implements Vehicle{} 









