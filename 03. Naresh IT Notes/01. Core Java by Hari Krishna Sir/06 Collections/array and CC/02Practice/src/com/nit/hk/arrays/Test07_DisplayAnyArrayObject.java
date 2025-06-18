package com.nit.hk.arrays;

/*
 * Develop a class with a parameterized method to display
 * elements of any passed array object.
 * 
 */

public class Test07_DisplayAnyArrayObject {
	public static void main(String[] args) {
		
		byte[] ba = {3, 4, 5} ;
		short[] sa = {3, 4, 5} ;
		int[] ia = {3, 4, 5} ;
		long[] la = {3, 4, 5} ;
		float[] fa = {3, 4, 5} ;
		double[] da = {3, 4, 5} ;
		char[] ca = {3, 4, 5} ;
		boolean[] boa = {true, false, true} ;
		
		String[] sta = {"a", "b", "c"} ;

		Integer[] ita = {40, 50, 60} ;
		
		ArrayPrinter.print(ba);
		ArrayPrinter.print(sa);
		ArrayPrinter.print(ia);
		ArrayPrinter.print(la);
		ArrayPrinter.print(fa);
		ArrayPrinter.print(da);
		ArrayPrinter.print(ca);
		ArrayPrinter.print(boa);
		ArrayPrinter.print(sta);
		ArrayPrinter.print(ita);
		
		
		
	}	
}
