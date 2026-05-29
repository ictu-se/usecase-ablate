# Deterministic random code snippets
### client-backend/src/main/java/com/dhitha/lms/clientbackend/client/OrderClient.java
package com.dhitha.lms.clientbackend.client;

import com.dhitha.lms.clientbackend.dto.BookOrderDTO;
import com.dhitha.lms.clientbackend.dto.BookOrderHistoryDTO;
import java.util.List;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;

/**
 * Client to connect to LMS-ORDER-SERVICE registered in the Eureka server with name {@literal
 * "lms-order-service"}
 *
 * @author Dhiraj
 */
@FeignClient(name = "lms-order-service", path = "/api/orders/v1/")
public interface OrderClient {

  @GetMapping(value = "/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
  BookOrderDTO findById(@PathVariable Long id);

  @GetMapping(value = "/users/{userId}", produces = MediaType.APPLICATION_JSON_VALUE)
  List<BookOrderDTO> findAllByUser(@PathVariable Long userId);

  @GetMapping(value = "/users/{userId}/history", produces = MediaType.APPLICATION_JSON_VALUE)
  List<BookOrderHistoryDTO> findAllHistoryOfUser(@PathVariable Long userId);

  @GetMapping(value = "/books/{bookId}", produces = MediaType.APPLICATION_JSON_VALUE)
  List<BookOrderDTO> findAllByBook(@PathVariable Long bookId);

  @GetMapping(value = "/overdue/return", produces = MediaType.APPLICATION_JSON_VALUE)
  List<BookOrderDTO> findAllReturnOverdue(
      @RequestParam(value = "userId", required = false) Long userId);

  @GetMapping(value = "/overdue/collect", produces = MediaType.APPLICATION_JSON_VALUE)
  List<BookOrderDTO> findAllCollectionOverdue(
      @RequestParam(value = "userId", required = false) Long userId);

  @PostMapping(
      produces = MediaType.APPLICATION_JSON_VALUE,
      consumes = MediaType.APPLICATION_JSON_VALUE)
  BookOrderDTO orderBook(@RequestBody BookOrderDTO orderDTO);

  @PutMapping(value = "/{id}/collect")
  BookOrderDTO collectBook(@PathVariable Long id);

  @PutMapping(value = "/{id}/return")
  BookOrderDTO returnBook(@PathVariable Long id);
}

### client-frontend/tests/unit/example.spec.js
import { expect } from "chai";
import { shallowMount } from "@vue/test-utils";
import HelloWorld from "@/components/HelloWorld.vue";

describe("HelloWorld.vue", () => {
  it("renders props.msg when passed", () => {
    const msg = "new message";
    const wrapper = shallowMount(HelloWorld, {
      propsData: { msg }
    });
    expect(wrapper.text()).to.include(msg);
  });
});

### user/src/main/java/com/dhitha/lms/user/dto/ErrorDTO.java
package com.dhitha.lms.user.dto;

import java.io.Serializable;
import java.time.LocalDateTime;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * Common DTO for all Errors
 *
 * @author Dhiraj
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ErrorDTO implements Serializable {
  private static final long serialVersionUID = 1L;

  private String error;

  private String error_description;

  private int status;

  private LocalDateTime timestamp;
}

### client-backend/src/main/java/com/dhitha/lms/clientbackend/dto/AuthRequestDTO.java
package com.dhitha.lms.clientbackend.dto;

import javax.validation.constraints.NotEmpty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author Dhiraj
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class AuthRequestDTO {
  @NotEmpty
  private String username;
  @NotEmpty
  private String password;
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

### client-frontend/src/service/user.js
import resource from "@/resource/resource";
import { sendResponse } from "@/util/responseUtil.js";

export const getAllUsers = async () => {
  let response = await resource.get("/admin/users");
  return sendResponse(response, 200);
};

export const getUser = async id => {
  let response = await resource.get(`/admin/users/${id}`);
  return sendResponse(response, 200);
};

export const saveUser = async user => {
  let response = await resource.post("/admin/users/", {
    name: user.name,
    email: user.email,
    username: user.username,
    userRoles: user.userRoles
  });
  return sendResponse(response, 201);
};

export const updateUser = async user => {
  let response = await resource.put(`/admin/users/${user.id}`, {
    name: user.name,
    email: user.email,
    enabled: user.enabled,
    userRoles: user.userRoles
  });
  return sendResponse(response, 200);
};

export const deleteUser = async id => {
  let response = await resource.delete(`/admin/users/${id}`);
  return sendResponse(response, 204);
};

export const getLoggedInUser = async () => {
  let response = await resource.get("/users/me");
  return sendResponse(response, 200);
};

export const updateMe = async user => {
  let response = await resource.put("/users/me", {
    name: user.name,
    email: user.email
  });
  return sendResponse(response, 200);
};

export const changePassword = async cred => {
  let response = await resource.post("/users/me/change-password", {
    password: cred.password
  });
  return sendResponse(response, 200);
};

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

### client-frontend/babel.config.js
module.exports = {
  presets: ["@vue/cli-plugin-babel/preset"]
};

### order/src/main/java/com/dhitha/lms/order/dto/InventoryDTO.java
package com.dhitha.lms.order.dto;

import java.io.Serializable;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * DTO for exchange with the Inventory Service
 *
 * @author Dhiraj
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class InventoryDTO implements Serializable {
  private static final long serialVersionUID = 1L;

  private Long bookId;

  private String isbn;

  private String bookReferenceId;

  private Integer categoryId;
}

### order/src/main/java/com/dhitha/lms/order/dto/BookOrderHistoryDTO.java
package com.dhitha.lms.order.dto;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonProperty.Access;
import java.io.Serializable;
import java.time.LocalDateTime;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * DTO for {@link com.dhitha.lms.order.entity.BookOrderHistory}
 *
 * @author Dhiraj
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class BookOrderHistoryDTO implements Serializable {
  private static final long serialVersionUID = 1L;
  private Long orderId;

  private Long userId;

  private Long bookId;

  private String bookIsbn;

  private String bookName;

  private String bookReferenceId;

  private LocalDateTime orderedAt;

  private LocalDateTime collectedAt;

  private LocalDateTime returnedAt;

  private Long lateFees;
}

### book/src/main/java/com/dhitha/lms/book/entity/Category.java
package com.dhitha.lms.book.entity;

import java.io.Serializable;
import java.util.List;
import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;

/**
 * Entity for Categories of {@link Book} in LMS
 *
 * @author Dhiraj
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "category")
public class Category implements Serializable {
  private static final long serialVersionUID = 1L;

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Integer id;

  @Column(name = "name", nullable = false, unique = true)
  private String name;

  @ToString.Exclude
  @EqualsAndHashCode.Exclude
  @OneToMany(mappedBy = "category", fetch = FetchType.LAZY, cascade = CascadeType.ALL)
  private List<Book> books;
}

### inventory/src/main/java/com/dhitha/lms/inventory/error/InventoryNotFoundException.java
package com.dhitha.lms.inventory.error;

/**
 * Exception in case no inventory available in LMS for provided input
 * @author Dhiraj
 */
public class InventoryNotFoundException extends Exception{

  public InventoryNotFoundException(String message) {
    super(message);
  }
}

### client-frontend/src/util/responseUtil.js
export const sendResponse = (response, status) => {
  if (response.status !== status) {
    throw new Error(response.data);
  } else {
    return response.data;
  }
};

### inventory/src/main/java/com/dhitha/lms/inventory/entity/InventoryId.java
package com.dhitha.lms.inventory.entity;

import java.io.Serializable;
import javax.persistence.Column;
import javax.persistence.Embeddable;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * Embeddable Id for {@link Inventory}
 * @author Dhiraj
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Embeddable
public class InventoryId implements Serializable {
    private static final long serialVersionUID = 1L;

    @Column(name = "book_id", updatable = false, nullable = false)
    private Long bookId;

    @Column(name = "isbn", updatable = false, nullable = false)
    private String isbn;

    @Column(name = "book_reference_id", updatable = false, nullable = false)
    private String bookReferenceId;
}

### order/src/main/java/com/dhitha/lms/order/repository/BookOrderRepository.java
package com.dhitha.lms.order.repository;

import com.dhitha.lms.order.entity.BookOrder;
import java.time.LocalDateTime;
import java.util.List;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Repository for {@link BookOrder}
 *
 * @author Dhiraj
 */
@Repository
public interface BookOrderRepository extends JpaRepository<BookOrder, Long> {

  /**
   * Find all orders for a book id
   *
   * @param bookId -
   * @return list of orders for a book id or empty list if none found
   */
  List<BookOrder> findByBookId(Long bookId);

  /**
   * Find all orders for a user id
   *
   * @param userId
   * @return list of orders for a user id or empty list if none found
   */
  List<BookOrder> findByUserId(Long userId);

  /**
   * Find all the orders of books that have returnBy date before the passed date
   *
   * @param currentDate -
   * @return list of orders or empty list if none found
   */
  List<BookOrder> findByReturnByBefore(LocalDateTime currentDate);

  /**
   * Find all the orders of books that have collectBy date before the passed date
   *
   * @param currentDate -
   * @return list of orders or empty list if none found
   */
  List<BookOrder> findByCollectByBefore(LocalDateTime currentDate);

  /**
   * Find all the orders of books that have returnBy date before the passed date for a user
   *
   * @param currentDate -
   * @param userId -
   * @return list of orders or empty list if none found
   */
  List<BookOrder> findByReturnByBeforeAndUserId(LocalDateTime currentDate, Long userId);

  /**
   * Find all the orders of books that have collectBy date before the passed date for a user
   *
   * @param currentDate -
   * @param userId -
   * @return list of orders or empty list if none found
   */
  List<BookOrder> findByCollectByBeforeAndUserId(LocalDateTime currentDate, Long userId);

  /**
   * Check if order exists for a user for a book
   *
   * @param userId -
   * @param bookId -
   * @return true if exists otherwise false
   */
  boolean existsByUserIdAndBookId(Long userId, Long bookId);
}

### auth/src/main/java/com/dhitha/lms/auth/dto/AuthResponseDTO.java
package com.dhitha.lms.auth.dto;

import java.io.Serializable;
import java.time.LocalDateTime;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/** @author Dhiraj */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AuthResponseDTO implements Serializable {
  private static final long serialVersionUID = 1L;

  private String header;

  private String payload;

  private String signature;

  private UserDTO userDTO;
}

### client-frontend/src/service/order.js
import resource from "@/resource/resource";
import { sendResponse } from "@/util/responseUtil.js";

export const getUsersOrder = async () => {
  let response = await resource.get("/orders/me");
  return sendResponse(response, 200);
};

export const getUsersOrderHistory = async () => {
  let response = await resource.get("/orders/me/history");
  return sendResponse(response, 200);
};

export const getUsersOrderReturnOverdue = async () => {
  let response = await resource.get("/orders/me/overdue/return");
  return sendResponse(response, 200);
};

export const getUsersOrderCollectionOverdue = async () => {
  let response = await resource.get("/orders/me/overdue/collect");
  return sendResponse(response, 200);
};

export const orderNewBook = async book => {
  let response = await resource.post("/orders/me", {
    bookId: book.id,
    bookIsbn: book.isbn,
    bookName: book.name
  });
  return sendResponse(response, 201);
};

export const findOrders = async (type, id) => {
  var response;
  switch (type) {
    case "order":
      response = await resource.get(`/admin/orders/${id}`);
      break;
    case "user":
      response = await resource.get(`/admin/orders/users/${id}`);
      break;
    case "book":
      response = await resource.get(`/admin/orders/books/${id}`);
      break;
  }
  return sendResponse(response, 200);
};

export const collectOrder = async id => {
  let response = await resource.put(`/admin/orders/${id}/collect`);
  return sendResponse(response, 200);
};

export const returnOrder = async id => {
  let response = await resource.put(`/admin/orders/${id}/return`);
  return sendResponse(response, 200);
};

export const findOrdersHistoryOfUser = async userId => {
  let response = await resource.get(`/admin/orders/users/${userId}/history`);
  return sendResponse(response, 200);
};

export const findOrderOverdue = async (type, userType, userId) => {
  let response;
  switch (type) {
    case "collection":
      if (userType == "user") {
        response = await resource.get(
          `/admin/orders/users/${userId}/overdue/collect`
        );
      } else {
        response = await resource.get(`/admin/orders/overdue/collect`);
      }
      break;
    case "return":
      if (userType == "user") {
        response = await resource.get(
          `/admin/orders/users/${userId}/overdue/return`
        );
      } else {
        response = await resource.get(`/admin/orders/overdue/return`);
      }
      break;
  }
  return sendResponse(response, 200);
};

### inventory/src/main/java/com/dhitha/lms/inventory/entity/Inventory.java
package com.dhitha.lms.inventory.entity;

import java.io.Serializable;
import javax.persistence.Column;
import javax.persistence.EmbeddedId;
import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.UniqueConstraint;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * Entity to represent inventory in LMS
 *
 * @author Dhiraj
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Entity
@Table(
    name = "inventory",
    uniqueConstraints =
        @UniqueConstraint(
            name = "unique_id_reference",
            columnNames = {"book_id", "isbn", "book_reference_id"}))
public class Inventory implements Serializable {
  private static final long serialVersionUID = 1L;

  @EmbeddedId private InventoryId id;

  @Column(name = "category_id", updatable = false)
  private Integer categoryId;

  @Column(name = "available", columnDefinition = "BIT(1) DEFAULT 1")
  private Boolean available;
}

### client-frontend/src/resource/resource.js
import axios from "axios";
import router from "@/router/router";
import store from "@/store/store";
import * as util from "@/util/authUtil";

const axiosInstance = axios.create({
  baseURL: "http://localhost:8086/lms",
  withCredentials: true,
  timeout: 10000
});

axiosInstance.interceptors.request.use(config => {
  store.commit("setErrorMessage", null);
  if (config.url === "/login") {
    return config;
  } else {
    if (util.isAuthenticated()) {
      if (config.url.startsWith("/admin")) {
        if (util.isAdmin()) {
          return config;
        } else {
          store.commit(
            "setErrorMessage",
            "Not enough permission to access resource"
          );
          return Promise.reject("Not enough permission to access resource");
        }
      }
      return config;
    } else {
      store.commit("setErrorMessage", "Kindly Login to continue");
      router.push("/login");
    }
  }
});

axiosInstance.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error.response && error.response.data) {
      if (error.response.status == 401) {
        console.log(error.response.data.error_description);
        util.removeSessionUser();
        if (router.history.current.path !== "/login") {
          router.push("/login");
          store.commit(
            "setErrorMessage",
            error.response.data.error_description
          );
        } else {
          store.commit("setErrorMessage", "Kindly Login to continue");
        }
        return;
      } else if (error.response.status == 403) {
        store.commit("setErrorMessage", error.response.data.error_description);
      }
      return Promise.reject(error.response.data);
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;

### auth/src/main/java/com/dhitha/lms/auth/AuthApplication.java
package com.dhitha.lms.auth;

import com.fasterxml.jackson.datatype.jsr310.ser.LocalDateTimeSerializer;
import java.time.format.DateTimeFormatter;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.gson.GsonBuilderCustomizer;
import org.springframework.boot.autoconfigure.jackson.Jackson2ObjectMapperBuilderCustomizer;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.openfeign.EnableFeignClients;
import org.springframework.context.annotation.Bean;

@EnableFeignClients
@EnableDiscoveryClient
@SpringBootApplication
public class AuthApplication {

  public static void main(String[] args) {
    SpringApplication.run(AuthApplication.class, args);
  }

  @Bean
  public Jackson2ObjectMapperBuilderCustomizer jsonCustomizer() {
    return builder ->
        builder.serializers(
            new LocalDateTimeSerializer(DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss")));
  }
}

### auth/src/main/java/com/dhitha/lms/auth/controller/AuthController.java
package com.dhitha.lms.auth.controller;

import com.dhitha.lms.auth.dto.AuthRequestDTO;
import com.dhitha.lms.auth.dto.AuthResponseDTO;
import com.dhitha.lms.auth.error.GenericException;
import com.dhitha.lms.auth.service.AuthService;
import javax.validation.Valid;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.util.Assert;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * REST controller for Auth Service
 *
 * @author Dhiraj
 */
@RestController
@RequestMapping("/v1")
@RequiredArgsConstructor
@Slf4j
public class AuthController {
  private final AuthService authService;

  @PostMapping(
      value = "/token/authenticate",
      produces = MediaType.APPLICATION_JSON_VALUE,
      consumes = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<AuthResponseDTO> authenticateUser(
      @RequestBody @Valid AuthRequestDTO authDTO) throws GenericException {
    log.info("Authenticating .....");
    AuthResponseDTO authenticate = authService.authenticate(authDTO);
    log.info("Authenticated : {}", authenticate);
    return ResponseEntity.ok().body(authenticate);
  }

  @PostMapping(
      value = "/token/verify",
      produces = MediaType.APPLICATION_JSON_VALUE,
      consumes = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<AuthResponseDTO> verifyToken(
      @RequestHeader(value = HttpHeaders.AUTHORIZATION) String token) throws GenericException {
    log.info("Verification token {} ", token);
    Assert.notNull(token, "token cannot be null");
    if(token.startsWith("Bearer ")){
      token = token.substring(7);
    }else{
      throw new IllegalArgumentException("Bearer token missing");
    }
    return ResponseEntity.ok(authService.verifyToken(token));
  }
}