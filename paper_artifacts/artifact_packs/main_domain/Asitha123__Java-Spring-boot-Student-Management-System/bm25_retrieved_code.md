# README-derived retrieval query
Asitha123 Java Spring boot Student Management System ## README.md
# Java-Spring-boot-Student-Management-System

Command-line Instructions

Prerequisites:

•	Install the latest version of Java and Maven.


Eclipse Instructions

Prerequisites:

•	Install Eclipse, the Maven plugin, and optionally the GitHub plugin.
•	Set up Eclipse Preferences

•	Window > Preferences... (or on Mac, Eclipse > Preferences...)

Select Maven

•	check on "Download Artifact Sources"
•	check on "Download Artifact JavaDoc"



Run

•	Right-click on project
•	Run As > Java Application
•	If asked, type "student-management-system" and click OK

Database
•	MongoDB README.md
student-management-system/pom.xml
student-management-system/src/main/java/com/studentmgr/App.java
student-management-system/src/main/java/com/studentmgr/common/dao/GenericDao.java
student-management-system/src/main/java/com/studentmgr/common/dao/SequenceDao.java
student-management-system/src/main/java/com/studentmgr/common/dao/impl/GenericDaoImpl.java
student-management-system/src/main/java/com/studentmgr/common/dao/impl/SequenceDaoImpl.java
student-management-system/src/main/java/com/studentmgr/common/exception/BadRequestException.java
student-management-system/src/main/java/com/studentmgr/common/exception/DataAccessException.java
student-management-system/src/main/java/com/studentmgr/common/exception/DuplicateEmailRegisteredException.java
student-management-system/src/main/java/com/studentmgr/common/exception/ListenerTypeNotFound.java
student-management-system/src/main/java/com/studentmgr/common/exception/OldPasswordNotMatch.java
student-management-system/src/main/java/com/studentmgr/common/exception/RequiredFieldMissingException.java
student-management-system/src/main/java/com/studentmgr/common/exception/ResourceNotFoundException.java
student-management-system/src/main/java/com/studentmgr/common/exception/ServiceException.java
student-management-system/src/main/java/com/studentmgr/common/exception/UnauthorizedAccessException.java
student-management-system/src/main/java/com/studentmgr/common/messages/ErrorMessage.java
student-management-system/src/main/java/com/studentmgr/common/messages/InfoMessage.java
student-management-system/src/main/java/com/studentmgr/common/model/EntityBase.java
student-management-system/src/main/java/com/studentmgr/common/model/Sequence.java
student-management-system/src/main/java/com/studentmgr/common/response/CommonResponse.java
student-management-system/src/main/java/com/studentmgr/common/service/GenericService.java
student-management-system/src/main/java/com/studentmgr/common/service/impl/GenericServiceImpl.java
student-management-system/src/main/java/com/studentmgr/common/sse/ListenerType.java
student-management-system/src/main/java/com/studentmgr/common/sse/SseEmitterApplicationEventListener.java
student-management-system/src/main/java/com/studentmgr/common/sse/SubmissionEvent.java
student-management-system/src/main/java/com/studentmgr/config/AppConfiguration.java
student-management-system/src/main/java/com/studentmgr/config/SetupRoom.java
student-management-system/src/main/java/com/studentmgr/controller/TemplateController.java
student-management-system/src/main/java/com/studentmgr/dao/MeetingDao.java
student-management-system/src/main/java/com/studentmgr/dao/RoomDao.java
student-management-system/src/main/java/com/studentmgr/dao/StudentDao.java
student-management-system/src/main/java/com/studentmgr/dao/impl/MeetingDaoImpl.java
student-management-system/src/main/java/com/studentmgr/dao/impl/RoomDaoImpl.java
student-management-system/src/main/java/com/studentmgr/dao/impl/StudentDaoImpl.java
student-management-system/src/main/java/com/studentmgr/model/Meeting.java
student-management-system/src/main/java/com/studentmgr/model/Room.java
student-management-system/src/main/java/com/studentmgr/model/Student.java
student-management-system/src/main/java/com/studentmgr/service/MeetingService.java
student-management-system/src/main/java/com/studentmgr/service/RoomService.java
student-management-system/src/main/java/com/studentmgr/service/StudentService.java
student-management-system/src/main/java/com/studentmgr/service/impl/MeetingServiceImpl.java
student-management-system/src/main/java/com/studentmgr/service/impl/RoomServiceImpl.java
student-management-system/src/main/java/com/studentmgr/service/impl/StudentServiceImpl.java
student-management-system/src/main/resources/_logback.xml
student-management-system/src/main/resources/application.yml
student-management-system/src/test/java/com/thk/homeservice/AppTest.java

