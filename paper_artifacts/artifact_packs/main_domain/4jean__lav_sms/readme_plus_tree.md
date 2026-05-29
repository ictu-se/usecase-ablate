# README
## readme.md
## **Laravel School Management System** 

**LAVSMS** is developed for educational institutions like schools and colleges built on Laravel 8

**SCREENSHOTS** 

**Dashboard**
<img src="https://i.ibb.co/D4T0z6T/dashboard.png" alt="dashboard" border="0">

**Login**
<img src="https://i.ibb.co/Rh1Bfwk/login.png" alt="login" border="0">

**Student Marksheet**
<img src="https://i.ibb.co/GCgv5ZR/marksheet.png" alt="marksheet" border="0">

**System Settings**
<img src="https://i.ibb.co/Kmrhw69/system-settings.png" alt="system-settings" border="0">

**Print Marksheet**
<div style="clear: both"> </div>
<img src="https://i.ibb.co/5c1GHCj/capture-20210530-115521-crop.png" alt="print-marksheet">

**Print Tabulation Sheet & Marksheet**
<img src="https://i.ibb.co/QmscPfn/capture-20210530-115802.png" alt="tabulation-sheet" border="0">

<hr />  

There are 7 types of user accounts. They include:
 
Administrators (Super Admin & Admin)
- Librarian
- Accountant
- Teacher
- Student
- Parent

**Requirements** 

Check Laravel 8 Requirements https://laravel.com/docs/8.x

**Installation**
- Install dependencies (composer install)
- Set Database Credentials & App Settings in dotenv file (.env)
- Migrate Database (php artisan migrate)
- Database seed (php artisan db:seed)

**Login Credentials**
After seeding. Login details as follows:

| Account Type  | Username | Email | Password |
| ------------- | -------- | ----- | -------- |
| Super Admin | cj | cj@cj.com | cj |
|  Admin | admin | admin@admin.com | cj |
|  Teacher | teacher | teacher@teacher.com | cj |
|  Parent | parent | parent@parent.com | cj |
|  Accountant | accountant | accountant@accountant.com | cj |
|  Student | student | student@student.com | cj |

#### **FUNCTIONS OF ACCOUNTS** 

**-- SUPER ADMIN**
- Only Super Admin can delete any record
- Create any user account
 
**-- Administrators (Super Admin & Admin)**

- Manage students class/sections
- View marksheet of students
- Create, Edit and manage all user accounts & profiles
- Create, Edit and manage Exams & Grades
- Create, Edit and manage Subjects
- Manage noticeboard of school
- Notices are visible in calendar in dashboard
- Edit system settings
- Manage Payments & fees

**-- ACCOUNTANT**
- Manage Payments & fees
- Print Payment Receipts

**-- LIBRARIAN**
- Manage Books in the Library

**-- TEACHER**
- Manage Own Class/Section
- Manage Exam Records for own Subjects
- Manage Timetable if Assigned as Class Teacher
- Manage own profile
- Upload Study Materials

**-- STUDENT**
- View teacher profile
- View own class subjects
- View own marks and class timetable
- View Payments
- View library and book status
- View noticeboard and school events in calendar
- Manage own profile

**-- PARENT**
- View teacher profile
- View own child's marksheet (Download/Print PDF)
- View own child's Timetable
- View own child's payments
- View noticeboard and school events in calendar
- Manage own profile

### **Contributing**

Your Contributions & suggestions are welcomed. Please use Pull Request

### **Security Vulnerabilities**

If you discover a security vulnerability within LAV_SMS, please send an e-mail to CJ Inspired via cjay.pub@gmail.com. All security vulnerabilities will be promptly addressed.

***Please Note*** that some sections of this project are in the work-in-progress stage and would be updated soon. These include:

- The Noticeboard/Calendar in the Dashboard Area
- Librarian/Acountant user pages
- Library Resources/Study Materials Upload for Students

### **Contact [CJ INSPIRED]**
- Phone : +2347068149559

