package com.nit.hk.collections;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Optional;
import java.util.stream.Stream;

/**
 * - A Stream API is a predefined library available from Java 8v
 *   in the package "java.util.stream"
 *   
 * - A stream is a flow of data or objects
 * - A Java 8 stream API is used for 
 * 		1. retrieving objects from collection and
 * 		2. processing those objects 
 *   with less code by avoiding loops and conditions
 *   
 * - With Stream API we can write concise code(less code or direct code)  
 *   by following functional programming style with functional interface and 
 *   lambda expression.
 *   
 * - The Functional interface is meant for defining method parameters and 
 *   return types to receive and return logic directly to stream API
 *   for retrieving and processing objects
 *   
 * - The Lambda expression and method reference are meant implementing 
 *   functional interfaces and passing logic directly as argument
 *   without creating extra class and object     
 *   
 * - In addition to Stream API in Java 8v "43 predefined functional interfaces"
 *   are provided in the package java.util.function to use them with Stream API
 *   
 * - Among them the important functional interfaces are
 * 		1. Consumer		-> a parameterized functional interface
 * 		2. Supplier		-> a return type functional interface
 * 		3. Function     -> a parameterized and return type functional interface
 * 		4. Predicate	-> a parameterized boolean valued function on the given value  
 *   
 * 		5. BiConsumer		-> a two parameterized functional interface
 * 		6. BooleanSupplier	-> a return type functional interface
 * 		7. BiFunction     	-> a two parameterized and return type functional interface
 * 		8. BiPredicate		-> a two parameterized boolean valued function on the given value  
 *   	
 *   	9. UnaryOperator
 *   	10. BinaryOperator
 *   	....	
 *   	....	
 *   	....	
 *   	....	
 *  
 *  - Examples of Stream API method those used functional interfaces 
 *  
 *   	pubic void forEach(Consumer){
 *   
 *   	}		
 *   
 *   	pubic void forEach(BiConsumer){
 *   
 *   	}		
 *   
 *   	public ??? filter(Predicate){
 *   
 *   	}
 *   
 *   	public ??? map(Function){
 *   
 *   	}
 *   
 *   	public ??? generate(Supplier)
 *    
 *    
 *  - How to obtain stream object?
 *  	
 *  	Stream s1 = col.steam();			//sequential stream		
 *  	Stream s1 = col.parallelSteam()		//parallel stream
 *  
 *  - on a stream object we can perform two types of operations
 *  	1. intermediate operations
 *  	2. terminal operation
 *  
 *  - The operations those process objects in collection and 
 *    returns new Stream object with result objects are called
 *    intermediate operations. 
 *      For example: filter(), map(), flatMap(), ..... 
 *  
 *  - The operation that is applied at end of the stream and 
 *    returns result from this Stream is called terminal operation
 *    	For example: forEach(), collect(), count(), max(), min(), ...
 *    
 *  - The Intermediate operations are applied in between source and terminal
 *    operations and we can apply multiple intermediate operations.
 *
 *  - The Stream object structure
 *  	refer the attached diagram
 *  
 *  - All intermediate and terminal operations method are available in 
 *    the interface Stream in the package java.util.stream package.
 *    
 * Intermediate operations
	The Stream interface in Java 8 provides a set of 
	intermediate operations that can be used to transform or filter 
	the elements in a stream. Here are some of the most	commonly used 
	intermediate operations:
	
	1. filter(Predicate<T> predicate): This operation filters the elements in the 
		stream based on a given predicate and returns a new stream with only the 
		filtered elements.

	2. map(Function<T, R> mapper): This operation applies a function to each element in 
		the stream and returns a new stream with the transformed elements.

	3. flatMap(Function<T, Stream<R>> mapper): This operation applies a function that	
		returns a stream to each element in the stream, and then flattens the 
		resulting streams into a single stream.

	4. distinct(): This operation returns a new stream with only the distinct elements	
		from the original stream.

	5. sorted(): This operation returns a new stream with the elements sorted in 
		natural order.

	6. sorted(Comparator<T> comparator): This operation returns a new stream with the 
		elements sorted based on a given comparator.

	7. peek(Consumer<T> action): This operation applies a consumer to each element in	
		the stream and returns a new stream with the same elements.

	8. limit(long maxSize): This operation returns a new stream with only the first
		maxSize elements from the original stream.

	9. skip(long n): This operation returns a new stream with all the elements from the 
		original stream except for the first n elements.

	These intermediate operations are useful for transforming, filtering, and 
	manipulating the elements in a stream before performing a terminal operation. By 
	chaining multiple intermediate operations together, you can create complex stream 
	pipelines that perform advanced data processing tasks.
   
 * Terminal operations
	The Stream interface in Java 8 provides a set of terminal operations that can be 
	used to produce a result or side-effect. Here are some of the most commonly used 
	terminal operations:

	1. forEach(Consumer<T> action): This operation applies a consumer to each element 
		in the stream.

	2. toArray(): This operation returns an array containing the elements of the 
		stream.

	3. reduce(BinaryOperator<T> accumulator): This operation applies a binary operator 
		to the elements in the stream and returns a result.

	4. collect(Collector<T,A,R> collector): This operation collects the elements in the 
		stream into a collection or other data structure.

	5. min(Comparator<T> comparator): This operation returns the minimum element in the 
		stream based on a given comparator.

	6. max(Comparator<T> comparator): This operation returns the maximum element in the 
		stream based on a given comparator.

	7. count(): This operation returns the number of elements in the stream.

	8. anyMatch(Predicate<T> predicate): This operation returns true if any element in 
		the stream matches a given predicate.

	9. allMatch(Predicate<T> predicate): This operation returns true if all elements in	
		the stream match a given predicate.

	10. noneMatch(Predicate<T> predicate): This operation returns true if no element in 
		the stream matches a given predicate.

	These terminal operations are used to produce a result or side-effect after 
	performing intermediate operations on a stream. By combining intermediate and 
	terminal operations, you can create powerful stream pipelines that perform complex 
	data processing tasks.   
 */
