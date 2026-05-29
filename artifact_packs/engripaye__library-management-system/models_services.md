# Models/services
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

### src/main/java/org/engripaye/librarymanagementsystem/repository/UserRepository.java
package org.engripaye.librarymanagementsystem.repository;

import org.engripaye.librarymanagementsystem.model.AppUser;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<AppUser, Long> {
}