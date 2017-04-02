package net.floodlightcontroller.mactracker;

import java.math.BigInteger;

public class DH {

	String publicValue;
	long prime;
	int base;
	int privateKey;
	
	public DH(){

	    //prime = (long)Math.pow(2,768); 
	    prime = (long)Math.pow(2,60); 

	    base = 5;
	  		  
	    privateKey = genRandom(2);
	    publicValue = (((long)Math.pow(base,privateKey)) % prime)+"";
		  
	}
	
	public int genRandom(int bits){	
		
	    long range_start = (long)Math.pow(10,(bits-1));
	    long range_end = (long)(Math.pow(10,(bits-1))-1);
	    int x = (int)(range_start + range_end * Math.random());
	    System.err.println("Private key of controller is " + x);
	    return x ;
	    
	}
	
	public String genSessionKey(BigInteger otherPublic){
		//String sessionKey = (((long)Math.pow(otherPublic,privateKey)) % prime)+"";
		String sessionKey = (otherPublic.pow(privateKey)).mod(new BigInteger(prime+"")).toString();
		return sessionKey.substring(0, 16);
		//return sessionKey ;
		
	}
	
	public static void main(String[] args) {

		DH dh = new DH();
		//System.err.println(dh.genSessionKey(new BigInteger("55511151231257827021181583404541015625")));
		
	}
	
}
