# Oracle upper-bound selected context
This condition is selected with checked trace paths and is used only as an upper-bound comparator.

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

# Oracle-selected code and test snippets
### routes/web.php
<?php

use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/


Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::middleware(['auth', 'master'])->group(function () {
    Route::get('/masters', 'MasterController@index')->name('masters.index');
    Route::resource('/schools', 'SchoolController')->only(['index', 'edit', 'store', 'update']);
});

Route::get('/home', 'HomeController@index')->name('home');

Route::middleware(['auth'])->group(function (){
  Route::get('logs', '\Rap2hpoutre\LaravelLogViewer\LogViewerController@index');
  // Route::get('/view-attendance/section/{section_id}',function($section_id){
  //   if($section_id > 0){
  //     $attendances = App\Attendance::with(['student'])->where('section_id', $section_id)->get();
  //   }
  // });
  Route::get('attendances/students/{teacher_id}/{course_id}/{exam_id}/{section_id}', 'AttendanceController@addStudentsToCourseBeforeAtt')->middleware(['teacher']);
  Route::get('attendances/{section_id}/{student_id}/{exam_id}', 'AttendanceController@index');
  Route::get('attendances/{section_id}', 'AttendanceController@sectionIndex')->middleware(['teacher']);
  Route::post('attendance/take-attendance','AttendanceController@store')->middleware(['teacher']);
  Route::get('attendance/adjust/{student_id}','AttendanceController@adjust')->middleware(['teacher']);
  Route::post('attendance/adjust','AttendanceController@adjustPost')->middleware(['teacher']);
});

Route::middleware(['auth','teacher'])->prefix('grades')->group(function (){
  Route::get('all-exams-grade', 'GradeController@allExamsGrade');
  Route::get('section/{section_id}', 'GradeController@gradesOfSection');
  Route::get('t/{teacher_id}/{course_id}/{exam_id}/{section_id}', 'GradeController@tindex')->name('teacher-grade');
  Route::get('c/{teacher_id}/{course_id}/{exam_id}/{section_id}', 'GradeController@cindex');
  Route::post('calculate-marks','GradeController@calculateMarks');
  Route::post('save-grade','GradeController@update');
});


Route::get('grades/{student_id}', 'GradeController@index')->middleware(['auth','teacher.student']);

