package trumanz.webDocker.controller;

import org.junit.Test;

public class controllerTest {
	@Test
	public void test() throws Exception{
		WebDockerServer webDockerServer =  new WebDockerServer(8080);
		webDockerServer.start();
		
		webDockerServer.stop();
	}
	

}
