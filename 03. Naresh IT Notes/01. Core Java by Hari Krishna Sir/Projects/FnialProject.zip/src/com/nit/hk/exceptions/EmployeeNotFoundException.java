package com.nit.hk.exceptions;

public class EmployeeNotFoundException extends Exception {

	private static final long serialVersionUID = 1L;

	public EmployeeNotFoundException() {
		super();
	}
	
	public EmployeeNotFoundException(String errMsg) {
		super(errMsg);
	}

	public EmployeeNotFoundException(Exception e) {
		super(e);
	}
	
}
