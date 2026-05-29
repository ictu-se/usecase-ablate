# README-derived retrieval query
knowledgefactory4u librarymanagementsystem ## README.md
# Java, Spring Boot Mini Project - Library Management System


# Local setup

Step 1: Download or clone the source code from GitHub to the local machine

Step 2: Install JDK 17 - https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html

Step 3: Install IntelliJ IDEA or Eclipse or Apache NetBeans IDE

Step 4: Install Apache Maven - https://maven.apache.org/install.html

Step 5:  ```mvn clean install```

Step 6:  ```mvn spring-boot:run```

Step 7: From the browser call the endpoint http://localhost:9080

Step 8: Admin Login User Id: ```admin@admin.in``` & Password: ```Temp123```


# Admin Login Interface

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiuctxupeOK4Nh8j-nomwwapjkcVvkYig3lX7qoifcXE76_6CnOXMZ-CLww7G180qegsCkrtyUlaqpJsWm9GzhX9QUFxyNyEUAXFD5UWJpvh2BdIr0wyAnFC38QOdsL_1vak8LtxYHrZyplCU_Sri-7kM9nXxI9heXXB0621rzJgL6j1CSweX6xjaorg/s945/admin-login.png">

# Add new books, update books, view books, delete books

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYMpuCQx3lGsS4T_H4ziyDWIkBpYV5qgo5JHFMV0Drper48H7YfygEdv0htE3yWo8mlypUW9W7NFY00UtrVznFfFYIzNGAXBeskhBb_kHAJrVKnI7O5mZt0_c085n6ir-cNVEYsTYffn6WgCmoBiZULR88ah_YxDC-ywRKPTsxj58GcHFnyyeX00RsNA/s800/library-management-system.png">

# Add new authors, update authors, view authors, delete authors

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixAW5k4E9IXf_OuVO1S5m100KS1xFo2ZrFoLnZYvNLjfpmIdI8W0ukd6yQn6oTsSWBKjDdAIGsnPf0EhgRwKzfpVq3mJXMcqG94Qp2oCCy0Pzf01b3kXP2ahgbvpFQND60c7cHwPNZ7A6uXh7fxqvB5od26PleS3giunEN-uAuFIuKijjELspH1_gLcw/s934/authors-list.png">

# Add new categories, update categories, view categories, delete categories

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYe6-eBO4HZjqE1Rr0PLoHS1dlvlnwuagwQtX6eRavoDsWRGk4yfguhWIdcOFRgM4H7985xL1bdiLQLqX_iU7RzddDb1yiQ0P3M0sfwUdTRlRGMg85Kp2KKTsVZH5WGlptL6LFRTITq4oSCJFFCZwGML1RrxI-chu-xb4eXOWIoZpNlFWLLUzkW6zLdQ/s935/categorylist.png">

