package trumanz.webDocker.server.api.services;


import java.util.HashMap;
import java.util.Map;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.HttpHeaders;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.UriInfo;

import trumanz.webDocker.server.api.resources.ResourceInstance;

@Path("/hosts/")
public class HostService extends BaseService {
	
	@GET
	@Produces(MediaType.APPLICATION_JSON)
	public Response getHosts(String body, @Context HttpHeaders headers, @Context UriInfo ui){
		
		return  null;
		
		/*
		return handleRequest(headers, body, ui, Request.Type.GET,
				createHostResource(null, ui));
		*/
	}
	


	ResourceInstance createHostResource(String hostName, UriInfo ui){
		/*
		Map<Resource.Type, String> mapIds = new HashMap<Resource.Type, String>();
		mapIds.put(Resource.Type.Host, hostName);
		
		return createResource(Resource.Type.Host, mapIds);
		*/
		return null;
	}

}
