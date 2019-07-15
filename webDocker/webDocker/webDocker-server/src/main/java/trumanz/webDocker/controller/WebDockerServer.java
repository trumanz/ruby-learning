package trumanz.webDocker.controller;

import java.util.LinkedList;
import java.util.List;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.core.Response;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletContextHandler;
import org.eclipse.jetty.servlet.ServletHolder;
import org.glassfish.jersey.server.ServerProperties;
import org.junit.Assert;

/**
 * Hello world!
 *
 */
public class WebDockerServer 
{
	private Server server = null;
	
	public WebDockerServer(int port) {
		
		ServletContextHandler rootServletContexHandler = new ServletContextHandler(ServletContextHandler.SESSIONS);
		
		ServletHolder sh = new ServletHolder(org.glassfish.jersey.servlet.ServletContainer.class);
		sh.setInitParameter(ServerProperties.PROVIDER_PACKAGES, "trumanz.webDocker.controller.api");
		sh.setInitOrder(0);
		rootServletContexHandler.addServlet(sh,"/api/v1/*");
		
		sh = new ServletHolder(org.glassfish.jersey.servlet.ServletContainer.class);
		sh.setInitParameter(ServerProperties.PROVIDER_PACKAGES, "trumanz.webDocker.AgentApi");
		sh.setInitOrder(0);
		rootServletContexHandler.addServlet(sh,"/agent/v1/*");
		
		server = new Server(port);
		server.setHandler(rootServletContexHandler);
	
	}
	public void start() throws Exception{
		server.start();
	}
	public void stop() throws Exception{
		server.stop();
	}
	
	public void HostUpdateStatus(String host){
		agents.add(host);		
	}
	public List<String>  getHosts(){
		return agents;
	}

	private List<String> agents = new LinkedList<String>();
	
    public static void main( String[] args ) throws Exception
    {
       
    }
}