Route::middleware(['auth','accountant'])->prefix('fees')->name('fees.')->group(func
...[truncated]...

### app/Http/Controllers/SchoolController.php
<?php

namespace App\Http\Controllers;

use App\User;
use App\School;
use App\Myclass;
use App\Section;
use App\Department;
use Illuminate\Http\Request;
use App\Http\Requests\SchoolRequest;

class SchoolController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index() {
      $schools = School::orderBy('created_at', 'desc')->paginate();

      return view('schools.index', compact('schools'));
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(SchoolRequest $request)
    {
        School::create([
            'name'        => $request->name,
            'established' => $request->established,
            'about'       => $request->about,
            'medium'      => $request->medium,
            'code'        => date("y").substr(number_format(time() * mt_rand(), 0, '', ''), 0, 6),
            'theme'       => 'flatly'
        ]);

        return redirect()->route('schools.index')->with('status', __('Created'));
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($school_id)
    {
      $admins = User::bySchool($school_id)->where('role','admin')->get();
      return view('school.admin-list',compact('admins'));
    }

    public function edit(School $school) {
        return view('schools.edit', compact('school'));
    }

    public function update(Request $request, School $school) {
        $school->name = $request->name;
        $school->about = $request->about;
        $school->save();

        return redirect()->route('schools.index');
    }

    public function addDepartment(Request $request){
      $request->validate([
        'department_name' => 'required|string|max:50',
      ]);
      $s = new Department;
      $s->school_id = \Auth::user()->school_id;
      $s->department_name = $request->department_name;
      $s->save();
      return back()->with('status', __('Created'));
    }

    public function changeTheme(Request $request){
      $tb = School::find($request->s);
      $tb->theme = $request->school_theme;
      $tb->save();
      return back();
    }

	public function setIgnoreSessions(Request $request){
		$request->session()->put('ignoreSessions', $request->ignoreSessions);
		return response()->json([
		  'data' => [
			'success' => "Setting saved"
		  ]
		]);
	}

    /**
     * Remove the spe
...[truncated]...

### app/School.php
<?php

namespace App;

use App\Model;

class School extends Model
{
  /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name', 'about', 'medium', 'code', 'theme',
    ];

  public function users()
  {
    return $this->hasMany('App\User');
  }

  public function departments()
  {
    return $this->hasMany('App\Department');
  }

  public function gradesystems()
  {
    return $this->hasMany('App\Gradesystem');
  }
}

### tests/Browser/MasterUserManagesSchoolsTest.php
<?php

namespace Tests\Browser;

use App\User;
use Tests\Browser\Pages\MasterPage;
use Tests\Browser\Pages\SchoolPage;
use Tests\DuskTestCase;
use Laravel\Dusk\Browser;
use Illuminate\Foundation\Testing\DatabaseMigrations;

class MasterUserManagesSchoolsTest extends DuskTestCase
{
    use DatabaseMigrations;

    public function setUp() {
        parent::setUp();
        $this->master = factory(User::class)->states('master')->create();
    }

    /** @test */
    public function master_user_can_see_list_schools() {
        $this->browse(function (Browser $browser) {
            $browser->loginAs($this->master)
                ->visit(new MasterPage)
                ->clickLink('Manage Schools')
                ->assertSee('School List');
        });
    }

    /** @test */
    public function master_user_creates_school() {
        $this->browse(function (Browser $browser) {
            $browser->loginAs($this->master)
                ->visit(new SchoolPage)
                ->pause(1000)
                ->click('@create-school-button')
                ->pause(1000)
                ->createSchool('Benito Juárez')
                ->assertSee('Benito Juárez');
        });
    }

    /** @test */
    public function master_user_updates_school() {
        $this->browse(function (Browser $browser) {
            $browser->loginAs($this->master)
                    ->visit(new SchoolPage)
                    ->pause(1000)
                    ->click('@edit-school-link')
                    ->pause(1000)
                    ->updateSchool($this->master->school_id, 'New name')
                    ->assertSee('New name');
        });
    }
}

### tests/Feature/Manage/SchoolModuleTest.php
<?php

namespace Tests\Feature\Manage;

use App\User;
use App\School;
use App\Myclass;
use App\Section;
use App\Department;
use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class SchoolModuleTest extends TestCase
{
    use RefreshDatabase;

    public function setUp() {
        parent::setUp();
        $master = factory(User::class)->states('master')->create();
        $this->actingAs($master);
        $this->withoutExceptionHandling();
    }

    /** @test */
    public function it_shows_schools_list() {
        $this->get(route('schools.index'))
           ->assertStatus(200)
            ->assertViewIs('schools.index');
    }

    /** @test */
    public function it_creates_a_new_school() {
        $school = make(School::class);

        $this->post(route('schools.store'), $school->toArray())
            ->assertRedirect(route('schools.index'));
    }

    /** @test */
    public function it_shows_edit_school() {
        $school = create(School::class);

        $this->get(route('schools.edit', $school))
            ->assertStatus(200)
            ->assertViewIs('schools.edit');
    }

    /** @test */
    public function a_school_can_being_edited() {
        $school = create(School::class, ['name' => 'Benito Juárez']);

        $school->name = 'New name';

        $this->from(route('schools.edit', $school->id))
            ->put(route('schools.update', $school->id), $school->toArray())
            ->assertRedirect(route('schools.index'));
    }

}

### tests/Unit/App/SchoolTest.php
<?php

namespace Tests\Unit\App;

use App\School;
use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class SchoolTest extends TestCase
{
    use RefreshDatabase;

    protected $school;

    public function setUp() {
        parent::setUp();
        $this->school = create(School::class);
    }

    /** @test */
    public function a_school_is_an_instance_of_School() {
        $this->assertInstanceOf('App\School', $this->school);
    }

    /** @test */
    public function a_school_has_users() {
        $this->assertInstanceOf(
            'Illuminate\Database\Eloquent\Collection', $this->school->users
        );
    }

    /** @test */
    public function a_school_has_departments() {
        $this->assertInstanceOf(
            'Illuminate\Database\Eloquent\Collection', $this->school->departments
        );
    }

}

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
            return $this->userService->indexView('list.teacher-list',$this->userService->getTeachers());
        else
            return view('home');
    }

    /**
     * @param $school_code
     * @param $role
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\View\View
     */
    public function indexOther($school_code, $role){
        if($this->userService->isAccountant($role))
            return $this->userService->indexOtherView('accounts.accountant-list', $this->userService->getAccountants());
        else if($this->userService->isLibrarian($role))
            return $this->userService->indexOtherView('library.librarian-list', $this->userService->getLibrarians());
        else
            return view('home');
    }

    /**
     * @return \Illuminate\Http\RedirectResponse
     */
    public function redir
...[truncated]...

### app/User.php
<?php

namespace App;

use App\Model;
use Laravel\Cashier\Billable;
use Laravel\Passport\HasApiTokens;
use Illuminate\Auth\Authenticatable;
use Illuminate\Notifications\Notifiable;
use Lab404\Impersonate\Models\Impersonate;
use Illuminate\Auth\Passwords\CanResetPassword;
use Illuminate\Foundation\Auth\Access\Authorizable;
use Illuminate\Contracts\Auth\Authenticatable as AuthenticatableContract;
use Illuminate\Contracts\Auth\Access\Authorizable as AuthorizableContract;
use Illuminate\Contracts\Auth\CanResetPassword as CanResetPasswordContract;

class User extends Model implements
    AuthenticatableContract,
    AuthorizableContract,
    CanResetPasswordContract
{
    use Authenticatable, Authorizable, CanResetPassword, HasApiTokens, Notifiable, Impersonate, Billable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name', 'email', 'password', 'role', 'code',/* school code*/'student_code', 'active', 'verified', 'school_id', 'section_id', 'address', 'about', 'phone_number', 'blood_group', 'nationality', 'gender', 'department_id',
    ];

    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password', 'remember_token',
    ];

    public function scopeStudent($q)
    {
        return $q->where('role', 'student');
    }

    public function section()
    {
        return $this->belongsTo('App\Section');
    }

    public function school()
    {
        return $this->belongsTo('App\School');
    }

    public function department()
    {
        return $this->belongsTo('App\Department','department_id', 'id');
    }

    public function studentInfo(){
        return $this->hasOne('App\StudentInfo','student_id');
    }

    public function studentBoardExam(){
        return $this->hasMany('App\StudentBoardExam','student_id');
    }

    public function notifications(){
        return $this->hasMany('App\Notification','student_id');
    }

    public function hasRole(string $role): bool
    {
        return $this->role == $role ? true : false;
    }
}

