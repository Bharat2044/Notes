package com.nit.hk.arrays;

import java.util.Arrays;

public class Test03_ArrayInitialization {
	public static void main(String[] args) {
		//create an array object with 5 integers 
		//3,4,5,6,7

//Syntax #1:array creation with new kw and size		
		int[] ia1 = new int[5];
		System.out.println(Arrays.toString(ia1));
		
		ia1[0] = 3;
		ia1[1] = 4;
		ia1[2] = 5;
		ia1[3] = 6;
		ia1[4] = 7;
		
		System.out.println(Arrays.toString(ia1));
		System.out.println();
		
//Syntax #2: array creation with { }
		int[] ia2 = {3, 4, 5, 6, 7};
		System.out.println(Arrays.toString(ia2));
		System.out.println();
		
		sum(ia1);
		sum(ia2);
		System.out.println();
		
//syntax #3: array object creation with values without out referenced variable assignment 
		//to pass as argument to a method and no need to use this array object 
		//after method call
		
		sum(new int[3]); //only default values 
		//sum({5, 6, 7}); //CE: no type information to create an array object
		sum(new int[]{5, 6, 7}); //array object with values
		
	}
	
	static void sum(int[] ia) {
		int sum = 0;
		
		for(int value : ia) {
			sum = sum + value;
		}
		System.out.println("sum of all values: "+ sum);
	}
}
