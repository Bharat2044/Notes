package com.nit.hk.customcollection;


public class A implements Comparable<A>{

	private int x;
	private int y;

	public A(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public int getX() {
		return x;
	}

	public void setX(int x) {
		this.x = x;
	}

	public int getY() {
		return y;
	}

	public void setY(int y) {
		this.y = y;
	}
	
	@Override
	public int hashCode() {
		return x;
	}
	
	@Override
	public boolean equals(Object obj) {
		System.out.println("In eq "+ this + "  " + obj);
		if(obj instanceof A a)
			return this.x == a.x &&
					this.y == a.y;
		
		return super.equals(obj);
	}

	@Override
	public int compareTo(A a) {  //a2.compareTo(a1);
		return this.x - a.x ;
	}
	
	@Override
	public String toString() {
		return "A(" + x + ", " + y + ")";
	}
	
	
}
