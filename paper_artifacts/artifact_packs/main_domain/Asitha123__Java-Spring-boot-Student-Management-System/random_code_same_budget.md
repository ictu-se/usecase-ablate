# Deterministic random code snippets
### student-management-system/src/main/java/com/studentmgr/common/exception/ServiceException.java
package com.studentmgr.common.exception;

public class ServiceException extends Exception {

	private static final long serialVersionUID = -7796502366163043439L;
	
	public static final String SERVICE_FAILED = "SERVICE_FAILED";
    public static final String DATA_ACCESS_FAILED = "DATA_ACCESS_FAILED";
    
	public ServiceException(Exception exception) {
		super(exception);
	}
    
	public ServiceException(String message, Exception exception) {
		super(message, exception);
	}
	
	public ServiceException(String message) {
		super(message);
	}
	
}

### student-management-system/src/main/java/com/studentmgr/common/exception/ResourceNotFoundException.java
package com.studentmgr.common.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value=HttpStatus.NOT_FOUND)  //404
public class ResourceNotFoundException extends RuntimeException{

	private static final long serialVersionUID = -2217466109027636423L;

	public ResourceNotFoundException() {
	}
	
	public ResourceNotFoundException(String message){
		super(message);
	}
}

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

### student-management-system/src/main/java/com/studentmgr/common/model/Sequence.java
package com.studentmgr.common.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection="Sequence")
public class Sequence {

	@Id
	private String id;

	private int seq;

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public int getSeq() {
		return seq;
	}

	public void setSeq(int seq) {
		this.seq = seq;
	}
}

### student-management-system/src/main/java/com/studentmgr/common/exception/ListenerTypeNotFound.java
package com.studentmgr.common.exception;

import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(reason="ListenerType Not Found")  //500
public class ListenerTypeNotFound extends RuntimeException{

	/**
	 * 
	 */
	private static final long serialVersionUID = -6747852635122018488L;

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

### student-management-system/src/main/java/com/studentmgr/model/Room.java
package com.studentmgr.model;

import org.springframework.data.mongodb.core.mapping.Document;

import com.studentmgr.common.model.EntityBase;

@Document(collection = "Room")
public class Room extends EntityBase{

}

### student-management-system/src/main/java/com/studentmgr/dao/MeetingDao.java
package com.studentmgr.dao;

import com.studentmgr.common.dao.GenericDao;
import com.studentmgr.model.Meeting;

public interface MeetingDao extends GenericDao<Meeting>{
}

### student-management-system/src/main/java/com/studentmgr/common/dao/SequenceDao.java
package com.studentmgr.common.dao;

import com.studentmgr.common.exception.DataAccessException;
import com.studentmgr.common.model.Sequence;

public interface SequenceDao  extends GenericDao<Sequence>{

	Integer getNextSequenceId(String key) throws DataAccessException;
	Integer getNextSequenceId(String key, Integer start) throws DataAccessException;
	
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

### student-management-system/src/main/java/com/studentmgr/common/response/CommonResponse.java
package com.studentmgr.common.response;

public class CommonResponse {

	private int status;
	private Object message;
	
	public CommonResponse(int status, Object message) {
		this.status = status;
		this.message = message;
	}
	public int getStatus() {
		return status;
	}
	public void setStatus(int status) {
		this.status = status;
	}
	public Object getMessage() {
		return message;
	}
	public void setMessage(Object message) {
		this.message = message;
	}
	
	
	
}

### student-management-system/src/main/java/com/studentmgr/common/exception/UnauthorizedAccessException.java
package com.studentmgr.common.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value=HttpStatus.UNAUTHORIZED)  //400
public class UnauthorizedAccessException extends RuntimeException{

	/**
	 * 
	 */
	private static final long serialVersionUID = -878810853364598782L;

	public UnauthorizedAccessException() {
	}
	
	public UnauthorizedAccessException(String message) {
		super(message);
	}
}

### student-management-system/src/main/java/com/studentmgr/service/StudentService.java
package com.studentmgr.service;

import com.studentmgr.common.service.GenericService;
import com.studentmgr.model.Student;

public interface StudentService extends GenericService<Student>{
	
}

### student-management-system/src/main/java/com/studentmgr/common/exception/RequiredFieldMissingException.java
package com.studentmgr.common.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value=HttpStatus.BAD_REQUEST)  //400
public class RequiredFieldMissingException extends RuntimeException {

	private static final long serialVersionUID = 3582955683863543348L;
	
	public RequiredFieldMissingException(Object... fields) {
		super(String.format("Required Field Missing [%s]", fields));
	}

}

### student-management-system/src/main/java/com/studentmgr/common/service/GenericService.java
package com.studentmgr.common.service;

import java.util.List;

import com.studentmgr.common.exception.DataAccessException;
import com.studentmgr.common.exception.ServiceException;

public interface GenericService<T>{

	T getById(Object id) throws ServiceException;

	T add(T obj) throws ServiceException;

	T edit(T obj) throws ServiceException;

	boolean delete(T object) throws ServiceException;

	List<T> getAll() throws ServiceException;
    
    ServiceException translateException(DataAccessException de);
    
}

### student-management-system/src/main/java/com/studentmgr/common/exception/BadRequestException.java
package com.studentmgr.common.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value=HttpStatus.BAD_REQUEST, reason="Bad Request")  //400
public class BadRequestException extends RuntimeException{

	private static final long serialVersionUID = -6659322898478118584L;

	public BadRequestException() {
	}
	
	public BadRequestException(String message) {
		super(message);
	}
	
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

### student-management-system/src/main/java/com/studentmgr/common/sse/ListenerType.java
package com.studentmgr.common.sse;

public enum ListenerType {
	
	USER,
	ITEM,
	ITEM_TYPES;
	
	public String prepareKey(String id){
		return this.name() + "-" + id;
	}
}

### student-management-system/src/main/java/com/studentmgr/model/Meeting.java
package com.studentmgr.model;

import org.springframework.data.mongodb.core.mapping.DBRef;
import org.springframework.data.mongodb.core.mapping.Document;

import com.studentmgr.common.model.EntityBase;

@Document(collection = "Meeting")
public class Meeting extends EntityBase{

	private String title;
	
	private String date;
	
	@DBRef
	private Room room;

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getDate() {
		return date;
	}

	public void setDate(String date) {
		this.date = date;
	}

	public Room getRoom() {
		return room;
	}

	public void setRoom(Room room) {
		this.room = room;
	}
	
}

### student-management-system/src/main/java/com/studentmgr/service/RoomService.java
package com.studentmgr.service;

import com.studentmgr.common.service.GenericService;
import com.studentmgr.model.Room;

public interface RoomService extends GenericService<Room>{
	
}

### student-management-system/src/main/java/com/studentmgr/model/Student.java
package com.studentmgr.model;

import org.springframework.data.mongodb.core.mapping.Document;

import com.studentmgr.common.model.EntityBase;

@Document(collection = "Student")
public class Student extends EntityBase {

	public static final String GENDER_MALE = "male";
	public static final String GENDER_FEMALE = "female";

	private String name;

	private int sid;

	private String gender;

	private String address;

	private String contactNo;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getSid() {
		return sid;
	}

	public void setSid(int sid) {
		this.sid = sid;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public String getContactNo() {
		return contactNo;
	}

	public void setContactNo(String contactNo) {
		this.contactNo = contactNo;
	}

}