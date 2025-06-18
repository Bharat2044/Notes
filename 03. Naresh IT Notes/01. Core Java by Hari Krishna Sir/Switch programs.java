class Test34_switch{

	public static void main(String[] args){
		dayName(8);
	}

	static void dayName(int day) {
		switch(day){
			case 1:
				System.out.println("Today is MON");
				break;
				
			case 2:
				System.out.println("Today is TUE");
				break;

			case 3: 
				System.out.println("Today is WED");
				break;	

			case 4:
				System.out.println("Today is THU");
				break;

			case 5:
				System.out.println("Today is FRI");
				break;
				
			case 6:
				System.out.println("Today is SAT");
				break;

			case 7: 
				System.out.println("Today is SUN");
				break;

			default: 
				System.out.println("Invalid number");
				System.out.println("Enter between (1-7) only");		

		}//switch close
	}//method close
}//class close


class Test35_switch_With_ABandAUB{
	
	public static void main(String[] args){
		dayName(new Integer(7));
	}

	static void dayName(Integer day) {
		switch(day){
			case 1:
				System.out.println("Today is MON");
				break;
				
			case 2:
				System.out.println("Today is TUE");
				break;

			case 3: 
				System.out.println("Today is WED");
				break;	

			case 4:
				System.out.println("Today is THU");
				break;

			case 5:
				System.out.println("Today is FRI");
				break;
				
			case 6:
				System.out.println("Today is SAT");
				break;

			case 7: 
				System.out.println("Today is SUN");
				break;

			default: 
				System.out.println("Invalid number");
				System.out.println("Enter between (1-7) only");

		}//switch close
	}//method close
}//class close

enum Day {																					
	MON, TUE, WED, THU, FRI, SAT, SUN								
}																										

class Test36_switch_With_enum{
	public static void main(String[] args){
		displayDayNum(Day.THU);
	}	

	static void displayDayNum(Day day){
		switch(day){
			case MON:
				System.out.println(day + " is day 1 in the week");
				break;

			case TUE: 
				System.out.println(day + " is day 2 in the week");
				break;

			case WED: 
				System.out.println(day + " is day 3 in the week");
				break;
				
			case THU: 
				System.out.println(day + " is day 4 in the week");
				break;

			case FRI: 
				System.out.println(day + " is day 5 in the week");
				break;

			case SAT: 
				System.out.println(day + " is day 6 in the week");
				break;

			case SUN: 
				System.out.println(day + " is day 7 in the week");
				break;

			default:
				System.out.println(day + " is not supporting");

		}//switch close
	}//method close
}//class close