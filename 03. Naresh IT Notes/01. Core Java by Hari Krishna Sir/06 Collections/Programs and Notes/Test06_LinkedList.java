import java.util.LinkedList;

/*
 * 1. A ListList is a Collections Framework collection available from Java 1.2v
 * 2. If out more operations are inserting and removing in at beginning and in the middle
 * 		we must choose LinkedList 
 * 3. LinedList is a non-synchronized collection, suitable to use in single threaded application
 * 		in multithread model application it give wrong result
 * 4. It is ordered collection, stores objects in insertion order
 * 5. It has two constructors to create new instance
 * 6. Its implemented data structure is doubly linked list
 * 7. Default capacity: 0  incremental capacity: 1
 * 8. All four types of objects are allowed to store: H, H, U and D
 * 9. null is allowed and multiple nulls are allowed 
 * 10. Objects are stored in insertion order
 * 11. object can be retrieved in only sequential [but look like random access]
 * 12. internal methods called in Linked class methods and executed from adding object class is equals()
 * 		in searching and removing operations equals() method is called in contains() and remove() methods
 * 		and its is executed from our class, if not overridden it is executed from Object class  
 */
public class Test06_LinkedList {

	public static void main(String[] args) {
		
		LinkedList<Object> ll = new LinkedList<>();
		
		System.out.println("size: " + ll.size());
		System.out.println("eles: " + ll);
		
		ll.add("a");	System.out.println("eles: " + ll);
		ll.add("b");	System.out.println("eles: " + ll);
		ll.add(5);		System.out.println("eles: " + ll);
		ll.add(6.7);	System.out.println("eles: " + ll);
		ll.add('p');	System.out.println("eles: " + ll);
		ll.add(true);	System.out.println("eles: " + ll);
		ll.add(null);	System.out.println("eles: " + ll);		
		ll.add("a");	System.out.println("eles: " + ll);
		ll.add(5);		System.out.println("eles: " + ll);
		ll.add(null);	System.out.println("eles: " + ll);		
		ll.add(6.7);	System.out.println("eles: " + ll);
		ll.add(true);	System.out.println("eles: " + ll);
		ll.add(new Ex(5,6));	System.out.println("eles: " + ll);
		
		System.out.println("size: " + ll.size());
		System.out.println();
		
		System.out.println(ll.get(3)); //looks like random access, but it is sequenctial 
		System.out.println();  
		
		for(int i=0; i<ll.size(); i++) {	//sequential access
			System.out.println(ll.get(i));
		}
		
	}
}


