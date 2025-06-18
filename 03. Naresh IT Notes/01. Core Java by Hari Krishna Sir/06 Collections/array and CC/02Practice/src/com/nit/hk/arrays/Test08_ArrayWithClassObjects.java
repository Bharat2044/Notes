package com.nit.hk.arrays;

import java.util.Arrays;

public class Test08_ArrayWithClassObjects {
	public static void main(String[] args) {

//static nature code, because individual variables declaration
//for storing each object reference 
		Student s1 = new Student();
		s1.setSno(101);
		s1.setSname("HK");
		s1.setCourse("CJ");
		s1.setFee(2500);
		
		Student s2 = new Student(102, "BK", "Acting", 3500);
		
//dynamic nature code for storing Student objects on demand
//we must create array object by using Student
		Student[] sa = new Student[3];	
		System.out.println(Arrays.toString(sa));
		System.out.println();
		
		sa[0] = new Student();
		sa[0].setSno(101);
		sa[0].setSname("HK");
		sa[0].setCourse("CJ");
		sa[0].setFee(2500);
		
		//System.out.println(sa[0]); //sa[0].toString();
		System.out.println(Arrays.toString(sa)); 
										//sa[0].toString();
										//sa[1]		
										//sa[2]
		
		sa[1] = new Student(102, "Balayaa Babu", "Acting", 3500);
		System.out.println(Arrays.toString(sa)); 
									//sa[0].toString();
									//sa[1].toString();		
									//sa[2]
		
////////////////////////////////////////////////////////////////////////////
		System.out.println();
		
		Student[] sa2 = {new Student(), new Student(102, "BK", "Acting", 3500)};
		System.out.println(Arrays.toString(sa2));
		
	}
}







