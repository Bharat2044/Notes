package com.nit.hk.helper;

import java.util.HashMap;

public class DeptMap {
	
	private static HashMap<String, Integer> deptMap;
	
	static {
		deptMap = new HashMap<>();
		deptMap.put("CRT", 1);
		deptMap.put("C", 2);
		deptMap.put("DS", 3);
		deptMap.put("COREJAVA", 4);
		deptMap.put("ORACLE", 5);
		deptMap.put("HTML", 6);
		deptMap.put("ADVJAVA", 7);
	}
	
	public static int getDeptID(String dept) {
		return deptMap.get(dept.toUpperCase());
	}
}