# Add new publishers, update publishers, view publishers, delete publishers

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcNQAd4UVi_bYQQSvW49hn0rQ1O7bEBDyN4DDNJSH1rtxBg37QIHQKAp7ELGbFV4Xva2F0DmhTkA3vKVeZcmKs7lODgTulsJr1aLyBckEojzxzZE5FYlfuEwD62Qco6PsjdNVPEWT76GlyVnSP94zNZK59w3CMRuvbYjoc1-MpyXj-WCeNEjPDm6mucw/s938/publishers-list.png"> README.md
pom.xml
src/main/java/com/knf/dev/librarymanagementsystem/Application.java
src/main/java/com/knf/dev/librarymanagementsystem/constant/Item.java
src/main/java/com/knf/dev/librarymanagementsystem/controller/AuthorController.java
src/main/java/com/knf/dev/librarymanagementsystem/controller/BookController.java
src/main/java/com/knf/dev/librarymanagementsystem/controller/CategoryController.java
src/main/java/com/knf/dev/librarymanagementsystem/controller/FileExportController.java
src/main/java/com/knf/dev/librarymanagementsystem/controller/IndexController.java
src/main/java/com/knf/dev/librarymanagementsystem/controller/PublisherController.java
src/main/java/com/knf/dev/librarymanagementsystem/entity/Author.java
src/main/java/com/knf/dev/librarymanagementsystem/entity/Book.java
src/main/java/com/knf/dev/librarymanagementsystem/entity/Category.java
src/main/java/com/knf/dev/librarymanagementsystem/entity/Publisher.java
src/main/java/com/knf/dev/librarymanagementsystem/entity/Role.java
src/main/java/com/knf/dev/librarymanagementsystem/entity/User.java
src/main/java/com/knf/dev/librarymanagementsystem/exception/NotFoundException.java
src/main/java/com/knf/dev/librarymanagementsystem/repository/AuthorRepository.java
src/main/java/com/knf/dev/librarymanagementsystem/repository/BookRepository.java
src/main/java/com/knf/dev/librarymanagementsystem/repository/CategoryRepository.java
src/main/java/com/knf/dev/librarymanagementsystem/repository/PublisherRepository.java
src/main/java/com/knf/dev/librarymanagementsystem/repository/UserRepository.java
src/main/java/com/knf/dev/librarymanagementsystem/securityconfig/SecurityConfiguration.java
src/main/java/com/knf/dev/librarymanagementsystem/service/AuthorService.java
src/main/java/com/knf/dev/librarymanagementsystem/service/BookService.java
src/main/java/com/knf/dev/librarymanagementsystem/service/CategoryService.java
src/main/java/com/knf/dev/librarymanagementsystem/service/FileService.java
src/main/java/com/knf/dev/librarymanagementsystem/service/PublisherService.java
src/main/java/com/knf/dev/librarymanagementsystem/service/UserService.java
src/main/java/com/knf/dev/librarymanagementsystem/service/impl/AuthorServiceImpl.java
src/main/java/com/knf/dev/librarymanagementsystem/service/impl/BookServiceImpl.java
src/main/java/com/knf/dev/librarymanagementsystem/service/impl/CategoryServiceImpl.java
src/main/java/com/knf/dev/librarymanagementsystem/service/impl/FileServiceImpl.java
src/main/java/com/knf/dev/librarymanagementsystem/service/impl/PublisherServiceImpl.java
src/main/java/com/knf/dev/librarymanagementsystem/service/impl/UserServiceImpl.java
src/main/java/com/knf/dev/librarymanagementsystem/util/Mapper.java
src/main/java/com/knf/dev/librarymanagementsystem/vo/AuthorRecord.java
src/main/java/com/knf/dev/librarymanagementsystem/vo/BookRecord.java
src/main/java/com/knf/dev/librarymanagementsystem/vo/CategoryRecord.java
src/main/java/com/knf/dev/librarymanagementsystem/vo/PublisherRecord.java
src/main/resources/application.properties
src/test/java/com/quickstartdev/librarymanagementsystem/ApplicationTests.java

# BM25 selected code snippets
### README.md
# Java, Spring Boot Mini Project - Library Management System


# Local setup

Step 1: Download or clone the source code from GitHub to the local machine

Step 2: Install JDK 17 - https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html

Step 3: Install IntelliJ IDEA or Eclipse or Apache NetBeans IDE

Step 4: Install Apache Maven - https://maven.apache.org/install.html

Step 5:  ```mvn clean install```

Step 6:  ```mvn spring-boot:run```

Step 7: From the browser call the endpoint http://localhost:9080

Step 8: Admin Login User Id: ```admin@admin.in``` & Password: ```Temp123```


# Admin Login Interface

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiiuctxupeOK4Nh8j-nomwwapjkcVvkYig3lX7qoifcXE76_6CnOXMZ-CLww7G180qegsCkrtyUlaqpJsWm9GzhX9QUFxyNyEUAXFD5UWJpvh2BdIr0wyAnFC38QOdsL_1vak8LtxYHrZyplCU_Sri-7kM9nXxI9heXXB0621rzJgL6j1CSweX6xjaorg/s945/admin-login.png">

# Add new books, update books, view books, delete books

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYMpuCQx3lGsS4T_H4ziyDWIkBpYV5qgo5JHFMV0Drper48H7YfygEdv0htE3yWo8mlypUW9W7NFY00UtrVznFfFYIzNGAXBeskhBb_kHAJrVKnI7O5mZt0_c085n6ir-cNVEYsTYffn6WgCmoBiZULR88ah_YxDC-ywRKPTsxj58GcHFnyyeX00RsNA/s800/library-management-system.png">

# Add new authors, update authors, view authors, delete authors

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixAW5k4E9IXf_OuVO1S5m100KS1xFo2ZrFoLnZYvNLjfpmIdI8W0ukd6yQn6oTsSWBKjDdAIGsnPf0EhgRwKzfpVq3mJXMcqG94Qp2oCCy0Pzf01b3kXP2ahgbvpFQND60c7cHwPNZ7A6uXh7fxqvB5od26PleS3giunEN-uAuFIuKijjELspH1_gLcw/s934/authors-list.png">

# Add new categories, update categories, view categories, delete categories

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhYe6-eBO4HZjqE1Rr0PLoHS1dlvlnwuagwQtX6eRavoDsWRGk4yfguhWIdcOFRgM4H7985xL1bdiLQLqX_iU7RzddDb1yiQ0P3M0sfwUdTRlRGMg85Kp2KKTsVZH5WGlptL6LFRTITq4oSCJFFCZwGML1RrxI-chu-xb4eXOWIoZpNlFWLLUzkW6zLdQ/s935/categorylist.png">