# BM25 selected code snippets
### README.md
# Java-Spring-boot-Student-Management-System

Command-line Instructions

Prerequisites:

•	Install the latest version of Java and Maven.


Eclipse Instructions

Prerequisites:

•	Install Eclipse, the Maven plugin, and optionally the GitHub plugin.
•	Set up Eclipse Preferences

•	Window > Preferences... (or on Mac, Eclipse > Preferences...)

Select Maven

•	check on "Download Artifact Sources"
•	check on "Download Artifact JavaDoc"



Run

•	Right-click on project
•	Run As > Java Application
•	If asked, type "student-management-system" and click OK

Database
•	MongoDB

### student-management-system/pom.xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>

	<groupId>com.studentmgr</groupId>
	<artifactId>student-management-system</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<packaging>jar</packaging>

	<name>student-management-system</name>
	<url>http://maven.apache.org</url>

	<properties>
		<!-- versions -->
		<java.version>1.8</java.version>
		<!-- versions -->
		
		<http.port>8080</http.port>
		<mongo.host>localhost</mongo.host>
		<mongo.port>27017</mongo.port>
		<mongo.database>std_mgr_db</mongo.database>
		<mongo.username></mongo.username>
		<mongo.password></mongo.password>
		
	</properties>

	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>1.5.2.RELEASE</version>
	</parent>

	<dependencies>

		<!-- Spring MVC & REST, use Embedded Tomcat -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>

		<!-- Spring Data - Mongo -->
		<dependency>
			<groupId>org.springframework.data</groupId>
			<artifactId>spring-data-mongodb</artifactId>
		</dependency>
		
		<!-- Tomcat embedded container-->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-tomcat</artifactId>
			<scope>provided</scope>
		</dependency>

		<dependency>
			<groupId>javax.servlet</groupId>
			<artifactId>jstl</artifactId>
		</dependency>

		<dependency>
			<groupId>org.apache.tomcat.embed</groupId>
			<artifactId>tomcat-embed-jasper</artifactId>
			<scope>provided</scope>
		</dependency>
		
		<dependency>
			<groupId>org.eclipse.jdt.core.compiler</groupId>
			<artifactId>ecj</artifactId>
			<version>4.6.1</version>
			<scope>provided</scope>
		</dependency>

		<dependency>
			<groupId>org.webjars</groupId>
			<artifactId>bootstrap</artifactId>
			<version>3.3.7</version>
		</dependency>
		
		<!-- Spring - Devtools for refresh server -->
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-devtools</artifactId>
			<optional>true</optional>
		</dependency>
		
		<!-- Logger -->
		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-classic</artifactId>
		</dependency>

		<dependency>
			<groupId>ch.qos.logback</groupId>
			<artifactId>logback-core</artifactId>
		</dependency>
		<!-- Logger -->

		<!-- Testing starter -->
		<dependency>
			<groupId>org.spr
...[truncated]...

### student-management-system/src/main/java/com/studentmgr/service/impl/MeetingServiceImpl.java
package com.studentmgr.service.impl;

import javax.annotation.PostConstruct;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.studentmgr.common.service.impl.GenericServiceImpl;
import com.studentmgr.dao.MeetingDao;
import com.studentmgr.model.Meeting;
import com.studentmgr.service.MeetingService;

@Service
public class MeetingServiceImpl extends GenericServiceImpl<Meeting> implements MeetingService{

	@Autowired
	protected MeetingDao meetingDao;
	
	@PostConstruct
	void init() {
        init(Meeting.class, meetingDao);
    }
	
}

