# Models/services
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

### student-management-system/src/main/java/com/studentmgr/model/Room.java
package com.studentmgr.model;

import org.springframework.data.mongodb.core.mapping.Document;

import com.studentmgr.common.model.EntityBase;

@Document(collection = "Room")
public class Room extends EntityBase{

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

### student-management-system/src/main/java/com/studentmgr/service/RoomService.java
package com.studentmgr.service;

import com.studentmgr.common.service.GenericService;
import com.studentmgr.model.Room;

public interface RoomService extends GenericService<Room>{
	
}

### student-management-system/src/main/java/com/studentmgr/service/MeetingService.java
package com.studentmgr.service;

import com.studentmgr.common.service.GenericService;
import com.studentmgr.model.Meeting;

public interface MeetingService extends GenericService<Meeting>{
	
}

### student-management-system/src/main/java/com/studentmgr/service/StudentService.java
package com.studentmgr.service;

import com.studentmgr.common.service.GenericService;
import com.studentmgr.model.Student;

public interface StudentService extends GenericService<Student>{
	
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

### student-management-system/src/main/java/com/studentmgr/common/model/EntityBase.java
package com.studentmgr.common.model;

import org.springframework.data.annotation.Id;

public abstract class EntityBase{
    
	public static final Integer STATUS_DELETED = -999;
	
    @Id
    private String id;
    
    protected Integer status;

    public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public Integer getStatus() {
		return status;
	}

	public void setStatus(Integer status) {
		this.status = status;
	}

    @Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((id == null) ? 0 : id.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		EntityBase other = (EntityBase) obj;
		if (id == null) {
			if (other.id != null)
				return false;
		} else if (!id.equals(other.id))
			return false;
		return true;
	}

	@Override
    public String toString() {
        return "EntityBase{" +
                "id=" + id +
                '}';
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