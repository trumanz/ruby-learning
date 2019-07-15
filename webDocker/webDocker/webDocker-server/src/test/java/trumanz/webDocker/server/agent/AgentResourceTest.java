package trumanz.webDocker.server.agent;

import java.util.Set;

import javax.ws.rs.client.Entity;
import javax.ws.rs.core.Application;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.apache.log4j.Logger;
import org.glassfish.jersey.client.ClientConfig;
import org.glassfish.jersey.jackson.JacksonFeature;
import org.glassfish.jersey.server.ResourceConfig;
import org.glassfish.jersey.test.JerseyTest;
import org.glassfish.jersey.test.TestProperties;
import org.junit.Test;
import org.mockito.Mockito;

import com.google.gson.JsonObject;
import com.google.inject.AbstractModule;
import com.google.inject.Guice;
import com.google.inject.Injector;

import trumanz.webDocker.server.WebDockerException;
import trumanz.webDocker.server.agent.rest.AgentResource;

import org.junit.Assert;

public class AgentResourceTest extends JerseyTest {
	private static String PACKAGE_NAME = "trumanz.webDocker.server.agent.rest";
	private static Logger logger = Logger.getLogger(AgentResourceTest.class);
	
	@Override
	protected Application configure(){
		enable(TestProperties.DUMP_ENTITY);
		enable(TestProperties.LOG_TRAFFIC);
		
		Application application = new ResourceConfig().packages(PACKAGE_NAME)
				.register(MyObjectMapperProvider.class)
				.register(JacksonFeature.class);
		 Set<Class<?>>  classes = application.getClasses();
		 for(Class<?> c : classes){
			 logger.info(c.getName());
		 }
		 return application;
	}
	
	@Override
	protected void configureClient(ClientConfig config)
	{
		//config.register(providerClass)
		
	}
	
	Injector injector = Guice.createInjector(new MyModule());
	
	@Test
	public void agentRegistration() {
		
		//RegistrationResponse response = null;
		
		JsonObject jsonObject = createDummyJSONRegister();
		
		Response response  = target("register/dummyhost").request()
				.accept(MediaType.APPLICATION_JSON)
				.post(Entity.entity(jsonObject.toString(), MediaType.APPLICATION_JSON_TYPE), 
						Response.class);
		Assert.assertEquals(200, response.getStatus());
	
		
		//Assert.assertEquals(response.getResponseStatus(), RegistrationStatus.OK);
		 
	}



	private JsonObject createDummyJSONRegister(){
		JsonObject json =  new  JsonObject();
		json.addProperty("hostName", "dummyHost");
		return json;
	}
	
	
	public static class MyModule extends AbstractModule {

		@Override
		protected void configure() {
			RegistrationResponse regResponse = new RegistrationResponse();
			HeartBeatHandler handler = Mockito.mock(HeartBeatHandler.class); 
			
			try {
				Mockito.when(handler.handleRegistration(org.mockito.Matchers.any(Register.class)))
				.thenReturn(regResponse);
			} catch (WebDockerException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			bind(HeartBeatHandler.class).toInstance(handler);
			
			this.requestStaticInjection(AgentResource.class);
		}
		
	}
}