### student-management-system/src/main/java/com/studentmgr/service/impl/RoomServiceImpl.java
package com.studentmgr.service.impl;

import javax.annotation.PostConstruct;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.studentmgr.common.service.impl.GenericServiceImpl;
import com.studentmgr.dao.RoomDao;
import com.studentmgr.model.Room;
import com.studentmgr.service.RoomService;

@Service
public class RoomServiceImpl extends GenericServiceImpl<Room> implements RoomService{

	@Autowired
	protected RoomDao roomDao;
	
	@PostConstruct
	void init() {
        init(Room.class, roomDao);
    }
	
}

### student-management-system/src/main/java/com/studentmgr/service/impl/StudentServiceImpl.java
package com.studentmgr.service.impl;

import javax.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.studentmgr.common.service.impl.GenericServiceImpl;
import com.studentmgr.dao.StudentDao;
import com.studentmgr.model.Student;
import com.studentmgr.service.StudentService;

@Service
public class StudentServiceImpl extends GenericServiceImpl<Student> implements StudentService{

	@Autowired
	protected StudentDao studentDao;
	
	@PostConstruct
	void init() {
        init(Student.class, studentDao);
    }
	
}

### student-management-system/src/main/java/com/studentmgr/common/service/impl/GenericServiceImpl.java
package com.studentmgr.common.service.impl;

import java.util.List;

import com.studentmgr.common.dao.GenericDao;
import com.studentmgr.common.exception.DataAccessException;
import com.studentmgr.common.exception.ServiceException;
import com.studentmgr.common.service.GenericService;

public class GenericServiceImpl<T> implements GenericService<T> {
	
	@SuppressWarnings("unused")
	private Class<? extends T> type;
	protected GenericDao<T> genericDao;
	
	protected void init(Class<? extends T> type, GenericDao<T> dao) {
        this.type = type;
        this.genericDao = dao;
    }
	
	@Override
	public T getById(Object id) throws ServiceException{
		try{
			return genericDao.getById(id);
		}catch(DataAccessException de){
			throw translateException(de);
		}
	}
	
	@Override
	public List<T> getAll() throws ServiceException{
		try{
			return genericDao.getAll();
		}catch(DataAccessException de){
			throw translateException(de);
		}
	}

	@Override
	public T add(T obj) throws ServiceException{
		try{
			genericDao.add(obj);
			return obj;
		}catch(DataAccessException de){
			throw translateException(de);
		}
	}

	@Override
	public T edit(T obj) throws ServiceException{
		try{
			genericDao.modify(obj);
			return obj;
		}catch(DataAccessException de){
			throw translateException(de);
		}
	}

	@Override
	public boolean delete(T object) throws ServiceException{
		try{
			genericDao.delete(object);
			return true;
		}catch(DataAccessException de){
			throw translateException(de);
		}
	}

	@Override
	public ServiceException translateException(DataAccessException de) {
		return new ServiceException(de);
	}

}

### student-management-system/src/main/java/com/studentmgr/common/dao/impl/SequenceDaoImpl.java
package com.studentmgr.common.dao.impl;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.data.mongodb.core.FindAndModifyOptions;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.core.query.Update;
import org.springframework.stereotype.Repository;

import com.studentmgr.common.dao.SequenceDao;
import com.studentmgr.common.exception.DataAccessException;
import com.studentmgr.common.model.Sequence;

@Repository
public class SequenceDaoImpl extends GenericDaoImpl<Sequence>implements SequenceDao {

	private static final Logger logger = LoggerFactory.getLogger(SequenceDaoImpl.class);

	public SequenceDaoImpl() {
		super(Sequence.class);
	}

	@Override
	public Integer getNextSequenceId(String key) throws DataAccessException {
		return getNextSequenceId(key, 1);
	}

