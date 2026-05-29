# README-derived retrieval query
AdityaKshettri Student Database Management System using JAVA Spring Boot ## README.md
# Student-Database-Management-System-using-JAVA-Spring-Boot
In this project, I have worked on a Database Management System for Students where they can manage their courses, reviews and passport details using Spring Boot Web Platform. .mvn/wrapper/MavenWrapperDownloader.java
.mvn/wrapper/maven-wrapper.properties
README.md
pom.xml
src/main/java/studentdbms/StudentDBMSApplication.java
src/main/java/studentdbms/controller/CourseController.java
src/main/java/studentdbms/controller/PassportController.java
src/main/java/studentdbms/controller/ReviewController.java
src/main/java/studentdbms/controller/StudentController.java
src/main/java/studentdbms/entity/Course.java
src/main/java/studentdbms/entity/Passport.java
src/main/java/studentdbms/entity/Review.java
src/main/java/studentdbms/entity/Student.java
src/main/java/studentdbms/repository/CourseRepository.java
src/main/java/studentdbms/repository/PassportRepository.java
src/main/java/studentdbms/repository/ReviewRepository.java
src/main/java/studentdbms/repository/StudentRepository.java
src/main/java/studentdbms/service/CourseService.java
src/main/java/studentdbms/service/PassportService.java
src/main/java/studentdbms/service/ReviewService.java
src/main/java/studentdbms/service/StudentService.java
src/main/resources/application.properties
src/test/java/JavaRestMaster/JavaRestMasterApplicationTests.java

# BM25 selected code snippets
### README.md
# Student-Database-Management-System-using-JAVA-Spring-Boot
In this project, I have worked on a Database Management System for Students where they can manage their courses, reviews and passport details using Spring Boot Web Platform.