# Add new publishers, update publishers, view publishers, delete publishers

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcNQAd4UVi_bYQQSvW49hn0rQ1O7bEBDyN4DDNJSH1rtxBg37QIHQKAp7ELGbFV4Xva2F0DmhTkA3vKVeZcmKs7lODgTulsJr1aLyBckEojzxzZE5FYlfuEwD62Qco6PsjdNVPEWT76GlyVnSP94zNZK59w3CMRuvbYjoc1-MpyXj-WCeNEjPDm6mucw/s938/publishers-list.png">

### pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.6.4</version>
		<relativePath />
	</parent>
	<groupId>com.quickstartdev</groupId>
	<artifactId>librarymanagementsystem</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>librarymanagementsystem</name>
	<description>Library management system </description>

	<properties>
		<java.version>17</java.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-jpa</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-security</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-thymeleaf</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
		<dependency>
			<groupId>org.thymeleaf.extras</groupId>
			<artifactId>thymeleaf-extras-springsecurity5</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-devtools</artifactId>
			<scope>runtime</scope>
			<optional>true</optional>
		</dependency>
		<dependency>
			<groupId>com.opencsv</groupId>
			<artifactId>opencsv</artifactId>
			<version>5.6</version>
		</dependency>
		<dependency>
			<groupId>com.itextpdf</groupId>
			<artifactId>itextpdf</artifactId>
			<version>5.0.6</version>
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
...[truncated]...

### src/main/java/com/knf/dev/librarymanagementsystem/util/Mapper.java
package com.knf.dev.librarymanagementsystem.util;

import java.util.List;
import java.util.stream.Collectors;

import com.knf.dev.librarymanagementsystem.entity.Author;
import com.knf.dev.librarymanagementsystem.entity.Book;
import com.knf.dev.librarymanagementsystem.entity.Category;
import com.knf.dev.librarymanagementsystem.entity.Publisher;
import com.knf.dev.librarymanagementsystem.vo.AuthorRecord;
import com.knf.dev.librarymanagementsystem.vo.BookRecord;
import com.knf.dev.librarymanagementsystem.vo.CategoryRecord;
import com.knf.dev.librarymanagementsystem.vo.PublisherRecord;

public class Mapper {

	public static List<BookRecord> bookModelToVo(List<Book> books) {

		return books.stream().map(vo -> {
			var bookVo = new BookRecord(vo.getId(), vo.getIsbn(), vo.getName(), vo.getSerialName(),
					vo.getDescription());
			return bookVo;
		}).collect(Collectors.toList());
	}

	public static List<AuthorRecord> authorModelToVo(List<Author> authors) {

		return authors.stream().map(vo -> {
			var authorVo = new AuthorRecord(vo.getId(), vo.getName(), vo.getDescription());
			return authorVo;
		}).collect(Collectors.toList());

	}

	public static List<CategoryRecord> categoryModelToVo(List<Category> categories) {

		return categories.stream().map(vo -> {
			var categoryVo = new CategoryRecord(vo.getId(), vo.getName());
			return categoryVo;
		}).collect(Collectors.toList());

	}

	public static List<PublisherRecord> publisherModelToVo(List<Publisher> publishers) {

		return publishers.stream().map(vo -> {
			var publisherVo = new PublisherRecord(vo.getId(), vo.getName());
			return publisherVo;
		}).collect(Collectors.toList());

	}

}

### src/main/java/com/knf/dev/librarymanagementsystem/Application.java
package com.knf.dev.librarymanagementsystem;

import java.util.Arrays;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

import com.knf.dev.librarymanagementsystem.entity.Author;
import com.knf.dev.librarymanagementsystem.entity.Book;
import com.knf.dev.librarymanagementsystem.entity.Category;
import com.knf.dev.librarymanagementsystem.entity.Publisher;
import com.knf.dev.librarymanagementsystem.entity.Role;
import com.knf.dev.librarymanagementsystem.entity.User;
import com.knf.dev.librarymanagementsystem.repository.UserRepository;
import com.knf.dev.librarymanagementsystem.service.BookService;

@SpringBootApplication
public class Application {

	@Autowired
	private BCryptPasswordEncoder passwordEncoder;

	@Autowired
	private BookService bookService;

	@Autowired
	private UserRepository userRepository;

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

