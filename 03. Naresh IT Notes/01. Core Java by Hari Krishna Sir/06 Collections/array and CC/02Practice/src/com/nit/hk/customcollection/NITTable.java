package com.nit.hk.customcollection;

public class NITTable {
	
	private Object[] keys;
	private Object[] values;
	private int size;
	
	public NITTable() {
		keys = new Object[10];
		values = new Object[10];
		size = 0;
	}
	
//Operation #1: Adding objects to collection 	
	public void put(Object key, Object value) {
		if(size() == capacity()) {
			grow();
		}
		
		keys[size] = key;
		values[size] = value;
		size++;
	}
	
	private void grow() {
		int newCapacity = capacity() * 2;
		Object[] nextKeysArray = new Object[newCapacity];
		Object[] nextValuesArray = new Object[newCapacity];
		
		for(int i=0; i<keys.length; i++) {
			nextKeysArray[i] = keys[i];
			nextValuesArray[i] = values[i];
		}
		
		keys = nextKeysArray;
		values = nextValuesArray;
	
	}

//Operation #2: Finding size	
	public int capacity() {
		return keys.length;
	}
	
	public int size() {
		return size;
	}
	
//Operation #3: Printing objects
	@Override
	public String toString() {
		
		if(size == 0)
			return "{}";
			
		StringBuilder entriesDataBuilder = new StringBuilder();
		entriesDataBuilder.append("{");
		
		for (int i=0; i<size; i++) {
			entriesDataBuilder.append(keys[i]);
			entriesDataBuilder.append("=");
			entriesDataBuilder.append(values[i]);
			entriesDataBuilder.append(", ");
		}
		
		int start = entriesDataBuilder.lastIndexOf(", ");
		int end = start + 2;
		entriesDataBuilder.delete(start, end);
		
		entriesDataBuilder.append("}");
		
		return entriesDataBuilder.toString();
	}
	
	
}









