# Deterministic random code snippets
### src/main/java/org/engripaye/librarymanagementsystem/service/LoanService.java
package org.engripaye.librarymanagementsystem.service;

import jakarta.transaction.Transactional;
import lombok.AllArgsConstructor;
import org.engripaye.librarymanagementsystem.model.AppUser;
import org.engripaye.librarymanagementsystem.model.Book;
import org.engripaye.librarymanagementsystem.model.Loan;
import org.engripaye.librarymanagementsystem.repository.BookRepository;
import org.engripaye.librarymanagementsystem.repository.LoanRepository;
import org.engripaye.librarymanagementsystem.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDate;

@Service
@AllArgsConstructor
public class LoanService {

    private final LoanRepository loanRepository;
    private final UserRepository userRepository;
    private final BookRepository bookRepository;

    @Transactional
    public Loan borrow(Long userId, Long bookId, int days){
        AppUser user = userRepository.findById(userId).orElseThrow();
        Book book = bookRepository.findById(bookId).orElseThrow();

        if(book.getAvailableCopies() == null || book.getAvailableCopies() <= 0)
            throw new IllegalStateException("No Copies Available");

        //prevent duplicate active loan for same user/book
        loanRepository.findByUserAndBookAndReturnedAtIsNull(user, book)
                .ifPresent(I -> {throw new IllegalStateException("User already borrowed this book");});


        book.setAvailableCopies(book.getAvailableCopies() - 1);
        bookRepository.save(book);

        return loanRepository.save(Loan.builder()
                .user(user)
                .book(book)
                .borrowedAt(LocalDate.now())
                .dueAt(LocalDate.now().plusDays(days))
                .build());

    }

    @Transactional
    public Loan returnBook(Long loanId){
        Loan loan = loanRepository.findById(loanId).orElseThrow();
        if(loan.getReturnedAt() != null) return loan;

        Book book = loan.getBook();
        book.setAvailableCopies(book.getAvailableCopies() + 1);
        bookRepository.save(book);

        loan.setReturnedAt(LocalDate.now());
        return loanRepository.save(loan);
    }
}

### src/main/java/org/engripaye/librarymanagementsystem/repository/LoanRepository.java
package org.engripaye.librarymanagementsystem.repository;

import org.engripaye.librarymanagementsystem.model.AppUser;
import org.engripaye.librarymanagementsystem.model.Book;
import org.engripaye.librarymanagementsystem.model.Loan;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface LoanRepository extends JpaRepository<Loan, Long> {
    List<Loan> findByUserId(Long userId);
    Optional<Loan> findByUserAndBookAndReturnedAtIsNull(AppUser user, Book book);
}

### pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.5.5</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>org.engripaye</groupId>
    <artifactId>library-management-system</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>library-management-system</name>
    <description>library-management-system</description>
    <url/>
    <licenses>
        <license/>
    </licenses>
    <developers>
        <developer/>
    </developers>
    <scm>
        <connection/>
        <developerConnection/>
        <tag/>
        <url/>
    </scm>
    <properties>
        <java.version>21</java.version>
        <spring-ai.version>1.0.1</spring-ai.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-starter-model-openai</artifactId>
        </dependency>

        <dependency>
            <groupId>com.mysql</groupId>
            <artifactId>mysql-connector-j</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springdoc</groupId>
            <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
            <version>2.3.0</version>
        </dependency>

    </dependencies>
    <dependencyManagement>
        <dependencies>
      
...[truncated]...

### src/main/java/org/engripaye/librarymanagementsystem/controller/LoanController.java
package org.engripaye.librarymanagementsystem.controller;

import lombok.AllArgsConstructor;
import org.engripaye.librarymanagementsystem.dto.BorrowRequest;
import org.engripaye.librarymanagementsystem.model.Loan;
import org.engripaye.librarymanagementsystem.service.LoanService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/loans")
@AllArgsConstructor
public class LoanController {

    private final LoanService service;

    @PostMapping("/borrow")
    public Loan borrow(@RequestBody BorrowRequest borrowRequest){
        int days = (borrowRequest.days() == null || borrowRequest.days() <= 0) ? 14 : borrowRequest.days();
        return service.borrow(borrowRequest.userId(), borrowRequest.bookId(), days);
    }

    @PostMapping("/{loanId}/return")
    public Loan returnBook(@PathVariable Long loanId){
        return service.returnBook(loanId);
    }
}

### src/main/java/org/engripaye/librarymanagementsystem/config/SwaggerConfig.java
package org.engripaye.librarymanagementsystem.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Contact;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.info.License;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SwaggerConfig {

    @Bean
    public OpenAPI libraryManagementOpenAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("Library Management System API")
                        .description("REST API documentation for the Library Management System project")
                        .version("1.0.0")
                        .contact(new Contact()
                                .name("Ipaye Babatunde")
                                .email("b.tunde.ipaye@gmail.com")
                                .url("https://github.com/engripaye"))
                        .license(new License()
                                .name("Apache 2.0")
                                .url("https://springdoc.org")));
    }
}

### src/main/java/org/engripaye/librarymanagementsystem/service/UserService.java
package org.engripaye.librarymanagementsystem.service;

