import java.util.ArrayList;

public class Test08_AllOperationsByUsingAL {
	public static void main(String[] args) {
		
		ArrayList<Object> al = new ArrayList<>();
		System.out.println("size: "+ al.isEmpty());
		System.out.println("size: "+ al.size());
		System.out.println("eles: "+ al);
		System.out.println();

//Operation #1: adding objects
		al.add("a"); System.out.println("eles: "+ al);	
		al.add("b"); System.out.println("eles: "+ al);	
		al.add(5); System.out.println("eles: "+ al);	
		al.add(true); System.out.println("eles: "+ al);	
		al.add(6.7); System.out.println("eles: "+ al);	
		al.add('p'); System.out.println("eles: "+ al);	
		al.add(null); System.out.println("eles: "+ al);	
		al.add("a"); System.out.println("eles: "+ al);	
		al.add(5); System.out.println("eles: "+ al);	
		al.add(6.7); System.out.println("eles: "+ al);
		al.add("a"); System.out.println("eles: "+ al);
		
		al.add(new Ex(5, 6)); System.out.println("eles: "+ al);	
		al.add(new Sa(5, 6)); System.out.println("eles: "+ al);	
			
		System.out.println();
		
//Operation #2: counting
		System.out.println(al.isEmpty());
		System.out.println(al.size());
		
//Operation #3: printing
		System.out.println(al.toString());
		System.out.println();
		
//Operation #4: searching an object 
		//-> finding an object in collection that is matched with the passed argument object
		//-> if match found returns true, else returns false.
		//-> for finding the matched object with the passed argument, inside contains method 
		//argument object is compared with the objects available in collection by using equals() method
		//-> inside contains method equals() method is called inside for loop
		//until either match is found or until end of collection
			//if match found, return true and terminates iteration
			//if match is not found, comparison is continued until end of the collection
			//at end of collection it returns false
		
		//the equals() method called inside contains() method will be executed from
		//contains() method argument object class. If equals() method is not overridden in argument object class
		//it is executed from java.lang.Object class, this argument object is compared with the elements available 
		//in collection with reference. If these objects references are diff, return false, else returns true.
		
		//if you want to compare objects with state, we must override, equals() method in the argument object class.
		
		//Most important point: in written test exam. if you see a question on collection with contains method call,
		//silently check whether in argument object class equals() method is overridden or not. 
		//if not overridden, if the argument object is new ref object, choose output false.
		//if overridden, if the argument object data is same as the object data in collection, choose output true.
		
	//Note #1:
		//In String class and in all WCs equals() is overridden to compare String and WCs object with their state
		//When you find String object or WCO is passed as argument to contains(), we must compare those object
		//with the String and WCO available in collection with state
		
		
	//Note #2:
		//If we search for null, contains method does not use equals() method
		//it uses == operator, because it is not an object. 
		
	//Comparing the argument object with the object elements available in collection starts from 
	//0 index to end of the collection is called linear searching algorithm
		
		
		System.out.println(al.contains("a")); 				//"a".equals(e1 ... en) -> executed from String class
		System.out.println(al.contains(new String("a"))); 	//"a".equals(e1 ... en) -> executed from String class
		System.out.println(al.contains(new String("A"))); 	//"A".equals(e1 ... en) -> executed from String class
		System.out.println(al.contains(6.7)); 				//6.7.equals(e1 ... en) -> executed from Double class
		System.out.println(al.contains(new Double(6.7))); 	//6.7.equals(e1 ... en) -> executed from Double class
		
		System.out.println(al.contains(new Ex(5, 6))); //->false  
						//new Ex(5, 6).equals(e1 ... en) -> exe from Example class
								//new Ex(5,6).equals("a"); -> ref comparison -> false 
								//new Ex(5,6).equals("b"); -> ref comparison -> false 
								//new Ex(5,6).equals(5); -> ref comparison -> false 
								//new Ex(5,6).equals(6.7); -> ref comparison -> false 
								//new Ex(5,6).equals('p'); -> ref comparison -> false 
								//new Ex(5,6).equals(true); -> ref comparison -> false 
								//new Ex(5,6).equals(null); -> ref comparison -> false 
								//new Ex(5,6).equals("a"); -> ref comparison -> false 
								//new Ex(5,6).equals(5); -> ref comparison -> false 
								//new Ex(5,6).equals(6.7); -> ref comparison -> false 
								//new Ex(5,6).equals(new Ex(5,6)); -> ref comparison -> false 
								//new Ex(5,6).equals(new Sa(5,6)); -> ref comparison -> false
		
		System.out.println(al.contains(new Sa(5, 6))); //-> true (need data comparison -> so eq() overridden in Sa)
								//new Sa(5,6).equals("a"); -> type comparison -> false 
								//new Sa(5,6).equals("b"); -> type comparison -> false 
								//new Sa(5,6).equals(5); -> type comparison -> false 
								//new Sa(5,6).equals(6.7); -> type comparison -> false 
								//new Sa(5,6).equals('p'); -> type comparison -> false 
								//new Sa(5,6).equals(true); -> type comparison -> false 
								//new Sa(5,6).equals(null); -> type comparison -> false 
								//new Sa(5,6).equals("a"); -> type comparison -> false 
								//new Sa(5,6).equals(5); -> type comparison -> false 
								//new Sa(5,6).equals(6.7); -> type comparison -> false 
								//new Sa(5,6).equals(new Ex(5,6)); -> type comparison -> false 
								//new Sa(5,6).equals(new Sa(5,6)); -> type and data comparison -> true

		System.out.println(al.contains(null));	//->true
						//null.equals("a"); -> RE: NPE, not for null comparison equals() will not be used
							//null == "a"; -> false
							//null == "b"; -> false
							//null == 5; -> false
							//null == 6.7; -> false
							//null == 'p'; -> false
							//null == true; -> false
							//null == null; -> true
		
		//contains() method search for an object and returns true or false
		//hence with the contains method we can only find whether the object is available in collection or not
		
		//if we want to know the index of this matched object, we must use another method called 
		//indexOf(obj) or lastIndexOf(obj)
		
				//indexOf(-) returns first occurrence
				//lastIndexOf(-) returns last occurrence
		
		//if the passed object is not found, it returns -1
		
		System.out.println();
		System.out.println(al);
		
		System.out.println(al.contains("a"));
		System.out.println(al.indexOf("a"));
		System.out.println(al.lastIndexOf("a"));

		System.out.println(al.contains("A"));
		System.out.println(al.indexOf("A"));
		System.out.println(al.lastIndexOf("A"));

		System.out.println(al.contains(new Ex(5,6)));
		System.out.println(al.indexOf(new Ex(5,6)));
		System.out.println(al.lastIndexOf(new Ex(5,6)));

		System.out.println(al.contains(new Sa(5,6)));
		System.out.println(al.indexOf(new Sa(5,6)));
		System.out.println(al.lastIndexOf(new Sa(5,6)));
		System.out.println();
		
//Operation #5: retrieving [random access and sequential access]
		//public E get(int index)
		
		//random access
		System.out.println(al.get(0));
		System.out.println(al.get(5));
		System.out.println(al.get(10));
		System.out.println();
		
		//sequential access
		for (int i = 0; i < al.size(); i++) {
			System.out.print(al.get(i) +" ");
		} 
		
		System.out.println();
		
		//retrieving and storing an object in local variable
		
		//String s1 = al.get(0); //Rule #1: we must not assign get method to returning object type variable
								//we must assign to a variable of AL generic parameter type
		
		Object obj = al.get(0);
		//System.out.println(obj.toUpperCase()); //Rule #2: we can not call members specific to returned object
													//we must type cast object to its own type
		
		//String s1 = (String)obj;				//Rule #3: we must not type casting directly to sub type without checking
		//System.out.println(s1.toUpperCase());	//we may get CCE, we must instanceof condition
		
		if(obj instanceof String) {
			String s1 = (String)obj;
			System.out.println(s1.toUpperCase());
		}

		//al.get(-1);									//Rule #4: [index >= 0 and < size]
		//al.get(al.size());
		
		//for(int i=0; i<=al.size(); i++) {				//Rule #5: the condition operator must be 
		//	System.out.print(al.get(i));				//<al.size() or <=al.size()-1
		//}
		System.out.println();
		
		//After retrieving an object from a collection
		//if we modify object data by using local ref var
		//that modification is effected to collection also,
		//because the LRV and collection location are pointing to same object
		
		//if the object is immutable, the modification is not effected
		
		obj = al.get(0);
		String s1 = (String)obj;
		s1.concat("x");				//String is immutable modification is not effected
		System.out.println(al);
		
		obj = al.get(11);
		Ex e1 = (Ex)obj;
		e1.setX(8);					//Ex is mutable so modification is effected
		e1.setY(9);
		System.out.println(al);
		System.out.println();
		
		obj = al.get(5);			//static way retrieving 
		System.out.println(obj);

		int index = al.indexOf(true);	
		obj = al.get(index);			//dynamic way
		System.out.println(obj);

		index = al.indexOf("A");	
		//obj = al.get(index);			//RE: IOOBE
		//System.out.println(obj);
		
//Operation #6: removing object
		//public boolean remove(Object obj)  -> used for removing given object matching object from collection
											//it removes only one occurrence that is first occurrence
											//for finding the given object matched object in collection
											//it internally uses equals() method to compare the passed object
											//with the objects available in collection. 
											//		if equals() is not overridden in argument object class
											//		objects are compared with reference. Even though object
											//		is available it is not removed

		//public E remove(int index)	 -> used to remove the given index object
										//-> it does not use equals() method, because here no finding operation
										//-> if we pass byte/short/int/char value to remove them from collection
										//those values are not removed, instead those values index location objects 
										//are removed
										//for removing byte/short/int/char values from collection
										//we must pass them as wrapper class object
		
		//public void removeIf(Predicate p)  //-> used to remove objects those are matched given condition 	
		
		//public boolean removeAll(Collection c) //-> used for removing given collection elements from the current collection
												//-> it removes all occurrences of the elements
		
		//public boolean retainAll(Collection c)//-> used for removing elements from the current collection except passed collection elements
		
		//public void clear() //-> it is used for removing all elements from collection and making collection emepty
		
		System.out.println();
		System.out.println(al);
		System.out.print(al.remove("a")+"\t");
		System.out.println(al);
		System.out.print(al.remove(6.7)+"\t");
		System.out.println(al);
		System.out.print(al.remove(new Ex(8, 9))+"\t"); //equals() is not overridden so not removed 
		System.out.println(al);
		System.out.print(al.remove(new Sa(5, 6))+"\t"); //equals() is overridden so removed
		System.out.println(al);
		
		System.out.print(al.remove(5)+"\t");		//remove(index) is called and 5th index object is removed 
		System.out.println(al);
		System.out.print(al.remove((Integer)5)+"\t"); //remove(Object) is called and Integer(5) is removed
		System.out.println(al);
		//System.out.print(al.remove('p')+"\t"); //remove(index) is called. 'p' index is not available, IOOBE
		System.out.print(al.remove((Character)'p')+"\t"); //remove(index) is called. 'p' index is not available, IOOBE
		System.out.println(al);
		System.out.print(al.remove(true)+"\t"); //remove(index) is called. 'p' index is not available, IOOBE
		System.out.println(al);
		System.out.println();
		System.out.println();
		
		ArrayList<Integer> al2 = new ArrayList<>();
		for(int i=1; i<=10; i++) {
			al2.add(i*10);
		}								// 0   1    2  3   4   5    6  7   8    9 			
		System.out.println(al2);		//[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
		al2.remove(1);					//[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
		al2.remove(2);					//[10, 30, 40, 50, 60, 70, 80, 90, 100]	
		System.out.println(al2);		//[10, 30, 50, 60, 70, 80, 90, 100]
		
		System.out.println();
		
		ArrayList<Object> al3 = new ArrayList<>();
		for(int i=1; i<=10; i++) {
			if(i%2==0)
				al3.add(i*10);
			else
				al3.add("a"+i*10);
		}								// 0   1    2  3   4   5    6  7   8    9 			
		System.out.println(al3);		//[a10, 20, a30, 40, a50, 60, a70, 80, a90, 100]
//		for(int i=0; i<al3.size(); i++) {
//			obj = al3.get(i);
//			if(obj instanceof String)
//				al3.remove(i);
//		}
		
//		al3.removeIf( new Predicate<Object>() {
//			@Override
//			public boolean test(Object ele) { //a10   20     a30
//				return ele instanceof String; //true  false  true 
//			}
//		});

//		al3.removeIf((Object ele) -> { 			//a10   20     a30
//				return ele instanceof String; 	//true  false  true 
//		});

		al3.removeIf(ele -> ele instanceof String); 	
					//a10   20     a30
					//true  false  true 
		
		System.out.println(al3);		//[20, 40, 60, 80, 100]
		System.out.println();		
		
		al3.add(20);		
		al3.add(60);		
		al3.add(20);		
		al3.add(80);
		System.out.println(al3);
		al3.remove((Integer)20);
		System.out.println(al3);
			
		ArrayList<Object> al4 = new ArrayList<>();
		al4.add(20);
		al4.add(60);
		al4.add(80);

		//al3.removeAll(al4);
		//System.out.println(al3); //[40, 100]
		
		al3.retainAll(al4);
		System.out.println(al3); 	//[60, 80, 20, 60, 20, 80]
		
		al3.clear();
		System.out.println(al3); 	//[]
		System.out.println(); 	
		
//Operation #7: inserting object
		//public void add(int index, Object obj)
		System.out.println(al);
		al.add(0, "X");
		System.out.println(al);
		al.add(3, "Y");
		System.out.println(al);
		al.add(al.size(), "Z");
		System.out.println(al);

			//index>=0 and <=size
		//al.add(-1, "A");  //IOOBE
		//al.add(al.size()+1, "A");  //IOOBE
		
//Operation #8: replacing object
		//public Object set(int index, Object obj)
		al.set(1, "B");
		System.out.println(al);
		System.out.println();
		
//Operation #9: sorting objects
		ArrayList<Integer> al5 = new ArrayList<>();
		al5.add(3);
		al5.add(5);
		al5.add(4);
		System.out.println(al5);
		al5.sort(null);
		System.out.println(al5);
		
	}
}









