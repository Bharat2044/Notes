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

public class Test04_ArrayProblems03 {
	
	public static void main(String[] args) {

		NITCollection col = new NITCollection();
		
		System.out.println("capacity: " + col.capacity());
		System.out.println("size    : " + col.size());
		System.out.println("eles    : " + col);

		col.add("a");		
		col.add("b"); 	
		col.add(5); 	
		col.add(6.7); 	
		col.add('e'); 	
		col.add(true); 	
		col.add("a"); 	
		col.add(5); 	
		col.add(null); 	
		col.add(10); 	
	
		col.add(null); 
		col.add(new A(5, 6)); 
		col.add(new A(7, 8)); 
		col.add(new A(5, 6)); 
		col.add(6.7); 

		System.out.println("\ncapacity: " + col.capacity());
		System.out.println("size    : " + col.size());
		System.out.println("eles    : " + col);
			
		System.out.println("is 6.7 found: "+ col.contains(6.7));
		System.out.println("is true found: "+ col.contains(true));
		System.out.println("is A(5,6) found: "+ col.contains(new A(5, 6)));
		System.out.println("is null found: "+ col.contains(null));
		System.out.println("is \"a\" found: "+ col.contains("a"));
		System.out.println("is \"a\" found: "+ col.contains(new String("a")));
		System.out.println("is \"e\" found: "+ col.contains("e"));
		System.out.println();
		
		System.out.println("\"a\" index: "+ col.indexOf("a"));
		System.out.println("6.7 index: "+ col.indexOf(6.7));
		System.out.println("A(5,6) index: "+ col.indexOf(new A(5,6)));
		System.out.println("null index: "+ col.indexOf(null));
		System.out.println("null index: "+ col.lastIndexOf(null));
		System.out.println("A(5,6) index: "+ col.lastIndexOf(new A(5,6)));
		System.out.println();
		
		System.out.println(col);	
		System.out.println(col.capacity());	
		System.out.println(col.size());	
		System.out.println("1st index object: "+ col.get(1));
		System.out.println("8th index object: "+ col.get(8));
		System.out.println("11th index object: "+ col.get(11));
		System.out.println();
		//System.out.println("-1th index object: "+ col.get(-1));
		//System.out.println("17th index object: "+ col.get(15));
		//System.out.println("21th index object: "+ col.get(20));
		
		//develop a code to retrieve class A object 
		//with the data (7 and 8) dynamically. Means first
		//you must find the index of this A(7,8) object then 
		//you must retrieve that object reference.
		
		//After retrieving object, print its state
		//later modify its state with new values
		//then again display modified state
		
		int index = col.indexOf(new A(7,8));
		if(index != -1) {
			
			//A a = col.get(index);			//Rule #1
			
			Object obj = col.get(index);
			System.out.println(obj);
			
			//obj.setX(45);			//Rule #2
			//obj.setY(55);

			A a = (A)obj;
			a.setX(45);			
			a.setY(55);
			
			System.out.println(obj);
			
		}else {
			System.out.println("Object A(7,8) is not found");
		}
		
		System.out.println();
		
		System.out.println(col);
		System.out.println(col.remove(2));
		System.out.println(col);

		System.out.println(col.remove(true));
		System.out.println(col);

		System.out.println(col.remove("a"));
		System.out.println(col);

		System.out.println(col.remove(new A(5, 6)));
		System.out.println(col);

		System.out.println(col.remove(8));
		System.out.println(col);
		
		System.out.println(col.remove(5));
		System.out.println(col);

		System.out.println(col.remove((Integer)5));
		System.out.println(col);

		//System.out.println(col.remove('e'));
		System.out.println(col.remove((Character)'e'));
		System.out.println(col);
		System.out.println();
		System.out.println(col);
		col.add(2, "X");
		System.out.println(col);
		System.out.println();
		
		NITCollection col2 = new NITCollection();
		for(int i=1; i<=10; i++ ) {
			col2.add(i*10);
		}
		System.out.println(col2);
		col2.add(2, 105);
		System.out.println(col2);
		System.out.println();
		
		System.out.println(col);
		System.out.println(col.set(4, "Y"));
		System.out.println(col);
	}
	
}








