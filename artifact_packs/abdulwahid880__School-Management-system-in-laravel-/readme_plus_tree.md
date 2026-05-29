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