### app/StudentInfo.php
<?php

namespace App;

use App\Model;

class StudentInfo extends Model
{
    protected $table = 'student_infos';
    protected $fillable = array('student_id');
    /**
     * Get the student record associated with the user.
    */
    public function student()
    {
        return $this->belongsTo('App\User');
    }
}

### app/Http/Requests/User/CreateTeacherRequest.php
<?php

namespace App\Http\Requests\User;

use Illuminate\Foundation\Http\FormRequest;

/**
 * Class CreateTeacherRequest
 * @package App\Http\Requests\User
 */
class CreateTeacherRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     *
     * @return bool
     */
    public function authorize()
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array
     */
    public function rules()
    {
        return [
            'name' => 'required|string|max:255',
            'email' => 'sometimes|email|max:255|unique:users',
            'password' => 'required|string|min:6|confirmed',
            'gender' => 'required',
            'blood_group' => 'required',
            'department_id' => 'required|numeric',
            'phone_number' => 'required|unique:users',
        ];
    }
}

### tests/Feature/Auth/RegisterLoginTest.php
<?php

namespace Tests\Feature\Auth;

use App\User;
use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class RegisterLoginTest extends TestCase
{
    use RefreshDatabase;

    public function setUp()
    {
        parent::setUp();
    }
    /**
     * Unauthenticated User can't view a register form.
     *
     * @return void
     */
    public function test_unauthenticated_user_cannot_view_a_register_form(){
        $this->get('/register')
            ->assertStatus(302);
    }
    /**
     * User account can be created.
     *
     * @return void
     */
    public function test_user_can_be_created(){
        $master = factory(User::class)->states('master')->create();
        $this->actingAs($master);

        $this->assertDatabaseHas('users', $master->toArray());

        $admin = factory(User::class)->states('admin')->make();
        $this->followingRedirects()
            ->post('register/admin', $admin->toArray())
            ->assertStatus(200);
    }
    /**
     * User can view a login form.
     *
     * @return void
     */
    public function test_user_can_view_a_login_form(){
        $response = $this->get('/login');
        $response->assertSuccessful();
        $response->assertViewIs('auth.login');
    }
    /**
     * User can log in.
     *
     * @return void
     */
    public function test_user_can_log_in(){
        $user = factory(User::class)->states('admin')->create([
            'password' => bcrypt('secret'),
        ]);

        $this->assertDatabaseHas('users', $user->toArray());
        
        $response = $this->from('/login')->post('/login', [
            'email' => $user->email,
            'password' => 'secret',
        ]);
        
        $response->assertRedirect('/home');
        $this->assertAuthenticatedAs($user);
    }
}

