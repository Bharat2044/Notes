package com.nit.hk.arrays;

/*
 * Develop a method to take array of integers as argument
 * inside this method add and subtract all values available in this array
 * then return result of both sum and diff from this method
 * display values and result
 * 
 */
public class Test05_ArrayObjectAsArgumentAndReturnType {
	
	static int[] addSub(int[] ia) throws IllegalArgumentException {

		if(ia == null)
			throw new IllegalArgumentException("null is not allowed");
		
		if(ia.length == 0)
			throw new IllegalArgumentException("Array is empty"); 
			
		int add=ia[0];
		for(int i=1; i<ia.length; i++) {
			add += ia[i];
		}
		
		int sub=ia[0];
		for(int i=1; i<ia.length; i++) {
			sub -= ia[i];
		}
		
		return new int[]{add, sub};
	}
	
	public static void main(String[] args) {
		try {
			int[] ia = null;
			int[] resArray = addSub(ia);
			
			for(int i=0;i<ia.length-1; i++ ) {
				System.out.print(ia[i]+"+");
			}
			System.out.println(ia[ia.length-1]+" = "+resArray[0]);  //9
			
			for(int i=0;i<ia.length-1; i++ ) {
				System.out.print(ia[i]+"-");
			}
			System.out.println(ia[ia.length-1]+" = "+resArray[1]);  //-5
			
		}catch(IllegalArgumentException e) {
			System.out.println("Error: "+ e.getMessage());
			
		}
	}
}
