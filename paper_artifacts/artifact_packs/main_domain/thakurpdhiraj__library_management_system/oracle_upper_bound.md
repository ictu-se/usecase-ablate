# Oracle upper-bound selected context
This condition is selected with checked trace paths and is used only as an upper-bound comparator.

# README
## README.md
# Library Management System

A complete suite of book lending system with role based features : 
*(Check [Snapshots](#snapshots))*
1. Admin
    * Add books with isbn validation and inventory creation with unique id & generating downloadable (pdf) barcode.
    * Search, update and delete books or inventory.
    * Add, search, update and delete users.
    * Search orders based on order id, user id or book id.
    * Mark order as collected.
    * Mark order as returned and generate downloadable invoice with late fees as applicable.
    * Search user's order history.
    * Search orders that are overdue for return by user id or book id.

2. User
    * Order a new book based on inventory availability.
    * Search self orders and order history.
    * Filter orders based on return overdue.

3. All
    * Authentication with Login and Logout.
    * Role based authorization and views (front-end).
    * Update self account details & change password.
    
## Technology Stack & Frameworks
> `Java 11`  `Spring-Boot-2.3.4.RELEASE` `Spring-Cloud-Hoxton.SR8` `Spring-Security` `Spring Data JPA` `Vue JS 2` `Vuetify 2.4` `Docker` `Docker-Compose` `JUnit 5`

## Installation and Running
- **With Docker and Docker Compose Installed**
```docker
docker compose down
docker compose build
docker compose up
-------------------------
or run the start.sh file
-------------------------
./start.sh
```
- **Without Docker** *(`npm` & `maven` required locally)*

*For Backend*
```
./build.sh
Open terminal to './server' && mvn spring-boot:run
---------------------------------------------
Once ServerApplication.java is up & running
---------------------------------------------
Open terminal to './user' && mvn spring-boot:run
Open terminal to './book' && mvn spring-boot:run
Open terminal to './auth' && mvn spring-boot:run
Open terminal to './order' && mvn spring-boot:run
Open terminal to './inventory' && mvn spring-boot:run
Open terminal to './client-backend' && mvn spring-boot:run
```

*For Frontend*
```
Open terminal to './client-frontend' && npm run serve
```
## Ports Exposed
Application | Port 
----------- | ---- 
*auth* | `8081`
*book* | `8082`
*inventory* | `8083`
*order* | `8084`
*user* | `8085`
*client-backend* | `8086`
*server* | `8761`
*client-frontend* | `8080`

## Snapshots

* Admin
    * Search Orders
    ![Admin- Search Orders](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/admin_order_search.jpeg "Search Orders")
    * Search Order History
    ![Admin- Search Order History](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/admin_order_history.jpeg "Search Order History")
    * Search Order Overdue
    ![Admin- Search Order Overdue](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/admin_order_overdue.jpeg "Search Order Overdue")
    * Search Books
    ![Admin- Search Books](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/admin_book_find.jpeg "Search Books")
    * Add Book
    ![Admin- Add Book](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/admin_book_add.jpeg "Add Book")
    * Generated Inventory Barcode on Book Inventory Addition
    ![Admin- Inventory Barcode Generation](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/admin_book_add_barcode.jpeg "Inventory Barcode Generation")
    * Delete Book
    ![Admin- Delete Book](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/admin_book_delete.jpeg "Delete Book")
    * Find User
    ![Admin- Find User](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/admin_user_find.jpeg "Find User")
    * Add User
    ![Admin- Add User](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/admin_user_add.jpeg "Add User")
    * Delete User
    ![Admin- Delete User](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/admin_user_delete.jpeg "Delete User")
    
* User
    * Search Orders / Home
    ![User- Search Orders](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/user_home.jpeg "Search Orders")
    * Search Order History
    ![User- Search Order History](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/user_history.jpeg "Search Order History")
    * Order Book
    ![User- Order Book Step 1](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/user_new_1.jpeg "Order Book Step 1")
    ![User- Order Book Step 2](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/user_new_2.jpeg "Order Book Step 2")
    ![User- Order Book Step 3](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/user_new_3.jpeg "Order Book Step 3")
    
* All
    * Edit Account
    ![All- Edit Account](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/edit_account.jpeg "Edit Account")
    * Change Password
    ![All- Change Password](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/change_password.jpeg "Change Password")
    * Login
    ![All- Login](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/login.jpeg "Login")

# File tree
README.md
auth
  pom.xml
  src
    main
      java
        com
          dhitha
      resources
        application.yml
    test
      java
        com
          dhitha
      resources
        application-test.yml
book
  pom.xml
  src
    main
      java
        com
          dhitha
      resources
        application.yml
    test
      java
        com
          dhitha
      resources
        application-test.yml
client-backend
  pom.xml
  src
    main
      java
        com
          dhitha
      resources
        application.yml
client-frontend
  README.md
  babel.config.js
  jsconfig.json
  package-lock.json
  package.json
  src
    App.vue
    components
      admin
        books
          BookPage.vue
          DeleteBooks.vue
          EditBooks.vue
          FindBooks.vue
          NewBook.vue
        orders
          FindOrders.vue
          FindOrdersHistory.vue
          FindOrdersOverdue.vue
          OrderPage.vue
        users
          FindUsers.vue
          NewUser.vue
          UserPage.vue
      common
        Tabs.vue
      user
        account
          AccountPage.vue
          ChangePassword.vue
          EditAccount.vue
        orders
          MyOrdersPage.vue
          history
          neworder
          utility
    main.js
    plugins
      vuetify.js
    resource
      resource.js
    router
      router.js
    service
      auth.js
      book.js
      inventory.js
      order.js
      user.js
    store
      modules
        userStore.js
      store.js
    util
      authUtil.js
      responseUtil.js
      ruleUtil.js
    views
      AdminView.vue
      ErrorView.vue
      LoginView.vue
      UserView.vue
  tests
    unit
      example.spec.js
  vue.config.js
docker-compose.yml
inventory
  pom.xml
  src
    main
      java
        com
          dhitha
      resources
        application.yml
    test
      java
        com
          dhitha
      resources
        application-test.yml
lms_api.postman_collection.json
lms_api.postman_environment.json
lms_client.postman_collection.json
lms_client.postman_environment.json
order
  pom.xml
  src
    main
      java
        com
          dhitha
      resources
        application.yml
    test
      java
        com
          dhitha
      resources
        application-test.yml
server
  pom.xml
  src
    main
      java
        com
          dhitha
      resources
        application.yml
    test
      java
        com
          dhitha
user
  pom.xml
  src
    main
      java
        com
          dhitha
      resources
        application.yml
    test
      java
        com
          dhitha
      resources
        application-test.yml

# Oracle-selected code and test snippets
### client-frontend/src/components/admin/books/NewBook.vue
<template>
  <v-card>
    <v-container>
      <v-row v-if="message">
        <v-col cols="12">
          <v-card class="elevation-5">
            <v-alert
              dense
              outlined
              dismissible
              transition="scale-transition"
              :type="isError ? 'error' : 'success'"
            >
              {{ message }}
            </v-alert>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col :loading="loading">
          <v-form
            @submit.prevent="saveBook"
            :loading="loading"
            v-model="valid"
            ref="form"
          >
            <v-card flat>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Name *"
                        clearable
                        v-model="book.name"
                        :rules="[rules.required]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Author *"
                        clearable
                        v-model="book.author"
                        :rules="[rules.required]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Pages *"
                        clearable
                        v-model="book.pages"
                        :rules="[rules.required, rules.number]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-select
                        v-model="book.category"
                        item-text="name"
                        return-object
                        :items="categories"
                        :rules="[rules.required]"
                        label="Category *"
                      ></v-select>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Publication *"
                        clearable
                        v-model="book.publication"
                        :rules="[rules.required]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Published Year *"
                    
...[truncated]...

### client-backend/src/main/java/com/dhitha/lms/clientbackend/controller/admin/ClientBookAdminController.java
package com.dhitha.lms.clientbackend.controller.admin;

import com.dhitha.lms.clientbackend.client.BookClient;
import com.dhitha.lms.clientbackend.client.InventoryClient;
import com.dhitha.lms.clientbackend.dto.BookDTO;
import java.net.URI;
import java.util.List;
import java.util.Objects;
import javax.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

/**
 * REST controller for Books for admins
 *
 * @author Dhiraj
 */
@RestController
@RequestMapping("/admin/books")
@RequiredArgsConstructor
public class ClientBookAdminController {
  private final BookClient bookClient;
  private final InventoryClient inventoryClient;

  @PostMapping(
      consumes = MediaType.APPLICATION_JSON_VALUE,
      produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<BookDTO> save(@RequestBody @Valid BookDTO bookDTO) {
    BookDTO savedBook = bookClient.save(bookDTO);
    URI uri =
        ServletUriComponentsBuilder.fromCurrentRequest()
            .path("/{id}")
            .buildAndExpand(savedBook.getId())
            .toUri();
    return ResponseEntity.created(uri).body(savedBook);
  }

  @PutMapping(
      value = "/{id}",
      consumes = MediaType.APPLICATION_JSON_VALUE,
      produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<BookDTO> update(@PathVariable Long id, @RequestBody BookDTO bookDTO) {
    return ResponseEntity.ok(bookClient.update(id, bookDTO));
  }

  @DeleteMapping(value = "/{id}")
  public ResponseEntity<Void> delete(
      @PathVariable Long id,
      @RequestParam(required = false, name = "bookReference") List<String> bookReferenceList) {
    inventoryClient.delete(id, bookReferenceList);
    if (Objects.isNull(bookReferenceList) || bookReferenceList.isEmpty()) {
      bookClient.delete(id);
    }
    return ResponseEntity.noContent().build();
  }
}

### book/src/main/java/com/dhitha/lms/book/controller/BookController.java
package com.dhitha.lms.book.controller;

import com.dhitha.lms.book.dto.BookDTO;
import com.dhitha.lms.book.dto.CategoryDTO;
import com.dhitha.lms.book.error.BookNotFoundException;
import com.dhitha.lms.book.service.BookService;
import com.dhitha.lms.book.service.CategoryService;
import java.net.URI;
import java.util.List;
import javax.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

/**
 * REST Controller for {@link com.dhitha.lms.book.entity.Book}
 *
 * @author Dhiraj
 */
@RestController
@RequestMapping("/books/v1")
@RequiredArgsConstructor
public class BookController {

  private final BookService bookService;

  @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<List<BookDTO>> getAllBooks(BookDTO bookDTO,
      @RequestParam(value = "categoryId", required = false) Integer categoryId) {
    bookDTO.setCategory(new CategoryDTO(categoryId, null));
    List<BookDTO> bookList = bookService.findAll(bookDTO);
    return ResponseEntity.ok(bookList);
  }

  @GetMapping(value = "/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<BookDTO> getById(@PathVariable Long id) throws BookNotFoundException {
    return ResponseEntity.ok(bookService.findById(id));
  }

  @PostMapping(
      consumes = MediaType.APPLICATION_JSON_VALUE,
      produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<BookDTO> save(@RequestBody @Valid BookDTO bookDTO) {

    BookDTO savedBook = bookService.save(bookDTO);
    URI uri =
        ServletUriComponentsBuilder.fromCurrentRequest()
            .path("/{id}")
            .buildAndExpand(savedBook.getId())
            .toUri();
    return ResponseEntity.created(uri).body(savedBook);
  }

  @PutMapping(
      value = "/{id}",
      consumes = MediaType.APPLICATION_JSON_VALUE,
      produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<BookDTO> u
...[truncated]...

### inventory/src/main/java/com/dhitha/lms/inventory/controller/InventoryController.java
package com.dhitha.lms.inventory.controller;

import com.dhitha.lms.inventory.dto.InventoryDTO;
import com.dhitha.lms.inventory.error.GenericException;
import com.dhitha.lms.inventory.error.InventoryNotFoundException;
import com.dhitha.lms.inventory.service.InventoryService;
import java.util.List;
import javax.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * REST for Inventory
 *
 * @author Dhiraj
 */
@RestController
@RequestMapping("/v1/books")
@RequiredArgsConstructor
public class InventoryController {

  private final InventoryService inventoryService;

  @GetMapping(value = "/{bookId}", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<List<InventoryDTO>> getAll(@PathVariable Long bookId) {
    return ResponseEntity.ok(inventoryService.findAllBook(bookId));
  }

  @GetMapping(value = "/{bookId}/count", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<Long> getAvailableCount(@PathVariable Long bookId) {
    long count = inventoryService.getAvailableCount(bookId);
    return ResponseEntity.ok(count);
  }

  @PostMapping(value = "/{bookId}/order", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<InventoryDTO> orderIfAvailable(@PathVariable Long bookId)
      throws InventoryNotFoundException {
    InventoryDTO inventoryDTO = inventoryService.orderBookIfAvailable(bookId);
    return ResponseEntity.ok(inventoryDTO);
  }

  @PostMapping(value = "/{bookId}/return", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<Boolean> returnBook(
      @PathVariable Long bookId, @RequestParam String bookReferenceId) {
    return ResponseEntity.ok(inventoryService.returnBook(bookId, bookReferenceId));
  }

  @PostMapping(consumes = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<List<InventoryDTO>> save(
      @Valid @RequestBody InventoryDTO inventor
...[truncated]...

### inventory/src/main/java/com/dhitha/lms/inventory/service/InventoryServiceImpl.java
package com.dhitha.lms.inventory.service;

import com.dhitha.lms.inventory.dto.InventoryDTO;
import com.dhitha.lms.inventory.entity.Inventory;
import com.dhitha.lms.inventory.error.GenericException;
import com.dhitha.lms.inventory.error.InventoryNotFoundException;
import com.dhitha.lms.inventory.repository.InventoryRepository;
import java.security.SecureRandom;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;
import java.util.Set;
import java.util.UUID;
import java.util.stream.Collectors;
import javax.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.modelmapper.ModelMapper;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;
import org.springframework.util.Assert;

/**
 * Implementation for {@link InventoryService}
 *
 * @author Dhiraj
 */
@Service
@Slf4j
@RequiredArgsConstructor
@Transactional
public class InventoryServiceImpl implements InventoryService {

  private final InventoryRepository inventoryRepository;
  private final ModelMapper modelMapper;

  @Override
  public List<InventoryDTO> findAllBook(Long bookId) {
    return inventoryRepository.findByIdBookId(bookId).stream()
        .map(this::mapToDTO)
        .collect(Collectors.toList());
  }

  @Override
  public InventoryDTO orderBookIfAvailable(Long bookId) throws InventoryNotFoundException {
    InventoryDTO inventoryDTO =
        inventoryRepository.findByIdBookId(bookId).stream()
            .filter(Inventory::getAvailable)
            .findFirst()
            .map(this::mapToDTO)
            .orElseThrow(
                () ->
                    new InventoryNotFoundException(
                        "No inventory available for book id: " + bookId));
    inventoryRepository.updateAvailability(
        inventoryDTO.getBookId(), inventoryDTO.getBookReferenceId(), false);
    return inventoryDTO;
  }

  @Override
  public boolean returnBook(Long bookId, String bookReferenceId) {
    return inventoryRepository.updateAvailability(bookId, bookReferenceId, true) > 0;
  }

  @Override
  public long getAvailableCount(Long bookId) {
    return inventoryRepository.countByIdBookIdAndAvailable(bookId, true);
  }

  @Override
  @Transactional(rollbackOn = Exception.class)
  public List<InventoryDTO> add(InventoryDTO inventoryDTO, Integer count) throws GenericException {
    Assert.notNull(inventoryDTO, "Inventory cannot be null");
    count = count != null && count > 0 ? count : 1;
    Set<Inventory> set = new HashSet<>(count);
    SecureRandom secureRandom = new SecureRand
...[truncated]...

### book/src/test/java/com/dhitha/lms/book/controller/BookControllerTest.java
package com.dhitha.lms.book.controller;

import static org.hamcrest.Matchers.hasSize;
import static org.hamcrest.Matchers.is;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import com.dhitha.lms.book.dto.BookDTO;
import com.dhitha.lms.book.dto.CategoryDTO;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.MethodOrderer;
import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestMethodOrder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;

/**
 * Integration Tests {@link BookController} Depends on data-test.sql file
 *
 * @author Dhiraj
 */
@SpringBootTest
@AutoConfigureMockMvc
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
@ActiveProfiles("test")
class BookControllerTest {

  @Autowired private ObjectMapper objectMapper;

  @Autowired private MockMvc mockMvc;

  @Value("${lms.client.key}")
  private String apiKey;

  @Test
  @Order(0)
  void contextLoads() {}

  @Test
  @Order(1)
  void testGetAll() throws Exception {
    mockMvc
        .perform(get("/books/v1").header("lms-key", apiKey))
        .andExpect(status().isOk())
        .andExpect(jsonPath("$", hasSize(3)));
  }

  @Test
  @Order(2)
  void testGetAllByAuthor() throws Exception {
    mockMvc
        .perform(get("/books/v1").param("author", "JK").header("lms-key", apiKey))
        .andExpect(status().isOk())
        .andExpect(jsonPath("$", hasSize(2)))
        .andExpect(jsonPath("$[0].author", is("JK")))
        .andExpect(jsonPath("$[1].author", is("JK")));
  }

  @Test
  @Order(3)
  void testGetAllByName() throws Exception {
    mockMvc
        .perform(get("/books/v1").param("name", "Data Structure").header("lms-key", apiKey))
        .andExpect(status().isOk())
    
...[truncated]...

### inventory/src/test/java/com/dhitha/lms/inventory/controller/InventoryControllerTest.java
package com.dhitha.lms.inventory.controller;

import static org.hamcrest.Matchers.hasSize;
import static org.hamcrest.Matchers.is;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import com.dhitha.lms.inventory.dto.InventoryDTO;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.MethodOrderer;
import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestMethodOrder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.http.MediaType;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;

/**
 * Integration tests for {@link InventoryController}. Depends on /test/resources/data-test.sql file.
 *
 * @author Dhiraj
 */
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
@ActiveProfiles("test")
class InventoryControllerTest {

  private static final String PATH = "/v1/books";
  @Autowired private MockMvc mockMvc;
  @Autowired private ObjectMapper objectMapper;

  @Value("${lms.client.key}")
  private String apiKey;

  @Test
  @Order(1)
  @DisplayName("get, getAll: find all inventory for a book id, expected 200")
  void testGetAll() throws Exception {
    mockMvc
        .perform(get(PATH + "/{bookId}", 2).header("lms-key", apiKey))
        .andExpect(status().isOk())
        .andExpect(jsonPath("$", hasSize(3)));
  }

  @Test
  @Order(2)
  @DisplayName("get, getAll: find count of all inventory for a book id, expected 200")
  void testGetAvailableCount() throws Exception {
    checkCount(2, 3);
  }

  @Test
  @Order(3)
  @DisplayName("post, orderIfAvailable: order if available for a book id, expected 200")
  void testOrderIfAvailable() throws Exception {
    mockMvc
        .perform(
            post(PATH + "/
...[truncated]...

### book/src/test/java/com/dhitha/lms/book/service/BookServiceTest.java
package com.dhitha.lms.book.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.doThrow;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import com.dhitha.lms.book.dto.BookDTO;
import com.dhitha.lms.book.entity.Book;
import com.dhitha.lms.book.error.BookNotFoundException;
import com.dhitha.lms.book.repository.BookRepository;
import com.dhitha.lms.book.repository.BookSpecification;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.modelmapper.ModelMapper;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.data.jpa.domain.Specification;

/**
 * Unit test for {@link BookService}
 *
 * @author Dhiraj
 */
@ExtendWith(MockitoExtension.class)
class BookServiceTest {

  private final ModelMapper modelMapper = new ModelMapper();
  @Mock private BookRepository bookRepositoryMock;
  private BookService subject;

  @BeforeEach
  void init() {
    subject = new BookServiceImpl(bookRepositoryMock, modelMapper);
  }

  /* ********************** findAll ************************** */
  @Test
  void testFindAll() {
    Book book = Book.builder().name("book").build();
    when(bookRepositoryMock.findAll(any(BookSpecification.class))).thenReturn(Collections.singletonList(book));
    List<BookDTO> result = subject.findAll(BookDTO.builder().name("book").build());
    verify(bookRepositoryMock).findAll(any(BookSpecification.class));
    assertEquals(1, result.size());
    assertEquals("book", result.get(0).getName());
  }

  /* ********************** findById ************************** */
  @Test
  void testFindById() throws Exception {
    Book book = Book.builder().name("book").build();
    when(bookRepositoryMock.findById(1L)).thenReturn(Optional.of(book));
    BookDTO result = subject.findById(1L);
    verify(bookRepositoryMock).findById(1L);
    assertEquals(book.getName(), result.getName());
  }

  @Test
  void testFindByIdThrowsBookNotFoundException() throws Exception {
    assertThrows(
        BookNotFoundException.class,
        () -> {
          when(bookRepositoryMock.findById(1L)).thenReturn(Optional.empty())
...[truncated]...

### client-frontend/src/components/admin/books/FindBooks.vue
<template>
  <v-card>
    <v-container>
      <v-row v-if="message">
        <v-col cols="12">
          <v-card class="elevation-5">
            <v-alert
              dense
              outlined
              dismissible
              transition="scale-transition"
              :type="isError ? 'error' : 'success'"
            >
              {{ message }}
            </v-alert>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" sm="3" v-if="!showForm">
          <v-btn
            block
            color="primary"
            dark
            class="w-50"
            @click="showForm = true"
          >
            Refine Search
          </v-btn>
        </v-col>
        <v-col cols="12" v-else>
          <v-form
            @submit.prevent="getBooks"
            :loading="loading"
            v-model="valid"
            ref="searchForm"
          >
            <v-row>
              <v-col cols="12" sm="3">
                <v-text-field
                  label="Book Id"
                  clearable
                  v-model="book.id"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="3">
                <v-text-field
                  label="Book Name"
                  clearable
                  v-model="book.name"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="3">
                <v-text-field
                  label="Author Name"
                  clearable
                  v-model="book.author"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="3">
                <v-text-field
                  label="Publication Name"
                  clearable
                  v-model="book.publication"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="3">
                <v-text-field
                  label="ISBN"
                  clearable
                  v-model="book.isbn"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="3">
                <v-btn color="green" text dark :disabled="!valid" type="submit">
                  Search
                </v-btn>
                <v-btn color="blue darken-1" text dark @click="clearForm">
                  Clear
                </v-btn>
              </v-col>
            </v-row>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
    <v-data-table
      :headers="headers"
      :items="bookList"
      class="elevation-20"
      item-key="id"
      
...[truncated]...

### client-frontend/src/components/admin/books/EditBooks.vue
<template>
  <v-dialog v-model="editDialog" overlay-opacity="0.8" persistent>
    <v-form
      @submit.prevent="editBook"
      :loading="loading"
      v-model="valid"
      ref="editForm"
    >
      <v-card flat v-if="selectedBook">
        <v-card-text>
          <v-container>
            <v-row v-if="message">
              <v-col cols="12">
                <v-card class="elevation-5">
                  <v-alert
                    dense
                    outlined
                    dismissible
                    transition="scale-transition"
                    :type="isError ? 'error' : 'success'"
                  >
                    {{ message }}
                  </v-alert>
                </v-card>
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="12" sm="4">
                <v-text-field
                  label="Name *"
                  clearable
                  v-model="selectedBook.name"
                  :rules="[rules.required]"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  label="Author *"
                  clearable
                  v-model="selectedBook.author"
                  :rules="[rules.required]"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  label="Pages *"
                  clearable
                  v-model="selectedBook.pages"
                  :rules="[rules.required, rules.number]"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-select
                  v-model="selectedBook.category"
                  item-text="name"
                  return-object
                  :items="categories"
                  :rules="[rules.required]"
                  label="Category *"
                ></v-select>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  label="Publication *"
                  clearable
                  v-model="selectedBook.publication"
                  :rules="[rules.required]"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-text-field
                  label="Published Year *"
                  clearable
                  v-model="selectedBook.publicationYear"
                  :rules="[rules.year]"
                ></v-text-field>
              </v-col>
              <v-col cols=
...[truncated]...

### client-backend/src/main/java/com/dhitha/lms/clientbackend/controller/ClientBookController.java
package com.dhitha.lms.clientbackend.controller;

import com.dhitha.lms.clientbackend.client.BookClient;
import com.dhitha.lms.clientbackend.dto.BookDTO;
import java.util.List;
import lombok.RequiredArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * REST controller for Books
 *
 * @author Dhiraj
 */
@RestController
@RequestMapping("/books")
@PreAuthorize("hasAnyAuthority('ADMIN','USER')")
@RequiredArgsConstructor
public class ClientBookController {

  private final BookClient bookClient;

  @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<List<BookDTO>> getAllBooks(BookDTO bookDTO,
      @RequestParam(value = "categoryId", required = false) Integer categoryId) {
    List<BookDTO> bookList = bookClient.getAllBooks(bookDTO, categoryId);
    return ResponseEntity.ok(bookList);
  }

  @GetMapping(value = "/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<BookDTO> getById(@PathVariable Long id) {
    return ResponseEntity.ok(bookClient.getById(id));
  }
}

### client-frontend/src/components/admin/books/DeleteBooks.vue
<template>
  <v-dialog
    v-model="deleteDialog"
    :max-width="$vuetify.breakpoint.mobile ? '100vw' : '50vw'"
    overlay-opacity="0.97"
    persistent
  >
    <v-card v-if="selectedBook">
      <v-alert v-if="errorMessage" dense outlined dismissible type="error">
        {{ errorMessage }}
      </v-alert>
      <v-card-title>
        Are you sure you want to delete
        <p class="red--text my-0 mx-3 pa-0">{{ selectedBook.name }}</p>
        ?
      </v-card-title>
      <v-card-text>
        <div>
          <v-alert type="info" colored-border color="blue" border="left" dense>
            Book cannot be deleted if one of the copies is loaned
          </v-alert>
        </div>
        <div>
          <v-switch
            v-model="showRef"
            label="Delete Inventory"
            color="success"
            hide-details
          ></v-switch>
        </div>
        <div v-if="showRef">
          <v-checkbox
            v-for="item in references"
            :key="item.bookReferenceId"
            v-model="bookReferencesToDelete"
            :label="item.bookReferenceId"
            :value="item.bookReferenceId"
            :disabled="!item.available"
          ></v-checkbox>
        </div>
      </v-card-text>
      <v-card-actions>
        <v-btn
          color="green darken-1"
          text
          :disabled="!valid"
          @click="deleteBook"
        >
          OK
        </v-btn>
        <v-btn text @click="closeDelete">
          Cancel
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import * as bookService from "@/service/book";
import * as inventoryService from "@/service/inventory";
import find from "lodash/find";
export default {
  data() {
    return {
      bookReferencesToDelete: [],
      references: [],
      errorMessage: null,
      showRef: false
    };
  },
  computed: {
    valid() {
      if (this.showRef) {
        return this.bookReferencesToDelete.length > 0;
      } else {
        return find(this.references, { available: false }) === undefined;
      }
    }
  },
  props: {
    selectedBook: {
      type: Object,
      default: null
    },
    deleteDialog: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    deleteBook() {
      console.log(this.selectedBook.id, this.bookReferencesToDelete);
      bookService
        .deleteBook(this.selectedBook.id, this.bookReferencesToDelete)
        .then(() => {
          this.$emit("deleteSuccess");
        })
        .catch(err => {
          this.$emit("deleteFail", err);
        });
    },
    closeDele
...[truncated]...

### inventory/src/test/java/com/dhitha/lms/inventory/service/InventoryServiceTest.java
package com.dhitha.lms.inventory.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyLong;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.doThrow;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import com.dhitha.lms.inventory.dto.InventoryDTO;
import com.dhitha.lms.inventory.entity.Inventory;
import com.dhitha.lms.inventory.entity.InventoryId;
import com.dhitha.lms.inventory.error.InventoryNotFoundException;
import com.dhitha.lms.inventory.repository.InventoryRepository;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.modelmapper.ModelMapper;
import org.springframework.dao.EmptyResultDataAccessException;

/**
 * Unit tests for {@link InventoryService}
 *
 * @author Dhiraj
 */
@ExtendWith(MockitoExtension.class)
class InventoryServiceTest {

  private final ModelMapper modelMapper = new ModelMapper();
  @Mock private InventoryRepository repositoryMock;
  private InventoryService subject;

  @BeforeEach
  void init() {
    subject = new InventoryServiceImpl(repositoryMock, modelMapper);
  }

  @Test
  @DisplayName("findAllBook: valid input, expected success")
  void testFindAllOfBook() {
    when(repositoryMock.findByIdBookId(1L)).thenReturn(createMockInventory(1L, true));
    List<InventoryDTO> result = subject.findAllBook(1L);
    assertEquals(2, result.size());
    verify(repositoryMock).findByIdBookId(1L);
  }

  @Test
  @DisplayName("orderBookIfAvailable: book available, expected success")
  void testOrderBookIfAvailable() throws Exception {
    when(repositoryMock.findByIdBookId(1L)).thenReturn(createMockInventory(1L, true));
    when(repositoryMock.updateAvailability(1L, "abc", false)).thenReturn(1);
    InventoryDTO result = subject.orderBookIfAvailable(1L);
    assertEquals("abc", result.getBookReferenceId());
    verify(repositoryMock).findByIdBo
...[truncated]...

### client-frontend/src/components/admin/users/NewUser.vue
<template>
  <v-card flat>
    <v-container>
      <v-row v-if="message">
        <v-col cols="12">
          <v-card class="elevation-5">
            <v-alert
              dense
              outlined
              dismissible
              transition="scale-transition"
              :type="isError ? 'error' : 'success'"
            >
              {{ message }}
            </v-alert>
            <v-container v-if="userData">
              <v-row>
                <v-col
                  cols="6"
                  sm="3"
                  v-for="(value, key, i) in userData"
                  :key="i"
                >
                  <v-list-item two-line>
                    <v-list-item-content>
                      <v-list-item-title>{{ value }}</v-list-item-title>
                      <v-list-item-subtitle>{{ key }}</v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-col>
                <v-col cols="6" sm="3">
                  <v-btn text @click="userData = null" class="green--text">
                    Close
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col :loading="loading">
          <v-form
            @submit.prevent="saveUser"
            :loading="loading"
            v-model="valid"
            ref="form"
          >
            <v-card elevation="0">
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Name"
                        v-model="user.name"
                        :rules="[rules.required]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Username"
                        v-model="user.username"
                        :rules="[rules.required]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Email"
                        v-model="user.email"
                        :rules="[rules.required, rules.email]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-select
                        v-model="user.userRoles"
                        :items="ro
...[truncated]...

### client-frontend/src/components/admin/users/FindUsers.vue
<template>
  <v-card flat>
    <v-container>
      <v-row v-if="message">
        <v-col cols="12">
          <v-alert
            dense
            outlined
            dismissible
            transition="scale-transition"
            :type="isError ? 'error' : 'success'"
          >
            {{ message }}
          </v-alert>
        </v-col>
      </v-row>
      <v-row>
        <v-col :loading="loading">
          <v-container>
            <v-row>
              <v-col cols="12" sm="4">
                <v-text-field label="User ID" v-model="id"></v-text-field>
              </v-col>
              <v-col cols="12" sm="4">
                <v-btn
                  color="green"
                  dark
                  :disabled="!id"
                  text
                  @click="findUser"
                >
                  Search
                </v-btn>
              </v-col>
            </v-row>
          </v-container>
          <v-form v-model="valid" @submit.prevent="updateUser">
            <v-card v-if="user" class="elevation-5">
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="User Id"
                        v-model="user.id"
                        disabled
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Username"
                        v-model="user.username"
                        disabled
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Created At"
                        v-model="user.createdAt"
                        disabled
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Updated At"
                        v-model="user.updatedAt"
                        disabled
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
                        label="Name"
                        v-model="user.name"
                        :rules="[rules.required]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="4">
                      <v-text-field
             
...[truncated]...

### client-backend/src/main/java/com/dhitha/lms/clientbackend/controller/admin/ClientUserAdminController.java
package com.dhitha.lms.clientbackend.controller.admin;

import static com.dhitha.lms.clientbackend.util.Constants.DEFAULT_PWD;

import com.dhitha.lms.clientbackend.client.UserClient;
import com.dhitha.lms.clientbackend.dto.UserDTO;
import java.net.URI;
import java.util.List;
import javax.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

/**
 * REST controller for user service for admins
 *
 * @author Dhiraj
 */
@RestController
@RequestMapping("/admin/users")
@PreAuthorize("hasAuthority('ADMIN')")
@RequiredArgsConstructor
public class ClientUserAdminController {

  private final UserClient userClient;

  @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<List<UserDTO>> getAll() {
    return ResponseEntity.ok(userClient.getAll());
  }

  @GetMapping(value = "/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<UserDTO> get(@PathVariable Long id) {
    return ResponseEntity.ok(userClient.get(id));
  }

  @PostMapping(
      consumes = MediaType.APPLICATION_JSON_VALUE,
      produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<UserDTO> save(@RequestBody @Valid UserDTO userDTO) {
    userDTO.setPassword(DEFAULT_PWD);
    userDTO.setAccountNonExpired(true);
    userDTO.setCredentialsNonExpired(false);
    userDTO.setAccountNonLocked(true);
    userDTO.setEnabled(true);
    UserDTO dbUser = userClient.save(userDTO);
    URI uri =
        ServletUriComponentsBuilder.fromCurrentRequest()
            .path("/{id}")
            .buildAndExpand(dbUser.getId())
            .toUri();
    return ResponseEntity.created(uri).body(dbUser);
  }

  @PutMapping(
      value = "/{id}",
      consumes = MediaType.APPLICATION_JSON_VALUE,
      produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<UserDTO> update(@PathVariable Long id, @RequestBody UserDTO user) {
    return Respons
...[truncated]...