public class Test25_StreamAPI {
	public static void main(String[] args) {
	
	//#1: Retrieve objects from collection and print	
		ArrayList<Object> al = new ArrayList<Object>();
		al.add("a");
		al.add(5);
		al.add("b");
		al.add(6);
		al.add("c");
		al.add(7);
		al.add("d");
		al.add(8);
		
		al.forEach(obj -> System.out.println(obj));

	//#2: Retrieve entries from Map and print	
		LinkedHashMap<Object, Object> lhm = new LinkedHashMap<>();
		lhm.put("a", 97);
		lhm.put("b", 98);
		lhm.put("c", 99);
		
		lhm.forEach((k, v) -> System.out.println(k + " " + v));
		System.out.println();

	//#3: Retrieve and print only String objects from ArrayList
		al.stream()
			.filter(obj -> obj instanceof String)
			.forEach(obj -> System.out.println(obj));
		System.out.println();
		
	//#4: Retrieve and print only Integer objects from ArrayList
		al.stream()
			.filter(obj -> obj instanceof Integer)
			.forEach(System.out::println);

		System.out.println();
		
	//#5: Retrieve and print only even Integer objects from ArrayList
		al.stream()
			.filter(obj -> obj instanceof Integer)
			.filter(obj -> ((int)obj)%2==0)
			.forEach(System.out::println);
		System.out.println();
		
	//#6: Count numbers integers available in this AL	
		long count = al.stream()
						.filter(obj -> obj instanceof Integer)
						.count();
		System.out.println("The number of Integer availabe in AL are: " + count);
		
	//7: Retrieve/collect all integers available in AL
		List<Object> list = al.stream()
							  .filter(obj -> obj instanceof Integer)
							  .toList();
		System.out.println(list);
		
	//8. Retrieve all strings available in this AL and return them in upper case
			//"a" => "A"  => mapping -> map()
		
		al.stream()
			.filter(obj -> obj instanceof String)
			.map(obj -> ((String)obj).toUpperCase())
			.forEach(System.out::println);
		
	//9. retrieving the max number available in the collection
		System.out.println(al);
		Optional<Object> max = al.stream()
			.filter(ele -> ele instanceof Integer)
			.max((o1, o2) -> ((Integer)o1).compareTo((Integer)o2));
		System.out.println("The max value avilable: " + max);	
		
		Object maxValue = max.get();
		System.out.println(maxValue);
		System.out.println();
		
	//10. retrieving the mix number available in the collection	
		Optional<Object> min = al.stream()
				.filter(ele-> ele instanceof Integer)
				.min((o1, o2) -> ((Integer)o1).compareTo((Integer)o2));

		Object minValue = min.get();
		System.out.println("The min value available: "+ minValue);
		
	}
}

