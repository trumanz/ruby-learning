package trumanz.webDocker.server.agent.rest;

import javax.servlet.http.HttpServletRequest;
import javax.ws.rs.Consumes;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;

import com.google.inject.Inject;

import trumanz.webDocker.server.WebDockerException;
import trumanz.webDocker.server.agent.HeartBeatHandler;
import trumanz.webDocker.server.agent.Register;
import trumanz.webDocker.server.agent.RegistrationResponse;
import trumanz.webDocker.server.agent.RegistrationStatus;

@Path("/")
public class AgentResource {
	
	private static HeartBeatHandler hh;
	
	@Inject
	public static void init(HeartBeatHandler instance){
		hh = instance;
	}
	
	@POST
	@Path("register/{hostName}")
	@Consumes(MediaType.APPLICATION_JSON)
	@Produces({MediaType.APPLICATION_JSON})
	public RegistrationResponse register(Register message, @Context HttpServletRequest req){
		
		RegistrationResponse response = null;
		try{
			response = hh.handleRegistration(message);
		} catch (WebDockerException ex){
			response = new RegistrationResponse();
			response.setResponseStatus(RegistrationStatus.FAILED);
			response.setLog(ex.getMessage());
		}
		return response;
	}

}
