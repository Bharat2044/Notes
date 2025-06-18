import java.util.Vector;
/*
 * 1. A vector is a legacy collection available from Java 1.0
 * 2. When we need to store multiple objects including duplicates in insertion order
 * 		with thread safety in multithreaded application we must use Vector
 * 3. Vector is synchronized collection, suitable to use in Multithreaded application
 * 		in single thread model application it give less performance because of synchronization locking and unlokcing
 * 4. It is ordered collection, stores objects in insertion order
 * 5. It has 4 constructors for creating new instance
 * 6. Its implemented data structure is growable array algorithm
 * 7. Default capacity: 10  incremental capacity: double or 1
 * 8. All four types of objects are allowed to store: H, H, U and D
 * 9. null is allowed and multiple nulls are allowed 
 * 10. Objects are stored in insertion order
 * 11. object can be retrieved in both random and sequential
 * 12. internal methods called in Vector class method and executed from adding object class
 * 		in searching and removing operation equals() method is called in contains() and remove() methods
 * 		and its is executed from our class, if not overridden it is executed from Object class  
 */
public class Test04_Vector {
	public static void main(String[] args) {
		
		Vector<Object> v1 = new Vector<>();
		System.out.println("capcaity: "+ v1.capacity());
		System.out.println("size: " + v1.size());
		System.out.println("eles: " + v1);
		
		v1.add("a");	System.out.println("eles: " + v1);
		v1.add("b");	System.out.println("eles: " + v1);
		v1.add(5);		System.out.println("eles: " + v1);
		v1.add(6.7);	System.out.println("eles: " + v1);
		v1.add('p');	System.out.println("eles: " + v1);
		v1.add(true);	System.out.println("eles: " + v1);
		v1.add(null);	System.out.println("eles: " + v1);		
		v1.add("a");	System.out.println("eles: " + v1);
		v1.add(5);		System.out.println("eles: " + v1);
		v1.add(null);	System.out.println("eles: " + v1);		
		v1.add(6.7);	System.out.println("eles: " + v1);
		v1.add(true);	System.out.println("eles: " + v1);
		v1.add(new Ex(5,6));	System.out.println("eles: " + v1);
		
		System.out.println("size: " + v1.size());
		System.out.println("capcaity: "+ v1.capacity());
		
		System.out.println(v1.get(3)); //reandom access
		System.out.println();  
		
		for(int i=0; i<v1.size(); i++) {	//sequential access
			System.out.println(v1.get(i));
		}
		
	}
}
