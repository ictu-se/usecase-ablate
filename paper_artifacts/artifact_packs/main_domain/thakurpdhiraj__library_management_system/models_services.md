# Models/services
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
import com.dhitha.lms.order.entity.BookOrder;
import com.dhitha.lms.order.error.GenericException;
import com.dhitha.lms.order.error.OrderNotFoundException;
import com.dhitha.lms.order.repository.BookOrderRepository;
import java.time.LocalDateTime;
import java.util.Collections;
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
 * Unit tests for {@link BookOrderService}
 *
 * @author Dhiraj
 */
@ExtendWith(MockitoExtension.class)
class BookOrderServiceTest {

  @Mock private BookOrderRepository repositoryMock;
  @Mock private BookOrderHistoryService historyMock;
  @Mock private InventoryService inventoryServiceMock;
  private final ModelMapper modelMapper = new ModelMapper();

  private BookOrderService subject;

  @BeforeEach
  void init() {
    subject =
        new BookOrderServiceImpl(repositoryMock, historyMock, modelMapper, inventoryServiceMock);
  }

  @Test
  @DisplayName("findById: order found, expected success")
  void testFindByIdSuccess() throws Exception {
    when(repositoryMock.findById(1L)).thenReturn(Optional.of(BookOrder.builder().build()));
    subject.findById(1L);
    verify(repositoryMock).findById(1L);
  }

  @Test
  @DisplayName("findById: order not found, expected OrderNotFoundException")
  void testFindByIdNotFound() {
    assertThrows(
        OrderNotFoundException.class,
        () -> {
          when(repositoryMock.findById(1L)).thenReturn(Optional.empty());
          subject.findById(1L);
        });
    verify(repositoryMock).findById(1L);
  }

