import java.util.Collection;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Test09_AllOperationsByUsingLL {
	public static void main(String[] args) {
		
		LinkedList<Object> ll = new LinkedList<>();
		System.out.println("size: "+ ll.size());	
		System.out.println("eles: "+ ll);
		System.out.println();
		
//Operation #1: Adding objects to LL
		ll.add("a"); 			System.out.println(ll);	
		ll.add("b"); 			System.out.println(ll);	
		ll.add(5); 				System.out.println(ll);	
		ll.add(6.7); 			System.out.println(ll);	
		ll.add('p'); 			System.out.println(ll);	
		ll.add(true); 			System.out.println(ll);	
		ll.add(null); 			System.out.println(ll);	
		ll.add(new Ex(5,6)); 	System.out.println(ll);	
		ll.add(new Sa(5,6)); 	System.out.println(ll);	
		ll.add(null); 			System.out.println(ll);
		ll.add("a"); 			System.out.println(ll);	
		ll.add(5); 				System.out.println(ll);
		System.out.println();
		
//Operation #2: Counting objects
		System.out.println("size: "+ ll.size());	

//Operation #3: Printing objects
		System.out.println("eles: "+ ll);
		System.out.println();
		
//Operation #4: Searching object
		System.out.println(ll.contains("a"));	
		System.out.println(ll.contains("A"));	
		System.out.println(ll.contains(5));	
		System.out.println(ll.contains(null));	
		System.out.println(ll.contains(new Ex(5, 6)));	 //equals() ???
		System.out.println(ll.contains(new Sa(5, 6)));	 //equals() ???
		System.out.println();
		
		System.out.println(ll.indexOf("a"));	
		System.out.println(ll.indexOf("A"));	
		System.out.println(ll.indexOf(5));	
		System.out.println(ll.indexOf(null));	
		System.out.println(ll.indexOf(new Ex(5, 6)));	 //equals() ???
		System.out.println(ll.indexOf(new Sa(5, 6)));	 //equals() ???
		System.out.println();
		
//Operation #5: retrieving object
		//public E get(int index)
		System.out.println(ll.get(0));  //sequential moving over LL for the index with [node.next] help
		System.out.println(ll.get(5));	//once it reaches the given index location, it returns item reference
		System.out.println(ll.get(7));	//from this location Node object. get() follows Binary Searching algorithm
										//for finding the given index Node
		
		//System.out.println(ll.get(-1));	
		//System.out.println(ll.get(ll.size()));
		System.out.println();
		
//Operation #6: removing object
		Collection<Object> col = new LinkedList<>();
		//col.remove(obj);
		//col.removeAll(col);
		//col.removeIf(pred);
		
		List<Object> list = new LinkedList<>();
		//list.remove(index);
		
		Queue<Object> queue = new LinkedList<>();
		//queue.remove();
		
		Deque<Object> deque = new LinkedList<>();
		//deque.removeFirst();
		//deque.removeLast();
		//deque.removeFirstOccurrence(obj);
		//deque.removeLastOccurrence(obj);
		
		System.out.println(ll);
		System.out.println(ll.remove("a"));
		System.out.println(ll);
		

//Operation #7: inserting object	
		ll.add(3, "X");  //BSA 
		System.out.println(ll); 

//Operation #8: replacing object	
		ll.set(6, "Y");  //BSA 
		System.out.println(ll); 
		System.out.println(); 
		
//Operation #9: sorting object
		LinkedList<String> ll2 = new LinkedList<>();
		ll2.add("a");
		ll2.add("c");
		ll2.add("b");
		System.out.println(ll2);
		ll2.sort(null);
		System.out.println(ll2);
		
		
		
		
		
	}
}