	@Bean
	public CommandLineRunner initialCreate() {
		return (args) -> {

			var book = new Book("AP1287", "Spring in Action ", "CXEF12389", "Book description");
			book.addAuthors(new Author("Matt", "dummy description"));
			book.addCategories(new Category("Dummy categary"));
			book.addPublishers(new Publisher("Dummy publisher"));
			bookService.createBook(book);

			var book1 = new Book("BP567#R", "Spring Microservices", "KCXEF12389", "Description1");
			book1.addAuthors(new Author("Maxwell", "Test description1"));
			book1.addCategories(new Category("New category"));
			book1.addPublishers(new Publisher("publisher2"));
			bookService.createBook(book1);

			var book2 = new Book("GH67F#", "Spring Boot", "UV#JH", "description2");
			book2.addAuthors(new Author("Josh Lang", "Test description2"));
			book2.addCategories(new Category("Spring category"));
			book2.addPublishers(new Publisher("publisher3"));
			bookService.createBook(book2);

			var user = new User("admin", "admin", "admin@admin.in", passwordEncoder.encode("Temp123"),
					Arrays.asList(new Role("ROLE_ADMIN")));
			userRepository.save(user);

		};
	}
}

### src/main/java/com/knf/dev/librarymanagementsystem/controller/PublisherController.java
package com.knf.dev.librarymanagementsystem.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import com.knf.dev.librarymanagementsystem.entity.Publisher;
import com.knf.dev.librarymanagementsystem.service.PublisherService;

@Controller
public class PublisherController {

	private final PublisherService publisherService;

	public PublisherController(PublisherService publisherService) {
		this.publisherService = publisherService;

	}

	@RequestMapping("/publishers")
	public String findAllPublishers(Model model) {

		model.addAttribute("publishers", publisherService.findAllPublishers());
		return "list-publishers";
	}

	@RequestMapping("/publisher/{id}")
	public String findPublisherById(@PathVariable("id") Long id, Model model) {

		model.addAttribute("publisher", publisherService.findPublisherById(id));
		return "list-publisher";
	}

	@GetMapping("/addPublisher")
	public String showCreateForm(Publisher publisher) {
		return "add-publisher";
	}

	@RequestMapping("/add-publisher")
	public String createPublisher(Publisher publisher, BindingResult result, Model model) {
		if (result.hasErrors()) {
			return "add-publisher";
		}

		publisherService.createPublisher(publisher);
		model.addAttribute("publisher", publisherService.findAllPublishers());
		return "redirect:/publishers";
	}

	@GetMapping("/updatePublisher/{id}")
	public String showUpdateForm(@PathVariable("id") Long id, Model model) {

		model.addAttribute("publisher", publisherService.findPublisherById(id));
		return "update-publisher";
	}

	@RequestMapping("/update-publisher/{id}")
	public String updatePublisher(@PathVariable("id") Long id, Publisher publisher, BindingResult result, Model model) {
		if (result.hasErrors()) {
			publisher.setId(id);
			return "update-publishers";
		}

		publisherService.updatePublisher(publisher);
		model.addAttribute("publisher", publisherService.findAllPublishers());
		return "redirect:/publishers";
	}

	@RequestMapping("/remove-publisher/{id}")
	public String deletePublisher(@PathVariable("id") Long id, Model model) {
		publisherService.deletePublisher(id);

		model.addAttribute("publisher", publisherService.findAllPublishers());
		return "redirect:/publishers";
	}

}

### src/main/java/com/knf/dev/librarymanagementsystem/controller/CategoryController.java
package com.knf.dev.librarymanagementsystem.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import com.knf.dev.librarymanagementsystem.entity.Category;
import com.knf.dev.librarymanagementsystem.service.CategoryService;

@Controller
public class CategoryController {

	private final CategoryService categoryService;

	public CategoryController(CategoryService categoryService) {
		this.categoryService = categoryService;

	}

	@RequestMapping("/categories")
	public String findAllCategories(Model model) {

		model.addAttribute("categories", categoryService.findAllCategories());
		return "list-categories";
	}

	@RequestMapping("/category/{id}")
	public String findCategoryById(@PathVariable("id") Long id, Model model) {

		model.addAttribute("category", categoryService.findCategoryById(id));
		return "list-category";
	}

	@GetMapping("/addCategory")
	public String showCreateForm(Category category) {
		return "add-category";
	}

	@RequestMapping("/add-category")
	public String createCategory(Category category, BindingResult result, Model model) {
		if (result.hasErrors()) {
			return "add-category";
		}

		categoryService.createCategory(category);
		model.addAttribute("category", categoryService.findAllCategories());
		return "redirect:/categories";
	}

	@GetMapping("/updateCategory/{id}")
	public String showUpdateForm(@PathVariable("id") Long id, Model model) {

		model.addAttribute("category", categoryService.findCategoryById(id));
		return "update-category";
	}

	@RequestMapping("/update-category/{id}")
	public String updateCategory(@PathVariable("id") Long id, Category category, BindingResult result, Model model) {
		if (result.hasErrors()) {
			category.setId(id);
			return "update-category";
		}

		categoryService.updateCategory(category);
		model.addAttribute("category", categoryService.findAllCategories());
		return "redirect:/categories";
	}

