package net.floodlightcontroller.mactracker;

import java.util.ArrayList;

import net.floodlightcontroller.mactracker.AES.Mode;
import net.floodlightcontroller.mactracker.AES.Padding;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.math.BigInteger;
import java.net.*;

public class ServerHandler extends Thread{

	static ArrayList<String> usernames;
	static ArrayList<String> passwords;
	
	DH dh;
	String sessionKey;
	
	BufferedReader streamIn;
    PrintStream streamOut;
    Socket socket;
    int useridindex = 0;
    
	public ServerHandler(Socket socket){
		this.socket=socket;
		dh = new DH();
		//initiate();
	}
	public long nextID(){
    	ServerCentral.curID = 4*ServerCentral.curID + 1;
    	return ServerCentral.curID;
    }
	

	public void run(){
		
		try {
			System.err.println("New client just connected");
			streamOut = new PrintStream(socket.getOutputStream(), true);
			streamIn = new BufferedReader(new InputStreamReader(socket.getInputStream()));
		} 
		catch (Exception e1) {
			try {
				socket.close();
				e1.printStackTrace();
			} 
			catch (Exception e2) {
				e2.printStackTrace();
			}
			e1.printStackTrace();
		}
	
		while(true){

			try{
				Thread.sleep(1);
				String message = streamIn.readLine();
								
            	if(message == null){
            		//System.err.println("No more messages . Closing socket ...");
            		//socket.close();
            		//break;
            	}
            	else{
					Thread.sleep(1);
					
					System.err.println("Client sent --> "+message);
					
					if(message.startsWith("KEY")){
						String sent = message.substring(3);						
						sessionKey = dh.genSessionKey(new BigInteger(sent));
						long id = nextID();
						ServerCentral.idToKey.put(id, sessionKey);
						System.err.println("Session Key : "+sessionKey);
						streamOut.println(dh.publicValue+"_"+id);
						}
					else {
						
						if(message.startsWith("PATH")){
							String sent = message.substring(4);
							
							String [] info = sent.split("_");
							long id = Long.parseLong(info[0].trim());
							
							String encPath = info[1];
							AES aes = new AES();
							String decPath = aes.decrypt(encPath,Mode.ECB,Padding.NoPadding,ServerCentral.idToKey.get(id));
							System.err.println("The path is : "+decPath);
							
							streamOut.println("OK");
							
							String [] nodes = decPath.split(" ");
							for (String cur : nodes) {
								ServerCentral.idToNextHob.put(nextID(), cur);
							}
							
							System.err.println(ServerCentral.idToNextHob.toString());
							
							
						}
						else if(message.startsWith("NEXT")){
							String sentID = message.substring(4);
							String nextHob = ServerCentral.idToNextHob.get(Long.parseLong(sentID));
							System.err.println("NEXT HOB : "+nextHob);
							streamOut.println(nextHob);
						}
					}
					
                    //streamOut.println("You sent : " + message);
					
				}
            
			}
			catch(Exception e){
				e.printStackTrace();
				try {
					socket.close();
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				return;
				
			}
	    }
			
    }

}