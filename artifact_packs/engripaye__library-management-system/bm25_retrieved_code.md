# README-derived retrieval query
engripaye library management system ## README.md
---

# 📚 Library Management System

A **Java Spring Boot application** designed to manage books, users, and borrowing records efficiently. The system provides **RESTful APIs** for searching books, borrowing, and returning, with **MySQL** as the persistent data store and **JPA/Hibernate** for ORM.

---

## 🚀 Features

* 🔎 **Book Management** – add, update, delete, and search books
* 👤 **User Management** – register and manage library users
* 📖 **Borrowing & Returns** – track borrowed books and return history
* 🗄️ **MySQL Database** – reliable data storage for users and books
* ⚡ **RESTful APIs** – built with **Spring Boot** for easy integration
* 🔗 **JPA/Hibernate ORM** – clean database interactions

---

## 🛠️ Tech Stack

* **Backend:** Java 17+, Spring Boot
* **Database:** MySQL
* **ORM:** JPA/Hibernate
* **Build Tool:** Maven/Gradle
* **Testing:** JUnit, Mockito

---

## 📂 Project Structure

```
library-management-system/
│── src/
│   ├── main/
│   │   ├── java/com/example/library/
│   │   │   ├── controller/     # REST controllers
│   │   │   ├── model/          # Entity classes
│   │   │   ├── repository/     # JPA repositories
│   │   │   ├── service/        # Business logic
│   │   │   └── LibraryApplication.java
│   │   └── resources/
│   │       ├── application.properties  # DB config
│   │       └── data.sql / schema.sql   # Sample data
│   └── test/java/com/example/library/  # Unit tests
│
│── pom.xml       # Maven dependencies
│── README.md     # Documentation
```

---

## ⚡ Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

### 2️⃣ Configure Database

Update **`application.properties`** with your MySQL settings:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/librarydb
spring.datasource.username=root
spring.datasource.password=yourpassword
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

### 3️⃣ Build & Run Application

Using Maven:

```bash
mvn clean install
mvn spring-boot:run
```

App will start at 👉 `http://localhost:8080`

---

## 📡 API Endpoints

### 🔹 Books

* `GET /api/books` → Get all books
* `GET /api/books/{id}` → Get book by ID
* `POST /api/books` → Add new book
* `PUT /api/books/{id}` → Update book details
* `DELETE /api/books/{id}` → Delete a book

### 🔹 Users

* `GET /api/users` → Get all users
* `POST /api/users` → Register new user

### 🔹 Borrowing

* `POST /api/borrow/{bookId}/user/{userId}` → Borrow a book
* `POST /api/return/{bookId}/user/{userId}` → Return a borrowed book

---

## 🧪 Testing

Run unit tests with Maven:

```bash
mvn test
```

---

## 🚀 Future Improvements

* [ ] Add authentication & role-based access control
* [ ] Implement fine calculation for late returns
* [ ] Add reporting/dashboard for admin users
* [ ] Dockerize the application for deployment

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to your branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📜 License

MIT License © 2025 \[Engr. Ipaye Babatunde]

---

Would you like me to also **generate a professional architecture diagram (Java + Spring Boot + MySQL)** image for this README, like I did for your other projects? .mvn/wrapper/maven-wrapper.properties
Docker-compose.yml
README.md
pom.xml
src/main/java/org/engripaye/librarymanagementsystem/LibraryManagementSystemApplication.java
src/main/java/org/engripaye/librarymanagementsystem/config/SwaggerConfig.java
src/main/java/org/engripaye/librarymanagementsystem/controller/BookController.java
src/main/java/org/engripaye/librarymanagementsystem/controller/LoanController.java
src/main/java/org/engripaye/librarymanagementsystem/controller/UserController.java
src/main/java/org/engripaye/librarymanagementsystem/dto/BorrowRequest.java
src/main/java/org/engripaye/librarymanagementsystem/model/AppUser.java
src/main/java/org/engripaye/librarymanagementsystem/model/Book.java
src/main/java/org/engripaye/librarymanagementsystem/model/Loan.java
src/main/java/org/engripaye/librarymanagementsystem/repository/BookRepository.java
src/main/java/org/engripaye/librarymanagementsystem/repository/LoanRepository.java
src/main/java/org/engripaye/librarymanagementsystem/repository/UserRepository.java
src/main/java/org/engripaye/librarymanagementsystem/service/BookService.java
src/main/java/org/engripaye/librarymanagementsystem/service/LoanService.java
src/main/java/org/engripaye/librarymanagementsystem/service/UserService.java
src/main/resources/application.yaml
src/test/java/org/engripaye/librarymanagementsystem/LibraryManagementSystemApplicationTests.java