import lombok.AllArgsConstructor;
import org.engripaye.librarymanagementsystem.model.AppUser;
import org.engripaye.librarymanagementsystem.repository.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@AllArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    public List<AppUser> list(){
        return userRepository.findAll();
    }

    public AppUser create(AppUser create){
        return userRepository.save(create);
    }

    public AppUser get(Long id){
        return userRepository.findById(id).orElseThrow();
    }
}

### src/main/java/org/engripaye/librarymanagementsystem/model/Loan.java
package org.engripaye.librarymanagementsystem.model;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDate;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Loan {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(optional = false)
    private AppUser user;
    @ManyToOne(optional = false)
    private Book book;

    private LocalDate borrowedAt;
    private LocalDate dueAt;
    private LocalDate returnedAt;

    private boolean isActive() {
        return returnedAt == null;
    }
}

### src/main/java/org/engripaye/librarymanagementsystem/service/BookService.java
package org.engripaye.librarymanagementsystem.service;

import lombok.AllArgsConstructor;
import org.engripaye.librarymanagementsystem.model.Book;
import org.engripaye.librarymanagementsystem.repository.BookRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@AllArgsConstructor
public class BookService {

    private final BookRepository bookRepository;

    public List<Book> list(){
        return bookRepository.findAll();
    }

    public Book create(Book book){
        if(book.getAvailableCopies() == null) book.setAvailableCopies(book.getTotalCopies());
        return bookRepository.save(book);
    }

    public List<Book> search(String search){
        if(search == null || search.isBlank()) return bookRepository.findAll();
        var byTitle = bookRepository.findByTitleContainingIgnoreCase(search);
        var byAuthor = bookRepository.findByTitleContainingIgnoreCase(search);
        byAuthor.stream().filter(book -> !byTitle.contains(book)).forEach(byTitle::add);
        return byTitle;
    }

    public Book get(Long id){
        return bookRepository.findById(id).orElseThrow();
    }

}

### src/main/java/org/engripaye/librarymanagementsystem/repository/UserRepository.java
package org.engripaye.librarymanagementsystem.repository;

import org.engripaye.librarymanagementsystem.model.AppUser;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<AppUser, Long> {
}

### src/test/java/org/engripaye/librarymanagementsystem/LibraryManagementSystemApplicationTests.java
package org.engripaye.librarymanagementsystem;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class LibraryManagementSystemApplicationTests {

    @Test
    void contextLoads() {
    }

}

### src/main/java/org/engripaye/librarymanagementsystem/model/AppUser.java
package org.engripaye.librarymanagementsystem.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import lombok.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AppUser {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank private String fullName;

    @Email @Column(unique = true)
    private String email;

}

### src/main/java/org/engripaye/librarymanagementsystem/repository/BookRepository.java
package org.engripaye.librarymanagementsystem.repository;

import org.engripaye.librarymanagementsystem.model.Book;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

public interface BookRepository extends JpaRepository<Book, Long> {
    Optional<Book> findByIsbn(String id);

    List<Book> findByTitleContainingIgnoreCase(String q);
    List<Book> findByAuthorContainingIgnoreCase(String q);
}

### src/main/java/org/engripaye/librarymanagementsystem/dto/BorrowRequest.java
package org.engripaye.librarymanagementsystem.dto;

public record BorrowRequest
        (Long userId,
         Long bookId,
         Integer days) {}

### src/main/java/org/engripaye/librarymanagementsystem/controller/UserController.java
package org.engripaye.librarymanagementsystem.controller;

import lombok.AllArgsConstructor;
import org.engripaye.librarymanagementsystem.model.AppUser;
import org.engripaye.librarymanagementsystem.service.UserService;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping("/api/users")
@AllArgsConstructor
public class UserController {

    private final UserService userService;

    @GetMapping
    public List<AppUser> list(){
        return userService.list();
    }

    @PostMapping
    public AppUser create(@Valid @RequestBody AppUser create) {
        return userService.create(create);
    }

    @GetMapping("/{id}")
    public AppUser get(@PathVariable Long id){
        return userService.get(id);
    }
}

### src/main/java/org/engripaye/librarymanagementsystem/model/Book.java
package org.engripaye.librarymanagementsystem.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotBlank;
import lombok.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Book {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank private String title;
    @NotBlank private String author;

    @Column(unique = true)
    @NotBlank private String isbn;

    private Integer totalCopies;
    private Integer availableCopies;
}

### src/main/java/org/engripaye/librarymanagementsystem/controller/BookController.java
package org.engripaye.librarymanagementsystem.controller;

import lombok.AllArgsConstructor;
import org.engripaye.librarymanagementsystem.model.Book;
import org.engripaye.librarymanagementsystem.service.BookService;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping("/api/books")
@AllArgsConstructor
public class BookController {

    private final BookService service;


    @GetMapping
    public List<Book> list() {
        return service.list();
    }

    @PostMapping
    public Book create(@Valid @RequestBody Book book) {
        return service.create(book);
    }

    @GetMapping("/search")
    public List<Book> search(@RequestParam(required = false) String search){
        return service.search(search);
    }

    @GetMapping("/{id}")
    public Book get(@PathVariable Long id){
        return service.get(id);
    }
}

### src/main/java/org/engripaye/librarymanagementsystem/LibraryManagementSystemApplication.java
package org.engripaye.librarymanagementsystem;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class LibraryManagementSystemApplication {

    public static void main(String[] args) {
        SpringApplication.run(LibraryManagementSystemApplication.class, args);
    }

}