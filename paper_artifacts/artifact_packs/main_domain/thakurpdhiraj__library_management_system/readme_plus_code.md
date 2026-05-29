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

# Code snippets
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

### user/src/test/java/com/dhitha/lms/user/controller/UserControllerTest.java
package com.dhitha.lms.user.controller;

import static org.hamcrest.Matchers.hasSize;
import static org.hamcrest.Matchers.is;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.header;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import com.dhitha.lms.user.dto.UserDTO;
import com.fasterxml.jackson.databind.MapperFeature;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.Collections;
import org.junit.jupiter.api.DisplayName;
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
 * Integration tests {@link UserController}. Depends on the data-test.sql file
 *
 * @author Dhiraj
 */
@SpringBootTest
@AutoConfigureMockMvc
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
@ActiveProfiles("test")
class UserControllerTest {

  private final ObjectMapper objectMapper = new ObjectMapper();
  @Autowired private MockMvc mockMvc;

  @Value("${lms.client.key}")
  private String apiKey;

  @Test
  @DisplayName("Test if context loads")
  @Order(0)
  void contextLoads() {}

  @Test
  @DisplayName("get, find by id: invalid data, expected 404")
  @Order(1)
  void testGetUserNotFound() throws Exception {
    mockMvc
        .perform(get("/v1/{id}", 200).header("lms-key", apiKey))
        .andExpect(status().isNotFound());
  }

