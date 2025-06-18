package com.nit.hk.arrays;

import java.util.Arrays;
import java.util.Scanner;

/*
 * Develop a program to read 5 values from keyboard
 * storing them in array, add those values 
 * display all five values and result
 * 
 */
public class Test04_ArrayObjectWithDynamicSizeAndValues {
	public static void main(String[] args) {
		
		Scanner scn = new Scanner(System.in);
		
		System.out.print("How many values do you want to enter?: ");
		int numberOfValues = scn.nextInt();
		
		int[] ia = new int[numberOfValues];
		System.out.println(Arrays.toString(ia));

		for(int i=0; i<numberOfValues; i++) {
			System.out.print("\nEnter value "+(i+1)+": ");
			ia[i] = scn.nextInt();
			System.out.println(Arrays.toString(ia));
		}
		System.out.println();
		
//		int sum = 0;
//		for(int value : ia) {
//			sum += value;
//		}
		
		int sum = Arrays.stream(ia).sum();
		
		for(int i=0; i<ia.length-1; i++) {
			System.out.print(ia[i]+"+");
		}
		
		System.out.println(ia[ia.length-1]+"="+sum);
	}
}
