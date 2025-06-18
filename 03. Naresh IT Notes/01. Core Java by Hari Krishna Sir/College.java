//inheritance 
//==========
//Need of this chapter?
	//Upto now we have been learning creating an object individually
	//Now in this chapter we are learning creaing an object extending from an existing object

//What is inheritance and why inheritance?
	//The process of creating a new object deriving from an existing object 
	//by obtaining its type, properties and behaviours
	//for "extending or implementing" the functionality of this exissting object
	//by reusing existing properties and behaviours is called inheritance

//How to develop inheritance?
	//By using two keywords
		//1. extends
		//2. implements

//If we need to derive a class from an exsiting class, we must use extends keyword
//If we need to derive an interface from an exsiting interface, we must also use extends keyword
//If we need to derive an class from an exsiting interface, we must use implements keyword

//For example:

class Person {
    static int eyes		= 2;
	static int ears		= 2;
	static int hands	= 2;
	static int legs		= 2;

	String name;
	double height;
	double weight;

	long mobile;
	String email;
	long aadhaar;
	String address;
   
   

   void eat(){
       System.out.println(name + "  is eating");
   }
    
   void sleep(){
       System.out.println(name + "  is sleeping");
   }

}


class  Student extends Person{

     int sno;
	 String course;
	 double fee;

	 void listen(){
		System.out.println(name + " is listening "+ course);
	 }

	 void write() {
		System.out.println(name + " is writing "+ course + " notes");
	 }

	 void read() { 
		 System.out.println(name + " is reading "+ course + " notes");	  
	 }
	 
	 @Override
	 public String toString() {
		 return "  eyes\t\t: "+ eyes +	"\n" +
			 		"  ears\t\t: " + ears +"\n" +
			 		"  hands\t\t: " + hands+"\n" +
			 		"  legs\t\t: " + legs+"\n" +
			 		"  name\t\t: " + name+"\n" +
			 		"  height\t: " + height+"\n" +
			 		"  weight\t: " + weight+"\n" +
			 		"  sno\t\t: " + sno+"\n" +
			 		"  course\t: " + course+"\n" +
			 		"  fee\t\t: " + fee;
	 }


		 
}

class Faculty extends Person{
	int eno;
	String dept;
	String subject;
	double sal;
	double exp;

	void teach(){
		System.out.println(name + " is teaching "+ subject);
	}

	 @Override
	 public String toString() {
		 return "  eyes\t\t: "+ eyes +	"\n" +
			 		"  ears\t\t: " + ears +"\n" +
			 		"  hands\t\t: " + hands+"\n" +
			 		"  legs\t\t: " + legs+"\n" +
			 		"  name\t\t: " + name+"\n" +
			 		"  height\t: " + height+"\n" +
			 		"  weight\t: " + weight+"\n" +
			 		"  eno\t\t: " + eno+"\n" +
			 		"  dept\t\t: " + dept+"\n" +
			 		"  subject\t: " + subject+"\n" +
			 		"  sal\t\t: " + sal+"\n" +
			 		"  exp\t\t: " + exp;
	 }
      
}

class Admin extends Person{

	int ano;
	String block;
	double sal;
	double exp;

   void check(){
        System.out.println(name + " is checking "+ block + " persons ID cards");
   }

   	 @Override
	 public String toString() {
		 return "  eyes\t\t: "+ eyes +	"\n" +
			 		"  ears\t\t: " + ears +"\n" +
			 		"  hands\t\t: " + hands+"\n" +
			 		"  legs\t\t: " + legs+"\n" +
			 		"  name\t\t: " + name+"\n" +
			 		"  height\t: " + height+"\n" +
			 		"  weight\t: " + weight+"\n" +
			 		"  ano\t\t: " + ano+"\n" +
			 		"  block\t\t: " + block+"\n" +
			 		"  sal\t\t: " + sal+"\n" +
			 		"  exp\t\t: " + exp;
	 }

}

class College {
	public static void main(String[] args) {
       
	   Person p1 = new Person();
	   p1.name = "HK";
       p1.eat();
	   p1.sleep();
	   //p1.listen(); //(can not access child class members by using parent reference)
		System.out.println();

	   Student s1 = new Student();
	   s1.name = "HK";
	   s1.height = 6.5;
	   s1.weight = 300;

	   s1.sno = 101;
	   s1.course = "CJ";
	   s1.fee = 2500;

		System.out.println("s1 object details");	   
		System.out.println(s1);	   
		
		s1.eat();
		s1.sleep();
		s1.listen();
		s1.write();
		s1.read();

		//Faculty object
		Faculty f1 = new Faculty();
		f1.eno = 7279;
		f1.name = "HK";
		f1.dept  = "Java";
		f1.subject = "CJ";
		f1.sal = 99999999;
		f1.exp = 16;
		
		System.out.println("\nf1 object details");
		System.out.println(f1);

		//Admin object
		Admin a1 = new Admin();
		a1.ano = 1234;
		a1.name = "Rambabu";
		a1.block  = "HK Block";
		a1.sal = 100000;
		a1.exp = 17;
		
		System.out.println("\na1 object details");
		System.out.println(a1);
	}
	
}