### tests/Feature/UserModuleTest.php
<?php

namespace Tests\Feature;

use App\User;
use App\School;
use App\Section;
use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class UserModuleTest extends TestCase
{
    use RefreshDatabase;

    public function setUp() {
        parent::setUp();
        $admin = factory(User::class)->states('admin')->create();
        $this->actingAs($admin);
        $this->withoutExceptionHandling();
    }
    /** @test */
    public function can_view_students_of_a_school(){
        $school = factory(School::class)->create();
        $response = $this->get('users/'.$school->code.'/1/0');
        $response->assertStatus(200);
        $response->assertViewIs('list.student-list');
        $response->assertViewHas('users');
    }
    /** @test */
    public function can_view_teachers_of_a_school(){
        $school = factory(School::class)->create();
        $response = $this->get('users/'.$school->code.'/0/1');
        $response->assertStatus(200);
        $response->assertViewIs('list.teacher-list');
        $response->assertViewHas('users');
    }
    /** @test */
    public function can_view_accountants_of_a_school(){
        $school = factory(School::class)->create();
        $response = $this->get('users/'.$school->code.'/accountant');
        $response->assertStatus(200);
        $response->assertViewIs('accounts.accountant-list');
        $response->assertViewHas('users');
    }
    /** @test */
    public function can_view_librarians_of_a_school(){
        $school = factory(School::class)->create();
        $response = $this->get('users/'.$school->code.'/librarian');
        $response->assertStatus(200);
        $response->assertViewIs('library.librarian-list');
        $response->assertViewHas('users');
    }
    /** @test */
    public function can_view_students_of_a_section(){
        $section = factory(Section::class)->create();
        $response = $this->get('section/students/'.$section->id);
        $response->assertStatus(200);
        $response->assertViewIs('profile.section-students');
        $response->assertViewHas('students');
    }
    /** @test */
    public function can_view_promote_section_students_form(){
        $section = factory(Section::class)->create();
        $response = $this->get('school/promote-students/'.$section->id);
        $response->assertStatus(200);
        $response->assertViewIs('school.promote-students');
        $response->assertViewHas(['students','classes','section_id',]);
    }
    /** @test */
    public function can_promote_section_students(){
       
...[truncated]...

### tests/Unit/App/UsersTest.php
<?php

namespace Tests\Unit\App;

use App\User;
use App\School;
use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class UsersTest extends TestCase
{
    use RefreshDatabase;

    protected $user;

    public function setUp() {
        parent::setUp();
        $this->user = create(User::class);
    }

    /** @test */
    public function an_user_is_an_instance_of_User() {
        $this->assertInstanceOf('App\User', $this->user);
    }

    /** @test */
    public function an_user_belongs_to_section() {
        $this->assertInstanceOf('App\Section', $this->user->section);
    }

    /** @test */
    public function an_user_belongs_to_school() {
        $this->assertInstanceOf('App\School', $this->user->school);
    }

    /** @test */
    public function an_user_belongs_to_department() {
        $this->assertInstanceOf('App\Department', $this->user->department);
    }

    /** @test */
    public function an_user_has_role() {
        $accountant = factory(User::class)->states('accountant')->create();
        $admin      = factory(User::class)->states('admin')->create();
        $librarian  = factory(User::class)->states('librarian')->create();
        $master     = factory(User::class)->states('master')->create();
        $student    = factory(User::class)->states('student')->create();
        $teacher    = factory(User::class)->states('teacher')->create();

        $this->assertTrue($accountant->hasRole('accountant'));
        $this->assertTrue($admin->hasRole('admin'));
        $this->assertTrue($librarian->hasRole('librarian'));
        $this->assertTrue($master->hasRole('master'));
        $this->assertTrue($student->hasRole('student'));
        $this->assertTrue($teacher->hasRole('teacher'));
    }

    /** @test */
    public function the_users_are_filter_by_school() {
        $school = create(School::class);
        $users  = create(User::class, ['school_id' => $school->id], 2);

        $other_school = create(School::class);
        $other_users  = create(User::class, ['school_id' => $other_school->id], 4);

        $this->assertEquals(User::bySchool($school->id)->count(), $users->count());
    }
}

### tests/Browser/LoginTest.php
<?php

namespace Tests\Browser;

use App\User;
use Tests\DuskTestCase;
use Laravel\Dusk\Browser;
use Illuminate\Foundation\Testing\DatabaseMigrations;

class LoginTest extends DuskTestCase
{
    use DatabaseMigrations;

    /** @test */
    public function user_master_can_sign_in() {
        $user = factory(User::class)->states('master')->create();

        $this->browse(function ($browser) use ($user) {
            $browser->visit('/login')
                    ->waitForText('Login')
                    ->type('email', $user->email)
                    ->type('password', 'secret')
                    ->press('Login')
                    ->assertPathIs('/masters');
        });
    }
}

### app/Http/Controllers/MyclassController.php
<?php

namespace App\Http\Controllers;

use App\Myclass as Myclass;
use App\Http\Resources\ClassResource;
use Illuminate\Http\Request;

class MyclassController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
     public function index($school_id)
     {
       return ($school_id > 0)? ClassResource::collection(Myclass::bySchool($school_id)->get()):response()->json([
         'Invalid School id: '. $school_id,
         404
       ]);
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
      $request->validate([
        'class_number' => 'required'
      ]);
      $tb = new Myclass;
      $tb->class_number = $request->class_number;
      $tb->school_id = \Auth::user()->school_id;
      $tb->group = (!empty($request->group))?$request->group:'';
      $tb->save();
      return back()->with('status', __('Created'));
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        return new ClassResource(Myclass::find($id));
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
      $tb = Myclass::find($id);
      $tb->class_number = $request->class_number;
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
      return (Myclass::destroy($id))?response()->json([
        'status' => 'success'
      ]):response()->json([
        'status' => 'error'
      ]);
    }
}

### app/Http/Controllers/SectionController.php
<?php

namespace App\Http\Controllers;

use App\Section as Section;
use App\Http\Resources\SectionResource;
use Illuminate\Http\Request;

class SectionController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
     public function index()
     {
      $classes = \App\Myclass::bySchool(\Auth::user()->school->id)
                  ->get();
      $classeIds = \App\Myclass::bySchool(\Auth::user()->school->id)
                    ->pluck('id')
                    ->toArray();
      $sections = \App\Section::whereIn('class_id',$classeIds)
                  ->orderBy('section_number')
                  ->get();
      $exams = \App\ExamForClass::whereIn('class_id',$classeIds)
                  ->where('active', 1)
                  ->groupBy('class_id')
                  ->get();
      return view('school.sections',[
        'classes'=>$classes,
        'sections'=>$sections,
        'exams'=>$exams
      ]);
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
      $request->validate([
        'section_number' => 'required',
        'room_number' => 'required|numeric',
        'class_id' => 'required|numeric',
      ]);
      $tb = new Section;
      $tb->section_number = $request->section_number;
      $tb->room_number = $request->room_number;
      $tb->class_id = $request->class_id;
      $tb->save();
      return back()->with('status', __('Created'));
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        return new SectionResource(Section::find($id));
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
      $tb = Section::find($id);
      $tb->section_number = $request->section_number;
      $tb->room_number = $request->room_number;
    
...[truncated]...

### app/Myclass.php
<?php

namespace App;

use App\Model;

class Myclass extends Model
{
    protected $table = "classes";
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'class_number', 'group', 'school_id',
    ];
    /**
     * Get the school record associated with the user.
    */
    public function school()
    {
        return $this->belongsTo('App\School');
    }

	public function sections()
    {
        return $this->hasMany('App\Section','class_id');
    }

    // public function exam()
    // {
    //     return $this->belongsTo('App\ExamForClass');
    // }

	public function books()
    {
        return $this->hasMany('App\Book','class_id');
    }
}

### app/Section.php
<?php

namespace App;

use App\Model;

class Section extends Model
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'section_number', 'room_number', 'class_id', 'user_id',
    ];
    /**
     * Get the class record associated with the user.
    */
    public function class()
    {
        return $this->belongsTo('App\Myclass');
    }
}

