package com.nit.hk.beans;

import com.nit.hk.helper.DeptMap;

public class Employee extends Person {

	private static final long serialVersionUID = 1L;
	
	private int eno;
	private String dept;
	private double sal;
	private float exp;
	private String desig;
	private String reportTo;
	
	public Employee() {
		// no-op
		//for supporting deserialization
	} 
	
	public Employee(String name, double height, double weight, String gender, String bloodGroup, String dob, int eno) {
		super(name, height, weight, gender, bloodGroup, dob);
		this.eno = eno;
	}

	
	public int getEno() {
		return eno;
	}

	public void setEno(int eno) {
		this.eno = eno;
	}

	public String getDept() {
		return dept;
	}

	public void setDept(String dept) {
		this.dept = dept;
	}

	public double getSal() {
		return sal;
	}

	public void setSal(double sal) {
		this.sal = sal;
	}

	public float getExp() {
		return exp;
	}

	public void setExp(float exp) {
		this.exp = exp;
	}

	public String getDesig() {
		return desig;
	}

	public void setDesig(String desig) {
		this.desig = desig;
	}

	public String getReportTo() {
		return reportTo;
	}

	public void setReportTo(String reportTo) {
		this.reportTo = reportTo;
	}
	
	@Override
	public int hashCode() {
		return DeptMap.getDeptID(dept);
	}
	
	@Override
	public boolean equals(Object obj) {
		if(obj instanceof Employee e)
			return this.dept.equals(e.dept) &&
						this.eno == e.eno;
		return false;
	}
	
	@Override
	public String toString() {
		return super.toString();
	}
	
}
