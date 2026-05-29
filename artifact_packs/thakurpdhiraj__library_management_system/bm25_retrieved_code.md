# README-derived retrieval query
thakurpdhiraj library management system ## README.md
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
    ![All- Login](https://github.com/thakurpdhiraj/projectscreenshots/blob/master/Project_Screenshot/library_management_system/login.jpeg "Login") README.md
auth/pom.xml
auth/src/main/java/com/dhitha/lms/auth/AuthApplication.java
auth/src/main/java
...[truncated]...

# BM25 selected code snippets
### README.md
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
    ![Admin- Search Order History](https://github.com/thakurpdhiraj/projectscr
...[truncated]...

### order/src/main/java/com/dhitha/lms/order/service/BookOrderService.java
package com.dhitha.lms.order.service;

import com.dhitha.lms.order.dto.BookOrderDTO;
import com.dhitha.lms.order.entity.BookOrder;
import com.dhitha.lms.order.error.GenericException;
import com.dhitha.lms.order.error.OrderNotFoundException;
import java.util.List;

/**
 * Service for {@link BookOrder}
 *
 * @author Dhiraj
 */
public interface BookOrderService {

  /**
   * Find a book order by id
   *
   * @param id - order id
   * @return order details
   * @throws OrderNotFoundException if no order present with corresponding id
   */
  BookOrderDTO findById(Long id) throws OrderNotFoundException;

  /**
   * Find all orders of a user
   *
   * @param userId -
   * @return list of orders or empty list if none found
   */
  List<BookOrderDTO> findAllByUser(Long userId);

  /**
   * Find all orders for a book
   *
   * @param bookId -
   * @return list of orders or empty list if none found
   */
  List<BookOrderDTO> findAllByBook(Long bookId);

  /**
   * Find all orders for which the returned date is overdue
   *
   * @return list of
   */
  List<BookOrderDTO> findAllReturnOverdue();

  /**
   * Find all orders for which the returned date is overdue for a user
   *
   * @param userId
   * @return
   */
  List<BookOrderDTO> findAllReturnOverdueForUser(Long userId);

  /**
   * Find all order for which collection date is overdue
   *
   * @return
   */
  List<BookOrderDTO> findAllCollectionOverdue();

  /**
   * Find all orders for which collection date is overdue for a user
   *
   * @param userId
   * @return
   */
  List<BookOrderDTO> findAllCollectionOverdueForUser(Long userId);

  /**
   * Order a new book, Connects with Inventory service to fnd if book is available
   *
   * @param orderDTO order details to add if possible
   * @return new order with generated id
   * @throws GenericException if order cannot be placed due to book/service unavailability
   */
  BookOrderDTO orderBook(BookOrderDTO orderDTO) throws GenericException;

  /**
   * Mark a order as collected
   *
   * @param id - order id
   * @return order detail with collectedAt date marked as present datetime
   * @throws OrderNotFoundException if no order present with id
   */
  BookOrderDTO collectBook(Long id) throws OrderNotFoundException;

  /**
   * Mark the book as returned, Connects with inventory servie to return the book and deletes the
   * order and adds it to order history
   *
   * @param id order id
   * @throws OrderNotFoundException if no order present with id
   * @throws GenericException if order cannot be returned due to book/service unavailability
   */
  BookOrderDTO 
...[truncated]...

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

### inventory/src/main/java/com/dhitha/lms/inventory/service/InventoryService.java
package com.dhitha.lms.inventory.service;

import com.dhitha.lms.inventory.dto.InventoryDTO;
import com.dhitha.lms.inventory.error.GenericException;
import com.dhitha.lms.inventory.error.InventoryNotFoundException;
import java.util.List;

/**
 * Service for {@link InventoryDTO}
 *
 * @author Dhiraj
 */
public interface InventoryService {

  /**
   * Find all inventory details by book id
   *
   * @param bookId -
   * @return List of inventory for existing book id
   */
  List<InventoryDTO> findAllBook(Long bookId);

  /**
   * Check if any book reference for a book id is available in LMS If yes mark the first book as
   * unavailable and return the marked book
   *
   * @param bookId -
   * @return first available book
   * @throws InventoryNotFoundException if none of the books are available for a book id
   */
  InventoryDTO orderBookIfAvailable(Long bookId) throws InventoryNotFoundException;

  /**
   * Mark the book with corresponding reference as available in inventory
   *
   * @param bookId -
   * @param bookReferenceId -
   * @return true if book is present in LMS and marking the book as available was successful
   */
  boolean returnBook(Long bookId, String bookReferenceId);

  /**
   * Count of books available
   *
   * @param bookId -
   * @return total number of book available for requested book id
   */
  long getAvailableCount(Long bookId);

  /**
   * Add {@literal 'count'} number of books. Generates unique reference number for each book
   *
   * @param inventory DTO containing the book id , isbn , category for the new book
   * @param count total inventory to add
   * @throws GenericException if a book with combination of book id and book reference is already
   *     present
   */
  List<InventoryDTO> add(InventoryDTO inventory, Integer count) throws GenericException;

  /**
   * Delete an inventory of all books by book id
   *
   * @param bookId -
   * @throws InventoryNotFoundException if no inventory present with book id
   */
  void delete(Long bookId) throws InventoryNotFoundException;

  /**
   * Delete specific book reference of a book type
   *
   * @param bookId -
   * @param bookReferenceId -
   * @throws InventoryNotFoundException in case no book is present wih combination of book id and
   *     book reference id
   */
  void delete(Long bookId, List<String> bookReferenceId) throws InventoryNotFoundException;
}

### auth/src/main/java/com/dhitha/lms/auth/service/AuthServiceImpl.java
package com.dhitha.lms.auth.service;

import com.dhitha.lms.auth.client.UserClient;
import com.dhitha.lms.auth.dto.AuthRequestDTO;
import com.dhitha.lms.auth.dto.AuthResponseDTO;
import com.dhitha.lms.auth.dto.UserDTO;
import com.dhitha.lms.auth.error.GenericException;
import com.nimbusds.jwt.JWTClaimsSet;
import feign.FeignException;
import feign.FeignException.FeignClientException;
import java.text.ParseException;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;

/**
 * Implementation for {@link AuthService}
 *
 * @author Dhiraj
 */
@Service
@RequiredArgsConstructor
@Log4j2
public class AuthServiceImpl implements AuthService {

  private final UserClient userClient;

  private final TokenService tokenService;

  @Override
  public AuthResponseDTO authenticate(AuthRequestDTO authDTO) throws GenericException {
    try {
      UserDTO userDTO = userClient.getByCredentials(authDTO);
      //TODO: Check for account expired, enabled and other details
      String idToken = tokenService.generateIdToken(userDTO);
      StringTokenizer stringTokenizer = new StringTokenizer(idToken, "\\.");
      return AuthResponseDTO.builder()
          .header(stringTokenizer.nextToken())
          .payload(stringTokenizer.nextToken())
          .signature(stringTokenizer.nextToken())
          .userDTO(userDTO)
          .build();
    } catch (FeignException.NotFound e) {
      log.warn("authenticate:(AuthRequestDTO) -> Invalid Credentials");
      // if below status is changed to 401, check https://github.com/OpenFeign/feign/issues/260
      // feign cannot send the response body which results in empty response
      throw new GenericException("Invalid Username / Password", HttpStatus.NOT_FOUND.value());
    } catch (NoSuchElementException | FeignClientException e) {
      log.error("authenticate:(AuthRequestDTO) ->  Error connecting to User Service: ", e);
      throw new GenericException();
    }
  }

  @Override
  public AuthResponseDTO verifyToken(String token) throws GenericException {
    JWTClaimsSet jwtClaimsSet = tokenService.verifyToken(token);
    log.info("Verification ClaimSet: {}", jwtClaimsSet.toJSONObject(true));

    try {
      UserDTO userDTO = new UserDTO();
      userDTO.setId(Long.valueOf(jwtClaimsSet.getSubject()));
      if (jwtClaimsSet.getStringClaim("roles") != null) {
        userDTO.setUserRoles(Arrays.asList(jwtClaimsSet.getStringCl
...[truncated]...

### server/pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.3.4.RELEASE</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.dhitha.lms</groupId>
	<artifactId>server</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>server</name>
	<description>Eureka Server for Library Management System</description>

	<properties>
		<java.version>11</java.version>
		<spring-cloud.version>Hoxton.SR8</spring-cloud.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
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
	</dependencies>

	<dependencyManagement>
		<dependencies>
			<dependency>
				<groupId>org.springframework.cloud</groupId>
				<artifactId>spring-cloud-dependencies</artifactId>
				<version>${spring-cloud.version}</version>
				<type>pom</type>
				<scope>import</scope>
			</dependency>
		</dependencies>
	</dependencyManagement>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>

	<repositories>
		<repository>
			<id>spring-milestones</id>
			<name>Spring Milestones</name>
			<url>https://repo.spring.io/milestone</url>
		</repository>
	</repositories>

</project>

### book/src/main/java/com/dhitha/lms/book/service/CategoryService.java
package com.dhitha.lms.book.service;

import com.dhitha.lms.book.dto.CategoryDTO;
import com.dhitha.lms.book.error.CategoryNotFoundException;
import com.dhitha.lms.book.error.GenericException;
import java.util.List;

/**
 * Service for {@link CategoryDTO}
 *
 * @author Dhiraj
 */
public interface CategoryService {

  /**
   * Find Category by ID
   *
   * @param id -
   * @return category corresponding to the id
   * @throws CategoryNotFoundException in case no category exists with id
   */
  CategoryDTO findById(Integer id) throws CategoryNotFoundException;

  /**
   * Find all category in LMS
   *
   * @return list of category
   */
  List<CategoryDTO> findAll();

  /**
   * Add a new Category with unique name
   *
   * @param categoryDTO - new category to persist
   * @return added category with new generated id
   * @throws GenericException if category with same name present
   */
  CategoryDTO save(CategoryDTO categoryDTO) throws GenericException;

  /**
   * Update an existing category
   *
   * @param categoryDTO category to update, id must not be null
   * @return updated category, null values are ignored
   * @throws CategoryNotFoundException in case no category exists with id
   * @throws GenericException if name of category is changed and category with same name exists
   */
  CategoryDTO update(CategoryDTO categoryDTO) throws CategoryNotFoundException, GenericException;

  /**
   * Delete a category
   *
   * @param id -
   * @throws CategoryNotFoundException in case no category exists with id
   */
  void delete(Integer id) throws CategoryNotFoundException;
}

### user/src/main/java/com/dhitha/lms/user/service/UserService.java
package com.dhitha.lms.user.service;

import com.dhitha.lms.user.dto.UserDTO;
import com.dhitha.lms.user.error.GenericException;
import com.dhitha.lms.user.error.UserNotFoundException;
import java.util.List;

/**
 * Service class for {@link UserDTO}
 *
 * @author Dhiraj
 */
public interface UserService {

  /**
   * Find and validate the user's credentials
   * @param username username of user
   * @param password raw password to validate
   * @return user matching the credentials
   * @throws UserNotFoundException if no user exists or credentials are incorrect
   */
  UserDTO findByCredentials(String username,String password) throws UserNotFoundException;

  /**
   * Find all users in LMS
   * @return list of users
   */
  List<UserDTO> findAll();

  /**
   * Find a user by id
   *
   * @param id unique identifier
   * @return user corresponding to the id
   * @throws UserNotFoundException if no user exists with id
   */
  UserDTO findById(Long id) throws UserNotFoundException;

  /**
   * Find a user by id
   *
   * @param username unique identifier
   * @return user corresponding to the username
   * @throws UserNotFoundException if no user exists with username
   */
  UserDTO findByUserName(String username) throws UserNotFoundException;

  /**
   * Save a user
   *
   * @param user user to save
   * @return saved user with new id
   */
  UserDTO save(UserDTO user) throws GenericException;

  /**
   * Update a user
   *
   * @param user user to update with null properties ignored
   * @return updated user
   * @throws UserNotFoundException if no user exists with id of passed user
   */
  UserDTO update(UserDTO user) throws UserNotFoundException;

  /**
   * Delete a user
   *
   * @param id id of user to delete
   * @throws UserNotFoundException if no user with id exists
   */
  void delete(Long id) throws UserNotFoundException;
}

### client-frontend/src/components/user/orders/neworder/NewOrder.vue
<template>
  <v-dialog v-model="dialog" fullscreen persistent overlay-opacity="1">
    <template v-slot:activator="{ on, attrs }">
      <v-btn dark color="deep-purple darken-4" v-bind="attrs" v-on="on">
        <v-icon left dark>
          mdi-book-plus
        </v-icon>
        New Order
      </v-btn>
    </template>
    <!-- Re render on open-->
    <v-card v-if="dialog">
      <v-toolbar flat>
        <v-toolbar-title>New Order</v-toolbar-title>
        <v-divider class="mx-5" inset vertical></v-divider>
        <v-spacer />
        <h3 v-if="$vuetify.breakpoint.mobile && stepNumber === 1">
          Choose Book
        </h3>
        <h3 v-if="$vuetify.breakpoint.mobile && stepNumber === 2">
          Search Inventory
        </h3>
        <h3 v-if="$vuetify.breakpoint.mobile && stepNumber === 3">
          Finalize Order
        </h3>
        <v-spacer />
        <v-btn icon @click="close">
          <v-icon>mdi-close-circle</v-icon>
        </v-btn>
      </v-toolbar>
      <v-alert
        dense
        outlined
        type="error"
        transition="scale-transition"
        v-if="errorMessage"
      >
        {{
          errorMessage
            ? errorMessage
            : "Something went wrong. Please try again!"
        }}
      </v-alert>
      <v-stepper v-model="stepNumber">
        <v-stepper-header>
          <v-stepper-step :complete="stepNumber > 1" step="1" color="green">
            Choose Book
          </v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step :complete="stepNumber > 2" step="2" color="green">
            Search Inventory
          </v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step step="3" color="green">
            Finalize Order
          </v-stepper-step>
        </v-stepper-header>

        <v-stepper-items>
          <!-- Choose Book -->
          <v-stepper-content step="1" class="pa-2">
            <ChooseBook @searchInventory="searchInventory" />
          </v-stepper-content>
          <!-- Search Inventory -->
          <v-stepper-content step="2">
            <SearchInventory
              :selectedNewBook="selectedNewBook"
              @goBack="goBack"
              @finalizeOrder="finalizeOrder"
            />
          </v-stepper-content>
          <!-- Order Book -->
          <v-stepper-content step="3">
            <OrderBook
              :selectedNewBook="selectedNewBook"
              @goBack="goBack"
              @orderBook="orderBook"
            />
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-card>
 
...[truncated]...

### client-backend/src/main/java/com/dhitha/lms/clientbackend/controller/ClientAuthController.java
package com.dhitha.lms.clientbackend.controller;

import com.dhitha.lms.clientbackend.client.AuthClient;
import com.dhitha.lms.clientbackend.dto.AuthRequestDTO;
import com.dhitha.lms.clientbackend.dto.AuthResponseDTO;
import com.dhitha.lms.clientbackend.dto.UserDTO;
import com.dhitha.lms.clientbackend.util.Constants;
import com.dhitha.lms.clientbackend.util.CookieUtil;
import javax.servlet.http.HttpServletResponse;
import javax.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Authentication Controller for Login
 *
 * <p>Logout is handled in {@link com.dhitha.lms.clientbackend.config.SecurityConfig}
 *
 * @author Dhiraj
 */
@RestController
@RequiredArgsConstructor
public class ClientAuthController {

  private final AuthClient authClient;

  @PreAuthorize("permitAll()")
  @PostMapping(
      value = "/login",
      produces = MediaType.APPLICATION_JSON_VALUE,
      consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
  public ResponseEntity<?> authenticateUser(
      @Valid AuthRequestDTO authDTO, HttpServletResponse response) {
    AuthResponseDTO authResponseDTO = authClient.authenticateUser(authDTO);
    String idToken = authResponseDTO.getHeader() + "." + authResponseDTO.getPayload();
    CookieUtil.addCookie(Constants.ID_COOKIE_NAME, idToken, false, response);
    CookieUtil.addCookie(
        Constants.SIGNATURE_COOKIE_NAME, authResponseDTO.getSignature(), true, response);
    UserDTO userDTO = authResponseDTO.getUserDTO();
    return ResponseEntity.ok(userDTO);
  }
}

### client-frontend/README.md
# client-frontend

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your unit tests
```
npm run test:unit
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### client-frontend/src/router/router.js
import Vue from "vue";
import VueRouter from "vue-router";
import store from "@/store/store";
import * as util from "@/util/authUtil";

import UserView from "@/views/UserView.vue";
import LoginView from "@/views/LoginView.vue";
import AdminView from "@/views/AdminView.vue";
import ErrorView from "@/views/ErrorView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "UserView",
    component: UserView,
    meta: {
      reqAuth: true,
      reqRole: "USER"
    }
  },
  {
    path: "/admin*",
    name: "AdminView",
    component: AdminView,
    meta: {
      reqAuth: true,
      reqRole: "ADMIN"
    }
  },
  {
    path: "/login",
    name: "LoginView",
    component: LoginView,
    meta: {
      reqAuth: false,
      reqRole: "ANY"
    }
  },
  {
    path: "/error",
    name: "ErrorView",
    component: ErrorView,
    meta: {
      reqAuth: false,
      reqRole: "ANY"
    }
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.reqAuth)) {
    if (!util.isAuthenticated()) {
      next({
        path: "/login",
        query: { redirect: to.fullPath }
      });
    } else {
      if (to.matched.some(record => record.meta.reqRole == "ADMIN")) {
        if (util.isAdmin()) {
          next();
        } else {
          store.commit("setErrorMessage", "Insufficient Privilege.");
          next("/error");
        }
      } else if (to.matched.some(record => record.meta.reqRole == "USER")) {
        if (!util.isAdmin()) {
          next();
        } else {
          next("/admin");
        }
      } else {
        next();
      }
    }
  } else {
    next();
  }
});

export default router;

### order/pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.3.4.RELEASE</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.dhitha.lms</groupId>
	<artifactId>order</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>order</name>
	<description>Orders for Library Management System</description>

	<properties>
		<java.version>11</java.version>
		<spring-cloud.version>Hoxton.SR8</spring-cloud.version>
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
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-openfeign</artifactId>
		</dependency>
		<dependency>
			<groupId>com.h2database</groupId>
			<artifactId>h2</artifactId>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>org.projectlombok</groupId>
			<artifactId>lombok</artifactId>
			<version>1.18.16</version>
		</dependency>
		<dependency>
			<groupId>org.modelmapper</groupId>
			<artifactId>modelmapper</artifactId>
			<version>2.3.8</version>
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

	<dependencyManagement>
		<dependencies>
			<dependency>
				<groupId>org.
...[truncated]...

### auth/pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.3.4.RELEASE</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.dhitha.lms</groupId>
	<artifactId>auth</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>auth</name>
	<description>Authentication Server for Library Management System</description>

	<properties>
		<java.version>11</java.version>
		<spring-cloud.version>Hoxton.SR8</spring-cloud.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-security</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-openfeign</artifactId>
		</dependency>
		<dependency>
			<groupId>com.nimbusds</groupId>
			<artifactId>nimbus-jose-jwt</artifactId>
			<version>8.20.1</version>
		</dependency>
		<dependency>
			<groupId>org.bouncycastle</groupId>
			<artifactId>bcprov-jdk15on</artifactId>
			<version>1.64</version>
		</dependency>
		<dependency>
			<groupId>org.bouncycastle</groupId>
			<artifactId>bcpkix-jdk15on</artifactId>
			<version>1.64</version>
		</dependency>
		<dependency>
			<groupId>org.projectlombok</groupId>
			<artifactId>lombok</artifactId>
			<version>1.18.16</version>
		</dependency>
		<dependency>
			<groupId>org.modelmapper</groupId>
			<artifactId>modelmapper</artifactId>
			<version>2.3.8</version>
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

	<dependencyManagement>
		<dependenc
...[truncated]...

### book/src/main/java/com/dhitha/lms/book/service/BookService.java
package com.dhitha.lms.book.service;

import com.dhitha.lms.book.dto.BookDTO;
import com.dhitha.lms.book.error.BookNotFoundException;
import java.util.List;

/**
 * Service for {@link BookDTO}
 *
 * @author Dhiraj
 */
public interface BookService {

  /**
   * Find all books in LMS
   *
   * @param bookDTO books to search
   * @return list of books
   */
  List<BookDTO> findAll(BookDTO bookDTO);

  /**
   * Find book with id
   *
   * @param id -
   * @return book corresponding to the id
   * @throws BookNotFoundException if no book exists with id
   */
  BookDTO findById(Long id) throws BookNotFoundException;

  /**
   * Save a book
   *
   * @param bookDTO book to save
   * @return saved book with new generated id
   */
  BookDTO save(BookDTO bookDTO);

  /**
   * Update a book
   *
   * @param bookDTO book to update, null values will be ignored
   * @return updated book
   * @throws BookNotFoundException if no book exists with id
   */
  BookDTO update(BookDTO bookDTO) throws BookNotFoundException;

  /**
   * Delete a book
   *
   * @param id -
   * @throws BookNotFoundException if no book exists with id
   */
  void delete(Long id) throws BookNotFoundException;
}

### user/pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>2.3.4.RELEASE</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>
	<groupId>com.dhitha.lms</groupId>
	<artifactId>user</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<name>user</name>
	<description>Users for Library Management System</description>

	<properties>
		<java.version>11</java.version>
		<spring-cloud.version>Hoxton.SR8</spring-cloud.version>
	</properties>

	<dependencies>
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
			<artifactId>spring-boot-starter-security</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.cloud</groupId>
			<artifactId>spring-cloud-starter-openfeign</artifactId>
		</dependency>
		<dependency>
			<groupId>com.h2database</groupId>
			<artifactId>h2</artifactId>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>org.projectlombok</groupId>
			<artifactId>lombok</artifactId>
			<version>1.18.16</version>
		</dependency>
		<dependency>
			<groupId>org.modelmapper</groupId>
			<artifactId>modelmapper</artifactId>
			<version>2.3.8</version>
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

	<dependencyManagement>
		<dependencies>
			<dependency>
				<groupId>org.spr
...[truncated]...

### client-backend/src/main/java/com/dhitha/lms/clientbackend/controller/ClientOrderController.java
package com.dhitha.lms.clientbackend.controller;

import com.dhitha.lms.clientbackend.client.OrderClient;
import com.dhitha.lms.clientbackend.dto.BookOrderDTO;
import com.dhitha.lms.clientbackend.dto.BookOrderHistoryDTO;
import com.dhitha.lms.clientbackend.dto.UserDTO;
import com.dhitha.lms.clientbackend.util.OrderUtil;
import java.net.URI;
import java.util.List;
import java.util.Map;
import lombok.RequiredArgsConstructor;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

/**
 * Controller for Orders
 *
 * @author Dhiraj
 */
@RestController
@RequestMapping("/orders")
@PreAuthorize("hasAuthority('USER')")
@RequiredArgsConstructor
public class ClientOrderController {

  private final OrderClient client;

  private final OrderUtil orderUtil;


  @GetMapping(value = "/me", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<List<BookOrderDTO>> findAllByUser(Authentication authentication) {
    UserDTO userDTO = (UserDTO)authentication.getPrincipal();
    List<BookOrderDTO> userOrders = client.findAllByUser(userDTO.getId());
    return ResponseEntity.ok(userOrders);
  }

  @GetMapping(value = "/me/history", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<List<BookOrderHistoryDTO>> findAllHistoryOfUser(Authentication authentication) {
    UserDTO userDTO = (UserDTO)authentication.getPrincipal();
    List<BookOrderHistoryDTO> userOrders = client.findAllHistoryOfUser(userDTO.getId());
    return ResponseEntity.ok(userOrders);
  }

  @GetMapping(value = "/me/overdue/return", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<List<BookOrderDTO>> findAllReturnOverdueOfUser(Authentication authentication) {
    UserDTO
...[truncated]...