	@RequestMapping("/remove-category/{id}")
	public String deleteCategory(@PathVariable("id") Long id, Model model) {
		categoryService.deleteCategory(id);

		model.addAttribute("category", categoryService.findAllCategories());
		return "redirect:/categories";
	}

}

### src/main/java/com/knf/dev/librarymanagementsystem/service/impl/FileServiceImpl.java
package com.knf.dev.librarymanagementsystem.service.impl;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.http.HttpServletResponse;

import org.springframework.http.HttpHeaders;
import org.springframework.stereotype.Service;

import com.knf.dev.librarymanagementsystem.constant.Item;
import com.knf.dev.librarymanagementsystem.service.AuthorService;
import com.knf.dev.librarymanagementsystem.service.BookService;
import com.knf.dev.librarymanagementsystem.service.CategoryService;
import com.knf.dev.librarymanagementsystem.service.FileService;
import com.knf.dev.librarymanagementsystem.service.PublisherService;
import com.knf.dev.librarymanagementsystem.util.Mapper;
import com.knf.dev.librarymanagementsystem.vo.AuthorRecord;
import com.knf.dev.librarymanagementsystem.vo.BookRecord;
import com.knf.dev.librarymanagementsystem.vo.CategoryRecord;
import com.knf.dev.librarymanagementsystem.vo.PublisherRecord;
import com.opencsv.CSVWriter;
import com.opencsv.bean.StatefulBeanToCsv;
import com.opencsv.bean.StatefulBeanToCsvBuilder;
import com.opencsv.exceptions.CsvDataTypeMismatchException;
import com.opencsv.exceptions.CsvRequiredFieldEmptyException;

@Service
public class FileServiceImpl implements FileService {

	private final BookService bookService;

	private final AuthorService authorService;

	private final PublisherService publisherService;

	private final CategoryService categoryService;

	public FileServiceImpl(BookService bookService, AuthorService authorService, PublisherService publisherService,
			CategoryService categoryService) {
		this.authorService = authorService;
		this.categoryService = categoryService;
		this.publisherService = publisherService;
		this.bookService = bookService;
	}

