class  ReadingAllIntegers {
	public static void main(String[] args) {
		
		for(int i=0; i<args.length; i++){
			try{
				int value = Integer.parseInt(args[i]);
				System.out.println(value);
			}catch(NumberFormatException e){ 
				//System.out.println("NFE is raised");
			}

		}

	}
}
