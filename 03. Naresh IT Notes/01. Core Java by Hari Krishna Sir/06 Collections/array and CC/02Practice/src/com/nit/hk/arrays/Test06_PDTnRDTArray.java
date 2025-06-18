package com.nit.hk.arrays;
/*
 * Develop a program to create an array to store  
 * 	1. student numbers as one group
 * 	2. student names as one group
 * 
 *  display both arrays' elements(values/objects) on console
 *  with user defined method which must be common to both objects
 *   
 */
public class Test06_PDTnRDTArray {
	public static void main(String[] args) {
		
		int[] 		snoArray 	= {101, 102, 103};
		
		
		String[]	snameArray 	= {"HK", "BK", "PK"};
			
		display(snoArray);
		display(snameArray);
		
	}
	
	
	static void display(Object array) {
		System.out.println(array);
		
		if(array instanceof int[]) {
			int[] iArray = (int[])array;
			
			for(int i=0; i<iArray.length; i++) {
				System.out.println(iArray[i]);
			}
			
		}else if(array instanceof String[] sArray) {//java 14v
			
			for(int i=0; i<sArray.length; i++) {
				System.out.println(sArray[i]);
			}
		}
		
		System.out.println();
	}
}










