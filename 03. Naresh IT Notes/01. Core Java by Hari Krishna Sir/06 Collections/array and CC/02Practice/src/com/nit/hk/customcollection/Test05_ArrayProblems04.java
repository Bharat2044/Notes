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
 *  3. Array does not have inbuilt methods to perform different operations 
 *      on array elements like searching, sorting, removing, inserting etc..
 *      because Array does not implement any data structure, it language level raw object       
 *  
 *  4. It can not store objects/values in different formats
 *  	it can store objects/values on in indexed format only
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

public class Test05_ArrayProblems04 {
	
	public static void main(String[] args) {

		//Array form with Index 
		NITCollection col = new NITCollection();
		col.add(7279);
		col.add("HK");
		col.add("Naresh IT");
		col.add("Java");
		
		System.out.println(col);
		
		//table format with key,value pair
		NITTable table = new NITTable();
		table.put("eno", 7279);
		table.put("ename", "HK");
		table.put("Institute", "Naresh IT");
		table.put("Teaches", "Java");
		
		System.out.println(table);
				
	}
	
}