# File tree
SECURITY.md
_ide_helper.php
app
  Console
    Kernel.php
  Exceptions
    Handler.php
  Helpers
    Mk.php
    Pay.php
    Qs.php
  Http
    Controllers
      AjaxController.php
      Auth
        ForgotPasswordController.php
        LoginController.php
        RegisterController.php
        ResetPasswordController.php
        VerificationController.php
      Controller.php
      HomeController.php
      MyAccountController.php
      MyParent
        MyController.php
      SuperAdmin
        SettingController.php
      SupportTeam
        BookController.php
        BookRequestController.php
        DormController.php
        ExamController.php
        GradeController.php
        MarkController.php
        MyClassController.php
        PaymentController.php
        PinController.php
        PromotionController.php
        SectionController.php
        StudentRecordController.php
        SubjectController.php
        TimeTableController.php
        UserController.php
      TestController.php
    Kernel.php
    Middleware
      Authenticate.php
      CheckForMaintenanceMode.php
      Custom
        Admin.php
        ExamIsLocked.php
        MyParent.php
        Student.php
        SuperAdmin.php
        Teacher.php
        TeamAccount.php
        TeamSA.php
        TeamSAT.php
      EncryptCookies.php
      PreventRequestsDuringMaintenance.php
      RedirectIfAuthenticated.php
      TrimStrings.php
      TrustProxies.php
      VerifyCsrfToken.php
    Requests
      Dorm
        DormCreate.php
        DormUpdate.php
      Exam
        ExamCreate.php
        ExamUpdate.php
      Grade
        GradeCreate.php
        GradeUpdate.php
      Mark
        MarkSelector.php
        MarkUpdate.php
      MyClass
        ClassCreate.php
        ClassUpdate.php
      Payment
        PaymentCreate.php
        PaymentUpdate.php
      Pin
        PinCreate.php
        PinVerify.php
      Section
        SectionCreate.php
        SectionUpdate.php
      SettingUpdate.php
      Student
        StudentRecordCreate.php
        StudentRecordUpdate.php
      Subject
        SubjectCreate.php
        SubjectUpdate.php
      TimeTable
        TSRequest.php
        TTRecordRequest.php
        TTRequest.php
      UserChangePass.php
      UserRequest.php
      UserUpdate.php
  Models
    BloodGroup.php
    Book.php
    BookRequest.php
    ClassType.php
    Dorm.php
    Exam.php
    ExamRecord.php
    Grade.php
    Lga.php
    Mark.php
    MyClass.php
    Nationality.php
    Payment.php
    PaymentRecord.php
    Pin.php
    Promotion.php
    Receipt.php
    Section.php
    Setting.php
    Skill.php
    StaffRecord.php
    State.php
    StudentRecord.php
    Subject.php
    TimeSlot.php
    TimeTable.php
    TimeTableRecord.php
    UserType.php
  Providers
    AppServiceProvider.php
    AuthServiceProvider.php
    BroadcastServiceProvider.php
    EventServiceProvider.php
    RouteServiceProvider.php
  Repositories
    DormRepo.php
    ExamRepo.php
    LocationRepo.php
    MarkRepo.php
    MyClassRepo.php
    PaymentRepo.php
    PinRepo.php
    SettingRepo.php
    StudentRepo.php
    TimeTableRepo.php
    UserRepo.php
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
  hashing.php
  logging.php
  mail.php
  queue.php
  services.php
  session.php
  view.php
package.json
phpunit.xml
readme.md
resources
  views
    auth
      login.blade.php
      passwords
        Dmail.blade.php
        email.blade.php
        reset.blade.php
      register.blade.php
      verify.blade.php
    layouts
      app.blade.php
      login_master.blade.php
      master.blade.php
    pages
      accountant
        menu.blade.php
      admin
        dashboard.blade.php
        menu.blade.php
      librarian
        menu.blade.php
      other
        privacy_policy.blade.php
        terms_of_use.blade.php
      parent
        children.blade.php
        menu.blade.php
      student
        menu.blade.php
      super_admin
        menu.blade.php
        settings.blade.php
      support_team
        classes
          edit.blade.php
          index.blade.php
        dashboard.blade.php
        dorms
          edit.blade.php
          index.blade.php
        exams
          edit.blade.php
          index.blade.php
        grades
          edit.blade.php
          index.blade.php
        marks
          batch_fix.blade.php
          bulk.blade.php
          edit.blade.php
          index.blade.php
          manage.blade.php
          print
          random.blade.php
          select_year.blade.php
          selector.blade.php
          show
          tabulation
        my_account.blade.php
        payments
        pins
        sections
        students
        subjects
        timetables
        users
      teacher
    partials
    test.blade.php
routes
server.php
tests
webpack.mix.js