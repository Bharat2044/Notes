public class Sa{

	private int x;
	private int y;

	public Sa(int x, int y) {
		this.x = x;
		this.y = y;
	}

	public int getX() {
		return x;
	}

	public void setX(int x) {
		this.x = x;
	}

	public int getY() {
		return y;
	}

	public void setY(int y) {
		this.y = y;
	}

												//sa.equals("a")
												//sa.equals(new Ex(5, 6))
												//sa.equals(new Sa(5, 6))
	@Override				
	public boolean equals(Object obj) {
									//this arg   obj ele
		System.out.println(this + "  " + obj);
		if(obj instanceof Sa s) { //Java 14v
			//Sa s = (Sa)obj;
			return this.x == s.x &&
					this.y == s.y;
		}
		
		return false;
	}

	@Override
	public String toString() {
		return "Sa(x=" + x + ", y=" + y + ")";
	}
	
}
