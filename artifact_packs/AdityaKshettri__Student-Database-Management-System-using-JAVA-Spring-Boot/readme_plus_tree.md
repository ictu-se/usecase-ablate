# README
## README.md
# Student-Database-Management-System-using-JAVA-Spring-Boot
In this project, I have worked on a Database Management System for Students where they can manage their courses, reviews and passport details using Spring Boot Web Platform.

# File tree
.mvn
  wrapper
    MavenWrapperDownloader.java
    maven-wrapper.properties
README.md
pom.xml
src
  main
    java
      studentdbms
        StudentDBMSApplication.java
        controller
          CourseController.java
          PassportController.java
          ReviewController.java
          StudentController.java
        entity
          Course.java
          Passport.java
          Review.java
          Student.java
        repository
          CourseRepository.java
          PassportRepository.java
          ReviewRepository.java
          StudentRepository.java
        service
          CourseService.java
          PassportService.java
          ReviewService.java
          StudentService.java
    resources
      application.properties
  test
    java
      JavaRestMaster
        JavaRestMasterApplicationTests.java