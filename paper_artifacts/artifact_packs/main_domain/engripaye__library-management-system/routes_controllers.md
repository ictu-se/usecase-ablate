# Routes/controllers
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