### tests/Feature/Manage/ClassModuleTest.php
<?php

namespace Tests\Feature\Manage;

use App\User;
use App\Myclass;
use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class ClassModuleTest extends TestCase
{
    use RefreshDatabase;

    public function setUp() {
        parent::setUp();
        $admin = factory(User::class)->states('admin')->create();
        $this->actingAs($admin);
        $this->withoutExceptionHandling();
    }

    /** @test */
    public function view_is(){
         $this->get('school/sections')
            ->assertViewIs('school.sections');
    }

    /** @test */
    public function it_shows_the_class_list() {
        $this->get('school/sections')
            ->assertStatus(200)
            ->assertViewHas('classes');
    }

    /** @test */
    public function admin_can_create_class() {
        $class = factory(Myclass::class)->make();
        $this->followingRedirects()
            ->post('school/add-class', $class->toArray())
            ->assertStatus(200);

        $this->assertDatabaseHas('classes', $class->toArray());

        $this->get('settings')
            ->assertSee('Manage '.$class['class_number']);
    }
}

### tests/Feature/Manage/SectionModuleTest.php
<?php

namespace Tests\Feature\Manage;

use App\Section;
use App\User;
use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class SectionModuleTest extends TestCase
{
    use RefreshDatabase;

    public function setUp() {
        parent::setUp();
        $admin = factory(User::class)->states('admin')->create();
        $this->actingAs($admin);
        $this->withoutExceptionHandling();
    }
    /** @test */
    public function view_is(){
         $this->get('school/sections')
            ->assertViewIs('school.sections');
    }
    /** @test */
    public function it_shows_the_section_list() {
        $this->get('school/sections')
            ->assertStatus(200)
            ->assertViewHas('sections');
    }
    /** @test */
    public function admin_can_create_section() {
        $section = factory(Section::class)->make();
        $this->followingRedirects()
            ->post('school/add-section', $section->toArray())
            ->assertStatus(200);

        $this->assertDatabaseHas('sections', $section->toArray());

        $this->get('settings')
            ->assertSee('Section '.$section['section_number']);
    }
}

