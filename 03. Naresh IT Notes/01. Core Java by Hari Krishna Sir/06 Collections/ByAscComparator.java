package com.nit.hk.suncollections;

import java.util.Comparator;

public class ByAscComparator implements Comparator<B> {

	@Override
	public int compare(B b1, B b2) {
		return b1.getY() - b2.getY();
	}

}
