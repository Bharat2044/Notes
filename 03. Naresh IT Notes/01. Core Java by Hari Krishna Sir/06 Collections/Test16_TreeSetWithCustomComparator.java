package com.nit.hk.suncollections;

import java.util.Comparator;
import java.util.TreeSet;

public class Test16_TreeSetWithCustomComparator {
	public static void main(String[] args) {
		
		TreeSet<B> ts1 = new TreeSet<>(); //uses default sorting order give in  
		ts1.add(new B(5, 6));			  //Comparable implementation
		ts1.add(new B(7, 9));			  //class B in comparaTp(-) method
		ts1.add(new B(6, 4));			  //with x value
		System.out.println(ts1);
		
		TreeSet<B> ts2 = new TreeSet<>(new ByAscComparator());
		ts2.add(new B(5, 6));			//now TS uses Comparator implementation
		ts2.add(new B(7, 9));			//given in ByAscComparator class 
		ts2.add(new B(6, 4));					
		System.out.println(ts2);
		
		TreeSet<B> ts3 = new TreeSet<B>(
							new Comparator<B>() { //AIC implementation
								public int compare(B b1, B b2) {
									return b2.getY() - b1.getY();
								}
							});
		
		ts3.add(new B(5, 6));			
		ts3.add(new B(7, 9));			 
		ts3.add(new B(6, 4));					
		System.out.println(ts3);
		
		TreeSet<B> ts4 = new TreeSet<B>(
								(b1, b2) -> b2.getY() - b1.getY());
		
		ts4.add(new B(5, 6));			
		ts4.add(new B(7, 9));			 
		ts4.add(new B(6, 4));					
		System.out.println(ts4);
		
		TreeSet<B> ts5 = new TreeSet<B>(new MRComparator()::compareBYDesc);
		TreeSet<B> ts6 = new TreeSet<B>(new ByAscComparator()::compare);
		TreeSet<B> ts7 = new TreeSet<B>(new BxDescComparator()::compare);

		ts5.add(new B(5, 6));			
		ts5.add(new B(7, 9));			 
		ts5.add(new B(6, 4));					
		System.out.println(ts5);

		ts6.add(new B(5, 6));			
		ts6.add(new B(7, 9));			 
		ts6.add(new B(6, 4));					
		System.out.println(ts6);
		
		ts7.add(new B(5, 6));			
		ts7.add(new B(7, 9));			 
		ts7.add(new B(6, 4));					
		System.out.println(ts7);
		
		TreeSet<B> ts8 = new TreeSet<B>(
								(b1, b2) ->  {
									//sort on x wise, if x value is same
									//sort on y wise ascending order
									//System.out.println(b1 + "  " + b2);
									int xDiff = b1.getX() - b2.getX();
									if(xDiff == 0) {
										return b1.getY() - b2.getY();
									}
									
									return xDiff;	
								});
		
		ts8.add(new B(5, 6));
		ts8.add(new B(5, 4));
		ts8.add(new B(4, 8));
		ts8.add(new B(3, 8));
		System.out.println(ts8);
		
		
	}
}