### tests/Unit/App/MyclassTest.php
<?php

namespace Tests\Unit\App;

use App\School;
use App\Myclass;
use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class MyclassTest extends TestCase
{
    use RefreshDatabase;

    protected $class;

    public function setUp() {
        parent::setUp();
        $this->class = create(Myclass::class);
    }

    /** @test */
    public function a_class_is_an_instance_of_Myclass() {
        $this->assertInstanceOf('App\Myclass', $this->class);
    }

    /** @test */
    public function a_class_belongs_to_school() {
        $this->assertInstanceOf('App\School', $this->class->school);
    }

    /** @test */
    public function a_class_has_sections() {
        $this->assertInstanceOf(
            'Illuminate\Database\Eloquent\Collection', $this->class->sections
        );
    }

    /** @test */
    public function a_class_has_books() {
        $this->assertInstanceOf(
            'Illuminate\Database\Eloquent\Collection', $this->class->books
        );
    }

    /** @test */
    public function my_class_are_filter_by_school() {
        $school = create(School::class);
        $klass  = create(Myclass::class, ['school_id' => $school->id], 2);

        $other_school = create(School::class);
        $other_klass  = create(Myclass::class, ['school_id' => $other_school->id], 4);

        $this->assertEquals(Myclass::bySchool($school->id)->count(), $klass->count());
    }
}

