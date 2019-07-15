package trumanz.webDocker.server.api.services;

public interface Request {
	public enum Type{
		GET,
		POST,
		PUT,
		DELETE,
		QUERY_POST
	}

}
