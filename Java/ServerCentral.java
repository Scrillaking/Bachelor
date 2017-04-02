package net.floodlightcontroller.mactracker;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;


public class ServerCentral extends Thread{
	
	ServerSocket server ;
	ArrayList<Boolean> onlinetable;
	ArrayList<ServerHandler> clients;
	
	public ServerCentral()throws Exception {
		server = new ServerSocket(4500);
		System.err.println("Initialized socket server at port 4500");

		
		
		
		
		while(true){
			try {
				
				// listening for a connection 
				Thread.sleep(1);
				Socket socket = server.accept(); // accept new connection and create new socket
				socket.setSoTimeout(0);
				System.err.println("Switch Connected with port : " + socket.getInetAddress().toString());
				ServerHandler x = new ServerHandler(socket);
				x.start();
				
				
			} catch (IOException e) {
				}
			
			
			
			
			
		}
		

	}
	
	



	public static void main (String[]args) throws Exception{
		@SuppressWarnings("unused")
		ServerCentral x = new ServerCentral();
	}

}
