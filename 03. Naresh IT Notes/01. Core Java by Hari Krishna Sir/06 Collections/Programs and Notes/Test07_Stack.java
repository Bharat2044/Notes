import java.util.Stack;

/*
 * Stack is meant for retrieving objects in LIFO order
 */
public class Test07_Stack {
	public static void main(String[] args) {
		
		Stack<Object> stack  = new Stack<>();
		stack.push("a");
		stack.push("b");
		stack.push("c");
		stack.push("d");
		stack.push("e");
		stack.push("f");
		
		System.out.println(stack);
		System.out.println(stack.pop());
		System.out.println(stack);
		System.out.println(stack.pop());
		System.out.println(stack);
		System.out.println(stack.peek());
		System.out.println(stack);
		System.out.println(stack.peek());
		System.out.println(stack);
		
	
		stack.add("X");						
		System.out.println(stack);
		
		System.out.println(stack.get(2));  //random access
		
		stack.remove(2);
		System.out.println(stack);
	}
}