### tests/Unit/App/SectionTest.php
<?php

namespace Tests\Unit\App;

use App\Section;
use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class SectionTest extends TestCase
{
    use RefreshDatabase;

    protected $section;

    public function setUp() {
        parent::setUp();
        $this->section = create(Section::class);
    }

    /** @test */
    public function a_section_is_an_instance_of_Section() {
        $this->assertInstanceOf('App\Section', $this->section);
    }

    /** @test */
    public function a_section_belongs_to_class() {
        $this->assertInstanceOf('App\Myclass', $this->section->class);
    }
}

### tests/Unit/App/RoutineTest.php
<?php

namespace Test\Unit\App;

use App\School;
use App\Routine;
use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;

class RoutineTest extends TestCase
{
    use RefreshDatabase;

    /** @test */
    public function the_routines_are_filter_by_school() {
        $school   = create(School::class);
        $routines = create(Routine::class, ['school_id' => $school->id], 2);

        $other_school   = create(School::class);
        $other_routines = create(Routine::class, ['school_id' => $other_school->id], 4);

        $this->assertEquals(Routine::bySchool($school->id)->count(), $routines->count());
    }
}

### app/Http/Controllers/AttendanceController.php
<?php

namespace App\Http\Controllers;

use App\Attendance;
use App\User;
use App\Http\Resources\AttendanceResource;
use Illuminate\Http\Request;
use App\Http\Requests\Attendance\StoreAttendanceRequest;
use App\Http\Traits\GradeTrait;
use App\Services\Attendance\AttendanceService;

class AttendanceController extends Controller
{
    use GradeTrait;
    
    protected $attendanceService;

    public function __construct(AttendanceService $attendanceService){
      $this->attendanceService = $attendanceService;
    }
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index($section_id, $student_id, $exam_id)
    {
      if($section_id > 0 && \Auth::user()->role != 'student'){
        // View attendances of students of a section
        $students = $this->attendanceService->getStudentsBySection($section_id);
        $attendances = $this->attendanceService->getTodaysAttendanceBySectionId($section_id);
        $attCount = $this->attendanceService->getAllAttendanceBySecAndExam($section_id,$exam_id);

        return view('attendance.attendance', [
          'students' => $students,
          'attendances' => $attendances,
          'attCount' => $attCount,
          'section_id'=>$section_id,
 
...[truncated]...