	@Override
	public Integer getNextSequenceId(String key, Integer start) throws DataAccessException {
		
		if (logger.isDebugEnabled())
			logger.debug("getNextSequenceId {}", key);

		try {
			// get sequence id
			Query query = new Query(Criteria.where("id").is(key));

			// increase sequence id by 1
			Update update = new Update();
			update.inc("seq", 1);

			// return new increased id
			FindAndModifyOptions options = new FindAndModifyOptions();
			options.returnNew(true);

			// this is the magic happened.
			Sequence seqId = mongoOperations.findAndModify(query, update, options, Sequence.class);

			// if no id, throws SequenceException
			// optional, just a way to tell user when the sequence id is failed
			// to
			// generate.
			if (seqId == null) {
				seqId = new Sequence();
				seqId.setId(key);
				seqId.setSeq(start);
				mongoOperations.insert(seqId);
				return start;
			} else {
				return seqId.getSeq();
			}

		} catch (Exception e) {
			throw new DataAccessException(e);
		}
	}

}

### student-management-system/src/test/java/com/thk/homeservice/AppTest.java
package com.thk.homeservice;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class AppTest 
    extends TestCase
{
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( AppTest.class );
    }

    /**
     * Rigourous Test :-)
     */
    public void testApp()
    {
        assertTrue( true );
    }
}

### student-management-system/src/main/java/com/studentmgr/config/SetupRoom.java
package com.studentmgr.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.studentmgr.common.exception.ServiceException;
import com.studentmgr.model.Room;
import com.studentmgr.service.RoomService;

@Component
public class SetupRoom {

	@Autowired
	public SetupRoom(RoomService roomService) {
		
		Room r1 = new Room();
		r1.setId("r1");
		
		Room r2 = new Room();
		r2.setId("r2");
		
		Room r3 = new Room();
		r3.setId("r3");
		
		Room r4 = new Room();
		r4.setId("r4");
		
		try {
			roomService.add(r1);
			roomService.add(r2);
			roomService.add(r3);
			roomService.add(r4);
		} catch (ServiceException e) {
			e.printStackTrace();
		}
		
	}
	
}

### student-management-system/src/main/java/com/studentmgr/dao/impl/MeetingDaoImpl.java
package com.studentmgr.dao.impl;

import org.springframework.stereotype.Repository;

import com.studentmgr.common.dao.impl.GenericDaoImpl;
import com.studentmgr.dao.MeetingDao;
import com.studentmgr.model.Meeting;

@Repository
public class MeetingDaoImpl extends GenericDaoImpl<Meeting> implements MeetingDao {

	public MeetingDaoImpl() {
		super(Meeting.class);
	}
}

### student-management-system/src/main/java/com/studentmgr/dao/impl/RoomDaoImpl.java
package com.studentmgr.dao.impl;

import org.springframework.stereotype.Repository;

import com.studentmgr.common.dao.impl.GenericDaoImpl;
import com.studentmgr.dao.RoomDao;
import com.studentmgr.model.Room;

@Repository
public class RoomDaoImpl extends GenericDaoImpl<Room> implements RoomDao {

	public RoomDaoImpl() {
		super(Room.class);
	}
}

### student-management-system/src/main/resources/application.yml
# Spring properties
spring:
  application:
    name: student-management-system
  mvc:
    view:
      prefix: /WEB-INF/jsp/
      suffix: .jsp
    
# Mongo properties
  data:
    mongodb:
      host: @mongo.host@
      port: @mongo.port@
      database: @mongo.database@


# HTTP Server
server:
  port: @http.port@ # HTTP (Tomcat) port

### student-management-system/src/main/java/com/studentmgr/dao/impl/StudentDaoImpl.java
package com.studentmgr.dao.impl;

import org.springframework.stereotype.Repository;

import com.studentmgr.common.dao.impl.GenericDaoImpl;
import com.studentmgr.dao.StudentDao;
import com.studentmgr.model.Student;

@Repository
public class StudentDaoImpl extends GenericDaoImpl<Student> implements StudentDao {

	public StudentDaoImpl() {
		super(Student.class);
	}
}

### student-management-system/src/main/java/com/studentmgr/App.java
package com.studentmgr;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.web.support.SpringBootServletInitializer;

@SpringBootApplication
public class App extends SpringBootServletInitializer{
	
	@Override
	protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
		return application.sources(App.class);
	}
	
    public static void main( String[] args )
    {
        SpringApplication.run(App.class, args);   
    }
}

### student-management-system/src/main/java/com/studentmgr/common/dao/GenericDao.java
package com.studentmgr.common.dao;

