package trumanz.webDocker.server.agent;

public class RegistrationResponse {
	
	private String log;
	private RegistrationStatus responseStatus;

	public String getLog() {
		return log;
	}

	public void setLog(String log) {
		this.log = log;
	}

	public RegistrationStatus getResponseStatus() {
		return responseStatus;
	}

	public void setResponseStatus(RegistrationStatus responseStatus) {
		this.responseStatus = responseStatus;
	}
	

}