  @Test
  @DisplayName("get, find by id: valid data, expected 200")
  @Order(2)
  void testGetUserFound() throws Exception {
    mockMvc
        .perform(get("/v1/{id}", 1).header("lms-key", apiKey))
        .andExpect(status().isOk())
        .andExpect(jsonPath("$.id", is(1)))
        .andExpect(jsonP
...[truncated]...

### book/src/test/java/com/dhitha/lms/book/controller/CategoryControllerTest.java
package com.dhitha.lms.book.controller;

import static org.hamcrest.Matchers.hasSize;
import static org.hamcrest.Matchers.is;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

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
 * Integration Tests for {@link CategoryController}
 *
 * @author Dhiraj
 */
@SpringBootTest
@AutoConfigureMockMvc
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
@ActiveProfiles("test")
class CategoryControllerTest {

  @Autowired private MockMvc mockMvc;

  @Value("${lms.client.key}")
  private String apiKey;

  @Test
  @Order(0)
  void testFindAll() throws Exception {
    mockMvc
        .perform(
            get("/categories/v1")
                .header("lms-key", apiKey)
                .accept(MediaType.APPLICATION_JSON_VALUE))
        .andExpect(status().isOk())
        .andExpect(jsonPath("$", hasSize(2)));
  }

  @Test
  @Order(1)
  void testFindById() throws Exception {
    mockMvc
        .perform(
            get("/categories/v1/1")
                .header("lms-key", apiKey)
                .accept(MediaType.APPLICATION_JSON_VALUE))
        .andExpect(status().isOk())
        .andExpect(jsonPath("$.id", is(1)))
        .andExpect(jsonPath("$.name", is("TECHNOLOGY")));
  }

  @Test
  @Order(2)
  void testFindByIdNotFound() throws Exception {
    mockMvc
        .perform(
            get("/categories/v1/404")
                .header("lms-key", apiKey)
                .accept(MediaType.APPLICATION_JSON_VALUE))
        .andExpect(status().isNotFound());
  }

  @Test
  @Order(3)
  void testSave() throws Exception {
    moc
...[truncated]...

### order/src/test/java/com/dhitha/lms/order/controller/BookOrderControllerTest.java
package com.dhitha.lms.order.controller;

import static org.hamcrest.Matchers.hasSize;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.notNullValue;
import static org.hamcrest.Matchers.nullValue;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.header;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import com.dhitha.lms.order.dto.BookOrderDTO;
import com.dhitha.lms.order.dto.InventoryDTO;
import com.dhitha.lms.order.error.GenericException;
import com.dhitha.lms.order.service.InventoryService;
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
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;

/**
 * Integration tests for {@link BookOrderController}. Depends on src/test/resources/data-test.sql
 *
 * @author Dhiraj
 */
@SpringBootTest
@AutoConfigureMockMvc
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
@ActiveProfiles("test")
class BookOrderControllerTest {

  @MockBean private InventoryService inventoryService;

  @Autowired private ObjectMapper objectMapper;

  @Autowired private MockMvc mockMvc;

  @Value("${lms.client.key}")
  private String apiKey;

  @Test
  @Order(0)
  @DisplayName("get, findById: Test api without api key authentication, expected 403")
  void testAuthenticationApiKey() throws Exception {
    mockMvc.perform(get("/v1/{id}", 1)).andExpect(status().isForbidden());
  }

  @Test
  @Order(1)
  @DisplayName("get, findById: Find order by id, expected 200")
  void testFindById() throws
...[truncated]...

### auth/src/test/java/com/dhitha/lms/auth/controller/AuthControllerTest.java
package com.dhitha.lms.auth.controller;

import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import com.dhitha.lms.auth.TestUtils;
import com.dhitha.lms.auth.client.UserClient;
import com.dhitha.lms.auth.dto.AuthRequestDTO;
import com.dhitha.lms.auth.dto.AuthResponseDTO;
import com.fasterxml.jackson.databind.ObjectMapper;
import feign.FeignException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;

/**
 * Integration Tests for {@link AuthController}
 *
 * @author Dhiraj
 */
@SpringBootTest
@AutoConfigureMockMvc
@ActiveProfiles("test")
class AuthControllerTest {

  private final ObjectMapper objectMapper = new ObjectMapper();

  @Autowired private MockMvc mockMvc;

  @MockBean private UserClient mockUserClient;

  @Value("${lms.client.key}")
  private String apiKey;

  @Test
  @DisplayName("post, authenticateUser: valid input no api key, expected 403")
  void testAuthenticateWithoutApiKey() throws Exception {
    AuthRequestDTO mockRequest = new AuthRequestDTO("admin", "pass");
    when(mockUserClient.getByCredentials(mockRequest)).thenReturn(TestUtils.createMockUser());
    mockMvc
        .perform(
            post("/v1/token/authenticate")
                .content(objectMapper.writeValueAsString(mockRequest))
                .contentType(MediaType.APPLICATION_JSON_VALUE)
                .accept(MediaType.APPLICATION_JSON_VALUE))
        .andExpect(status().isForbidden());
  }

  @Test
  @DisplayName("post, authenticateUser: valid input invalid api key, expected 403")
  void testAuthenticateInvalidApiKey() throws Exception {
    AuthRequestDTO mockRequest = new AuthRequestDTO("admin", "password");
    when(mockUserClient.getByCredentials(mockRequest)).thenThrow(FeignException.NotFound.class);
    mockMvc
        .perform(
            post("/v1/token/authenticate")
                .header("lms-key", "invalid")
                .content(objectMapper.w
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

### client-frontend/src/views/UserView.vue
<template>
  <v-container class="pa-0">
    <v-row v-if="errorMessage">
      <v-col cols="12">
        <v-alert dense outlined transition="scale-transition" type="error">
          {{
            errorMessage
              ? errorMessage
              : "Something went wrong. Please try again!"
          }}
        </v-alert>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <Tabs :tabs="tabs" :right="true" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Tabs from "@/components/common/Tabs";
import MyOrdersPage from "@/components/user/orders/MyOrdersPage";
import AccountPage from "@/components/user/account/AccountPage";
export default {
  methods: {},
  components: {
    Tabs
  },
  computed: {
    errorMessage() {
      return this.$store.getters.getErrorMessage;
    }
  },
  data() {
    return {
      tabs: [
        {
          id: 0,
          name: "Orders",
          icon: "mdi-book-multiple",
          component: MyOrdersPage
        },
        {
          id: 1,
          name: "Account",
          icon: "mdi-account-edit",
          component: AccountPage
        }
      ]
    };
  }
};
</script>

### client-frontend/src/views/AdminView.vue
<template>
  <v-container class="px-0">
    <v-row v-if="errorMessage" class="mt-3">
      <v-col cols="12">
        <v-alert
          dense
          outlined
          dismissible
          transition="scale-transition"
          type="error"
        >
          {{
            errorMessage
              ? errorMessage
              : "Something went wrong. Please try again!"
          }}
        </v-alert>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <Tabs :tabs="tabs" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Tabs from "@/components/common/Tabs";
import OrderPage from "@/components/admin/orders/OrderPage";
import UserPage from "@/components/admin/users/UserPage";
import BookPage from "@/components/admin/books/BookPage";
import AccountPage from "@/components/user/account/AccountPage";
export default {
  methods: {},
  components: {
    Tabs
  },
  computed: {
    errorMessage() {
      return this.$store.getters.getErrorMessage;
    }
  },
  data() {
    return {
      tabs: [
        {
          id: 0,
          name: "Orders",
          icon: "mdi-book-multiple",
          component: OrderPage
        },
        {
          id: 1,
          name: "Books",
          icon: "mdi-book-open-page-variant",
          component: BookPage
        },
        {
          id: 2,
          name: "Users",
          icon: "mdi-account-multiple",
          component: UserPage
        },
        {
          id: 3,
          name: "Account",
          icon: "mdi-account-edit",
          component: AccountPage
        }
      ]
    };
  }
};
</script>

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

### user/src/test/java/com/dhitha/lms/user/service/UserServiceTest.java
package com.dhitha.lms.user.service;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyLong;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.doThrow;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import com.dhitha.lms.user.dto.UserDTO;
import com.dhitha.lms.user.entity.User;
import com.dhitha.lms.user.error.GenericException;
import com.dhitha.lms.user.error.UserNotFoundException;
import com.dhitha.lms.user.repository.UserRepository;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.Spy;
import org.mockito.junit.jupiter.MockitoExtension;
import org.modelmapper.ModelMapper;
import org.springframework.dao.DataIntegrityViolationException;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

/**
 * Unit tests for {@link UserService}
 *
 * @author Dhiraj
 */
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

  private static final String ENCODED_PASS =
      "$2y$10$NzzC81zVp.Wn6WvtCMW/t.dg4tbvErIUzAwwdy0uC4PgycdeUAw0K";

  private final ModelMapper modelMapper = new ModelMapper();

  @Spy private final PasswordEncoder passwordEncoder = new BCryptPasswordEncoder();

  @Mock private UserRepository userRepositoryMock;

  private UserService subject;

  @BeforeEach
  void init() {
    subject = new UserServiceImpl(userRepositoryMock, modelMapper, passwordEncoder);
  }

  /* ********************** findByCredentials ************************** */
  @Test
  @DisplayName("findByCredentials: valid input happy flow, expected success")
  void testFindByCredentials() throws Exception {
    when(userRepositoryMock.findByUsername("username"))
        .thenReturn(createMockOptionalUser(1L, "user"));
    UserDTO result = subject.findByCredentials("username", "pass");
    assertE
...[truncated]...

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

### user/src/main/java/com/dhitha/lms/user/controller/UserController.java
package com.dhitha.lms.user.controller;

import com.dhitha.lms.user.dto.UserDTO;
import com.dhitha.lms.user.error.GenericException;
import com.dhitha.lms.user.error.UserNotFoundException;
import com.dhitha.lms.user.service.UserService;
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
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

/**
 * REST Controller for {@link UserDTO}
 *
 * @author Dhiraj
 */
@RestController
@RequestMapping("/v1")
@RequiredArgsConstructor
public class UserController {
  private final UserService userService;

  @PostMapping(
      value = "/validate",
      consumes = MediaType.APPLICATION_JSON_VALUE,
      produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<UserDTO> getByCredentials(@RequestBody UserDTO user)
      throws UserNotFoundException {
    UserDTO dbUser = userService.findByCredentials(user.getUsername(), user.getPassword());
    return ResponseEntity.ok(dbUser);
  }

  @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<List<UserDTO>> getAll() {
    return ResponseEntity.ok(userService.findAll());
  }

  @GetMapping(value = "/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<UserDTO> get(@PathVariable Long id) throws UserNotFoundException {
    UserDTO user = userService.findById(id);
    return ResponseEntity.ok(user);
  }

  @PostMapping(
      consumes = MediaType.APPLICATION_JSON_VALUE,
      produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<UserDTO> save(@RequestBody @Valid UserDTO user) throws GenericException {
    UserDTO dbUser = userService.save(user);
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
     
...[truncated]...

### book/src/test/java/com/dhitha/lms/book/service/CategoryServiceTest.java
package com.dhitha.lms.book.service;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.doThrow;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import com.dhitha.lms.book.dto.CategoryDTO;
import com.dhitha.lms.book.entity.Category;
import com.dhitha.lms.book.error.CategoryNotFoundException;
import com.dhitha.lms.book.repository.CategoryRepository;
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

/**
 * Unit tests for {@link CategoryService}
 *
 * @author Dhiraj
 */
@ExtendWith(MockitoExtension.class)
class CategoryServiceTest {

  private final ModelMapper modelMapper = new ModelMapper();
  @Mock private CategoryRepository categoryRepositoryMock;
  private CategoryService subject;

  @BeforeEach
  void init() {
    subject = new CategoryServiceImpl(categoryRepositoryMock, modelMapper);
  }

  /* ******************** findById **************************** */
  @Test
  void testFindById() throws Exception {
    when(categoryRepositoryMock.findById(1)).thenReturn(Optional.of(new Category(1, "CAT", null)));
    CategoryDTO result = subject.findById(1);
    verify(categoryRepositoryMock).findById(1);
    assertEquals("CAT", result.getName());
  }

  @Test
  void testFindByIdThrowsCategoryNotFoundException() {
    assertThrows(
        CategoryNotFoundException.class,
        () -> {
          when(categoryRepositoryMock.findById(1)).thenReturn(Optional.empty());
          subject.findById(1);
        });
    verify(categoryRepositoryMock).findById(1);
  }

  /* ******************** findAll **************************** */
  @Test
  void testFindAll() {
    when(categoryRepositoryMock.findAll())
        .thenReturn(Collections.singletonList(new Category(1, "CAT", null)));
    List<CategoryDTO> result = subject.findAll();
    assertThat(result).hasSize(1).contains(new CategoryDTO(1, "CAT"));
  }

  /* ******************** save **************************** */
  @Test
  void testSave() throws Exception {
    w
...[truncated]...

### book/src/main/java/com/dhitha/lms/book/controller/CategoryController.java
package com.dhitha.lms.book.controller;

import com.dhitha.lms.book.dto.CategoryDTO;
import com.dhitha.lms.book.error.CategoryNotFoundException;
import com.dhitha.lms.book.error.GenericException;
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
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

/**
 * REST controller for {@link com.dhitha.lms.book.entity.Category}
 *
 * @author Dhiraj
 */
@RestController
@RequestMapping("/categories/v1")
@RequiredArgsConstructor
public class CategoryController {

  private final CategoryService categoryService;

  @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<List<CategoryDTO>> findAll() {
    return ResponseEntity.ok(categoryService.findAll());
  }

  @GetMapping(value = "/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<CategoryDTO> findById(@PathVariable Integer id)
      throws CategoryNotFoundException {
    return ResponseEntity.ok(categoryService.findById(id));
  }

  @PostMapping(
      consumes = MediaType.APPLICATION_JSON_VALUE,
      produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<CategoryDTO> save(@Valid @RequestBody CategoryDTO categoryDTO)
      throws GenericException {
    CategoryDTO savedCategory = categoryService.save(categoryDTO);
    URI uri =
        ServletUriComponentsBuilder.fromCurrentRequest()
            .path("/{id}")
            .buildAndExpand(savedCategory.getId())
            .toUri();
    return ResponseEntity.created(uri).body(savedCategory);
  }

  @PutMapping(
      value = "/{id}",
      consumes = MediaType.APPLICATION_JSON_VALUE,
      produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<CategoryDTO> update(
      @PathVariable Integer id, @Valid @RequestBody CategoryDTO categoryDTO)
      throws CategoryNotFoundException, GenericException {
    categoryDTO.setId(id);
    retur
...[truncated]...

### order/src/test/java/com/dhitha/lms/order/service/BookOrderServiceTest.java
package com.dhitha.lms.order.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyLong;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.doThrow;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import com.dhitha.lms.order.dto.BookOrderDTO;
import com.dhitha.lms.order.dto.InventoryDTO;
import com.dhitha.lms.order.enti
...[truncated]...