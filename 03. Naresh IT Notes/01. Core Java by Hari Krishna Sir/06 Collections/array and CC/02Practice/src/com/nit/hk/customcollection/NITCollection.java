package com.nit.hk.customcollection;


public class NITCollection {
	
	private Object[] elementData;
	private int elementCount;
	
	public NITCollection() {
		elementData = new Object[10];
		elementCount = 0;
	}
	
//Operation #1: Adding objects to collection 	
	public void add(Object obj) {
		if(size() == capacity()) {
			grow();
		}
		
		elementData[elementCount++] = obj;
	}
	
	private void grow() {
		
		Object[] nextArray = new Object[capacity() * 2];
		
		for(int i=0; i<elementData.length; i++) {
			nextArray[i] = elementData[i];
		}
		
		elementData = nextArray;
	
	}

//Operation #2: Finding size	
	public int capacity() {
		return elementData.length;
	}
	
	public int size() {
		return elementCount;
	}
	
//Operation #3: Printing objects
	@Override
	public String toString() {
		
		if(elementCount == 0)
			return "[]";
			
		StringBuilder elementDataBuilder = new StringBuilder();
		elementDataBuilder.append("[");
		
		for (int i=0; i<elementCount; i++) {
			elementDataBuilder.append(elementData[i]);
			elementDataBuilder.append(", ");
		}
		
		int start = elementDataBuilder.lastIndexOf(", ");
		int end = start + 2;
		elementDataBuilder.delete(start, end);
		
		elementDataBuilder.append("]");
		
		return elementDataBuilder.toString();
	}
	
//Operation #4: Searching an object
	public boolean contains(Object obj) {

		return indexOf(obj) >= 0;		
			
	}
	
//Operation #5: finding the index of the given object 	
	public int indexOf(Object obj) {
	
		if(obj == null) {
			for(int i=0; i<elementCount; i++) {
				if(elementData[i]==null)
					return i;
			}
			return -1;
		}else {
			for(int i=0; i<elementCount; i++) {
				if(obj.equals(elementData[i]))
					return i;
			}
			return -1;
		}
	}

//Operation #6: finding the index of last occurrence of the given object 	
	public int lastIndexOf(Object obj) {
		
		if(obj == null) {
			for(int i=elementCount-1; i>=0 ;i--) {
				if(elementData[i] == null)
					return i;
			}
		}else {
			for(int i=elementCount-1; i>=0 ;i--) {
				if(obj.equals(elementData[i]))
					return i;
			}
			
		}
		return -1;
	}
	
//Operation #7: Retrieving the object
	public Object get(int index) {
		checkIndex(index);	
		return elementData[index];
	}
	
	private void checkIndex(int index) {
		if(index<0 || index>=elementCount)
			throw new IndexOutOfBoundsException(index);
	}
	
//Operation #8: removing object by index
	public Object remove(int index) {

		checkIndex(index);
		
		Object obj = elementData[index];
		
		for(; index<elementCount-1; index++) {
			elementData[index] = elementData[index+1]; 
			//System.out.println(Arrays.toString(elementData));
		}
		
		elementData[elementCount-1] = null;
		elementCount--;
		
		return obj;
	}

//Operation #9: removing object by object
	public boolean remove(Object obj) {
		
		int index = indexOf(obj);
		if(index == -1)
			return false;
			
		remove(index);		
		return true;
	}
	
//Operation #10: inserting an object 
	public void add(int index, Object obj) {
		if(index<0 || index>elementCount)			
			throw new IndexOutOfBoundsException(index);
		
		if(size()==capacity())
			grow();
		
		for(int i=elementCount-1; i>=index; i--) {
			elementData[i+1] = elementData[i];
			//System.out.println(Arrays.toString(elementData));
		}
		
		elementData[index] = obj;
		elementCount++;		
	}
	
//Operation #11: replacing object 
	public Object set(int index, Object obj) {
		
		checkIndex(index);
		
		Object ele = elementData[index];
		elementData[index] = obj;
		
		return ele;
	
	}
	
}









