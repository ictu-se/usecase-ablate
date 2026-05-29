# Oracle upper-bound selected context
This condition is selected with checked trace paths and is used only as an upper-bound comparator.

# README
## README.md
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

# File tree
README.md
student-management-system
  pom.xml
  src
    main
      java
        com
          studentmgr
      resources
        _logback.xml
        application.yml
    test
      java
        com
          thk

# Oracle-selected code and test snippets
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

### student-management-system/src/main/java/com/studentmgr/service/StudentService.java
package com.studentmgr.service;

import com.studentmgr.common.service.GenericService;
import com.studentmgr.model.Student;

public interface StudentService extends GenericService<Student>{
	
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

### student-management-system/src/main/java/com/studentmgr/model/Room.java
package com.studentmgr.model;

import org.springframework.data.mongodb.core.mapping.Document;

import com.studentmgr.common.model.EntityBase;

@Document(collection = "Room")
public class Room extends EntityBase{

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