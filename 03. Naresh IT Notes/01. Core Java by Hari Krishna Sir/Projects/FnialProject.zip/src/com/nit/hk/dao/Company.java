package com.nit.hk.dao;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Enumeration;
import java.util.HashMap;

import com.nit.hk.beans.Employee;
import com.nit.hk.exceptions.DuplicateEmployeeExcepiton;
import com.nit.hk.exceptions.EmployeeClassNotFoundException;
import com.nit.hk.exceptions.EmployeeNotFoundException;

public class Company {
	
	private HashMap<String, ArrayList<Employee>> employeeMap ;
	
	public Company() throws EmployeeClassNotFoundException  {
		load();		
	}
	
	public void store(Employee emp) throws DuplicateEmployeeExcepiton {

		ArrayList<Employee> employeeList = employeeMap.get(emp.getDept());
		
		if(employeeList == null) {
			
			employeeList = new ArrayList<>();
			employeeList.add(emp);
			employeeMap.put(emp.getDept(), employeeList);
			
		}else {
			if(employeeList.contains(emp))
				throw new DuplicateEmployeeExcepiton(
					"The employee("+emp.getEno() + ", "+ emp.getName()+", " 
											+ emp.getDept()	+ ") already existed");
			employeeList.add(emp);
		}
		save();
			
	}
	
	public String store(ArrayList<Employee> empList) {

		StringBuilder duplicatesEmpsInfo = new StringBuilder();
		
		for(Employee emp : empList) {
			try {
				store(emp);
			} catch (DuplicateEmployeeExcepiton e) {
				duplicatesEmpsInfo.append(e.getMessage()+"\n");
			}
		}
		save();
		return duplicatesEmpsInfo.toString();

	}
	
	public Employee get(int eno, String dept) { 
		ArrayList<Employee> employeeList = employeeMap.get(dept);
		
		if(employeeList == null)
			return null;
		
		Employee emp = new Employee();
		emp.setEno(eno);
		emp.setDept(dept);
		
		int index = employeeList.indexOf(emp);
		if(index == -1) 
			return null;
		
		return employeeList.get(index) ;
		
	}
	
	public Enumeration<Employee> get(String dept) {
		ArrayList<Employee> employeList = employeeMap.get(dept);
		
		if(employeList != null)
			return Collections.enumeration(employeList);
		
		return Collections.emptyEnumeration();
	}

	public void updateSal(int eno, String dept, int perc) throws EmployeeNotFoundException{

		Employee emp = get(eno, dept); 
		if(emp == null)
			throw new EmployeeNotFoundException("Employee is not found with given details");
		
		emp.setSal(emp.getSal() +emp.getSal()*perc/100);
		save();		
	}

	public Employee remove(int eno, String dept) {
		
		Employee emp = get(eno, dept);
		if(emp != null) {
			employeeMap.get(dept).remove(emp);
			save();
			return emp;
		}

		return null;
	}
	
	public boolean remove(String dept) {

		ArrayList<Employee> employeeList =  employeeMap.remove(dept);
		if(employeeList != null) {
			save();
			return true;
		}
		return false;
		
	}

	@SuppressWarnings("unchecked")
	private void load() throws EmployeeClassNotFoundException {

		try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("empdata.ser")) ) {
			
			employeeMap = (HashMap<String, ArrayList<Employee>>)ois.readObject();
			System.out.println("employeeMap is loaded");
			
		} catch(ClassNotFoundException e) {
			throw new EmployeeClassNotFoundException(e);
		} catch (IOException e) {
			employeeMap = new HashMap<>();
			System.out.println("employeeMap is created with empty object");
		} 
		
		try { Thread.sleep(2000);}
		catch(InterruptedException e) { }
	}
	
	private void save() {
		try(ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("empdata.ser")) ){
			
			oos.writeObject(employeeMap);			
			oos.flush();
			System.out.println("Employee data is saved in file");
			
		}catch(FileNotFoundException e ) {
			System.out.println("The file empdata.ser unable create");
		}
		catch(IOException e) {
			e.printStackTrace();
		}
	}
}



							





							
							
							
							
							
							
							
							
							
							
							
							
							