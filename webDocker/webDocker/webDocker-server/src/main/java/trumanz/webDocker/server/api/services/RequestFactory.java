package trumanz.webDocker.server.api.services;

import javax.ws.rs.core.HttpHeaders;
import javax.ws.rs.core.UriInfo;

import trumanz.webDocker.server.api.resources.ResourceInstance;

public class RequestFactory {
	public Request createRequst(HttpHeaders headers, RequestBody body, UriInfo uriInfo, Request.Type requestType,
            ResourceInstance resource) {
		switch(requestType){
		case DELETE:
			break;
		case GET:
			return new GetRequest(headers, body, uriInfo, resource);
		case POST:
			break;
		case PUT:
			break;
		case QUERY_POST:
			break;
		default:
			break;
		
		}
		return null;
	}

}
