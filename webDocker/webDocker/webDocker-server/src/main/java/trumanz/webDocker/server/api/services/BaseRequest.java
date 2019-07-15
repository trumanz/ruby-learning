package trumanz.webDocker.server.api.services;

import javax.ws.rs.core.HttpHeaders;
import javax.ws.rs.core.UriInfo;

import trumanz.webDocker.server.api.resources.ResourceInstance;

public abstract class BaseRequest implements Request {

	private UriInfo m_uriInfo;
	private HttpHeaders m_headers;
	private RequestBody m_body;
	private ResourceInstance m_resource;


	public BaseRequest(HttpHeaders headers, RequestBody body, UriInfo uriInfo, ResourceInstance resource) {
		m_headers = headers;
		m_uriInfo = uriInfo;
		m_resource = resource;
		m_body = body;
	}
	/*
	@Override
	public Result process(){
		return null;
	}
	*/
}
