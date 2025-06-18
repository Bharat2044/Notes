package com.nit.hk.suncollections;

import java.util.TreeSet;

public class Test15_TreeSet {
	public static void main(String[] args) {
		
		TreeSet<Object> ts1 = new TreeSet<>();
		ts1.add("a");  //
		ts1.add("c");	//"c".compareTo("a") -> +ve -> RIGHT SIDE
		ts1.add("b");	//"b".compareTo("a") -> +ve -> RIGHT SIDE
						//"b".compareTo("c") -> -ve -> LEFT SIDE
		System.out.println(ts1);
		
		//ts.add(5);
		//ts.add(null);
		
		TreeSet<Integer> ts2 = new TreeSet<>();
		ts2.add(5);
		ts2.add(7);
		ts2.add(6);
		System.out.println(ts2);
		
		TreeSet<B> ts3 = new TreeSet<>();
		ts3.add(new B(5, 9));	//b1.compareTo(b1) //ignored stored
		ts3.add(new B(7, 2));	//b2.compareTo(b1) 	-> +ve -> RS
		ts3.add(new B(6, 4));   //b3.compareTo(b1)	-> +ve -> RS
								//b3.compareTo(b2)	-> -ve -> LS
		
		ts3.add(new B(6, 4));
		ts3.add(new B(6, 4));
		System.out.println(ts3);
		
		
		TreeSet<B> ts4 = new TreeSet<>(new BxDescComparator());
		ts4.add(new B(5, 9));	//
		ts4.add(new B(7, 2));	//cmpr.compare(b2, b1) 	-> -ve -> LS
		ts4.add(new B(6, 4));   //cmpr.compare(b3, b1)	-> -ve -> LS
								//cmpr.compare(b3, b2)	-> -ve -> RS
		
		ts4.add(new B(6, 4));
		ts4.add(new B(6, 4));
		System.out.println(ts4);
		
		
		
	}
}
