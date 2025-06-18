import java.util.ArrayList;

/*
 * 1. An ArrayList is a Collections Framework collection available from Java 1.2v
 * 2. When we need to store multiple objects including duplicates in insertion order
 * 		without thread safety in single threaded application or in method local operations we must use ArrayList
 * 3. ArrayList is a non-synchronized collection, suitable to use in single threaded application
 * 		in multithread model application it give wrong result
 * 4. It is ordered collection, stores objects in insertion order
 * 5. It has three constructors to create new instance
 * 6. Its implemented data structure is resizable array algorithm
 * 7. Default capacity: 10  incremental capacity: half or 1
 * 8. All four types of objects are allowed to store: H, H, U and D
 * 9. null is allowed and multiple nulls are allowed 
 * 10. Objects are stored in insertion order
 * 11. object can be retrieved in both random and sequential
 * 12. internal methods called in Vector class method and executed from adding object class
 * 		in searching and removing operation equals() method is called in contains() and remove() methods
 * 		and its is executed from our class, if not overridden it is executed from Object class  
 */
public class Test05_ArrayList {
	public static void main(String[] args) {
		
		ArrayList<Object> al = new ArrayList<>();
		
		System.out.println("size: " + al.size());
		System.out.println("eles: " + al);
		
		al.add("a");	System.out.println("eles: " + al);
		al.add("b");	System.out.println("eles: " + al);
		al.add(5);		System.out.println("eles: " + al);
		al.add(6.7);	System.out.println("eles: " + al);
		al.add('p');	System.out.println("eles: " + al);
		al.add(true);	System.out.println("eles: " + al);
		al.add(null);	System.out.println("eles: " + al);		
		al.add("a");	System.out.println("eles: " + al);
		al.add(5);		System.out.println("eles: " + al);
		al.add(null);	System.out.println("eles: " + al);		
		al.add(6.7);	System.out.println("eles: " + al);
		al.add(true);	System.out.println("eles: " + al);
		al.add(new Ex(5,6));	System.out.println("eles: " + al);
		
		System.out.println("size: " + al.size());
		
		System.out.println(al.get(3)); //reandom access
		System.out.println();  
		
		for(int i=0; i<al.size(); i++) {	//sequential access
			System.out.println(al.get(i));
		}
		
	}
}
