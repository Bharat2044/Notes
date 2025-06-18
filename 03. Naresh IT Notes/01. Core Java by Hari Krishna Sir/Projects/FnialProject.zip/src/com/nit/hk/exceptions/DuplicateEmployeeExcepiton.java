package com.nit.hk.exceptions;

public class DuplicateEmployeeExcepiton extends Exception {

	private static final long serialVersionUID = 1L;
	
	public DuplicateEmployeeExcepiton() {
		super();
	}

	public DuplicateEmployeeExcepiton(String errMsg) {
		super(errMsg);
	}
	
	
}

