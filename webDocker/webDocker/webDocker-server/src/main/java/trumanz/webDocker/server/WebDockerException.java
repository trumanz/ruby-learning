package trumanz.webDocker.server;

import java.io.IOException;

public class WebDockerException extends IOException {
	public WebDockerException(String message){
		super(message);
	}
}
