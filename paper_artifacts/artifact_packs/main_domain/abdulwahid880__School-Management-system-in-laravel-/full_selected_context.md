# README
## readme.md
## School Management and Accounting Software
[![Build Status](https://travis-ci.org/changeweb/Unifiedtransform.svg?branch=master)](https://travis-ci.org/changeweb/Unifiedtransform)
[![Linux](https://img.shields.io/travis/changeweb/Unifiedtransform/master.svg?label=linux)](https://travis-ci.org/changeweb/Unifiedtransform)
[![Code Climate](https://codeclimate.com/github/changeweb/Unifiedtransform/badges/gpa.svg)](https://codeclimate.com/github/changeweb/Unifiedtransform)
[![MadeWithLaravel.com shield](https://madewithlaravel.com/storage/repo-shields/1362-shield.svg)](https://madewithlaravel.com/p/unifiedtransform/shield-link)
[![Join the chat at https://gitter.im/Unifiedtransform](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Unifiedtransform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

We like to challenge the quality of what we build to make it better. To do so, we try to make the product intuitive, beautiful, and user friendly. Innovation and hard work help to fulfill these requirements. I believe in order to innovate we need to think differently. A few months ago I discovered there was no open source free school management software that met my quality standards. I happen to know a bit of programming so I decided to make one. I also believe that working with more people can push the standard higher than working alone. So I decided to make it open source and free.

## Featured on Laravel News !!
![Screenshot_2019-04-07 Laravel News](https://user-images.githubusercontent.com/9896315/55683832-1b3c8c80-5966-11e9-8dfb-ab30a79a98ed.png)
See the news [here](https://laravel-news.com/unified-transform-open-source-school-management-platform)

## Contribute

Unifiedtransform is 100% open source and free forever!!

Community contribution can make this product better!! See [Contribution guideline](https://github.com/changeweb/Unifiedtransform/blob/master/CONTRIBUTING.md) before making any Pull request.

When you contribute to a Github project you agree with this terms of [Github Terms of Service(Contributions Under Repository License)](https://help.github.com/en/articles/github-terms-of-service#6-contributions-under-repository-license).

Since this project is under **GNU General Public License v3.0**, according to Github's Terms of Service all your contributions are also under the same license terms.
Thus you permit the user of this software to use your contribution under the terms of **GNU General Public License v3.0**.

### Contributors Hall of Fame
[![](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/images/0)](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/links/0)[![](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/images/1)](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/links/1)[![](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/images/2)](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/links/2)[![](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/images/3)](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/links/3)[![](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/images/4)](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/links/4)[![](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/images/5)](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/links/5)[![](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/images/6)](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/links/6)[![](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/images/7)](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/links/7)

## Testing

- We want testable softwares. Most parts of the software are covered by tests. You also can contribute by writing test case!
- To run Feature and Unit Tests use `./vendor/bin/phpunit`.
- To run Browser Tests copy `.env.dusk.example` to `.env.dusk.local` and set `APP_KEY` with same token to environment variable in your `.env` file and run `php artisan serve --env=dusk.local` for execute the server then run `php artisan dusk`.

## License

GNU General Public License v3.0

## Features

This software has following features:

* Roles: Master, Admin, Teacher, Student, Librarian, Accountant

   **(You can Impersonate User Roles in Development environment)** See how [Impersonation](https://github.com/changeweb/Unifiedtransform/pull/118) works. Cool !!
* **Payment**
   * **[Stripe](http://stripe.com/)** is used. See configuration below
   * Students can pay from their accounts.
   * Student can view payment receipts (history)
   * View Screenshot below
* Attendance
* Mark
* Registration
* Notice, Syllabus
* Library
* Exam
* Grade
* Accounts
* Messaging (uses CKEditor 5)
* **Export/Import** Users (Students, Teachers) from/to **Excel**
   * [Laravel Excel](https://github.com/maatwebsite/Laravel-Excel) package is used.
   * **Important:** Single sheet supported in an Excel file. So delete any extra sheet in an Excel file.
   * Following excel column  names supported for both Teachers and Students:

      * `name, email, password, address, about, phone_number, blood_group, nationality, gender`.
   * Other columns:

      * For Teachers: `department`, (`class, section`) if assigned as class teacher.
      * For Students: `class, section, session, version, group, birthday, religion, father_name, father_phone_number, father_national_id, father_occupation, father_designation, father_annual_income, mother_name, mother_phone_number, mother_national_id, mother_occupation, mother_designation, mother_annual_income`
   * For any number(e.g: phone_number) starts with zero, put (') before zero.
* Supported Languages (**English, Spanish**)

   * To set default Language and Timezone, Edit as following in `config/app.php`:

      ```php
      'timezone' => 'Asia/Dhaka',//'UTC',
      'locale' => 'en',//'es-MX' for Spanish
      ```


## Framework used

- Laravel 5.5
- Bootstrap 3.3.7

## Server Requirements

- PHP >= 7.1.0
- OpenSSL PHP Extension
- PDO PHP Extension
- Mbstring PHP Extension
- Tokenizer PHP Extension
- XML PHP Extension

## How to Start
### Using a Container:

**Anyone having trouble related to `mysql-client`, PHP 7.3 needs mariadb instead of mysql.** See issue [#192](https://github.com/changeweb/Unifiedtransform/issues/192)

**[Docker](https://www.docker.com/)** is now supported.

You need to change Docker configuration files according to your need.

- Change following lines in `docker-compose.yml`

      MYSQL_ROOT_PASSWORD: your password
      MYSQL_USER: root
      MYSQL_PASSWORD: your password

- To run this software in Docker containers run `sudo docker-compose up -d`.
- Then run `sudo docker container ls --all`. Copy **Nginx** Container ID.
- Then run `sudo docker exec -it <container id> bash`
- Run `cp .env.example .env` and change following lines in `.env` file
   ```sh
   DB_HOST=db
   DB_PORT=3306
   DB_DATABASE=school
   DB_USERNAME=root
   DB_PASSWORD=your password
   ```
- Run `composer install`
- Run `php artisan key:generate`
- Run `php artisan migrate:fresh --seed`
- Visit `http://localhost:80`.

### Not using a Container:

Here are some basic steps to start using this application

**Note:** Instruction on cached data for Dashboard is given in **Good to know** segment below.

- Clone the repository

```sh
git clone https://github.com/changeweb/Unifiedtransform
```

- Copy the contents of the `.env.example` file to create `.env` in the same directory

- Run `composer install` for `developer` environment and run `composer install --optimize-autoloader --no-dev` for `production` environment to install Laravel packages (Remove **Laravel Debugbar**, **Laravel Log viewer** packages from **composer.json** and 

```php
   //Provider
   Barryvdh\Debugbar\ServiceProvider,
   Logviewer Service provider,
   //Alias
   Debugbar' => Barryvdh...
```
 from `config/app.php` before running **`composer install`** in **Production Environment**)

- Generate `APP_KEY` using `php artisan key:generate`

- Edit the database connection configuration in .env file e.g.

```sh
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=unifiedtransform
DB_USERNAME=unified
DB_PASSWORD=secret
```

> Note that this is just an example, and the values may vary depending on your database environment.

- Set the `APP_ENV` variable in your `.env` file according to your application environment (e.g. local, production) in `.env` file

- Migrate your Database with `php artisan migrate`

- Seed your Database with `php artisan db:seed`

- On localhost, serve your application with `php artisan serve`

> See **[Video Tutorial](https://vimeo.com/334331502)**.

[![Video Tutorial](https://user-images.githubusercontent.com/9896315/57624079-fbc30000-75b2-11e9-80b8-9bf92de3b1ac.png)](https://vimeo.com/334331502 "Unifiedtransform Installation")

#### (Optional)

- [Laravel Page Speed Package](https://github.com/renatomarinho/laravel-page-speed) is installed but not activated. If you want to use it to optimize your site automatically which results in a 35%+ optimization. You need to uncomment some lines from `Kernel.php` file and may need to run `php artisan vendor:publish --provider="RenatoMarinho\LaravelPageSpeed\ServiceProvider"`.

   **app/HTTP/Kernel.php**
   ```php
       //\RenatoMarinho\LaravelPageSpeed\Middleware\InlineCss::class,
       //\RenatoMarinho\LaravelPageSpeed\Middleware\ElideAttributes::class,
       //\RenatoMarinho\LaravelPageSpeed\Middleware\InsertDNSPrefetch::class,
       //\RenatoMarinho\LaravelPageSpeed\Middleware\RemoveComments::class,
       //\RenatoMarinho\LaravelPageSpeed\Middleware\TrimUrls::class,
       //\RenatoMarinho\LaravelPageSpeed\Middleware\RemoveQuotes::class,
       //\RenatoMarinho\LaravelPageSpeed\Middleware\CollapseWhitespace::class,
   ```
- To create a `Master`, go to the `database\seeds\UsersTableSeeder.php` and change the `name`, 
...[truncated]...

# File tree
.travis.yml
CODE_OF_CONDUCT.md
CONTRIBUTING.md
_config.yml
app
  Account.php
  AccountSector.php
  Attendance.php
  Book.php
  Console
    Kernel.php
  Course.php
  Department.php
  Event.php
  Events
    StudentInfoUpdateRequested.php
    UserRegistered.php
  Exam.php
  ExamForClass.php
  Exceptions
    Handler.php
  Exports
    StudentsExport.php
    TeachersExport.php
  Faq.php
  Fee.php
  Feedback.php
  Form.php
  Grade.php
  Gradesystem.php
  Homework.php
  Http
    Controllers
      AccountController.php
      AttendanceController.php
      Auth
        ForgotPasswordController.php
        LoginController.php
        RegisterController.php
        ResetPasswordController.php
      CashierController.php
      Controller.php
      CourseController.php
      EventController.php
      ExamController.php
      FaqController.php
      FeeController.php
      FeedbackController.php
      FormController.php
      GradeController.php
      GradesystemController.php
      HomeController.php
      HomeworkController.php
      IssuedbookController.php
      Library
        BookController.php
      MasterController.php
      MessageController.php
      MyclassController.php
      NoticeController.php
      NotificationController.php
      PaymentController.php
      RoutineController.php
      SchoolController.php
      SectionController.php
      SettingController.php
      SyllabusController.php
      UploadController.php
      UploadHandler.php
      UserController.php
    Kernel.php
    Middleware
      CheckAccountant.php
      CheckAdmin.php
      CheckLibrarian.php
      CheckMaster.php
      CheckMasterOrAdmin.php
      CheckStudent.php
      CheckTeacher.php
      CheckTeacherOrStudent.php
      EncryptCookies.php
      RedirectIfAuthenticated.php
      TrimStrings.php
      TrustProxies.php
      VerifyCsrfToken.php
    Requests
      Account
        StoreAccountRequest.php
        StoreSectorRequest.php
        UpdateAccountRequest.php
      Attendance
        StoreAttendanceRequest.php
      Course
        SaveConfigurationRequest.php
      Exam
        CreateExamRequest.php
      Grade
        CalculateMarksRequest.php
      Library
        BookRequest.php
      SchoolRequest.php
      User
        ChangePasswordRequest.php
        CreateAccountantRequest.php
        CreateAdminRequest.php
        CreateLibrarianRequest.php
        CreateTeacherRequest.php
        CreateUserRequest.php
        ImpersonateUserRequest.php
        UpdateUserRequest.php
    Resources
      AttendanceResource.php
      BookResource.php
      ClassResource.php
      CourseResource.php
      EventResource.php
      FaqResource.php
      FeedbackResource.php
      FormResource.php
      GradeResource.php
      HomeworkResource.php
      MessageResource.php
      NoticeResource.php
      NotificationResource.php
      RoutineResource.php
      SchoolResource.php
      SectionResource.php
      SyllabusResource.php
      UserResource.php
    Traits
      GradeTrait.php
  Imports
    FirstStudentSheetImport.php
    FirstTeacherSheetImport.php
    StudentsImport.php
    TeachersImport.php
  Issuedbook.php
  Listeners
    SendWelcomeEmail.php
    UpdateStudentInfo.php
  Mail
    SendWelcomeEmailToUser.php
  Message.php
  Model.php
  Myclass.php
  Notice.php
  Notification.php
  Payment.php
  Providers
    AppServiceProvider.php
    AuthServiceProvider.php
    BroadcastServiceProvider.php
    EventServiceProvider.php
    RouteServiceProvider.php
  Routine.php
  School.php
  Section.php
  Services
    Account
      AccountService.php
    Attendance
      AttendanceService.php
    Course
      CourseService.php
    Exam
      ExamService.php
    Grade
      GradeService.php
    IssueBook
      IssuedBookService.php
    User
      UserService.php
  StudentBoardExam.php
  StudentInfo.php
  Syllabus.php
  User.php
bootstrap
  app.php
composer.json
config
  app.php
  auth.php
  broadcasting.php
  cache.php
  database.php
  filesystems.php
  mail.php
  queue.php
  services.php
  session.php
  view.php
docker-compose.yml
package-lock.json
package.json
phpunit.dusk.xml
phpunit.xml
readme.md
resources
  views
    accounts
      accountant-list.blade.php
      edit_sector.blade.php
      expense-edit.blade.php
      expense-list.blade.php
      expense.blade.php
      income-edit.blade.php
      income-list.blade.php
      income.blade.php
      sector.blade.php
    attendance
      adjust.blade.php
      attendance.blade.php
      student-attendances.blade.php
    auth
      login.blade.php
      passwords
        email.blade.php
        reset.blade.php
      register.blade.php
    components
    course
    email
    events
    exams
    fees
    gpa
    grade
    home.blade.php
    layouts
    library
    list
    masters
    message
    notices
    pdf
    profile
    routines
    school
    schools
    settings
    stripe
    syllabus
    welcome.blade.php
routes
server.php
tests
webpack.mix.js

# Selected code and test snippets
### resources/views/schools/form.blade.php
<button class="btn btn-primary btn-lg btn-block" data-toggle="modal" data-target="#schoolModal" dusk="create-school-button">
    + @lang('Create School')
</button>

<!-- Modal -->
<div class="modal fade" id="schoolModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
    <div class="modal-dialog" role="document">
        <form class="form-horizontal" method="POST" action="{{ route('schools.store') }}">
            {{ csrf_field() }}
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">@lang('Create School')</h4>
                </div>
                <div class="modal-body">
                    <div class="form-group{{ $errors->has('school_name') ? ' has-error' : '' }}">
                        <label for="name" class="col-md-4 control-label">@lang('School Name')</label>

                        <div class="col-md-6">
                            <input id="name" type="text" class="form-control" name="name" value="{{ old('name') }}" placeholder="@lang('School Name')" required>

                            @if ($errors->has('name'))
                                <span class="help-block">
                                    <strong>{{ $errors->first('name') }}</strong>
                                </span>
                            @endif
                        </div>
                    </div>

                    <div class="form-group{{ $errors->has('medium') ? ' has-error' : '' }}">
                        <label for="medium" class="col-md-4 control-label">@lang('School Medium')</label>

                        <div class="col-md-6">
                            <select id="medium" class="form-control" name="medium">
                                <option selected="selected">@lang('Bangla')</option>
                                <option>@lang('English')</option>
                                <option>@lang('Hindi')</option>
                                <option>@lang('Spanish')</option>
                                <option>@lang('Chinese')</option>
                                <option>@lang('Arabic')</option>
                            </select>

                            @if ($errors->has('medium'))
                                <span class="help-block">
                                    <strong>{{ $errors->first('medium') }}</strong>
                                </span>
        
...[truncated]...

### resources/views/components/book-issue-form.blade.php
<form class="form-horizontal" action="{{url('library/issue-books')}}" method="post">
    {{ csrf_field() }}
    <div class="form-group{{ $errors->has('student_code') ? ' has-error' : '' }}">
        <label for="student_code" class="col-md-4 control-label">@lang('Student Code')</label>

        <div class="col-md-6">
            <input id="student_code" type="text" class="form-control" name="student_code" value="{{ old('student_code') }}"
                placeholder="@lang('Student Code')" required>

            @if ($errors->has('student_code'))
            <span class="help-block">
                <strong>{{ $errors->first('student_code') }}</strong>
            </span>
            @endif
        </div>
    </div>
    <div class="form-group{{ $errors->has('book_code') ? ' has-error' : '' }}">
        <label for="book_code" class="col-md-4 control-label">@lang('Book Title') &amp; @lang('Code') (<small>@lang('Type') & @lang('Search by Name/Code.')
                @lang('You can Select Multiple Books') (<i>@lang('Maximum') 10 @lang('books')</i>)</small>)</label>

        <div class="col-md-6">
            <select id="book_code" class="form-control" multiple name="book_id[]">
                @foreach($books as $book)
                <option value="{{$book->id}}">{{$book->title}} - {{$book->book_code}}</option>
                @endforeach
            </select>
        </div>
    </div>
    <div class="form-group{{ $errors->has('issue_date') ? ' has-error' : '' }}">
        <label for="issue_date" class="col-md-4 control-label">@lang('Issue Date')</label>

        <div class="col-md-6">
            <input id="issue_date" class="form-control datepicker" name="issue_date" value="{{ old('issue_date') }}"
                placeholder="@lang('Issue Date')" required>

            @if ($errors->has('issue_date'))
            <span class="help-block">
                <strong>{{ $errors->first('issue_date') }}</strong>
            </span>
            @endif
        </div>
    </div>
    <div class="form-group{{ $errors->has('return_date') ? ' has-error' : '' }}">
        <label for="return_date" class="col-md-4 control-label">@lang('Return Date')</label>

        <div class="col-md-6">
            <input id="return_date" class="form-control datepicker" name="return_date" value="{{ old('return_date') }}"
                placeholder="@lang('Return Date')" required>

            @if ($errors->has('return_date'))
            <span class="help-block">
                <strong>{{ $errors->first('return_date') }}</strong>
            </span>
            @endif
        </div>
 
...[truncated]...

### resources/views/library/books/form.blade.php
<div class="form-group{{ $errors->has('title') ? ' has-error' : '' }}">
    <label for="title" class="col-md-4 control-label">@lang('Book Title')</label>

    <div class="col-md-6">
        <input id="title" type="text" class="form-control" name="title" value="{{ $book->title Or old('title') }}" placeholder="@lang('Book Title')" required>

        @if ($errors->has('title'))
            <span class="help-block">
                <strong>{{ $errors->first('title') }}</strong>
            </span>
        @endif
    </div>
</div>

<div class="form-group{{ $errors->has('about') ? ' has-error' : '' }}">
    <label for="about" class="col-md-4 control-label">@lang('About Book')</label>

    <div class="col-md-6">
        <textarea rows="3" id="about" type="text" class="form-control" name="about" placeholder="@lang('About Book')" required>{{ $book->about Or old('about') }}</textarea>

        @if ($errors->has('about'))
            <span class="help-block">
                <strong>{{ $errors->first('about') }}</strong>
            </span>
        @endif
    </div>
</div>

<div class="form-group{{ $errors->has('book_code') ? ' has-error' : '' }}">
    <label for="book_code" class="col-md-4 control-label">@lang('Book Code')</label>

    <div class="col-md-6">
        <input id="book_code" type="text" class="form-control" name="book_code" value="{{ $book->book_code Or old('book_code') }}" placeholder="@lang('Book Code')" required>

        @if ($errors->has('book_code'))
            <span class="help-block">
                <strong>{{ $errors->first('book_code') }}</strong>
            </span>
        @endif
    </div>
</div>

<div class="form-group{{ $errors->has('author') ? ' has-error' : '' }}">
    <label for="author" class="col-md-4 control-label">@lang('Book Author')</label>

    <div class="col-md-6">
        <input id="author" type="text" class="form-control" name="author" value="{{ $book->author Or old('author') }}" placeholder="@lang('Book Author')" required>

        @if ($errors->has('author'))
            <span class="help-block">
                <strong>{{ $errors->first('author') }}</strong>
            </span>
        @endif
    </div>
</div>

<div class="form-group{{ $errors->has('price') ? ' has-error' : '' }}">
    <label for="price" class="col-md-4 control-label">@lang('Book Price')</label>

    <div class="col-md-6">
        <input id="price" type="number" class="form-control" name="price" value="{{ $book->price Or old('price') }}" placeholder="@lang('Book Price')" required>

        @if ($errors->has('price'))
            <span class="help-bloc
...[truncated]...

### resources/views/layouts/teacher/grade-form.blade.php
{{--<div class="well" style="font-size: 15px;">@lang('Choose Field to Display')</div>--}}
<style>
  #grade-labels > .label{
    margin-right: 1%;
  }
</style>
<div class="col-md-12" id="grade-labels">
  <span class="label label-danger checkbox-inline">
    <input type="checkbox" name="attendance" value="4" checked> @lang('Attendance')
  </span>
  <span class="label label-primary checkbox-inline">
    <input type="checkbox" name="quiz[]" value="5" checked> @lang('Quiz') 1
  </span>
  <span class="label label-primary checkbox-inline">
    <input type="checkbox" name="quiz[]" value="6"> @lang('Quiz') 2
  </span>
  <span class="label label-primary checkbox-inline">
    <input type="checkbox" name="quiz[]" value="7"> @lang('Quiz') 3
  </span>
  <span class="label label-primary checkbox-inline">
    <input type="checkbox" name="quiz[]" value="8"> @lang('Quiz') 4
  </span>
  <span class="label label-primary checkbox-inline">
    <input type="checkbox" name="quiz[]" value="9"> @lang('Quiz') 5
  </span>
  <span class="label label-success checkbox-inline">
    <input type="checkbox" name="assignment[]" value="10" checked> @lang('Assignment') 1
  </span>
  <span class="label label-success checkbox-inline">
    <input type="checkbox" name="assignment[]" value="11"> @lang('Assignment') 2
  </span>
  <span class="label label-success checkbox-inline">
    <input type="checkbox" name="assignment[]" value="12"> @lang('Assignment') 3
  </span>
  <span class="label label-info checkbox-inline">
    <input type="checkbox" name="ct[]" value="13" checked> @lang('Class Test') 1
  </span>
  <span class="label label-info checkbox-inline">
    <input type="checkbox" name="ct[]" value="14"> @lang('Class Test') 2
  </span>
  <span class="label label-info checkbox-inline">
    <input type="checkbox" name="ct[]" value="15"> @lang('Class Test') 3
  </span>
  <span class="label label-info checkbox-inline">
    <input type="checkbox" name="ct[]" value="16"> @lang('Class Test') 4
  </span>
  <span class="label label-info checkbox-inline">
    <input type="checkbox" name="ct[]" value="17"> @lang('Class Test') 5
  </span>
  <span class="label label-default checkbox-inline">
    <input type="checkbox" name="few" value="18">@lang('Final Exam Written')
  </span>
  <span class="label label-default checkbox-inline">
    <input type="checkbox" name="fem" value="19">@lang('Final Exam MCQ')
  </span>
  <span class="label label-warning checkbox-inline">
    <input type="checkbox" name="practical" value="20">@lang('Practical')
  </span>
</div>
<br />
<br />
<form action="{{url('grades/save-grade')}}"
...[truncated]...

### resources/views/layouts/master/add-class-form.blade.php
<button type="button" class="btn btn-danger btn-sm" data-toggle="modal" data-target="#addClassModal{{$school->id}}">+@lang('Add New Class')</button>

<!-- Modal -->
<div class="modal fade" id="addClassModal{{$school->id}}" tabindex="-1" role="dialog" aria-labelledby="addClassModal{{$school->id}}Label">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
        <h4 class="modal-title" id="myModalLabel">@lang('Add New Class')</h4>
      </div>
      <div class="modal-body">
      <form class="form-horizontal" action="{{url('school/add-class')}}" method="post">
          {{csrf_field()}}
          <div class="form-group">
            <label for="classNumber{{$school->id}}" class="col-sm-4 control-label">@lang('Class Number/Name')</label>
            <div class="col-sm-8">
              <input type="text" name="class_number" class="form-control" id="classNumber{{$school->id}}" placeholder="@lang('Class Number/Name')" required>
            </div>
          </div>
          {{--<div class="form-group">
            <label for="classRoomNumber{{$school->id}}" class="col-sm-4 control-label">@lang('Class Room Number')</label>
            <div class="col-sm-8">
              <input type="number" class="form-control" id="classRoomNumber{{$school->id}}" placeholder="@lang('Class Room Number')">
            </div>
          </div>
          --}}
          <div class="form-group">
            <label for="classRoomNumber{{$school->id}}" class="col-sm-4 control-label">@lang('Class Group (If Any)')</label>
            <div class="col-sm-8">
              <input type="text" class="form-control" name="group" id="classRoomNumber{{$school->id}}" placeholder="@lang('Science, Commerce, Arts, etc.')">
              <span id="helpBlock" class="help-block">@lang('Leave Empty if this Class belongs to no Group')</span>
            </div>
          </div>
          <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
              <button type="submit" class="btn btn-danger btn-sm">@lang('Submit')</button>
            </div>
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-danger btn-sm" data-dismiss="modal">@lang('Close')</button>
      </div>
    </div>
  </div>
</div>

### resources/views/layouts/master/add-course-form.blade.php
<a class="btn btn-xs btn-info pull-right" data-toggle="collapse" href="#collapseForNewCourse{{$section->id}}" aria-expanded="false" aria-controls="collapseForNewCourse{{$section->id}}">+ @lang('Add New Course')</a>
  <div class="collapse" id="collapseForNewCourse{{$section->id}}" style="margin-top:1%;">
    <div class="panel panel-default">
      <div class="panel-body">
      <form class="form-horizontal" action="{{url('courses/store')}}" method="post">
          {{csrf_field()}}
          <input type="hidden" name="class_id" value="{{$class->id}}"/>
          <input type="hidden" name="section_id" value="{{$section->id}}"/>
          <div class="form-group">
            <label for="courseName{{$section->id}}" class="col-sm-2 control-label">@lang('Course Name')</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" id="courseName{{$section->id}}" name="course_name" placeholder="@lang('Course Name')">
            </div>
          </div>
          <div class="form-group">
            <label for="teacherDepartment{{$section->id}}" class="col-sm-2 control-label">@lang('Teacher Department')</label>
            <div class="col-sm-10">
              <select class="form-control" id="teacherDepartment{{$section->id}}" name="teacher_department">
                <option value="0" selected disabled>@lang('Select Department')</option>
                @if(count($departments) > 0)
                  @php
                    $departments_of_this_school = $departments->filter(function ($department) use ($school){
                      return $department->school_id == $school->id;
                    });
                  @endphp
                  @foreach ($departments_of_this_school as $d)
                    <option value="{{$d->department_name}}">{{$d->department_name}}</option>
                  @endforeach
                @endif
              </select>
            </div>
          </div>
          <div class="form-group">
            <label for="assignTeacher{{$section->id}}" class="col-sm-2 control-label">@lang('Assign Course Teacher')</label>
            <div class="col-sm-10">
              <select class="form-control" id="assignTeacher{{$section->id}}" name="teacher_id">
                <option value="0" selected disabled>@lang('Select Department First')</option>
                @if(count($teachers) > 0)
                  @php
                    $teachers_of_this_school = $teachers->filter(function ($teacher) use ($school){
                      return $teacher->school_id == $school->id;
                    });
       
...[truncated]...

### resources/views/layouts/teacher/attendance-form.blade.php
@if ($errors->any())
    <div class="alert alert-danger">
        <ul>
            @foreach ($errors->all() as $error)
                <li>{{ $error }}</li>
            @endforeach
        </ul>
    </div>
@endif
<form action="{{url('attendance/take-attendance')}}" method="post">
      {{ csrf_field() }}
      <input type="hidden" name="section_id" value="{{$section_id}}">
      <input type="hidden" name="exam_id" value="{{$exam_id}}">
    <div class="table-responsive">
    <table class="table table-bordered table-hover">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">@lang('Student_Code')</th>
        <th scope="col">@lang('Name')</th>
        <th scope="col">@lang('Present')</th>
        <th scope="col">@lang('Total Attended')</th>
        <th scope="col">@lang('Total Missed')</th>
        <th scope="col">@lang('Total Escaped')</th>
        <th scope="col">@lang('Adjust Missed Attendance')</th>
      </tr>
    </thead>
    <tbody>
      @if (count($attendances) > 0)
        <input type="hidden" name="update" value="1">
        
        @foreach ($students as $student)
          <input type="hidden" name="students[]" value="{{$student->id}}">
        @endforeach
        @foreach ($attendances as $attendance)
        <tr>
          <th scope="row">{{($loop->index + 1)}}</th>
          <td>{{$attendance->student->student_code}}</td>
          <td>
            @if($attendance->present === 1)
              <span class="label label-success attdState">@lang('Present')</span>
            @elseif($attendance->present === 2)
              <span class="label label-warning attdState">@lang('Escaped')</span>
            @else
              <span class="label label-danger attdState">@lang('Absent')</span>
            @endif
            <a href="{{url('user/'.$attendance->student->student_code)}}">{{$attendance->student->name}}</a>
          </td>
          <td>
            <input type="hidden" name="attendances[]" value="{{$attendance->id}}">
            @if($attendance->present === 1)
              <div class="form-check">
                <input class="form-check-input position-static" type="checkbox" aria-label="Present" name="isPresent{{$loop->index}}" checked>
              </div>
            @else
            <div class="form-check">
              <input class="form-check-input position-static" type="checkbox" name="isPresent{{$loop->index}}" aria-label="Absent">
            </div>
            @endif
          </td>
          @if(count($attCount) > 0)
            @foreach ($attCount as $at)
              @if($at->student_id == $at
...[truncated]...

### app/Providers/RouteServiceProvider.php
<?php

namespace App\Providers;

use Illuminate\Support\Facades\Route;
use Illuminate\Foundation\Support\Providers\RouteServiceProvider as ServiceProvider;

class RouteServiceProvider extends ServiceProvider
{
    /**
     * This namespace is applied to your controller routes.
     *
     * In addition, it is set as the URL generator's root namespace.
     *
     * @var string
     */
    protected $namespace = 'App\Http\Controllers';

    /**
     * Define your route model bindings, pattern filters, etc.
     *
     * @return void
     */
    public function boot()
    {
        Route::patterns([
            'teacher_id' => '[0-9]+',
            'course_id' => '[0-9]+',
            'exam_id' => '[0-9]+',
            'section_id' => '[0-9]+',
            'student_id' => '[0-9]+',
            'school_code' => '[0-9]+',
            'user_code' => '[0-9]+',
            'id' => '[0-9]+',
            'code' => '[0-9]+',
            'role' => '[a-z]+',
        ]);

        parent::boot();
    }

    /**
     * Define the routes for the application.
     *
     * @return void
     */
    public function map()
    {
        $this->mapApiRoutes();

        $this->mapWebRoutes();

        //
    }

    /**
     * Define the "web" routes for the application.
     *
     * These routes all receive session state, CSRF protection, etc.
     *
     * @return void
     */
    protected function mapWebRoutes()
    {
        Route::middleware('web')
             ->namespace($this->namespace)
             ->group(base_path('routes/web.php'));
    }

    /**
     * Define the "api" routes for the application.
     *
     * These routes are typically stateless.
     *
     * @return void
     */
    protected function mapApiRoutes()
    {
        Route::prefix('api')
             ->middleware('api')
             ->namespace($this->namespace)
             ->group(base_path('routes/api.php'));
    }
}

### app/Http/Controllers/FormController.php
<?php

namespace App\Http\Controllers;

use App\Form as Form;
use App\Http\Resources\FormResource;
use Illuminate\Http\Request;

class FormController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index($school_id)
    {
      return ($school_id > 0)? FormResource::collection(Form::bySchool($school_id)->get()):response()->json(['Invalid School id: '. $school_id, 404]);
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
      $tb = new Form;
      $tb->file_path = $request->file_path;
      $tb->school_id = $request->school_id;

      return($tb->save())?response()->json([
        'status' => 'success'
        ]):response()->json([
          'status' => 'error'
        ]);
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        return new FormResource(Form::find($id));
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
      $tb = Form::find($id);
      $tb->file_path = $request->file_path;
      $tb->school_id = $request->school_id;
      return ($tb->save())?response()->json([
        'status' => 'success'
      ]):response()->json([
        'status' => 'error'
      ]);
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
      return (Form::destroy($id))?response()->json([
        'status' => 'success'
      ]):response()->json([
        'status' => 'error'
      ]);
    }
}

### resources/views/components/add-exam-form.blade.php
<form class="form-horizontal" action="{{url('exams/create')}}" method="post">
    {{ csrf_field() }}
    <div class="form-group{{ $errors->has('term') ? ' has-error' : '' }}">
        <label for="term" class="col-md-4 control-label">@lang('Terms')</label>

        <div class="col-md-6">
            <select id="term" class="form-control" name="term">
               <option value="1">@lang('1st Term')</option>
               <option value="2">@lang('2nd Term')</option>
               <option value="3">@lang('3rd Term')</option>
            </select>

            @if ($errors->has('term'))
                <span class="help-block">
                    <strong>{{ $errors->first('term') }}</strong>
                </span>
            @endif
        </div>
    </div>
    <div class="form-group{{ $errors->has('exam_name') ? ' has-error' : '' }}">
        <label for="exam_name" class="col-md-4 control-label">@lang('Examination Name')</label>

        <div class="col-md-6">
            <input id="exam_name" type="text" class="form-control" name="exam_name" value="{{ old('exam_name') }}" placeholder="@lang('Semester 1 Exam 2018, Final Exam 2019, ...')" required>

            @if ($errors->has('exam_name'))
                <span class="help-block">
                    <strong>{{ $errors->first('exam_name') }}</strong>
                </span>
            @endif
        </div>
    </div>
    <div class="form-group{{ $errors->has('start_date') ? ' has-error' : '' }}">
        <label for="start_date" class="col-md-4 control-label">@lang('Start Date')</label>

        <div class="col-md-6">
            <input id="start_date" type="text" class="form-control" name="start_date" value="{{ old('start_date') }}" placeholder="@lang('5th April...')" required>

            @if ($errors->has('start_date'))
                <span class="help-block">
                    <strong>{{ $errors->first('start_date') }}</strong>
                </span>
            @endif
        </div>
    </div>
    <div class="form-group{{ $errors->has('end_date') ? ' has-error' : '' }}">
        <label for="end_date" class="col-md-4 control-label">@lang('End Date')</label>

        <div class="col-md-6">
            <input id="end_date" type="text" class="form-control" name="end_date" value="{{ old('end_date') }}" placeholder="@lang('20th April...')" required>

            @if ($errors->has('end_date'))
                <span class="help-block">
                    <strong>{{ $errors->first('end_date') }}</strong>
                </span>
            @endif
        </div>
    </div>
    <div class="form-gro
...[truncated]...

### resources/views/components/excel-upload-form.blade.php
<form action="{{url('users/import/user-xlsx')}}" method="post" enctype="multipart/form-data">
    {{ csrf_field() }}
    <input type="hidden" name="type" value="{{$type}}">
    <div class="form-group">
        <input type="file" name="file">
    </div>
    <input type="submit" class="btn btn-default btn-sm" value="@lang('Upload')">
</form>

### resources/views/layouts/master/theme-form.blade.php
<form action="{{url('school/theme')}}" class="form-inline" method="post">
  {{csrf_field()}}
  <input type="hidden" name="s" value="{{$school->id}}">
  <div class="form-group">
      @include('layouts.theme-select')
      <button type="submit" class="btn btn-success btn-sm">@lang('Submit')</button>
  </div>
</form>

### resources/views/layouts/master/create-section-form.blade.php
<button class="btn btn-primary btn-block" id="create-section-btn-class-{{$class->id}}">+ @lang('Create a New Section')</button>
<br/>
<div class="panel panel-default" id="create-section-btn-panel-class-{{$class->id}}" style="display:none;">
  <div class="panel-body">
  <form class="form-horizontal" action="{{url('school/add-section')}}" method="post">
      {{csrf_field()}}
      <input type="hidden" name="class_id" value="{{$class->id}}"/>
      <div class="form-group">
        <label for="section_number{{$class->class_number}}" class="col-sm-2 control-label">@lang('Section Name')</label>
        <div class="col-sm-10">
          <input type="text" class="form-control" id="section_number{{$class->class_number}}" name="section_number" placeholder="@lang('A, B, C, etc..')">
        </div>
      </div>
      <div class="form-group">
        <label for="room_number{{$class->class_number}}" class="col-sm-2 control-label">@lang('Room Number')</label>
        <div class="col-sm-10">
          <input type="number" class="form-control" id="room_number{{$class->class_number}}" name="room_number" placeholder="@lang('Room Number')">
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-2 col-sm-10">
          <button type="submit" class="btn btn-danger btn-sm">@lang('Submit')</button>
        </div>
      </div>
    </form>
  </div>
</div>
<script>
  $("#create-section-btn-class-{{$class->id}}").click(function(){
    $("#create-section-btn-panel-class-{{$class->id}}").toggle();
  });
</script>

### resources/views/course/edit.blade.php
@extends('layouts.app')

@section('title', __('Course'))

@section('content')
<div class="container-fluid">
    <div class="row">
        <div class="col-md-2" id="side-navbar">
            @include('layouts.leftside-menubar')
        </div>
        <div class="col-md-10" id="main-container">
            <h2>@lang('Edit Course Data')</h2>
            @if (session('status'))
                <div class="alert alert-success">
                    {{ session('status') }}
                </div>
            @endif
            <div class="panel panel-default">
                <form class="form-horizontal" action="{{url('edit/course/'.$course->id)}}" method="post">
                    {{ csrf_field() }}
                    <div class="form-group{{ $errors->has('course_name') ? ' has-error' : '' }}">
                        <label for="course_name" class="col-md-4 control-label">@lang('Course Name')</label>

                        <div class="col-md-6">
                            <input id="course_name" type="text" class="form-control" name="course_name" value="{{ $course->course_name }}" required>

                            @if ($errors->has('course_name'))
                                <span class="help-block">
                                    <strong>{{ $errors->first('course_name') }}</strong>
                                </span>
                            @endif
                        </div>
                    </div>
                    <div class="form-group{{ $errors->has('course_time') ? ' has-error' : '' }}">
                        <label for="course_time" class="col-md-4 control-label">@lang('Course Time')</label>

                        <div class="col-md-6">
                            <input id="course_time" type="text" class="form-control" name="course_time" value="{{ $course->course_time }}" required>

                            @if ($errors->has('course_time'))
                                <span class="help-block">
                                    <strong>{{ $errors->first('course_time') }}</strong>
                                </span>
                            @endif
                        </div>
                    </div>
                    <div class="form-group">
                        <div class="col-sm-offset-4 col-sm-8">
                            <button type="submit" class="btn btn-danger">@lang('Save')</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
@endsection

### resources/views/layouts/user.blade.php
@extends('layouts.app')

@if(count($user) > 0)
  @section('title', $user->name)
@endif

@section('content')
<div class="container-fluid">
    <div class="row">
        <div class="col-md-2" id="side-navbar">
            @include('layouts.leftside-menubar')
        </div>
        <div class="col-md-9">
            <div class="panel panel-default">
              @if(count($user) > 0)
                <div class="panel-body">
                    @if (session('status'))
                        <div class="alert alert-success">
                            {{ session('status') }}
                        </div>
                    @endif

                    @component('components.user-profile',['user'=>$user])
                    @endcomponent
                </div>
              @else
                <div class="panel-body">
                    @lang('No Related Data Found.')
                </div>
              @endif
            </div>
        </div>
    </div>
</div>
@endsection

### resources/views/profile/user.blade.php
@extends('layouts.app')

@if(count(array($user)) > 0)
  @section('title', $user->name)
@endif

@section('content')
<div class="container-fluid">
    <div class="row">
        <div class="col-md-2" id="side-navbar">
            @include('layouts.leftside-menubar')
        </div>
        <div class="col-md-10" id="main-container">
            <div class="panel panel-default">
              @if(count(array($user)) > 0)
                <div class="panel-body">
                    @if (session('status'))
                        <div class="alert alert-success">
                            {{ session('status') }}
                        </div>
                    @endif

                    @component('components.user-profile',['user'=>$user])
                    @endcomponent
                </div>
              @else
                <div class="panel-body">
                    @lang('No Related Data Found.')
                </div>
              @endif
            </div>
        </div>
    </div>
</div>
@endsection

### resources/views/schools/edit.blade.php
@extends('layouts.app')

@section('title', __('Edit School'))

@section('content')
    <div class="panel panel-default">
        <div class="panel-body">
            <h2 class="text-center">@lang('Edit') {{$school->name}}</h2>

            <form class="form-horizontal" action="{{ route('schools.update', $school) }}" method="post">
                <input type="hidden" name="_method" value="PUT">
                {{ csrf_field() }}
                <div class="form-group{{ $errors->has('name') ? ' has-error' : '' }}">
                    <label for="name" class="col-md-4 control-label">@lang('School Name')</label>

                    <div class="col-md-6">
                        <input id="name" type="text" class="form-control" name="name" value="{{ $school->name }}" placeholder="@lang('School Name')" required>

                        @if ($errors->has('name'))
                            <span class="help-block">
                                <strong>{{ $errors->first('name') }}</strong>
                            </span>
                        @endif
                    </div>
                </div>

                <div class="form-group{{ $errors->has('about') ? ' has-error' : '' }}">
                    <label for="about" class="col-md-4 control-label">@lang('About School')</label>

                    <div class="col-md-6">
                        <textarea id="about" type="text" class="form-control" name="about"
                            placeholder="@lang('About School')" required>{{ $school->about }}</textarea>

                        @if ($errors->has('about'))
                            <span class="help-block">
                                <strong>{{ $errors->first('about') }}</strong>
                            </span>
                        @endif
                    </div>
                </div>

                <div class="form-group">
                    <div class="col-sm-offset-4 col-sm-8">
                        <a href="{{ route('schools.index') }}" class="btn btn-primary">@lang('Back')</a>
                        <button type="submit" class="btn btn-danger">@lang('Save')</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
@endsection

### app/Http/Controllers/UserController.php
<?php

namespace App\Http\Controllers;

use App\Department;
use App\Myclass;
use App\Section;
use App\StudentInfo;
use App\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;
use App\Http\Resources\UserResource;
use Illuminate\Support\Facades\Hash;
use App\Http\Requests\User\CreateUserRequest;
use App\Http\Requests\User\UpdateUserRequest;
use App\Http\Requests\User\CreateAdminRequest;
use App\Http\Requests\User\CreateTeacherRequest;
use App\Http\Requests\User\ChangePasswordRequest;
use App\Http\Requests\User\ImpersonateUserRequest;
use App\Http\Requests\User\CreateLibrarianRequest;
use App\Http\Requests\User\CreateAccountantRequest;
use Mavinoo\LaravelBatch\Batch;
use App\Events\UserRegistered;
use App\Events\StudentInfoUpdateRequested;
use Illuminate\Support\Facades\Log;
use App\Services\User\UserService;
/**
 * Class UserController
 * @package App\Http\Controllers
 */
class UserController extends Controller
{
    protected $userService;
    protected $user;

    public function __construct(UserService $userService, User $user){
        $this->userService = $userService;
        $this->user = $user;
    }
    /**
     * Display a listing of the resource.
     *
     * @param $school_code
     * @param $student_code
     * @param $teacher_code
     * @return \Illuminate\Http\Response
     */
    public function index($school_code, $student_code, $teacher_code){
        session()->forget('section-attendance');
        
        if($this->userService->isListOfStudents($school_code, $student_code))
            return $this->userService->indexView('list.student-list', $this->userService->getStudents());
        else if($this->userService->isListOfTeachers($school_code, $teacher_code))
            return $this->userService->indexView('list.teacher-list',$this->userService->getT
...[truncated]...