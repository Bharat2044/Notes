package com.nit.hk.arrays;

public class Test02_ArrayClassName {
	public static void main(String[] args) {
		
		byte[] 		ba = new byte[0];
		short[] 	sa = new short[0];
		int[] 		ia = new int[0];
		long[] 		la = new long[0];
		float[] 	fa = new float[0];
		double[] 	da = new double[0];
		char[] 		ca = new char[0];
		boolean[] 	boa= new boolean[0];
		String[] 	sta= new String[0];
		P[] 		pa = new P[0];
		
		System.out.println(ba); //[B@hc
		System.out.println(sa); //[S@hc
		System.out.println(ia); //[I@hc
		System.out.println(la); //[J@hc
		System.out.println(fa); //[F@hc
		System.out.println(da); //[D@hc
		System.out.println(ca); //
		System.out.println(""+ca); //[C@hc
		System.out.println(boa); //[Z@hc
		System.out.println(sta); //[Ljava.lang.String;@hc
		System.out.println(pa); //[Lcom.nit.hk.arrays.P;@hc
		
	}
}


class P{ }