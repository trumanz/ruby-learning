package trumanz.webDocker.server.api.services;

import javax.ws.rs.core.HttpHeaders;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.Status;
import javax.ws.rs.core.UriInfo;

import trumanz.webDocker.server.api.resources.ResourceInstance;
import trumanz.webDocker.server.api.services.Request.Type;

public class BaseService {

	protected Response handleRequest(HttpHeaders headers, String body, UriInfo uriInfo, Request.Type requestType,
			ResourceInstance resource) {
		return handleRequest(headers, body, uriInfo, requestType, null, resource);
	}
	
	private Response handleRequest(HttpHeaders headers, String body, UriInfo uriInfo, Type requestType,
			MediaType mediaType, ResourceInstance resource) {
		
		/*
		try{
			Request request = getRequestFactory().
		}
		
		Status status;
		
		Response.ResponseBuilder builder = Response.status(status).entity(serializer.serialize(result));
	
		if(mediaType != null){
			builder.type(mediaType);
		}
		return builder.build();
		*/
		return null;
	}

	/*
	protected ResourceInstance createResource(Resource.Type type, Map<Resource.Type, String> mapIds) {
		return m_resourceFactory.createResource(type, mapIds);
	}
	
	
	RequestFactory getRequestFactory(){
		return new RequestFactory();
	}
	*/

}
