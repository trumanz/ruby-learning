package trumanz.webDocker.server.api.services;

import javax.ws.rs.core.HttpHeaders;
import javax.ws.rs.core.UriInfo;

import trumanz.webDocker.server.api.resources.ResourceInstance;

public class GetRequest extends BaseRequest {
	
	public GetRequest(HttpHeaders headers, RequestBody body, UriInfo uriInfo, ResourceInstance resource) {
	    super(headers, body, uriInfo, resource);
	}

}