	@Override
	public void exportCSV(String fileName, HttpServletResponse response)
			throws CsvDataTypeMismatchException, CsvRequiredFieldEmptyException, IOException {
		var item = Item.getItemByValue(fileName);
		response.setContentType("text/csv");
		response.setHeader(HttpHeaders.CONTENT_DISPOSITION,
				"attachment; filename=\"" + item.get().getFileName() + "\"");

		switch (item.get()) {
		case BOOK:
			StatefulBeanToCsv<BookRecord> writer1 = getWriter(response.getWriter());
			writer1.write(Mapper.bookModelToVo(bookService.findAllBooks()));
			break;
		case AUTHOR:
			StatefulBeanToCsv<AuthorRecord> writer2 = getWriter(response.getWriter());
			writer2.write(Mapper.authorModelToVo(authorService.findAllAuthors()));
			break;
		case CATEGORY:
			StatefulBeanToCsv<CategoryRecord> writer3 = getWriter(response.getWriter());
			writer3
...[truncated]...

### src/main/java/com/knf/dev/librarymanagementsystem/entity/Book.java
package com.knf.dev.librarymanagementsystem.entity;

import java.util.HashSet;
import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;
import javax.persistence.Table;

@Entity
@Table(name = "books")
public class Book {

	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private Long id;

	@Column(name = "isbn", length = 50, nullable = false, unique = true)
	private String isbn;

	@Column(name = "name", length = 100, nullable = false)
	private String name;

	@Column(name = "serialName", length = 50, nullable = false)
	private String serialName;

	@Column(name = "description", length = 250, nullable = false)
	private String description;

	@ManyToMany(fetch = FetchType.LAZY, cascade = { CascadeType.PERSIST, CascadeType.MERGE, CascadeType.REMOVE })
	@JoinTable(name = "books_authors", joinColumns = { @JoinColumn(name = "book_id") }, inverseJoinColumns = {
			@JoinColumn(name = "author_id") })
	private Set<Author> authors = new HashSet<Author>();

	@ManyToMany(fetch = FetchType.LAZY, cascade = { CascadeType.PERSIST, CascadeType.MERGE })
	@JoinTable(name = "books_categories", joinColumns = { @JoinColumn(name = "book_id") }, inverseJoinColumns = {
			@JoinColumn(name = "category_id") })
	private Set<Category> categories = new HashSet<Category>();

	@ManyToMany(fetch = FetchType.LAZY, cascade = { CascadeType.PERSIST, CascadeType.MERGE })
	@JoinTable(name = "books_publishers", joinColumns = { @JoinColumn(name = "book_id") }, inverseJoinColumns = {
			@JoinColumn(name = "publisher_id") })
	private Set<Publisher> publishers = new HashSet<Publisher>();

	public Book(String isbn, String name, String serialName, String description) {
		this.isbn = isbn;
		this.name = name;
		this.serialName = serialName;
		this.description = description;
	}

	public void addAuthors(Author author) {
		this.authors.add(author);
		author.getBooks().add(this);
	}

	public void removeAuthors(Author author) {
		this.authors.remove(author);
		author.getBooks().remove(this);
	}

	public void addCategories(Category category) {
		this.categories.add(category);
		category.getBooks().add(this);
	}

	public void removeCategories(Category category) {
		this.categories.remove(category);
		category.getBooks().remove(this);
	}

	public void addPublishers(Publisher publisher) {
...[truncated]...

### src/main/java/com/knf/dev/librarymanagementsystem/service/impl/UserServiceImpl.java
package com.knf.dev.librarymanagementsystem.service.impl;

import java.util.Collection;
import java.util.stream.Collectors;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.knf.dev.librarymanagementsystem.entity.Role;
import com.knf.dev.librarymanagementsystem.repository.UserRepository;
import com.knf.dev.librarymanagementsystem.service.UserService;

@Service
public class UserServiceImpl implements UserService {

	private final UserRepository userRepository;

	public UserServiceImpl(UserRepository userRepository) {
		this.userRepository = userRepository;
	}

	@Override
	public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {

		var user = userRepository.findByEmail(username);
		if (user == null) {
			throw new UsernameNotFoundException("Invalid username or password.");
		}
		return new org.springframework.security.core.userdetails.User(user.getEmail(), user.getPassword(),
				mapRolesToAuthorities(user.getRoles()));
	}

	private Collection<? extends GrantedAuthority> mapRolesToAuthorities(Collection<Role> roles) {
		return roles.stream().map(role -> new SimpleGrantedAuthority(role.getName())).collect(Collectors.toList());
	}

}

### src/main/java/com/knf/dev/librarymanagementsystem/controller/BookController.java
package com.knf.dev.librarymanagementsystem.controller;

import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import org.springframework.data.domain.PageRequest;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.knf.dev.librarymanagementsystem.entity.Book;
import com.knf.dev.librarymanagementsystem.service.AuthorService;
import com.knf.dev.librarymanagementsystem.service.BookService;
import com.knf.dev.librarymanagementsystem.service.CategoryService;
import com.knf.dev.librarymanagementsystem.service.PublisherService;

@Controller
public class BookController {

	private final BookService bookService;
	private final AuthorService authorService;
	private final CategoryService categoryService;
	private final PublisherService publisherService;

	public BookController(PublisherService publisherService, CategoryService categoryService, BookService bookService,
			AuthorService authorService) {
		this.authorService = authorService;
		this.bookService = bookService;
		this.categoryService = categoryService;
		this.publisherService = publisherService;
	}

	@RequestMapping({ "/books", "/" })
	public String findAllBooks(Model model, @RequestParam("page") Optional<Integer> page,
			@RequestParam("size") Optional<Integer> size) {

		var currentPage = page.orElse(1);
		var pageSize = size.orElse(5);

		var bookPage = bookService.findPaginated(PageRequest.of(currentPage - 1, pageSize));

		model.addAttribute("books", bookPage);

		var totalPages = bookPage.getTotalPages();
		if (totalPages > 0) {
			var pageNumbers = IntStream.rangeClosed(1, totalPages).boxed().collect(Collectors.toList());
			model.addAttribute("pageNumbers", pageNumbers);
		}
		return "list-books";
	}

	@RequestMapping("/searchBook")
	public String searchBook(@Param("keyword") String keyword, Model model) {

		model.addAttribute("books", bookService.searchBooks(keyword));
		model.addAttribute("keyword", keyword);
		return "list-books";
	}

	@RequestMapping("/book/{id}")
	public String findBookById(@PathVariable("id") Long id, Model model) {

		model.addAttribute("book", bookService.findBookById(id));
		return "list-book";
	}

	@GetMapping("/add")
	public String
...[truncated]...

### src/main/java/com/knf/dev/librarymanagementsystem/service/impl/PublisherServiceImpl.java
package com.knf.dev.librarymanagementsystem.service.impl;

import java.util.List;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import com.knf.dev.librarymanagementsystem.entity.Publisher;
import com.knf.dev.librarymanagementsystem.exception.NotFoundException;
import com.knf.dev.librarymanagementsystem.repository.PublisherRepository;
import com.knf.dev.librarymanagementsystem.service.PublisherService;

@Service
public class PublisherServiceImpl implements PublisherService {

	private final PublisherRepository publisherRepository;

	public PublisherServiceImpl(PublisherRepository publisherRepository) {
		this.publisherRepository = publisherRepository;
	}

	@Transactional(readOnly = true, propagation = Propagation.SUPPORTS)
	@Override
	public List<Publisher> findAllPublishers() {
		return publisherRepository.findAll();
	}

	@Override
	public Publisher findPublisherById(Long id) {
		return publisherRepository.findById(id)
				.orElseThrow(() -> new NotFoundException(String.format("Publisher not found  with ID %d", id)));
	}

	@Override
	public void createPublisher(Publisher publisher) {
		publisherRepository.save(publisher);
	}

	@Override
	public void updatePublisher(Publisher publisher) {
		publisherRepository.save(publisher);
	}

	@Override
	public void deletePublisher(Long id) {
		var publisher = publisherRepository.findById(id)
				.orElseThrow(() -> new NotFoundException(String.format("Publisher not found  with ID %d", id)));

		publisherRepository.deleteById(publisher.getId());
	}

}

### src/main/java/com/knf/dev/librarymanagementsystem/service/impl/CategoryServiceImpl.java
package com.knf.dev.librarymanagementsystem.service.impl;

import java.util.List;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import com.knf.dev.librarymanagementsystem.entity.Category;
import com.knf.dev.librarymanagementsystem.exception.NotFoundException;
import com.knf.dev.librarymanagementsystem.repository.CategoryRepository;
import com.knf.dev.librarymanagementsystem.service.CategoryService;

@Service
public class CategoryServiceImpl implements CategoryService {

	private final CategoryRepository categoryRepository;

	public CategoryServiceImpl(CategoryRepository categoryRepository) {
		this.categoryRepository = categoryRepository;
	}

	@Transactional(readOnly = true, propagation = Propagation.SUPPORTS)
	@Override
	public List<Category> findAllCategories() {
		return categoryRepository.findAll();
	}

	@Transactional(readOnly = true, propagation = Propagation.SUPPORTS)
	@Override
	public Category findCategoryById(Long id) {
		return categoryRepository.findById(id)
				.orElseThrow(() -> new NotFoundException(String.format("Category not found  with ID %d", id)));
	}

	@Override
	public void createCategory(Category category) {
		categoryRepository.save(category);
	}

	@Override
	public void updateCategory(Category category) {
		categoryRepository.save(category);
	}

	@Override
	public void deleteCategory(Long id) {
		var category = categoryRepository.findById(id)
				.orElseThrow(() -> new NotFoundException(String.format("Category not found  with ID %d", id)));

		categoryRepository.deleteById(category.getId());
	}

}

### src/main/java/com/knf/dev/librarymanagementsystem/service/impl/BookServiceImpl.java
package com.knf.dev.librarymanagementsystem.service.impl;

import java.util.Collections;
import java.util.List;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import com.knf.dev.librarymanagementsystem.entity.Book;
import com.knf.dev.librarymanagementsystem.exception.NotFoundException;
import com.knf.dev.librarymanagementsystem.repository.BookRepository;
import com.knf.dev.librarymanagementsystem.service.BookService;

@Service
public class BookServiceImpl implements BookService {

	private final BookRepository bookRepository;

	public BookServiceImpl(BookRepository bookRepository) {
		this.bookRepository = bookRepository;
	}

	@Transactional(readOnly = true, propagation = Propagation.SUPPORTS)
	@Override
	public List<Book> findAllBooks() {
		return bookRepository.findAll();
	}

	@Transactional(readOnly = true, propagation = Propagation.SUPPORTS)
	@Override
	public List<Book> searchBooks(String keyword) {
		if (keyword != null) {
			return bookRepository.search(keyword);
		}
		return bookRepository.findAll();
	}

	@Transactional(readOnly = true, propagation = Propagation.SUPPORTS)
	@Override
	public Book findBookById(Long id) {
		return bookRepository.findById(id)
				.orElseThrow(() -> new NotFoundException(String.format("Book not found with ID %d", id)));
	}

	@Override
	public void createBook(Book book) {
		bookRepository.save(book);
	}

	@Override
	public void updateBook(Book book) {
		bookRepository.save(book);
	}

	@Override
	public void deleteBook(Long id) {
		var book = bookRepository.findById(id)
				.orElseThrow(() -> new NotFoundException(String.format("Book not found with ID %d", id)));

		bookRepository.deleteById(book.getId());
	}

	@Override
	public Page<Book> findPaginated(Pageable pageable) {
		long startTime = System.currentTimeMillis(); // 开始计时

		List<Book> allBooks = findAllBooks();
		int pageSize = pageable.getPageSize();
		int currentPage = pageable.getPageNumber();
		int startItem = currentPage * pageSize;
		List<Book> list;

		if (allBooks.size() < startItem) {
			list = Collections.emptyList();
		} else {
			int toIndex = Math.min(startItem + pageSize, allBooks.size());
			list = allBooks.subList(startItem, toIndex);
		}

		var bookPage = new PageImpl<>(list, PageRequest.of(currentPage, pageSize), allBooks.size
...[truncated]...

### src/main/java/com/knf/dev/librarymanagementsystem/controller/AuthorController.java
package com.knf.dev.librarymanagementsystem.controller;

import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.knf.dev.librarymanagementsystem.entity.Author;
import com.knf.dev.librarymanagementsystem.service.AuthorService;

@Controller
public class AuthorController {

	private final AuthorService authorService;

	public AuthorController(AuthorService authorService) {
		this.authorService = authorService;
	}

	@RequestMapping("/authors")
	public String findAllAuthors(Model model, @RequestParam("page") Optional<Integer> page,
			@RequestParam("size") Optional<Integer> size) {

		var currentPage = page.orElse(1);
		var pageSize = size.orElse(5);
		var bookPage = authorService.findPaginated(PageRequest.of(currentPage - 1, pageSize));

		model.addAttribute("authors", bookPage);

		int totalPages = bookPage.getTotalPages();
		if (totalPages > 0) {
			var pageNumbers = IntStream.rangeClosed(1, totalPages).boxed().collect(Collectors.toList());
			model.addAttribute("pageNumbers", pageNumbers);
		}
		return "list-authors";
	}

	@RequestMapping("/author/{id}")
	public String findAuthorById(@PathVariable("id") Long id, Model model) {

		model.addAttribute("author", authorService.findAuthorById(id));
		return "list-author";
	}

	@GetMapping("/addAuthor")
	public String showCreateForm(Author author) {
		return "add-author";
	}

	@RequestMapping("/add-author")
	public String createAuthor(Author author, BindingResult result, Model model) {
		if (result.hasErrors()) {
			return "add-author";
		}

		authorService.createAuthor(author);
		model.addAttribute("author", authorService.findAllAuthors());
		return "redirect:/authors";
	}

	@GetMapping("/updateAuthor/{id}")
	public String showUpdateForm(@PathVariable("id") Long id, Model model) {

		model.addAttribute("author", authorService.findAuthorById(id));
		return "update-author";
	}

	@RequestMapping("/update-author/{id}")
	public String updateAuthor(@PathVariable("id") Long id, Author author, BindingResult result, Model model) {
		if (result.hasErrors()) {
			author.setId(id);
			return "update-author";
		}

		authorService.updateAuthor
...[truncated]...

### src/main/java/com/knf/dev/librarymanagementsystem/service/impl/AuthorServiceImpl.java
package com.knf.dev.librarymanagementsystem.service.impl;

import java.util.Collections;
import java.util.List;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

import com.knf.dev.librarymanagementsystem.entity.Author;
import com.knf.dev.librarymanagementsystem.exception.NotFoundException;
import com.knf.dev.librarymanagementsystem.repository.AuthorRepository;
import com.knf.dev.librarymanagementsystem.service.AuthorService;

@Service
public class AuthorServiceImpl implements AuthorService {

	private final AuthorRepository authorRepository;

	public AuthorServiceImpl(AuthorRepository authorRepository) {
		this.authorRepository = authorRepository;
	}

	@Transactional(readOnly = true, propagation = Propagation.SUPPORTS)
	@Override
	public List<Author> findAllAuthors() {
		return authorRepository.findAll();
	}

	@Transactional(readOnly = true, propagation = Propagation.SUPPORTS)
	@Override
	public Author findAuthorById(Long id) {
		return authorRepository.findById(id)
				.orElseThrow(() -> new NotFoundException(String.format("Author not found with ID %d", id)));
	}

	@Override
	public void createAuthor(Author author) {
		authorRepository.save(author);
	}

	@Override
	public void updateAuthor(Author author) {
		authorRepository.save(author);
	}

	@Override
	public void deleteAuthor(Long id) {
		var author = authorRepository.findById(id)
				.orElseThrow(() -> new NotFoundException(String.format("Author not found with ID %d", id)));

		authorRepository.deleteById(author.getId());
	}

	@Override
	public Page<Author> findPaginated(Pageable pageable) {

		var pageSize = pageable.getPageSize();
		var currentPage = pageable.getPageNumber();
		var startItem = currentPage * pageSize;
		List<Author> list;

		if (findAllAuthors().size() < startItem) {
			list = Collections.emptyList();
		} else {
			var toIndex = Math.min(startItem + pageSize, findAllAuthors().size());
			list = findAllAuthors().subList(startItem, toIndex);
		}

		return new PageImpl<Author>(list, PageRequest.of(currentPage, pageSize), findAllAuthors().size());

	}

}

### src/main/java/com/knf/dev/librarymanagementsystem/securityconfig/SecurityConfiguration.java
package com.knf.dev.librarymanagementsystem.securityconfig;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.
...[truncated]...