import java.util.List;
import org.springframework.data.mongodb.core.MongoOperations;

import com.studentmgr.common.exception.DataAccessException;

public interface GenericDao<T> {
	/**
	 * This method delete given object from the database.
	 *
	 * @param id
	 *            - Object id to load
	 * @throws DataAccessException
	 *             - throws if an error occurs
	 */
	T getById(Object id) throws DataAccessException;

	/**
	 * This method delete given objects from the database.
	 * 
	 * @param id
	 * @return
	 * @throws DataAccessException
	 */
	List<T> getAllById(Object id) throws DataAccessException;

	/**
	 * This method queries all the objects
	 *
	 * @throws DataAccessException
	 *             - throws if an error occurs
	 */
	List<T> getAll() throws DataAccessException;

	/**
	 * This method delete given object from the database.
	 *
	 * @param object
	 *            - instance of Object class
	 * @throws DataAccessException
	 *             - throws if an error occurs
	 */
	void delete(T object) throws DataAccessException;

	/**
	 * This method insert a given object to the database.
	 *
	 * @param object
	 *            - instance of Object class
	 * @throws DataAccessException
	 *             - throws if an error occurs
	 */
	void add(T object) throws DataAccessException;

	/**
	 * This method update given object in the database.
	 *
	 * @param object
	 *            - instance of Object class
	 * @throws DataAccessException
	 *             - throws if an error occurs
	 */
	void modify(T object) throws DataAccessException;

	MongoOperations getMongoOperations();

}

### student-management-system/src/main/java/com/studentmgr/common/dao/SequenceDao.java
package com.studentmgr.common.dao;

import com.studentmgr.common.exception.DataAccessException;
import com.studentmgr.common.model.Sequence;

public interface SequenceDao  extends GenericDao<Sequence>{

	Integer getNextSequenceId(String key) throws DataAccessException;
	Integer getNextSequenceId(String key, Integer start) throws DataAccessException;
	
}

### student-management-system/src/main/java/com/studentmgr/common/dao/impl/GenericDaoImpl.java
package com.studentmgr.common.dao.impl;

import java.util.List;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.CacheConfig;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.cache.annotation.Caching;
import org.springframework.data.mongodb.core.MongoOperations;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;

import com.studentmgr.common.dao.GenericDao;
import com.studentmgr.common.exception.DataAccessException;

@CacheConfig(cacheResolver="dynamicCacheResolver")
public class GenericDaoImpl<T> implements GenericDao<T> {

	private static final Logger logger = LoggerFactory.getLogger(GenericDaoImpl.class);

	@Autowired
	protected MongoOperations mongoOperations;

	private Class<T> type;

	public GenericDaoImpl(Class<T> type) {
		this.type = type;
	}

	@Override
	@Caching(evict = { 
			@CacheEvict(cacheResolver="dynamicCacheResolver", allEntries = true)
		}
	)
	public void add(T object) throws DataAccessException {
		if (logger.isDebugEnabled())
			logger.debug("type {} add", type);
		try {
			mongoOperations.insert(object);
		} catch (Exception e) {
			throw new DataAccessException(e);
		}
	}

	@Override
	@Caching(evict = { 
			@CacheEvict(cacheResolver="dynamicCacheResolver", allEntries = true), 
			@CacheEvict(cacheResolver="dynamicCacheResolver", key="#object.id") 
		}
	)
	public void modify(T object) throws DataAccessException {
		if (logger.isDebugEnabled())
			logger.debug("type {} modify", type);
		try {
			mongoOperations.save(object);
		} catch (Exception e) {
			throw new DataAccessException(e);
		}
	}

	@Override
	@Cacheable(key="#id")
	public T getById(Object id) throws DataAccessException {
		if (logger.isDebugEnabled())
			logger.debug("type {} getById", type);
		try{
			return mongoOperations.findById(id, type);
		}catch(Exception e){
			throw new DataAccessException(e);
		}
	}
	
	@Override
	@Cacheable(key="#id")
	public List<T> getAllById(Object id) throws DataAccessException {
		if (logger.isDebugEnabled())
			logger.debug("type {} getById", type);
		try{
			return mongoOperations.find(new Query(Criteria.where("id").is(id)), type);
		}catch(Exception e){
			throw new DataAccessException(e);
		}
	}

