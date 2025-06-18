package com.nit.hk.blogic.calc;

import com.nit.hk.blogic.add.Addition;
import com.nit.hk.blogic.sub.Subtraction;
import com.nit.hk.blogic.mul.Multiplication;
import com.nit.hk.blogic.div.Division;

public class Calc {
	public static void main(String[] args) {
		System.out.println("Project exection started");
		Addition a = new Addition();
		Subtraction s = new Subtraction();
		Multiplication m = new Multiplication();
		Division d = new Division ();

		a.add(10, 5);
		s.sub(10, 5);
		m.mul(10, 5);
		d.div(10, 5);

		System.out.println("\n\nProject exection end");
	}
}