# BM25 selected code snippets
### README.md
---

# 📚 Library Management System

A **Java Spring Boot application** designed to manage books, users, and borrowing records efficiently. The system provides **RESTful APIs** for searching books, borrowing, and returning, with **MySQL** as the persistent data store and **JPA/Hibernate** for ORM.

---

## 🚀 Features

* 🔎 **Book Management** – add, update, delete, and search books
* 👤 **User Management** – register and manage library users
* 📖 **Borrowing & Returns** – track borrowed books and return history
* 🗄️ **MySQL Database** – reliable data storage for users and books
* ⚡ **RESTful APIs** – built with **Spring Boot** for easy integration
* 🔗 **JPA/Hibernate ORM** – clean database interactions

---

## 🛠️ Tech Stack

* **Backend:** Java 17+, Spring Boot
* **Database:** MySQL
* **ORM:** JPA/Hibernate
* **Build Tool:** Maven/Gradle
* **Testing:** JUnit, Mockito

---

## 📂 Project Structure

```
library-management-system/
│── src/
│   ├── main/
│   │   ├── java/com/example/library/
│   │   │   ├── controller/     # REST controllers
│   │   │   ├── model/          # Entity classes
│   │   │   ├── repository/     # JPA repositories
│   │   │   ├── service/        # Business logic
│   │   │   └── LibraryApplication.java
│   │   └── resources/
│   │       ├── application.properties  # DB config
│   │       └── data.sql / schema.sql   # Sample data
│   └── test/java/com/example/library/  # Unit tests
│
│── pom.xml       # Maven dependencies
│── README.md     # Documentation
```

---

## ⚡ Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

### 2️⃣ Configure Database

Update **`application.properties`** with your MySQL settings:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/librarydb
spring.datasource.username=root
spring.datasource.password=yourpassword
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

### 3️⃣ Build & Run Application

Using Maven:

```bash
mvn clean install
mvn spring-boot:run
```

App will start at 👉 `http://localhost:8080`

---

## 📡 API Endpoints

### 🔹 Books

* `GET /api/books` → Get all books
* `GET /api/books/{id}` → Get book by ID
* `POST /api/books` → Add new book
* `PUT /api/books/{id}` → Update book details
* `DELETE /api/books/{id}` → Delete a book

### 🔹 Users

* `GET /api/users` → Get all users
* `POST /api/users` → Register new user

### 🔹 Borrowing

* `POST /api/borrow/{bookId}/user/{userId}` → Borrow a book
* `POST /api/return/{bookId}/user/{userId}` → Return a borrowed book

---

## 🧪
...[truncated]...

### src/main/resources/application.yaml
spring:
  datasource:
    url: mysql://localhost:3307/library_db?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC
    username: root
    password: 1234567

  jpa:
    hibernate:
      ddl-auto: update
    show-sql: true
    properties:
      hibernate:
        format_sql: true

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

### .mvn/wrapper/maven-wrapper.properties
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
wrapperVersion=3.3.2
distributionType=only-script
distributionUrl=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.9.11/apache-maven-3.9.11-bin.zip

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

### Docker-compose.yml
services:
  mysql:
    image: mysql:8.0
    container_name: library_mysql
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: library_db
      MYSQL_USER: root
      MYSQL_PASSWORD: 1234567
    ports:
      - "3307:3306"
    volumes:
      - mysql_data:/var/lib/mysql
    command: --default-authentication-plugin=caching_sha2_password
  volumes:
    mysql_data:

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

### src/main/java/org/engripaye/librarymanagementsystem/repository/UserRepository.java
package org.engripaye.librarymanagementsystem.repository;

import org.engripaye.librarymanagementsystem.model.AppUser;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<AppUser, Long> {
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

### src/main/java/org/engripaye/librarymanagementsystem/dto/BorrowRequest.java
package org.engripaye.librarymanagementsystem.dto;

public record BorrowRequest
        (Long userId,
         Long bookId,
         Integer days) {}

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