package com.nit.hk.arrays;


//ArrayPrinter.java
class ArrayPrinter {

/*	static void print(Object obj) {
		
		System.out.print(obj +" --> ");
		
		if(obj instanceof byte[]) { 	//Java1.0 style
			byte[] ba = (byte[])obj;
			for(int i=0; i<ba.length; i++) {
				System.out.print(ba[i] + "  ");
			}
		}else if(obj instanceof short[]) {
			short[] sa = (short[])obj;
			for(int i=0; i<sa.length; i++) {
				System.out.print(sa[i] + "  ");
			}
		}else if(obj instanceof int[]) {
			int[] ia = (int[])obj;
			for(int i=0; i<ia.length; i++) {
				System.out.print(ia[i] + "  ");
			}
		}else if(obj instanceof long[] la) { //Java 14v: pattern matching for instanceof operator 
			for(long value : la) { //Java 5v: enhanced for loop (for each loop)
				System.out.print(value + "  ");
			}
		}else if(obj instanceof float[] fa) {  
			for(float value : fa) { 
				System.out.print(value + "  ");
			}
		}else if(obj instanceof double[] da) {  
			for(double value : da) { 
				System.out.print(value + "  ");
			}
		}else if(obj instanceof char[] ca) {  
			for(char value : ca) { 
				System.out.print(value + "  ");
			}
		}else if(obj instanceof boolean[] boa) {  
			for(boolean value : boa) { 
				System.out.print(value + "  ");
			}
		}else if(obj instanceof String[] sta) {  
			for(String value : sta) { 
				System.out.print(value + "  ");
			}
		}else if(obj instanceof Integer[] ita) {  
			for(Integer value : ita) { 
				System.out.print(value + "  ");
			}
		}
		System.out.println();
		
		
		
	}
*/
	static void print(byte[] ba) {
		System.out.print(ba +" --> ");
		for(int i=0; i<ba.length; i++) {
			System.out.print(ba[i] + "  ");
		}
		System.out.println();
	}
	static void print(short[] sa) {
		System.out.print(sa +" --> ");
		for(int i=0; i<sa.length; i++) {
			System.out.print(sa[i] + "  ");
		}
		System.out.println();
	}
	static void print(int[] ia) { 
		System.out.print(ia +" --> ");
		for(int i=0; i<ia.length; i++) {
			System.out.print(ia[i] + "  ");
		}
		System.out.println();
	}
	static void print(long[] la) { 
		System.out.print(la +" --> ");
		for(int i=0; i<la.length; i++) {
			System.out.print(la[i] + "  ");
		}
		System.out.println();
	}
	static void print(float[] fa) { 
		System.out.print(fa +" --> ");
		for(int i=0; i<fa.length; i++) {
			System.out.print(fa[i] + "  ");
		}
		System.out.println();
	}
	static void print(double[] da) { 
		System.out.print(da +" --> ");
		for(int i=0; i<da.length; i++) {
			System.out.print(da[i] + "  ");
		}
		System.out.println();
	}
	static void print(char[] ca) {
		System.out.print(ca +" --> ");
		for(int i=0; i<ca.length; i++) {
			System.out.print(ca[i] + "  ");
		}
		System.out.println();
	}
	static void print(boolean[] boa) { 
		System.out.print(boa +" --> ");
		for(int i=0; i<boa.length; i++) {
			System.out.print(boa[i] + "  ");
		}
		System.out.println();
	}
	
	
//	static void print(String[] sta) { 
//		System.out.print(sta +" --> ");
//		System.out.println();
//	}
//	static void print(Integer[] ita) { 
//		System.out.print(ita +" --> ");
//		System.out.println();
//		
//	}
	
	static void print(Object[] array) {
		System.out.print(array + " --> ");
		for(int i=0; i<array.length; i++) {
			System.out.print(array[i] + " ");
		}
		System.out.println();
	}

}
