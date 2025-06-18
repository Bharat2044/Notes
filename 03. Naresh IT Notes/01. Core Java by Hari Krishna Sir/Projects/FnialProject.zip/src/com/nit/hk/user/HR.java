package com.nit.hk.user;

import java.util.Enumeration;
import java.util.Scanner;

import com.nit.hk.beans.Employee;
import com.nit.hk.dao.Company;
import com.nit.hk.exceptions.DuplicateEmployeeExcepiton;
import com.nit.hk.exceptions.EmployeeClassNotFoundException;
import com.nit.hk.exceptions.EmployeeNotFoundException;

public class HR {
	public static void main(String[] args) {
		try(Scanner scn = new Scanner(System.in)) {
			Company c = new Company();
			
			loop: while(true) {
				
				System.out.println("\nChoose one option");
				System.out.println(" 1. Create emloyee");
				System.out.println(" 2. Get one employee");
				System.out.println(" 3. Get one dept all employee");
				System.out.println(" 4. Update emloyee Salary");
				System.out.println(" 5. Remove one emloyee");
				System.out.println(" 6. Remove dept");
				System.out.println(" 7. Exit");
				
				System.out.print("Enter option: ");
				int option = scn.nextInt(); scn.nextLine();
				
				switch(option) {
				
					case 1: {//save employee 
				
						try {
							Employee emp = new Employee();
							
							System.out.print("\n===== Enter Personal details =====");					
							
							System.out.print("  Enter eno\t\t: ");					
							emp.setEno(scn.nextInt()); scn.nextLine();
		
							System.out.print("  Enter ename\t\t: ");					
							emp.setName(scn.nextLine());
		
							System.out.print("  Enter dept\t\t: ");					
							emp.setDept(scn.nextLine());
		
							System.out.print("  Enter sal\t\t: ");					
							emp.setSal(scn.nextDouble()); scn.nextLine();
							
							System.out.print("\n===== Enter Address details =====");					
							System.out.println("Enter address: ");	
							emp.setAddress(scn.nextLine());
							
							c.store(emp);
							System.out.println("\nemployee is saved");
							
							try {Thread.sleep(1000);}
							catch(InterruptedException e) {}
							
						}catch (DuplicateEmployeeExcepiton e) {
							System.out.println("Error: "+ e.getMessage());
						}
						break;
					}//case 1 close
					
					case 2: { //get one employee
						System.out.print("\nEnter eno: ");
						int eno = scn.nextInt(); scn.nextLine();

						System.out.print("Enter dept: ");
						String dept = scn.nextLine();
						
						Employee emp = c.get(eno, dept);
						if(emp == null)
							System.out.println("Error: employee not found with the given details");
						else {
							System.out.println(emp);
						}
						try {Thread.sleep(1000);}
						catch(InterruptedException e) {}
						break;
					}//case 2 close
					
					case 3: { //get one dept all employees

						System.out.print("Enter dept: ");
						String dept = scn.nextLine();
						
						Enumeration<Employee> e = c.get(dept);
						if(!e.hasMoreElements()) {
							System.out.println("Error: given dept is not existed");
						}else {
							do {
								System.out.println(e.nextElement());
							}while(e.hasMoreElements());
						}
						
						try {Thread.sleep(1000);}
						catch(InterruptedException ex) {}
						
						break;
					}//case 3 close
					
					case 4: {//updating sal 
						System.out.print("\nEnter eno\t: ");
						int eno = scn.nextInt(); scn.nextLine();

						System.out.print("\nEnter dept\t: ");
						String dept = scn.nextLine();

						System.out.print("\nEnter hike pecr\t: ");
						int perc = scn.nextInt(); scn.nextLine();
						
						try {
							c.updateSal(eno, dept, perc);
							System.out.println("Employee salary is increased");
							
						} catch (EmployeeNotFoundException e) {
							System.out.println(e.getMessage());
						}
						
						try {Thread.sleep(1000);}
						catch(InterruptedException e) {}

						break;
						
					}//case 4 close
					
					case 5: {//remove one employee
						System.out.print("\nEnter eno\t: ");
						int eno = scn.nextInt(); scn.nextLine();

						System.out.print("\nEnter dept\t: ");
						String dept = scn.nextLine();
						
						Employee emp = c.remove(eno, dept);
						if(emp==null)
							System.out.println("Employee is not found withe the given detials");
						else
							System.out.println("Empolyee is removed");
						
						try {Thread.sleep(1000);}
						catch(InterruptedException e) {}

						break;
						
					}//case 5 is removed
					
					case 6: {
						System.out.print("\nEnter dept\t: ");
						String dept = scn.nextLine();
						
						boolean removed = c.remove(dept);
						if(removed) {
							System.out.println("Dept is removed");
						}else {
							System.out.println("Dept is not found");
						}
						
						try {Thread.sleep(1000);}
						catch(InterruptedException e) {}

						break;
						
					}//case 6 close
						
					case 7: { //exit
						System.out.println("^^^^^^^^^^^ Thank You :-) ^^^^^^^");
						break loop;
					}
					
					default : {
						System.out.println("\nInvalid option");
					}
					
				}//switch close 
			}//while(true)
			
		}catch(EmployeeClassNotFoundException e) {
			System.out.println("Error: " + e.getMessage());
		} 
		
	}
}