	@Override
	@Cacheable
	public List<T> getAll() throws DataAccessException {
		if (logger.isDebugEnabled())
			logger.debug("type {} getAll", type);

		try {
			return mongo
...[truncated]...

### student-management-system/src/main/java/com/studentmgr/common/sse/SseEmitterApplicationEventListener.java
package com.studentmgr.common.sse;

import java.io.IOException;
import java.util.Hashtable;
import java.util.Map;
import org.springframework.context.event.EventListener;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.mvc.method.annotation.SseEmitter;

@Component
public class SseEmitterApplicationEventListener {

	@EventListener
    public void submissionEventHandler(SubmissionEvent event) throws IOException {
        
		String key = event.getKey();
        Object message = event.getMessage();
        
        SseEmitter sseEmitter = sseEmitters.get(key);
 
        if ( sseEmitter == null ) {
            return;
        }
        
        sseEmitter.send(message, MediaType.APPLICATION_JSON);
    }
 
    public void addSseEmitters(ListenerType listenerType ,String id, SseEmitter sseEmitter) {
        sseEmitters.put(listenerType.prepareKey(id), sseEmitter);
    }
 
    private static Map<String, SseEmitter> sseEmitters = new Hashtable<>();
	
}

### student-management-system/src/main/java/com/studentmgr/controller/TemplateController.java
package com.studentmgr.controller;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import com.studentmgr.common.exception.ServiceException;
import com.studentmgr.model.Student;
import com.studentmgr.service.StudentService;

@Controller
public class TemplateController {

	private static final Logger LOG = LoggerFactory.getLogger(TemplateController.class);
	
	@Autowired
	private StudentService studentService;
	
	@RequestMapping("/")
	public String listPage(Model model){
		
		List<Student> students = new ArrayList<>();
		try{
			students = studentService.getAll();
		}catch(Exception e){
			LOG.error(e.getMessage());
		}
		
		model.addAttribute("students", students);
		
		return "list";
	}
	
	@RequestMapping("/save")
	public String savePage(@RequestParam(value="q", required=false) String id, Model model) throws ServiceException{
		
		Student student = null;
		if(!StringUtils.isEmpty(id))
			student = studentService.getById(id);
			
		model.addAttribute("genderList", Arrays.asList(Student.GENDER_MALE, Student.GENDER_FEMALE));
		model.addAttribute("student", student);
		return "save";
	}
	
	@RequestMapping(value="/save", method=RequestMethod.POST)
	public String saveBooking(@ModelAttribute Student student) throws ServiceException{
		
		if(StringUtils.isEmpty(student.getId())){
			student.setId(null);
			studentService.add(student);
		}
		else
			studentService.edit(student);
		
		return "redirect:/";
	}
	
	@RequestMapping("/delete")
	public String deleteBooking(@ModelAttribute Student student) throws ServiceException{
		studentService.delete(student);
		return "redirect:/";
	}
	
}

### student-management-system/src/main/java/com/studentmgr/service/MeetingService.java
package com.studentmgr.service;

import com.studentmgr.common.service.GenericService;
import com.studentmgr.model.Meeting;

public interface MeetingService extends GenericService<Meeting>{
	
}

### student-management-system/src/main/java/com/studentmgr/service/RoomService.java
package com.studentmgr.service;

import com.studentmgr.common.service.GenericService;
import com.studentmgr.model.Room;

public interface RoomService extends GenericService<Room>{
	
}

### student-management-system/src/main/java/com/studentmgr/common/sse/SubmissionEvent.java
package com.studentmgr.common.sse;

public class SubmissionEvent {

	private String key;
	private Object message;
	
	public SubmissionEvent(ListenerType type , String id, Object message) {
		this.key = type.prepareKey(id);
		this.message = message;
	}
	public String getKey() {
		return key;
	}
	public void setKey(String key) {
		this.key = key;
	}
	public Object getMessage() {
		return message;
	}
	public void setMessage(Object message) {
		this.message = message;
	}
	
	
	
}