  @Test
  @DisplayName("findAllByUser: order found, expected success")
  void testFindAllByUserIdSuccess() {

...[truncated]...

### order/src/test/java/com/dhitha/lms/order/service/BookOrderHistoryServiceTest.java
package com.dhitha.lms.order.service;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import com.dhitha.lms.order.entity.BookOrder;
import com.dhitha.lms.order.entity.BookOrderHistory;
import com.dhitha.lms.order.repository.BookOrderHistoryRepository;
import java.util.Collections;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.modelmapper.ModelMapper;

/**
 * Unit Tests for {@link BookOrderHistoryService }
 *
 * @author Dhiraj
 */
@ExtendWith(MockitoExtension.class)
class BookOrderHistoryServiceTest {

  @Mock private BookOrderHistoryRepository repositoryMock;
  private BookOrderHistoryService subject;

  @BeforeEach
  void init() {
    subject = new BookOrderHistoryServiceImpl(repositoryMock, new ModelMapper());
  }

  @Test
  void testSave() {
    when(repositoryMock.saveAndFlush(
            BookOrderHistory.builder().orderId(1L).bookId(1L).bookReferenceId("abc").build()))
        .thenReturn(
            BookOrderHistory.builder().orderId(1L).bookId(1L).bookReferenceId("abc").build());
    subject.save(BookOrder.builder().id(1L).bookId(1L).bookReferenceId("abc").build());
    verify(repositoryMock).saveAndFlush(any(BookOrderHistory.class));
  }

  @Test
  void testFindAllOfUser() {
    when(repositoryMock.findByUserId(1L)).thenReturn(Collections.singletonList(BookOrderHistory.builder().orderId(1L).bookId(1L).bookReferenceId("abc").build()));
    subject.findAllForUser(1L);
    verify(repositoryMock).findByUserId(1L);
  }
}

### auth/src/test/java/com/dhitha/lms/auth/service/AuthServiceTest.java
package com.dhitha.lms.auth.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import com.dhitha.lms.auth.TestUtils;
import com.dhitha.lms.auth.client.UserClient;
import com.dhitha.lms.auth.dto.AuthRequestDTO;
import com.dhitha.lms.auth.dto.AuthResponseDTO;
import com.dhitha.lms.auth.dto.UserDTO;
import com.dhitha.lms.auth.error.GenericException;
import com.nimbusds.jwt.JWTClaimsSet;
import com.nimbusds.jwt.JWTClaimsSet.Builder;
import feign.FeignException;
import feign.FeignException.FeignClientException;
import java.util.Date;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

/**
 * Unit tests for {@link AuthService}
 *
 * @author Dhiraj
 */
@ExtendWith(MockitoExtension.class)
class AuthServiceTest {

  @Mock private UserClient userClient;

  @Mock private TokenService tokenService;

  private AuthService subject;

  @BeforeEach
  void init() {
    subject = new AuthServiceImpl(userClient, tokenService);
  }

  @Test
  @DisplayName("authenticate: valid input, expected success")
  void testAuthenticateHappy() throws Exception {
    AuthRequestDTO reqMock = createMockReq();
    UserDTO userDTO = TestUtils.createMockUser();
    when(userClient.getByCredentials(reqMock)).thenReturn(userDTO);
    when(tokenService.generateIdToken(userDTO)).thenReturn("abc.xyz.pqr");

    AuthResponseDTO result = subject.authenticate(reqMock);
    assertEquals("abc", result.getHeader());
    assertEquals("xyz", result.getPayload());
    assertEquals("pqr", result.getSignature());
    assertEquals(userDTO, result.getUserDTO());

    verify(userClient).getByCredentials(reqMock);
    verify(tokenService).generateIdToken(userDTO);
  }

  @Test
  @DisplayName("authenticate: invalid credentials input, expected GenericException")
  void testAuthenticateWithInvalidCredentials() throws Exception {
    assertThrows(
        GenericException.class,
        () -> {
          AuthRequestDTO reqMock = createMockReq();
          when(userClient.getByCredentials(reqMock)).thenThrow(FeignException.NotFound.class);

          subject.authenticate(reqMock);
        });
    verify(userClient).getByCredentials(any(AuthRequestDTO.class));
    verify(tokenS
...[truncated]...

### auth/src/test/java/com/dhitha/lms/auth/service/TokenServiceTest.java
package com.dhitha.lms.auth.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import com.dhitha.lms.auth.TestUtils;
import com.dhitha.lms.auth.dto.UserDTO;
import com.dhitha.lms.auth.error.GenericException;
import com.nimbusds.jwt.JWTClaimsSet;
import java.io.File;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Spy;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.core.io.DefaultResourceLoader;
import org.springframework.core.io.FileSystemResource;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;

/**
 * Unit tests for {@link TokenService}
 *
 * @author Dhiraj
 */
@ExtendWith(MockitoExtension.class)
class TokenServiceTest {

  @Spy private ResourceLoader resourceLoader = new DefaultResourceLoader();

  private TokenService subject;

  @BeforeEach
  void init() {
    subject = new TokenServiceImpl(resourceLoader);
  }

  @Test
  @DisplayName("generateIdToken: valid input, expected success")
  void testGenerateIdTokenSuccess() throws Exception {
    UserDTO userDTO = TestUtils.createMockUser();
    String result = subject.generateIdToken(userDTO);
    assertEquals(3, result.split("\\.").length);
    verify(resourceLoader).getResource("classpath:/certs/lms-private-key.pem");
  }

  @Test
  @DisplayName("generateIdToken: valid input incorrect private key, expected GenericException")
  void testGenerateIdTokenIncorrectKey() {
    assertThrows(
        GenericException.class,
        () -> {
          Resource mockResource =
          resourceLoader.getResource("classpath:/certs/incorrect-private-key.pem");
          when(resourceLoader.getResource(anyString()))
              .thenReturn(mockResource);
          UserDTO userDTO = TestUtils.createMockUser();
          subject.generateIdToken(userDTO);
        });

    verify(resourceLoader).getResource("classpath:/certs/lms-private-key.pem");
  }

  @Test
  @DisplayName("verifyToken: valid token, expected success")
  void testVerifyTokenSuccess() throws Exception {
    // Not really a UNIT test??!, can't figure out proper way :(
    UserDTO userDTO = TestUtils.createMockUser();
    String mockToke
...[truncated]...

### order/src/test/java/com/dhitha/lms/order/service/InventoryServiceTest.java
package com.dhitha.lms.order.service;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.anyLong;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import com.dhitha.lms.order.client.InventoryClient;
import com.dhitha.lms.order.dto.InventoryDTO;
import com.dhitha.lms.order.error.GenericException;
import feign.FeignException;
import feign.FeignException.FeignClientException;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

/**
 * Unit tests for {@link InventoryService}
 *
 * @author Dhiraj
 */
@ExtendWith(MockitoExtension.class)
class InventoryServiceTest {

  @Mock private InventoryClient clientMock;

  private InventoryService subject;

  @BeforeEach
  void init() {
    subject = new InventoryServiceImpl(clientMock);
  }

  @Test
  @DisplayName("orderIfAvailable: successful order, expected success")
  void testOrderIfAvailable() throws Exception {
    when(clientMock.orderIfAvailable(1L)).thenReturn(InventoryDTO.builder().build());
    subject.orderIfAvailable(1L);
    verify(clientMock).orderIfAvailable(1L);
  }

  @Test
  @DisplayName("orderIfAvailable: inventory not available to order, expected GenericException")
  void testOrderIfAvailableNotAvailable() throws Exception {
    assertThrows(
        GenericException.class,
        () -> {
          when(clientMock.orderIfAvailable(1L)).thenThrow(FeignException.NotFound.class);
          subject.orderIfAvailable(1L);
          verify(clientMock).orderIfAvailable(1L);
        });
  }

  @Test
  @DisplayName("orderIfAvailable: unknown error on order, expected GenericException")
  void testOrderIfAvailableUnknownError() throws Exception {
    assertThrows(
        GenericException.class,
        () -> {
          when(clientMock.orderIfAvailable(1L)).thenThrow(FeignClientException.class);
          subject.orderIfAvailable(1L);
          verify(clientMock).orderIfAvailable(1L);
        });
  }

  @Test
  @DisplayName("returnBook: inventory client returned true on return of book,expected")
  void testReturnBook() throws Exception {
    when(clientMock.returnBook(1L, "abc")).thenReturn(true);
    subject.returnBook(1L, "abc");
    verify(clientMock).returnBook(anyLong(), anyString());
  }

  @Test
  @DisplayName(
      "returnBook: inventory client returned false on return or
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

### client-frontend/src/service/book.js
import resource from "@/resource/resource";
import { sendResponse } from "@/util/responseUtil.js";
import { omitBy, isEmpty } from "lodash";

export const findAllCategories = async () => {
  let response = await resource.get("/categories");
  return sendResponse(response, 200);
};

export const findAllBooks = async book => {
  const params = new URLSearchParams(omitBy(book, isEmpty));
  let response = await resource.get("/books", { params: params });
  return sendResponse(response, 200);
};

export const findBook = async id => {
  let response = await resource.get(`/books/${id}`);
  return sendResponse(response, 200);
};

export const saveBook = async book => {
  let response = await resource.post("/admin/books/", book);
  return sendResponse(response, 201);
};

export const updateBook = async book => {
  let response = await resource.put(`/admin/books/${book.id}`, book);
  return sendResponse(response, 200);
};

export const deleteBook = async (id, references) => {
  const params = new URLSearchParams(references.map(s => ["bookReference", s]));
  let response = await resource.delete(`/admin/books/${id}`, {
    params: params
  });
  return sendResponse(response, 204);
};

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

### book/src/main/java/com/dhitha/lms/book/entity/Book.java
package com.dhitha.lms.book.entity;

import java.io.Serializable;
import java.time.LocalDateTime;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.Lob;
import javax.persistence.ManyToOne;
import javax.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;

/**
 * Entity to represent books in LMS
 *
 * @author Dhiraj
 */
@Entity
@Table(name = "book")
@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class Book implements Serializable {
  private static final long serialVersionUID = 1L;

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Column(name = "isbn", nullable = false, unique = true)
  private String isbn;

  @Column(name = "name", nullable = false)
  private String name;

  @ManyToOne
  @JoinColumn(name = "category_id")
  private Category category;

  @Column(name = "author", nullable = false)
  private String author;

  @Column(name = "publication", nullable = false)
  private String publication;

  @Column(name = "publication_year")
  private Integer publicationYear;

  @Column(name = "pages", nullable = false)
  private Integer pages;

  @Lob
  @Column(name = "summary")
  private String summary;

  @CreationTimestamp
  @Column(name = "added_at")
  private LocalDateTime addedAt;
}

### user/src/main/java/com/dhitha/lms/user/entity/Role.java
package com.dhitha.lms.user.entity;


/**
 * Role of a user
 *
 * @author Dhiraj
 */
public enum  Role {
  USER,
  ADMIN
}

### user/src/main/java/com/dhitha/lms/user/entity/User.java
package com.dhitha.lms.user.entity;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.List;
import javax.persistence.CollectionTable;
import javax.persistence.Column;
import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.ToString;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

/**
 * Entity to represent user of LMS
 *
 * @author Dhiraj
 */
@Entity
@Table(name = "user")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class User implements Serializable {
  private static final long serialVersionUID = 1L;

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Column(name = "name", nullable = false)
  private String name;

  @Column(name = "email", nullable = false)
  private String email;

  @Column(name = "username", nullable = false, unique = true, updatable = false)
  private String username;

  @Column(name = "password", nullable = false)
  private String password;

  @Column(name = "account_non_expired", columnDefinition = "BIT(1) DEFAULT 1")
  private Boolean accountNonExpired;

  @Column(name = "account_non_locked", columnDefinition = "BIT(1) DEFAULT 1")
  private Boolean accountNonLocked;

  @Column(name = "credentials_non_expired", columnDefinition = "BIT(1) DEFAULT 1")
  private Boolean credentialsNonExpired;

  @Column(name = "enabled", columnDefinition = "BIT(1) DEFAULT 1")
  private Boolean enabled;

  @Column(name = "created_at", columnDefinition = "TIMESTAMP")
  @CreationTimestamp
  private LocalDateTime createdAt;

  @Column(name = "
...[truncated]...