### .mvn/wrapper/MavenWrapperDownloader.java
/*
 * Copyright 2007-present the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.net.*;
import java.io.*;
import java.nio.channels.*;
import java.util.Properties;

public class MavenWrapperDownloader {

    private static final String WRAPPER_VERSION = "0.5.6";
    /**
     * Default URL to download the maven-wrapper.jar from, if no 'downloadUrl' is provided.
     */
    private static final String DEFAULT_DOWNLOAD_URL = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/"
        + WRAPPER_VERSION + "/maven-wrapper-" + WRAPPER_VERSION + ".jar";

    /**
     * Path to the maven-wrapper.properties file, which might contain a downloadUrl property to
     * use instead of the default one.
     */
    private static final String MAVEN_WRAPPER_PROPERTIES_PATH =
            ".mvn/wrapper/maven-wrapper.properties";

    /**
     * Path where the maven-wrapper.jar will be saved to.
     */
    private static final String MAVEN_WRAPPER_JAR_PATH =
            ".mvn/wrapper/maven-wrapper.jar";

    /**
     * Name of the property which should be used to override the default download url for the wrapper.
     */
    private static final String PROPERTY_NAME_WRAPPER_URL = "wrapperUrl";

    public static void main(String args[]) {
        System.out.println("- Downloader started");
        File baseDirectory = new File(args[0]);
        System.out.println("- Using base directory: " + baseDirectory.getAbsolutePath());

        // If the maven-wrapper.properties exists, read it and check if it contains a custom
        // wrapperUrl parameter.
        File mavenWrapperPropertyFile = new File(baseDirectory, MAVEN_WRAPPER_PROPERTIES_PATH);
        String url = DEFAULT_DOWNLOAD_URL;
        if(mavenWrapperPropertyFile.exists()) {
            FileInputStream mavenWrapperPropertyFileInputStream = null;
            try {
                mavenWrapperPropertyFileInputStream = new FileInputStream(mavenWrapperPropertyFile);
                Properties mavenWrapperProperties = new Properties();
                mavenWrapperP
...[truncated]...

### pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.3.0.RELEASE</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>StudentDBMS</groupId>
	<artifactId>StudentDBMS</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>StudentDBMS</name>
	<description>StudentDBMS</description>

	<properties>
		<java.version>1.8</java.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-actuator</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-jpa</artifactId>
		</dependency>
		
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-thymeleaf</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-devtools</artifactId>
			<scope>runtime</scope>
			<optional>true</optional>
		</dependency>
		<dependency>
			<groupId>com.h2database</groupId>
			<artifactId>h2</artifactId>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
			<exclusions>
				<exclusion>
					<groupId>org.junit.vintage</groupId>
					<artifactId>junit-vintage-engine</artifactId>
				</exclusion>
			</exclusions>
		</dependency>
		<dependency>
			<groupId>org.springframework.security</groupId>
			<artifactId>spring-security-test</artifactId>
			<scope>test</scope>
		</dependency>
	</dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>

</project>

### src/main/java/studentdbms/StudentDBMSApplication.java
package studentdbms;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import studentdbms.entity.Course;
import studentdbms.entity.Student;
import studentdbms.service.CourseService;
import studentdbms.service.StudentService;

@SpringBootApplication
public class StudentDBMSApplication implements CommandLineRunner
{
	@Autowired
	private StudentService studentService;
	
	@Autowired
	private CourseService courseService;
	
	public static void main(String[] args) {
		SpringApplication.run(StudentDBMSApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception 
	{
		Student student = new Student("Aditya");
		studentService.save(student);
		Course course = new Course("Spring Boot");
		courseService.save(course);
		student.addCourse(course);
		studentService.save(student);
		course.addStudent(student);
		courseService.save(course);
	}

}

### src/main/java/studentdbms/controller/PassportController.java
package studentdbms.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import studentdbms.entity.Passport;
import studentdbms.entity.Student;
import studentdbms.service.PassportService;
import studentdbms.service.StudentService;

@Controller
@RequestMapping("/passports")
public class PassportController 
{
	@Autowired
	private StudentService studentService;
	
	@Autowired
	private PassportService passportService;
	
	@GetMapping("/add")
	public String add(Model model, @RequestParam("id") int id)
	{
		Passport thePassport = new Passport();
		model.addAttribute("thePassport", thePassport);
		model.addAttribute("id", id);
		return "passport-form";
	}
	
	@PostMapping("/save")
	public String save(@RequestParam("id") int id, @ModelAttribute("thePassport") Passport thePassport)
	{
		Student student = studentService.findById(id);
		thePassport.setStudent(student);
		passportService.save(thePassport);
		student.setPassport(thePassport);
		studentService.save(student);
		return "redirect:/students";
	}
	
}

### src/main/java/studentdbms/controller/StudentController.java
package studentdbms.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import studentdbms.entity.Course;
import studentdbms.entity.Student;
import studentdbms.service.CourseService;
import studentdbms.service.StudentService;

@Controller
@RequestMapping("/students")
public class StudentController 
{
	@Autowired
	private StudentService studentService;
	
	@Autowired
	private CourseService courseService;
	
	@GetMapping("")
	public String findAll(Model model)
	{
		List<Student> students = studentService.findAll();
		model.addAttribute("students", students);
		return "student-list";
	}
	
	@GetMapping("/add")
	public String add(Model model)
	{
		Student theStudent = new Student();
		model.addAttribute("theStudent", theStudent);
		return "student-form";
	}
	
	@PostMapping("/save")
	public String save(@ModelAttribute("theStudent") Student theStudent)
	{
		studentService.save(theStudent);
		return "redirect:/students";
	}
	
	@GetMapping("/{id}/courses")
	public String viewCourses(@PathVariable("id") int id, Model model)
	{
		Student student = studentService.findById(id);
		List<Course> courses = student.getCourses();
		if(courses.isEmpty()) {
			return "redirect:/students/" + id + "/addCourses";
		}
		model.addAttribute("remove_id", id);
		model.addAttribute("courses", courses);
		return "course-list";
	}
	
	@GetMapping("/{id}/addCourses")
	public String addCourses(@PathVariable("id") int id, Model model)
	{
		List<Course> studentCourses = studentService.findById(id).getCourses();
		List<Course> courses = courseService.findAll();
		List<Course> remainingCourses = new ArrayList<Course>();
		for(Course c: courses)
		{
			if(!studentCourses.contains(c)) {
				remainingCourses.add(c);
			}
		}
		model.addAttribute("courses", remainingCourses);
		model.addAttribute("add_id", id);
		return "course-list";
	}
	
	@GetMapping("/{sid}/addCourse")
	public String addCourse(@PathVariable("sid") int sid, @RequestParam("cid") int cid)
	{
		Student student = studentService.findById(sid);
		Course course = courseService.findById(cid);
		student.addCourse(cour
...[truncated]...

### src/main/java/studentdbms/controller/ReviewController.java
package studentdbms.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import studentdbms.entity.Course;
import studentdbms.entity.Review;
import studentdbms.service.CourseService;
import studentdbms.service.ReviewService;

@Controller
@RequestMapping("/reviews")
public class ReviewController 
{
	@Autowired
	private ReviewService reviewService;
	
	@Autowired
	private CourseService courseService;
	
	@GetMapping("/add")
	public String add(Model model, @RequestParam("id") int id)
	{
		Review theReview = new Review();
		model.addAttribute("theReview", theReview);
		model.addAttribute("id", id);
		return "review-form";
	}
	
	@PostMapping("/save")
	public String save(@ModelAttribute("theReview") Review theReview, @RequestParam("id") int id)
	{
		Course course = courseService.findById(id);
		theReview.setCourse(course);
		reviewService.save(theReview);
		course.addReview(theReview);
		courseService.save(course);
		return "redirect:/courses/"+id;
	}
	
	@GetMapping("/remove")
	public String remove(@RequestParam("id") int id, @RequestParam("cid") int cid)
	{
		Course course = courseService.findById(cid);
		Review review = reviewService.findById(id);
		course.removeReview(review);
		courseService.save(course);
		reviewService.remove(review);
		return "redirect:/courses/"+cid;
	}
}

### src/main/java/studentdbms/controller/CourseController.java
package studentdbms.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import studentdbms.entity.Course;
import studentdbms.entity.Review;
import studentdbms.service.CourseService;

@Controller
@RequestMapping("/courses")
public class CourseController 
{
	@Autowired
	private CourseService courseService;
	
	@GetMapping("")
	public String findAll(Model model)
	{
		List<Course> courses = courseService.findAll();
		model.addAttribute("courses", courses);
		return "course-list";
	}
	
	@GetMapping("/{id}")
	public String findById(@PathVariable("id") int id, Model model) 
	{
		Course course = courseService.findById(id);
		model.addAttribute("course", course);
		List<Review> reviews = course.getReviews();
		model.addAttribute("reviews", reviews);
		return "course-detail";
	}
	
	@GetMapping("/add")
	public String add(Model model)
	{
		Course theCourse = new Course();
		model.addAttribute("theCourse", theCourse);
		return "course-form";
	}
	
	@PostMapping("/save")
	public String save(@ModelAttribute("theCourse") Course theCourse)
	{
		courseService.save(theCourse);
		return "redirect:/courses";
	}
	
}

### .mvn/wrapper/maven-wrapper.properties
distributionUrl=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.6.3/apache-maven-3.6.3-bin.zip
wrapperUrl=https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.5.6/maven-wrapper-0.5.6.jar

### src/main/java/studentdbms/service/PassportService.java
package studentdbms.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import studentdbms.entity.Passport;
import studentdbms.repository.PassportRepository;

@Service
public class PassportService 
{
	@Autowired
	private PassportRepository passportRepository;
	
	@Transactional
	public Passport save(Passport passport) {
		return passportRepository.save(passport);
	}
}

### src/main/java/studentdbms/service/StudentService.java
package studentdbms.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import studentdbms.entity.Student;
import studentdbms.repository.StudentRepository;

@Service
public class StudentService
{
	@Autowired
	private StudentRepository studentRepository;
	
	public List<Student> findAll() {
		return studentRepository.findAll();
	}
	
	public Student findById(int id) {
		return studentRepository.findById(id).get();
	}
	
	@Transactional
	public Student save(Student student) {
		return studentRepository.save(student);
	}
}

### src/main/resources/application.properties
spring.h2.console.enabled=true
spring.datasource.url=jdbc:h2:mem:testdb

### src/main/java/studentdbms/service/ReviewService.java
package studentdbms.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import studentdbms.entity.Review;
import studentdbms.repository.ReviewRepository;

@Service
public class ReviewService 
{
	@Autowired
	private ReviewRepository reviewRepository;
	
	public Review findById(int id) {
		return reviewRepository.findById(id).get();
	}
	
	@Transactional
	public Review save(Review review) {
		return reviewRepository.save(review);
	}
	
	@Transactional
	public void remove(Review review) {
		reviewRepository.delete(review);
	}
}

### src/test/java/JavaRestMaster/JavaRestMasterApplicationTests.java
package JavaRestMaster;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class JavaRestMasterApplicationTests {

	@Test
	void contextLoads() {
	}

}

### src/main/java/studentdbms/entity/Course.java
package studentdbms.entity;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.persistence.OneToMany;

import com.fasterxml.jackson.annotation.JsonIgnore;

@Entity
public class Course 
{
	@Id
	@GeneratedValue
	private int id;
	
	@Column(unique = true)
	private String name;
	
	@OneToMany(mappedBy = "course")
	@JsonIgnore
	private List<Review> reviews = new ArrayList<>();
	
	@ManyToMany(mappedBy = "courses")
	@JsonIgnore
	private List<Student> students = new ArrayList<>();
	
	public Course() {}

	public Course(String name) {
		this.name = name;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getId() {
		return id;
	}

	public List<Review> getReviews() {
		return reviews;
	}

	public void addReview(Review review) {
		this.reviews.add(review);
	}
	
	public void removeReview(Review review) {
		this.reviews.remove(review);
	}

	public List<Student> getStudents() {
		return students;
	}

	public void addStudent(Student student) {
		this.students.add(student);
	}
	
	public void removeStudent(Student student) {
		this.students.remove(student);
	}

	@Override
	public String toString() {
		return "Course [id=" + id + ", name=" + name + "]";
	}
	
}

### src/main/java/studentdbms/service/CourseService.java
package studentdbms.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import studentdbms.entity.Course;
import studentdbms.repository.CourseRepository;

@Service
public class CourseService 
{
	@Autowired
	private CourseRepository courseRepository;
	
	public List<Course> findAll() {
		return courseRepository.findAll();
	}
	
	public Course findById(int id) {
		return courseRepository.findById(id).get();
	}
	
	@Transactional
	public Course save(Course course) {
		return courseRepository.save(course);
	}
}

### src/main/java/studentdbms/entity/Student.java
package studentdbms.entity;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;
import javax.persistence.OneToOne;

@Entity
public class Student 
{
	@Id
	@GeneratedValue
	private int id;
	
	@Column
	private String name;
	
	@OneToOne
	private Passport passport;
	
	@ManyToMany
	@JoinTable(name = "STUDENT_COURSE", 
		joinColumns = @JoinColumn(name="STUDENT_ID"), 
		inverseJoinColumns = @JoinColumn(name = "COURSE_ID"))
	private List<Course> courses = new ArrayList<>();

	public Student() {}

	public Student(String name) {
		this.name = name;
	}

	public int getId() {
		return id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Passport getPassport() {
		return passport;
	}

	public void setPassport(Passport passport) {
		this.passport = passport;
	}

	public List<Course> getCourses() {
		return courses;
	}

	public void addCourse(Course course) {
		this.courses.add(course);
	}
	
	public void removeCourse(Course course) {
		this.courses.remove(course);
	}

	public void setId(int id) {
		this.id = id;
	}

	public void setCourses(List<Course> courses) {
		this.courses = courses;
	}

	@Override
	public String toString() {
		return "Student [id=" + id + ", name=" + name + "]";
	}
}

### src/main/java/studentdbms/repository/StudentRepository.java
package studentdbms.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import studentdbms.entity.Student;

@Repository
public interface StudentRepository extends JpaRepository<Student, Integer>
{

}

### src/main/java/studentdbms/repository/PassportRepository.java
package studentdbms.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import studentdbms.entity.Passport;

@Repository
public interface PassportRepository extends JpaRepository<Passport, Integer>
{

}

### src/main/java/studentdbms/entity/Passport.java
package studentdbms.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToOne;

@Entity
public class Passport 
{
	@Id
	@GeneratedValue
	private int id;
	
	@Column(nullable = false, unique = true)
	private String number;
	
	@OneToOne(mappedBy = "passport")
	private Student student;
	
	public Passport() {}

	public Passport(String number) {
		this.number = number;
	}

	public int getId() {
		return id;
	}

	public String getNumber() {
		return number;
	}

	public void setNumber(String number) {
		this.number = number;
	}

	public Student getStudent() {
		return student;
	}

	public void setStudent(Student student) {
		this.student = student;
	}

	@Override
	public String toString() {
		return "Passport [id=" + id + ", number=" + number + "]";
	}
	
}

### src/main/java/studentdbms/repository/ReviewRepository.java
package studentdbms.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import studentdbms.entity.Review;

@Repository
public interface ReviewRepository extends JpaRepository<Review, Integer>
{

}

### src/main/java/studentdbms/repository/CourseRepository.java
package studentdbms.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import studentdbms.entity.Course;

@Repository
public interface CourseRepository extends JpaRepository<Course, Integer>
{
	
}