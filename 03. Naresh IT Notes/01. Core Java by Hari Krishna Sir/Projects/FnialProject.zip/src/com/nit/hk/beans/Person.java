package com.nit.hk.beans;

import java.io.Serializable;

//This class is designed to store its instances 
//either in file as part of serialization and deserialization
//by implementing Serializable interface and by declaring serialVersionUID field

//Also this class is designed to store its instances in
//Collection and Map objects with state wise comparison
//by overrdding hashCode() and equals() methods

//Also this class is designed to display this object state
//by overriding toString() method

public class Person implements Serializable {

	private static final long serialVersionUID = 1L;
	
	private int eyes; 
	private int ears; 
	private int hands; 
	private int legs;
	
	private String name;
	private double height;
	private double weight;
	private String gender;
	private String bloodGroup;
	private String dob;
	private String identificationMarks;
	private long mobile;
	private String email;
	
	private String fatherName;
	private String motherName;
	private String surName;
	private String maritalStatus;
	private String nationality;
	private String religion;
	private String motherTounge;
	private boolean vacinated1stDose;
	private boolean vacinated2ndDose;
	private boolean vacinatedBoosterDose;

	private int age;
	private long aadhaar;
	private String voterID;
	private String pan;
	private String passport;
	
	private String address;
	
	{	
		eyes = 2;
		ears = 2;
		hands = 2;
		legs = 2;
	}
	
	public Person() { 
		//no-op
		//it is for performing deserialization 
	}
	
	public Person(String name, double height, double weight, String gender, String bloodGroup, String dob) {
		this.name = name;
		this.height = height;
		this.weight = weight;
		this.gender = gender;
		this.bloodGroup = bloodGroup;
		this.dob = dob;
	}

	public int getEyes() {
		return eyes;
	}

	public void setEyes(int eyes) {
		this.eyes = eyes;
	}

	public int getEars() {
		return ears;
	}

	public void setEars(int ears) {
		this.ears = ears;
	}

	public int getHands() {
		return hands;
	}

	public void setHands(int hands) {
		this.hands = hands;
	}

	public int getLegs() {
		return legs;
	}

	public void setLegs(int legs) {
		this.legs = legs;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getHeight() {
		return height;
	}

	public void setHeight(double height) {
		this.height = height;
	}

	public double getWeight() {
		return weight;
	}

	public void setWeight(double weight) {
		this.weight = weight;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	public String getBloodGroup() {
		return bloodGroup;
	}

	public void setBloodGroup(String bloodGroup) {
		this.bloodGroup = bloodGroup;
	}

	public String getDob() {
		return dob;
	}

	public void setDob(String dob) {
		this.dob = dob;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public long getAadhaar() {
		return aadhaar;
	}

	public void setAadhaar(long aadhaar) {
		this.aadhaar = aadhaar;
	}

	public String getVoterID() {
		return voterID;
	}
	
	public void setVoterID(String voterID) {
		this.voterID = voterID;
	}

	public String getPan() {
		return pan;
	}

	public void setPan(String pan) {
		this.pan = pan;
	}

	public long getMobile() {
		return mobile;
	}

	public void setMobile(long mobile) {
		this.mobile = mobile;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}
	
	public void eat() {
		System.out.println(name + " is eating");
	}

	public void walk() {
		System.out.println(name + " is walking");
	}

	public void sleep() {
		System.out.println(name + " is sleeping");
	}

	public void learn() {
		System.out.println(name + " is learning");
	}
	
	@Override
	public int hashCode() {
		return (int)aadhaar;
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Person p)
			return this.aadhaar == p.aadhaar;
		
		return false;
	}
	
	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("================ Personal details =====================");
		sb.append("\n name\t: "+ name);
		sb.append("\n height\t: "+ height);
		sb.append("\n weight\t: "+ weight);
		sb.append("\n gender\t: "+ gender);
		sb.append("\n aadhaar\t: "+ aadhaar);
		sb.append("\n dob\t: "+ dob);
		sb.append("\n age\t: "+ age);
		sb.append("\n bloodGroup\t: "+ bloodGroup);
		sb.append("\n pan\t: "+ pan);
		sb.append("\n voterID\t: "+ voterID);
		sb.append("\n email\t: "+ email);
		sb.append("\n mobile\t: "+ mobile);
		
		sb.append("\n eyes\t: "+ eyes);
		sb.append("\n ears\t: "+ ears);
		sb.append("\n hands\t: "+ hands);
		sb.append("\n legs\t: "+ legs);
		
		sb.append("\n\n================ Address details =====================");
		sb.append("\n  "+ address);
		
		return sb.toString();
	}
}
