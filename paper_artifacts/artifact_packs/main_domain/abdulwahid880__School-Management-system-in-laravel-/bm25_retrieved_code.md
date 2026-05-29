# README-derived retrieval query
abdulwahid880 School Management system in laravel  ## readme.md
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
   
...[truncated]...

# BM25 selected code snippets
### readme.md
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
[![](https://sourcerer.io/fame/changeweb/changeweb/Unifiedtransform/im
...[truncated]...

### composer.json
{
    "name": "changeweb/unifiedtransform",
    "description": "A school management software.",
    "keywords": ["school", "management"],
    "license": "GPL 3",
    "type": "project",
    "require": {
        "php": ">=7.0.0",
        "doctrine/dbal": "^2.9",
        "fideloper/proxy": "~3.3",
        "jdavidbakr/laravel-cache-garbage-collector": "^1.0",
        "lab404/laravel-impersonate": "1.2",
        "laravel/cashier": "~7.0",
        "laravel/framework": "5.5.*",
        "laravel/passport": "^4.0",
        "laravel/tinker": "~1.0",
        "maatwebsite/excel": "^3.1",
        "maddhatter/laravel-fullcalendar": "^1.3",
        "mavinoo/laravel-batch": "2.0",
        "renatomarinho/laravel-page-speed": "^1.8"
    },
    "require-dev": {
        "barryvdh/laravel-debugbar": "^3.2",
        "filp/whoops": "~2.0",
        "friendsofphp/php-cs-fixer": "^2.14",
        "fzaninotto/faker": "~1.4",
        "laravel/dusk": "^2.0",
        "mockery/mockery": "~1.0",
        "phpunit/phpunit": "~6.0",
        "rap2hpoutre/laravel-log-viewer": "^0.22.1"
    },
    "autoload": {
        "classmap": [
            "database/seeds",
            "database/factories"
        ],
        "psr-4": {
            "App\\": "app/"
        }
    },
    "autoload-dev": {
        "psr-4": {
            "Tests\\": "tests/"
        },
        "files": [
            "tests/utilities/functions.php"
        ]
    },
    "extra": {
        "laravel": {
            "dont-discover": [
                "laravel/dusk",
                "barryvdh/laravel-debugbar",
                "rap2hpoutre/laravel-log-viewer"
            ]
        }
    },
    "scripts": {
        "post-root-package-install": [
            "@php -r \"file_exists('.env') || copy('.env.example', '.env');\""
        ],
        "post-create-project-cmd": [
            "@php artisan key:generate"
        ],
        "post-install-cmd": [
            "@php artisan passport:keys"
        ],
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover"
        ]
    },
    "config": {
        "preferred-install": "dist",
        "sort-packages": true,
        "optimize-autoloader": true
    }
}

### config/auth.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Authentication Defaults
    |--------------------------------------------------------------------------
    |
    | This option controls the default authentication "guard" and password
    | reset options for your application. You may change these defaults
    | as required, but they're a perfect start for most applications.
    |
    */

    'defaults' => [
        'guard' => 'web',
        'passwords' => 'users',
    ],

    /*
    |--------------------------------------------------------------------------
    | Authentication Guards
    |--------------------------------------------------------------------------
    |
    | Next, you may define every authentication guard for your application.
    | Of course, a great default configuration has been defined for you
    | here which uses session storage and the Eloquent user provider.
    |
    | All authentication drivers have a user provider. This defines how the
    | users are actually retrieved out of your database or other storage
    | mechanisms used by this application to persist your user's data.
    |
    | Supported: "session", "token"
    |
    */

    'guards' => [
        'web' => [
            'driver' => 'session',
            'provider' => 'users',
        ],

        'api' => [
            'driver' => 'passport',
            'provider' => 'users',
        ],
    ],

    /*
    |--------------------------------------------------------------------------
    | User Providers
    |--------------------------------------------------------------------------
    |
    | All authentication drivers have a user provider. This defines how the
    | users are actually retrieved out of your database or other storage
    | mechanisms used by this application to persist your user's data.
    |
    | If you have multiple user tables or models you may configure multiple
    | sources which represent each model / table. These sources may then
    | be assigned to any extra authentication guards you have defined.
    |
    | Supported: "database", "eloquent"
    |
    */

    'providers' => [
        'users' => [
            'driver' => 'eloquent',
            'model' => App\User::class,
        ],

        // 'users' => [
        //     'driver' => 'database',
        //     'table' => 'users',
        // ],
    ],

    /*
    |--------------------------------------------------------------------------
    | Resetting Passwords
    |------------------------------------------------------------------
...[truncated]...

### config/mail.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Mail Driver
    |--------------------------------------------------------------------------
    |
    | Laravel supports both SMTP and PHP's "mail" function as drivers for the
    | sending of e-mail. You may specify which one you're using throughout
    | your application here. By default, Laravel is setup for SMTP mail.
    |
    | Supported: "smtp", "sendmail", "mailgun", "mandrill", "ses",
    |            "sparkpost", "log", "array"
    |
    */

    'driver' => env('MAIL_DRIVER', 'smtp'),

    /*
    |--------------------------------------------------------------------------
    | SMTP Host Address
    |--------------------------------------------------------------------------
    |
    | Here you may provide the host address of the SMTP server used by your
    | applications. A default option is provided that is compatible with
    | the Mailgun mail service which will provide reliable deliveries.
    |
    */

    'host' => env('MAIL_HOST', 'smtp.mailgun.org'),

    /*
    |--------------------------------------------------------------------------
    | SMTP Host Port
    |--------------------------------------------------------------------------
    |
    | This is the SMTP port used by your application to deliver e-mails to
    | users of the application. Like the host we have set this value to
    | stay compatible with the Mailgun e-mail application by default.
    |
    */

    'port' => env('MAIL_PORT', 587),

    /*
    |--------------------------------------------------------------------------
    | Global "From" Address
    |--------------------------------------------------------------------------
    |
    | You may wish for all e-mails sent by your application to be sent from
    | the same address. Here, you may specify a name and address that is
    | used globally for all e-mails that are sent by your application.
    |
    */

    'from' => [
        'address' => env('MAIL_FROM_ADDRESS', 'hello@example.com'),
        'name' => env('MAIL_FROM_NAME', 'Example'),
    ],

    /*
    |--------------------------------------------------------------------------
    | E-Mail Encryption Protocol
    |--------------------------------------------------------------------------
    |
    | Here you may specify the encryption protocol that should be used when
    | the application send e-mail messages. A sensible default using the
    | transport layer security protocol should provide great security.
    |
    */

    'encryption' => env
...[truncated]...

### config/database.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Database Connection Name
    |--------------------------------------------------------------------------
    |
    | Here you may specify which of the database connections below you wish
    | to use as your default connection for all database work. Of course
    | you may use many connections at once using the Database library.
    |
    */

    'default' => env('DB_CONNECTION', 'mysql'),

    /*
    |--------------------------------------------------------------------------
    | Database Connections
    |--------------------------------------------------------------------------
    |
    | Here are each of the database connections setup for your application.
    | Of course, examples of configuring each database platform that is
    | supported by Laravel is shown below to make development simple.
    |
    |
    | All database work in Laravel is done through the PHP PDO facilities
    | so make sure you have the driver for your particular database of
    | choice installed on your machine before you begin development.
    |
    */

    'connections' => [

        'sqlite' => [
            'driver' => 'sqlite',
            'database' => env('DB_DATABASE', database_path('database.sqlite')),
            'prefix' => '',
        ],

        'mysql' => [
            'driver' => 'mysql',
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '3306'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'unix_socket' => env('DB_SOCKET', ''),
            'charset' => 'utf8mb4',
            'collation' => 'utf8mb4_unicode_ci',
            'prefix' => '',
            'strict' => false,
            'engine' => null,
        ],

        'pgsql' => [
            'driver' => 'pgsql',
            'host' => env('DB_HOST', '127.0.0.1'),
            'port' => env('DB_PORT', '5432'),
            'database' => env('DB_DATABASE', 'forge'),
            'username' => env('DB_USERNAME', 'forge'),
            'password' => env('DB_PASSWORD', ''),
            'charset' => 'utf8',
            'prefix' => '',
            'schema' => 'public',
            'sslmode' => 'prefer',
        ],

        'sqlsrv' => [
            'driver' => 'sqlsrv',
            'host' => env('DB_HOST', 'localhost'),
            'port' => env('DB_PORT', '1433'),
            'database' => env('DB_DATABASE', 'forge'),
            'username
...[truncated]...

### config/app.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Application Name
    |--------------------------------------------------------------------------
    |
    | This value is the name of your application. This value is used when the
    | framework needs to place the application's name in a notification or
    | any other location as required by the application or its packages.
    |
    */

    'name' => env('APP_NAME', 'Laravel'),

    /*
    |--------------------------------------------------------------------------
    | Application Environment
    |--------------------------------------------------------------------------
    |
    | This value determines the "environment" your application is currently
    | running in. This may determine how you prefer to configure various
    | services your application utilizes. Set this in your ".env" file.
    |
    */

    'env' => env('APP_ENV', 'production'),

    /*
    |--------------------------------------------------------------------------
    | Application Debug Mode
    |--------------------------------------------------------------------------
    |
    | When your application is in debug mode, detailed error messages with
    | stack traces will be shown on every error that occurs within your
    | application. If disabled, a simple generic error page is shown.
    |
    */

    'debug' => env('APP_DEBUG', false),

    /*
    |--------------------------------------------------------------------------
    | Application URL
    |--------------------------------------------------------------------------
    |
    | This URL is used by the console to properly generate URLs when using
    | the Artisan command line tool. You should set this to the root of
    | your application so that it is used when running Artisan tasks.
    |
    */

    'url' => env('APP_URL', 'http://localhost'),

    /*
    |--------------------------------------------------------------------------
    | Application Timezone
    |--------------------------------------------------------------------------
    |
    | Here you may specify the default timezone for your application, which
    | will be used by the PHP date and date-time functions. We have gone
    | ahead and set this to a sensible default for you out of the box.
    |
    */

    'timezone' => 'Asia/Dhaka',//'UTC',

    /*
    |--------------------------------------------------------------------------
    | Application Locale Configuration
    |------------------------------------------------------------------
...[truncated]...

### config/queue.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Queue Driver
    |--------------------------------------------------------------------------
    |
    | Laravel's queue API supports an assortment of back-ends via a single
    | API, giving you convenient access to each back-end using the same
    | syntax for each one. Here you may set the default queue driver.
    |
    | Supported: "sync", "database", "beanstalkd", "sqs", "redis", "null"
    |
    */

    'default' => env('QUEUE_DRIVER', 'sync'),

    /*
    |--------------------------------------------------------------------------
    | Queue Connections
    |--------------------------------------------------------------------------
    |
    | Here you may configure the connection information for each server that
    | is used by your application. A default configuration has been added
    | for each back-end shipped with Laravel. You are free to add more.
    |
    */

    'connections' => [

        'sync' => [
            'driver' => 'sync',
        ],

        'database' => [
            'driver' => 'database',
            'table' => 'jobs',
            'queue' => 'default',
            'retry_after' => 90,
        ],

        'beanstalkd' => [
            'driver' => 'beanstalkd',
            'host' => 'localhost',
            'queue' => 'default',
            'retry_after' => 90,
        ],

        'sqs' => [
            'driver' => 'sqs',
            'key' => 'your-public-key',
            'secret' => 'your-secret-key',
            'prefix' => 'https://sqs.us-east-1.amazonaws.com/your-account-id',
            'queue' => 'your-queue-name',
            'region' => 'us-east-1',
        ],

        'redis' => [
            'driver' => 'redis',
            'connection' => 'default',
            'queue' => 'default',
            'retry_after' => 90,
        ],

    ],

    /*
    |--------------------------------------------------------------------------
    | Failed Queue Jobs
    |--------------------------------------------------------------------------
    |
    | These options configure the behavior of failed queue job logging so you
    | can control which database and table are used to store the jobs that
    | have failed. You may change them to any database / table you wish.
    |
    */

    'failed' => [
        'database' => env('DB_CONNECTION', 'mysql'),
        'table' => 'failed_jobs',
    ],

];

### CONTRIBUTING.md
In order to contribute please maintain following rules:
- For any new changes use `dev_for_new_features` this branch.
- Make a Pull Request to `dev_for_new_features` this branch not to `master` so that master branch can only have stable changes.
- Before making any pull request discuss about the change in a New Issue.
- Describe the current behavior and explain which behavior you expected to see and why
- Explain why this changes will be useful to most Unifiedtransform users
- If you have changes on different features seperate them in different commits and pull requests
- Make one feature change at a time
- Share screenshots of your changes. It will make review process faster
- Share the reason behind your changes

### config/session.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Session Driver
    |--------------------------------------------------------------------------
    |
    | This option controls the default session "driver" that will be used on
    | requests. By default, we will use the lightweight native driver but
    | you may specify any of the other wonderful drivers provided here.
    |
    | Supported: "file", "cookie", "database", "apc",
    |            "memcached", "redis", "array"
    |
    */

    'driver' => env('SESSION_DRIVER', 'file'),

    /*
    |--------------------------------------------------------------------------
    | Session Lifetime
    |--------------------------------------------------------------------------
    |
    | Here you may specify the number of minutes that you wish the session
    | to be allowed to remain idle before it expires. If you want them
    | to immediately expire on the browser closing, set that option.
    |
    */

    'lifetime' => env('SESSION_LIFETIME', 120),

    'expire_on_close' => false,

    /*
    |--------------------------------------------------------------------------
    | Session Encryption
    |--------------------------------------------------------------------------
    |
    | This option allows you to easily specify that all of your session data
    | should be encrypted before it is stored. All encryption will be run
    | automatically by Laravel and you can use the Session like normal.
    |
    */

    'encrypt' => false,

    /*
    |--------------------------------------------------------------------------
    | Session File Location
    |--------------------------------------------------------------------------
    |
    | When using the native session driver, we need a location where session
    | files may be stored. A default has been set for you but a different
    | location may be specified. This is only needed for file sessions.
    |
    */

    'files' => storage_path('framework/sessions'),

    /*
    |--------------------------------------------------------------------------
    | Session Database Connection
    |--------------------------------------------------------------------------
    |
    | When using the "database" or "redis" session drivers, you may specify a
    | connection that should be used to manage these sessions. This should
    | correspond to a connection in your database configuration options.
    |
    */

    'connection' => null,

    /*
    |----------------------------------------------
...[truncated]...

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

### config/cache.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Cache Store
    |--------------------------------------------------------------------------
    |
    | This option controls the default cache connection that gets used while
    | using this caching library. This connection is used when another is
    | not explicitly specified when executing a given caching function.
    |
    | Supported: "apc", "array", "database", "file", "memcached", "redis"
    |
    */

    'default' => env('CACHE_DRIVER', 'file'),

    /*
    |--------------------------------------------------------------------------
    | Cache Stores
    |--------------------------------------------------------------------------
    |
    | Here you may define all of the cache "stores" for your application as
    | well as their drivers. You may even define multiple stores for the
    | same cache driver to group types of items stored in your caches.
    |
    */

    'stores' => [

        'apc' => [
            'driver' => 'apc',
        ],

        'array' => [
            'driver' => 'array',
        ],

        'database' => [
            'driver' => 'database',
            'table' => 'cache',
            'connection' => null,
        ],

        'file' => [
            'driver' => 'file',
            'path' => storage_path('framework/cache/data'),
        ],

        'memcached' => [
            'driver' => 'memcached',
            'persistent_id' => env('MEMCACHED_PERSISTENT_ID'),
            'sasl' => [
                env('MEMCACHED_USERNAME'),
                env('MEMCACHED_PASSWORD'),
            ],
            'options' => [
                // Memcached::OPT_CONNECT_TIMEOUT  => 2000,
            ],
            'servers' => [
                [
                    'host' => env('MEMCACHED_HOST', '127.0.0.1'),
                    'port' => env('MEMCACHED_PORT', 11211),
                    'weight' => 100,
                ],
            ],
        ],

        'redis' => [
            'driver' => 'redis',
            'connection' => 'default',
        ],

    ],

    /*
    |--------------------------------------------------------------------------
    | Cache Key Prefix
    |--------------------------------------------------------------------------
    |
    | When utilizing a RAM based store such as APC or Memcached, there might
    | be other applications utilizing the same cache. So, we'll specify a
    | value to get prefixed to all our keys so we can avoid collisions.
    |
    */

    'prefix' => env(
        'CAC
...[truncated]...

### docker-compose.yml
version: '3'
services:

  #PHP Service
  app:
    build:
      context: .
      dockerfile: Dockerfile
    image: digitalocean.com/php
    container_name: app
    restart: unless-stopped
    tty: true
    environment:
      SERVICE_NAME: app
      SERVICE_TAGS: dev
    working_dir: /var/www
    volumes:
      - ./:/var/www
      - ./php/local.ini:/usr/local/etc/php/conf.d/local.ini
    networks:
      - app-network

  #Nginx Service
  webserver:
    image: nginx:alpine
    container_name: webserver
    restart: unless-stopped
    tty: true
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./:/var/www
      - ./nginx/conf.d/:/etc/nginx/conf.d/
    networks:
      - app-network

  #MySQL Service
  db:
    image: mysql:5.7.22
    container_name: db
    restart: unless-stopped
    tty: true
    ports:
      - "3306:3306"
    environment:
      MYSQL_DATABASE: school
      MYSQL_ROOT_PASSWORD: x12345678y
      MYSQL_USER: root
      MYSQL_PASSWORD: x12345678y
      SERVICE_TAGS: dev
      SERVICE_NAME: mysql
    volumes:
      - dbdata:/var/lib/mysql/
      - ./mysql/my.cnf:/etc/mysql/my.cnf
    networks:
      - app-network

#Docker Networks
networks:
  app-network:
    driver: bridge
#Volumes
volumes:
  dbdata:
    driver: local

### .travis.yml
language: php
php:
- 7.2
- 7.1
before_script:
- cp .env.example .env
- composer install
- php artisan key:generate
script: vendor/bin/phpunit -c phpunit.xml

### routes/api.php
<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

// Route::group(['middleware' => 'auth:api'], function(){
//   Route::get('attendances/{section_id}/{student_id}', 'AttendanceController@index');
//   Route::post('attendance', 'AttendanceController@store');
//   Route::get('attendance/{id}', 'AttendanceController@show');
//   Route::put('attendance/{id}', 'AttendanceController@update');
//   //Route::delete('attendance/{id}', 'AttendanceController@destroy')
// });

// Route::group(['middleware' => 'auth:api'], function(){
//   Route::get('books/{class_id}', 'BookController@index');
//   Route::post('book', 'BookController@store');
//   Route::get('book/{id}', 'BookController@show');
//   Route::put('book/{id}', 'BookController@update');
//   //Route::delete('book/{id}', 'BookController@destroy')
// });

// Route::group(['middleware' => 'auth:api'], function(){
//   Route::get('courses/{teacher_id}', 'CourseController@index');
//   Route::post('course', 'CourseController@store');
//   Route::get('course/{id}', 'CourseController@show');
//   Route::put('course/{id}', 'CourseController@update');
//   //Route::delete('course/{id}', 'CourseController@destroy')
// });

// Route::group(['middleware' => 'auth:api'], function(){
//   Route::get('events/{class_id}', 'EventController@index');
//   Route::post('event', 'EventController@store');
//   Route::get('event/{id}', 'EventController@show');
//   Route::put('event/{id}', 'EventController@update');
//   //Route::delete('event/{id}', 'EventController@destroy')
// });

// Route::group(['middleware' => 'auth:api'], function(){
//   Route::get('faqs', 'FaqController@index');
//   Route::post('faq', 'FaqController@store');
//   Route::get('faq/{id}', 'FaqController@show');
//   Route::put('faq/{id}', 'FaqController@update');
//   //Route::delete('faq/{id}', 'FaqController@destroy')
// });

// Route::group(['middleware' => 'auth:api'], function(){
//   Route::get('feedbacks/{student_id}', 'FeedbackController@index');
//   Route::post('feedback', 'FeedbackController@store');
//   Route::get('feedback/{id}', 'FeedbackController@show');
//   Route::put('feedback/{id}', 'FeedbackController@update');
//   //Route::delete('feedback/{id}', 'FeedbackController
...[truncated]...

### app/Http/Controllers/UploadController.php
<?php

namespace App\Http\Controllers;
// error_reporting(E_ALL);
// ini_set('display_errors', 1);
//use App\Http\Controllers\UploadHandler;
use Illuminate\Http\Request;
use App\Imports\StudentsImport;
use App\Imports\TeachersImport;
use App\Exports\StudentsExport;
use App\Exports\TeachersExport;
use Maatwebsite\Excel\Facades\Excel;
/*
 * jQuery File Upload Plugin PHP Class
 * https://github.com/blueimp/jQuery-File-Upload
 *
 * Copyright 2010, Sebastian Tschan
 * https://blueimp.net
 *
 * Licensed under the MIT license:
 * https://opensource.org/licenses/MIT
 */

class UploadController extends Controller {

  public function upload(Request $request){

    $request->validate([
      'upload_type' => 'required',
      'file' => 'required|max:10000|mimes:doc,docx,png,jpeg,pdf,xlsx,xls,ppt,pptx,txt'
    ]);

    $upload_dir = 'school-'.auth()->user()->school_id.'/'.date("Y").'/'.$request->upload_type;

    $path = \Storage::disk('public')->putFile($upload_dir, $request->file('file'));//$request->file('file')->store($upload_dir);
    
    if($request->upload_type == 'notice'){
      $request->validate([
        'title' => 'required|string',
      ]);
      
      $tb = new \App\Notice;
      $tb->file_path = 'storage/'.$path;
      $tb->title = $request->title;
      $tb->active = 1;
      $tb->school_id = auth()->user()->school_id;
      $tb->user_id = auth()->user()->id;
      $tb->save();
    }else if($request->upload_type == 'event'){
      $request->validate([
        'title' => 'required|string',
      ]);
      $tb = new \App\Event;
      $tb->file_path = 'storage/'.$path;
      $tb->title = $request->title;
      $tb->active = 1;
      $tb->school_id = auth()->user()->school_id;
      $tb->user_id = auth()->user()->id;
      $tb->save();
    } else if($request->upload_type == 'routine'){
      $request->validate([
        'title' => 'required|string',
      ]);
      $tb = new \App\Routine;
      $tb->file_path = 'storage/'.$path;
      $tb->title = $request->title;
      $tb->active = 1;
      $tb->school_id = auth()->user()->school_id;
      $tb->user_id = auth()->user()->id;
      $tb->save();
    } else if($request->upload_type == 'syllabus'){
      $request->validate([
        'title' => 'required|string',
      ]);
      $tb = new \App\Syllabus;
      $tb->file_path = 'storage/'.$path;
      $tb->title = $request->title;
      $tb->active = 1;
      $tb->school_id = auth()->user()->school_id;
      $tb->user_id = auth()->user()->id;
      $tb->save();
    } else if($request->upload_type == 'profile' && $request->user_id > 0){
      $tb = \App\Us
...[truncated]...

### app/Http/Kernel.php
<?php

namespace App\Http;

use Illuminate\Foundation\Http\Kernel as HttpKernel;

class Kernel extends HttpKernel
{
    /**
     * The application's global HTTP middleware stack.
     *
     * These middleware are run during every request to your application.
     *
     * @var array
     */
    protected $middleware = [
        \Illuminate\Foundation\Http\Middleware\CheckForMaintenanceMode::class,
        \Illuminate\Foundation\Http\Middleware\ValidatePostSize::class,
        \App\Http\Middleware\TrimStrings::class,
        \Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull::class,
        \App\Http\Middleware\TrustProxies::class,
//         \RenatoMarinho\LaravelPageSpeed\Middleware\InlineCss::class,
//         \RenatoMarinho\LaravelPageSpeed\Middleware\ElideAttributes::class,
//         \RenatoMarinho\LaravelPageSpeed\Middleware\InsertDNSPrefetch::class,
//         \RenatoMarinho\LaravelPageSpeed\Middleware\RemoveComments::class,
//         \RenatoMarinho\LaravelPageSpeed\Middleware\TrimUrls::class,
//         \RenatoMarinho\LaravelPageSpeed\Middleware\RemoveQuotes::class,
//         \RenatoMarinho\LaravelPageSpeed\Middleware\CollapseWhitespace::class,
    ];

    /**
     * The application's route middleware groups.
     *
     * @var array
     */
    protected $middlewareGroups = [
        'web' => [
            \App\Http\Middleware\EncryptCookies::class,
            \Illuminate\Cookie\Middleware\AddQueuedCookiesToResponse::class,
            \Illuminate\Session\Middleware\StartSession::class,
            // \Illuminate\Session\Middleware\AuthenticateSession::class,
            \Illuminate\View\Middleware\ShareErrorsFromSession::class,
            \App\Http\Middleware\VerifyCsrfToken::class,
            \Illuminate\Routing\Middleware\SubstituteBindings::class,
        ],

        'api' => [
            'throttle:60,1',
            'bindings',
        ],
    ];

    /**
     * The application's route middleware.
     *
     * These middleware may be assigned to groups or used individually.
     *
     * @var array
     */
    protected $routeMiddleware = [
        'auth' => \Illuminate\Auth\Middleware\Authenticate::class,
        'master' => \App\Http\Middleware\CheckMaster::class,
        'master.admin' => \App\Http\Middleware\CheckMasterOrAdmin::class,
        'teacher.student' => \App\Http\Middleware\CheckTeacherOrStudent::class,
        'admin' => \App\Http\Middleware\CheckAdmin::class,
        'accountant' => \App\Http\Middleware\CheckAccountant::class,
        'librarian' => \App\Http\Middleware\CheckLibrarian::class,
        'st
...[t
...[truncated]...