//What is the problem if we donot develop inheritance among same type of objects?
	//1. Code Redundancy		(for sub type objects)
	//2. Tight Coupling				(for user type object (HAS-A realtion))
	//3. Static Binding				(for user type object (HAS-A realtion))

//Code Redundancy means
   //Same number of variables and methods we must develop in each and every sub class

//Tight Coupling 
	//Accepts only one particular sub class objects
   //means We can not declare one referenced variable for passing and storing all diff sub class objects

//Static Binding
	//invoked method is always executes from the same sub class object
	//means We can not invoke a method common to all sub classes to execute it from diff sub classes automatically
	//based on the sub class object we passed


//For example:
	//in above project if we donot develop inheriance, 
	//the properties and behaviours declared in Person class
	//we must declare in each and evey sub class

		//with inheritance we define them in super class Person common to all sub classes
		//and reusing those declared properties and behaviours as if they were defined in our sub class
			//This feature is called code reusability - Defining one time and accessing all diff palces

//If we define a user class Canteen to provide eat() operation for diff type of persons
//if we donot develop inheritance for Person type object, we must overload a method 
//for accepting all diff type of sub classes objects as shown below
//it leads two problems TC and SB

class Canteen{
	void eat(Student s){ //it can accept only Student object						-> Tight coupling
        s.eat(); //eat() alsways can be executed from only Student class	-> Static Binding
	}

	void eat(Faculty f){ //it can accept only Faculty object						-> Tight coupling
		f.eat(); //eat() alsways can be executed from only faculty class	-> static binding
	}

	void eat(Admin a){ //it can accept only Admin object						-> Tight coupling
		a.eat();//eat() alsways can be executed from only Admin class		-> static binding
	}

}

//In future if we got one more sub type object, we must modify code and must add only more overloaded 
//method for supporting this new sub type object. 

//If we develop inheritance, we can achieve LC and DB
	//1) we can define a paramerized method that can accepts all sub classes objects
	//       we can achieve Loose Coupling

	//2) and we can invoke a method to be executed from diff sub classes based on the passed sub class object
	//		we can achieve Dynamic Binding

class Canteen {
	void eat(Person p){ //now we can pass all its sub class objects S, F, A (it is LC)
          p.eat();					//this method is executed from P/S/F/A based on the object we passed
	}
}

//The above code is dynamic code. 
//in projects we must develop dynamic code common to all sub classes
//in future even if we get any new Person type object we no need to modify above code
//it access that new sub class object as argument and the eat() is exeuted from that sub class object.

//Q) If we need to add new properties and behaviours common to all sub classes, 
//where we must define them without inheritance and with inheritance?
	//without inheritance -> we must add in evey sub class	(code redundency)
	//with inheritance	  -> we must add in only super class (code reusability)

	//updata above project by adding 
	//mobile, email and aadhaar


//When we must develop inheritance?
	//1) when we find multiple objects of same type, we must develop inheritance
	//    for acheving code reusability, loose copuling and dynamic binding

	//2) for extending or for implementing existing object functionality
	//     by adding new properties and behavoiurs.    


//For fun if we develop inheritance, is there any problem?
	//Just for reusing members of an existing class if we develop inheritance
		//1) static binding -> class B always connected to class A, we can not remove this connection
		//2) egar loading -> class B loaded into JVM class A is also loaded even though we are not requied it
		//3) can not destroy memory-> when we create class B object, class A members memory is also allocated
															//in class B object, which we can not desotry with out destroying class B object

class A {
	int x = 10;
	int y = 20;
}

class B extends A {
	int p = 30;
	int q = 30;
}

//Solution: if we just want to reuse existing class members, access them by using HAS-A relation
//The advantage with HAS-A relation
	//1) dynamic binding	-> when even we need to connection other class we can connect
	//2) lazy loading			-> when ever we need to load other class, that time we load class
	//3) can destoy memory -> when we no need of that other class object, we can destory it 
												//without desotying our class object.

class B {

	 A a;  //HAS-A relation

	public static void main(String[] args) {
		
		B b = new B();
		b.a = new A();

		b.a = null;
	}
}


//Conclusion: 
	//Both extending and reusing ---> IS-A (inheritance)
	//Only reusing							--> HAS-A(composition)

	//for reusing pupose always favour to HAS-A relation over IS-A relation

//How can we decide whether to develop inherinace or not?
//Apply IS-A test

//new object IS-A exsing object?

class Animal {   //Animal IS-A Animal (no IS-A relation)

}


class Tiger  extends Animal{  //Tiger IS-A Animal (we must develop IS-A relation)

}

class Zoo  {   //Zoo IS-A Zoo (no inheritance relation
   						//Zoo HAS-A Animal
	Animal animal;
}

//As part of inheritance how many diff types of classes we will develop?
	//3 types of classes
		//1) super class 
		//2) sub class
		//3) user class





//Write a program to develop inheritance and show reusing super class
//static and non-static members in sub class and in user class (test) by using sub class reference.

	//-> Inside sub class we can access super class members eithe directly by their name
	//or by using sub class name or by using using sub class object

	//-> In user class we can access super class members only either by using 
	//sub class name or by using sub class reference

//Q) By using sub class reference, can we access all members available in super class?
//A) No, we can access only non-private members, means only visible members

	//private members are never visible
	//default members are visible within same package 
	//protected and public members are visible all places

	//for full program refer modifiers chapter




































