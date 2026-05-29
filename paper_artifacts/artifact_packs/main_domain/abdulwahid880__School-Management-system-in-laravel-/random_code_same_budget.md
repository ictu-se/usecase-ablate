# Deterministic random code snippets
### app/Syllabus.php
<?php

namespace App;

use App\Model;

class Syllabus extends Model
{
    protected $table = 'syllabuses';
    /**
    * Get the school record associated with the user.
    */
    public function school()
    {
        return $this->belongsTo('App\School');
    }
    /**
    * Get the class record associated with the syllabus.
    */
    public function myclass()
    {
        return $this->belongsTo('App\Myclass','class_id');
    }
}

### app/Http/Controllers/FeedbackController.php
<?php

namespace App\Http\Controllers;

use App\Feedback as Feedback;
use App\Http\Resources\FeedbackResource;
use Illuminate\Http\Request;

class FeedbackController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index($student_id)
    {
      return ($student_id > 0)? FeedbackResource::collection(Feedback::where('student_id', $student_id)->get()):response()->json(['Invalid Student id: '. $student_id, 404]);
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
      $tb = new Feedback;
      $tb->description = $request->description;
      $tb->teacher_id = $request->teacher_id;
      $tb->student_id = $request->student_id;

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
        return new FeedbackResource(Feedback::find($id));
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
      $tb = Feedback::find($id);
      $tb->description = $request->description;
      $tb->student_id = $request->student_id;
      $tb->teacher_id = $request->teacher_id;
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
      return (Feedback::destroy($id))?response()->json([
        'status' => 'success'
      ]):response()->json([
        'status' => 'error'
      ]);
    }
}

### tests/Browser/ExampleTest.php
<?php

namespace Tests\Browser;

use Tests\DuskTestCase;
use Laravel\Dusk\Browser;
use Illuminate\Foundation\Testing\DatabaseMigrations;

class ExampleTest extends DuskTestCase
{
    /** @test */
    public function it_shows_app_name() {
        $this->browse(function (Browser $browser) {
            $browser->visit('/')
                    ->assertSee('UnifiedTransform');
        });
    }
}

### tests/Browser/AdminUserManagesAcademicSettingsTest.php
<?php

namespace Tests\Browser;

use App\User;
use Tests\DuskTestCase;
use Laravel\Dusk\Browser;
use Tests\Browser\Pages\SettingPage;
use Illuminate\Foundation\Testing\DatabaseMigrations;

class AdminUserManagesAcademicSettingsTest extends DuskTestCase
{
    use DatabaseMigrations;

    public function setUp() {
        parent::setUp();
        $this->admin = factory(User::class)->states('admin')->create();
    }

    /** @test */
    public function admin_user_can_see_academic_settings() {
        $this->browse(function (Browser $browser) {
            $browser->loginAs($this->admin)
                ->visit(new SettingPage);
        });
    }
}

### app/Providers/AuthServiceProvider.php
<?php

namespace App\Providers;

use Laravel\Passport\Passport;
use Illuminate\Support\Facades\Gate;
use Illuminate\Foundation\Support\Providers\AuthServiceProvider as ServiceProvider;

class AuthServiceProvider extends ServiceProvider
{
    /**
     * The policy mappings for the application.
     *
     * @var array
     */
    protected $policies = [
        'App\Model' => 'App\Policies\ModelPolicy',
    ];

    /**
     * Register any authentication / authorization services.
     *
     * @return void
     */
    public function boot()
    {
        $this->registerPolicies();

        Passport::routes();
    }
}

### app/Http/Requests/User/CreateAdminRequest.php
<?php

namespace App\Http\Requests\User;

use Illuminate\Foundation\Http\FormRequest;

/**
 * Class CreateAdminRequest
 * @package App\Http\Requests\User
 */
class CreateAdminRequest extends FormRequest
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
            'password' => 'required|string|min:6|confirmed',
            'gender' => 'required',
            'blood_group' => 'required',
            'phone_number' => 'required|unique:users',
            'email' => 'email|max:255|unique:users',
        ];
    }
}

### app/Http/Resources/EventResource.php
<?php

namespace App\Http\Resources;

use Illuminate\Http\Resources\Json\Resource;

class EventResource extends Resource
{
    /**
     * Transform the resource into an array.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return array
     */
    public function toArray($request)
    {
        return [
            'id' => $this->id,
            'description' => $this->description,
            'class' => new ClassResource($this->class),
        ];
    }
}

### config/broadcasting.php
<?php

return [

    /*
    |--------------------------------------------------------------------------
    | Default Broadcaster
    |--------------------------------------------------------------------------
    |
    | This option controls the default broadcaster that will be used by the
    | framework when an event needs to be broadcast. You may set this to
    | any of the connections defined in the "connections" array below.
    |
    | Supported: "pusher", "redis", "log", "null"
    |
    */

    'default' => env('BROADCAST_DRIVER', 'null'),

    /*
    |--------------------------------------------------------------------------
    | Broadcast Connections
    |--------------------------------------------------------------------------
    |
    | Here you may define all of the broadcast connections that will be used
    | to broadcast events to other systems or over websockets. Samples of
    | each available type of connection are provided inside this array.
    |
    */

    'connections' => [

        'pusher' => [
            'driver' => 'pusher',
            'key' => env('PUSHER_APP_KEY'),
            'secret' => env('PUSHER_APP_SECRET'),
            'app_id' => env('PUSHER_APP_ID'),
            'options' => [
                //
            ],
        ],

        'redis' => [
            'driver' => 'redis',
            'connection' => 'default',
        ],

        'log' => [
            'driver' => 'log',
        ],

        'null' => [
            'driver' => 'null',
        ],

    ],

];

### app/Services/Grade/GradeService.php
<?php
namespace App\Services\Grade;

use App\Grade;
use App\Gradesystem;
use App\Exam;
use App\Course;
use App\Section;
use App\Myclass;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Log;

class GradeService {

  public $grades;
  public $gradesystems;
  public $course_id;
  public $exam_id;
  public $teacher_id;
  public $section_id;
  public $exams;
  // Calculation marks starts
  public $final_att_mark;
  public $final_assignment_mark;
  public $final_quiz_mark;
  public $final_ct_mark;
  public $final_finalExam_mark;
  public $final_practical_mark;
  public $quizCount;
  public $assignmentCount;
  public $ctCount;
  public $quizSum;
  public $assignmentSum;
  public $ctSum;
  public $field;
  public $grade;
  public $maxFieldNum;
  public $fieldCount;
  public $full_field_mark;
  public $field_percentage;
  public $avg_field_sum;
  public $final_default_value;
  // Calculation marks ends

  public function isLoggedInUserStudent(){
    return auth()->user()->role == 'student';
  }

  public function getExamByIdsFromGrades($grades){
    $examIds = $grades->map(function($grade){
      return $grade->exam_id;
    });
    $exams = Exam::whereIn('id', $examIds)
                  ->orderBy('id','desc')
                  ->get();
    return $exams;
  }

  public function getStudentGradesWithInfoCourseTeacherExam($student_id){
    return Grade::with(['student','course','teacher','exam'])
                  ->where('student_id', $student_id)
                  ->orderBy('exam_id')
                  ->latest()
                  ->get();
  }

  public function getGradeSystemBySchoolId($grades){
    $grade_system_name = isset($grades[0]->course->grade_system_name) ? $grades[0]->course->grade_system_name : false;
    return ($grade_system_name)?Gradesystem::where('school_id', auth()->user()->school_id)
                        ->where('grade_system_name', $grade_system_name)
                        //->groupBy('grade_system_name')
                        ->get() : Gradesystem::select('grade_system_name')
                        ->where('school_id', auth()->user()->school_id)
                        ->distinct()
                        ->get();
  }

  public function getGradeSystemByname($grade_system_name){
    return Gradesystem::where('school_id', auth()->user()->school_id)
                        ->where('grade_system_name', $grade_system_name)
                        ->get();
  }

  public function gradeIndexView($view){
    return view($view,[
        'grades' => $this->grades,
        'gradesystems' => $this->gradesystems,
        'exams' 
...[truncated]...

### app/Http/Requests/Course/SaveConfigurationRequest.php
<?php

namespace App\Http\Requests\Course;

use Illuminate\Foundation\Http\FormRequest;

class SaveConfigurationRequest extends FormRequest
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
            'grade_system_name' => 'required|string',
            'quiz_count' => 'required|numeric|min:0|max:5',
            'assignment_count' => 'required|numeric|min:0|max:3',
            'ct_count' => 'required|numeric|min:0|max:5',
            'quiz_percent' => 'required|numeric|min:0|max:100',
            'attendance_percent' => 'required|numeric|min:0|max:100',
            'assignment_percent' => 'required|numeric|min:0|max:100',
            'ct_percent' => 'required|numeric|min:0|max:100',
            'final_exam_percent' => 'required|numeric|min:0|max:100',
            'practical_percent' => 'required|numeric|min:0|max:100',
            'att_fullmark' => 'required|numeric|min:0|max:100',
            'quiz_fullmark' => 'required|numeric|min:0|max:100',
            'a_fullmark' => 'required|numeric|min:0|max:100',
            'ct_fullmark' => 'required|numeric|min:0|max:100',
            'final_fullmark' => 'required|numeric|min:0|max:100',
            'practical_fullmark' => 'required|numeric|min:0|max:100',
        ];
    }
}

### resources/views/components/excel-upload-form.blade.php
<form action="{{url('users/import/user-xlsx')}}" method="post" enctype="multipart/form-data">
    {{ csrf_field() }}
    <input type="hidden" name="type" value="{{$type}}">
    <div class="form-group">
        <input type="file" name="file">
    </div>
    <input type="submit" class="btn btn-default btn-sm" value="@lang('Upload')">
</form>

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

### app/Http/Middleware/VerifyCsrfToken.php
<?php

namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\VerifyCsrfToken as Middleware;

class VerifyCsrfToken extends Middleware
{
    /**
     * The URIs that should be excluded from CSRF verification.
     *
     * @var array
     */
    protected $except = [
        //
    ];
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

### resources/views/fees/all.blade.php
@extends('layouts.app')

@section('title', __('All Fees'))

@section('content')
<div class="container-fluid">
    <div class="row">
        <div class="col-md-2" id="side-navbar">
            @include('layouts.leftside-menubar')
        </div>
        <div class="col-md-10" id="main-container">
            <div class="panel panel-default">
                <div class="page-panel-title">@lang('All Fees')
                  <button class="btn btn-xs btn-success pull-right" role="button" id="btnPrint" ><i class="material-icons">print</i> @lang('Print Fees Form')</button>
              </div>
                <div class="panel-body">
                    @if (session('status'))
                        <div class="alert alert-success">
                            {{ session('status') }}
                        </div>
                    @endif
                    @component('components.fees-list',['fees'=>$fees])
                    @endcomponent
                </div>
            </div>
        </div>
    </div>
</div>
<script>
$("#btnPrint").on("click", function () {
    var feesTable = document.createElement('table');
    feesTable.setAttribute('class', 'table');
    feesTable.style.width = "100%";
    feesTable.style['border-collapse'] = "collapse";
    var htr = feesTable.insertRow();
    for(var j = 0; j < 3; j++){
      var htd = htr.insertCell();
      if(j == 0)
        cellText = @json( __('Sl.'));
      else if(j == 1)
        cellText = @json( __('Field Name'));
      else {
        cellText = @json( __('Amount (taka)'));
      }
      htd.appendChild(document.createTextNode(cellText));
    }
    $('input:checked').each(function(index, val) {
        var tr = feesTable.insertRow();
        for(var j = 0; j < 3; j++){
            var td = tr.insertCell();
            var cellText;
            if(j == 0)
              cellText = index + 1;
            else if(j == 1)
              cellText = this.value;
            else {
              cellText = '';
            }
            td.appendChild(document.createTextNode(cellText));
            td.style.border = '1px solid black';
            if(j == 0)
              td.style.width = '4%';
            else
              td.style.width = '48%';
        }
    });
    var schoolTable = feesTable.cloneNode(true);
    var printWindow = window.open('', '', 'height=720,width=1280');
    printWindow.document.write('<html><head><title>@lang("Fees Form")</title>');
    printWindow.document.write('<link href="{{url('css/app.css')}}" rel="stylesheet">');
    printWindow.document.write('</head><body>');
    printWindow.doc
...[truncated]...

### app/Events/UserRegistered.php
<?php

namespace App\Events;

use Illuminate\Broadcasting\Channel;
use Illuminate\Queue\SerializesModels;
use Illuminate\Broadcasting\PrivateChannel;
use Illuminate\Broadcasting\PresenceChannel;
use Illuminate\Foundation\Events\Dispatchable;
use Illuminate\Broadcasting\InteractsWithSockets;
use Illuminate\Contracts\Broadcasting\ShouldBroadcast;
use App\User;

class UserRegistered
{
    use Dispatchable, InteractsWithSockets, SerializesModels;

    public $user;
    public $password;

    /**
     * Create a new event instance.
     *
     * @return void
     */
    public function __construct(User $user, $password = null)
    {
        $this->user = $user;
        $this->password = $password;
    }
}

### resources/views/grade/student-grade.blade.php
@extends('layouts.app')

@section('title', __('Grade'))

@section('content')
<div class="container-fluid">
    <div class="row">
        <div class="col-md-2" id="side-navbar">
            @include('layouts.leftside-menubar')
        </div>
        <div class="col-md-10" id="main-container">
            @if(Auth::user()->role != 'student')
            <ol class="breadcrumb" style="margin-top: 3%;">
                <li><a href="{{url('grades/all-exams-grade')}}" style="color:#3b80ef;">@lang('Grades')</a></li>
                <li><a href="{{url()->previous()}}" style="color:#3b80ef;">@lang('Section Students')</a></li>
                <li class="active">@lang('History')</li>
            </ol>
            @endif
            <h2>@lang('Marks and Grades History')</h2>
            <div class="panel panel-default">
              @if(count($grades) > 0)
              @foreach ($grades as $grade)
                <?php
                    $studentName = $grade->student->name;
                    $classNumber = $grade->student->section->class->class_number;
                    $sectionNumber = $grade->student->section->section_number;
                ?>
                <div class="page-panel-title"><b>@lang('Student Code')</b> - {{$grade->student->student_code}} &nbsp;<b>@lang('Name')</b> -  {{$grade->student->name}} &nbsp;<b>@lang('Class')</b> - {{$grade->student->section->class->class_number}} &nbsp;<b>@lang('Section')</b> - {{$grade->student->section->section_number}}</div>
                 @break($loop->first)
              @endforeach
                <div class="panel-body">
                    @if (session('status'))
                        <div class="alert alert-success">
                            {{ session('status') }}
                        </div>
                    @endif

                    @include('layouts.student.grade-table')
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

### resources/views/layouts/teacher/grade-table.blade.php
<div class="table-responsive">
  <table class="table table-bordered table-hover">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">@lang('Student Code')</th>
      <th scope="col">@lang('Student Name')</th>
      <th scope="col">@lang('Attendance')</th>
        @for($i=1;$i<=5;$i++)
          <th scope="col">@lang('Quiz') {{$i}}</th>
        @endfor
        @for($i=1;$i<=3;$i++)
          <th scope="col">@lang('Assignment') {{$i}}</th>
        @endfor
        @for($i=1;$i<=5;$i++)
          <th scope="col">@lang('CT') {{$i}}</th>
        @endfor
        @if($grade->course->final_exam_percent > 0)
          <th scope="col">@lang('Written')</th>
          <th scope="col">@lang('Mcq')</th>
        @endif
        @if($grade->course->practical_percent > 0)
          <th scope="col">@lang('Practical')</th>
        @endif
      <th scope="col">@lang('Total Marks')</th>
      <th scope="col">@lang('GPA')</th>
      <th scope="col">@lang('Grade')</th>
    </tr>
  </thead>
  <tbody>
    @foreach ($grades as $grade)
    <tr>
      <th scope="row">{{($loop->index + 1)}}</th>
      <td>{{$grade->student->student_code}}</td>
      <td><a href="{{url('user/'.$grade->student->student_code)}}">{{$grade->student->name}}</a></td>
      <td>{{$grade->attendance}}</td>
      @for($i=1;$i<=5;$i++)
        <td>{{$grade['quiz'.$i]}}</td>
      @endfor
      @for($i=1;$i<=3;$i++)
        <td>{{$grade['assignment'.$i]}}</td>
      @endfor
      @for($i=1;$i<=5;$i++)
        <td>{{$grade['ct'.$i]}}</td>
      @endfor
      @if($grade->course->final_exam_percent > 0)
        <td>{{$grade->written}}</td>
        <td>{{$grade->mcq}}</td>
      @endif
      @if($grade->course->practical_percent > 0)
        <td>{{$grade->practical}}</td>
      @endif
      <td>{{$grade->marks}}</td>
      <td>{{$grade->gpa}}</td>
      <td>
        @foreach($gradesystems as $gs)
          @if($gs->point == $grade->gpa)
            {{$gs->grade}}
            @break
          @endif
        @endforeach
      </td>
    </tr>
    @endforeach
  </tbody>
</table>
</div>

### tests/Unit/App/ExamTest.php
<?php

namespace Test\Unit\App;

use App\Exam;
use App\School;
use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;

class ExamTest extends TestCase
{
    use RefreshDatabase;

    /** @test */
    public function the_exams_are_filter_by_school() {
        $school = create(School::class);
        $exams  = create(Exam::class, ['school_id' => $school->id], 2);

        $other_school = create(School::class);
        $other_exams  = create(Exam::class, ['school_id' => $other_school->id], 4);

        $this->assertEquals(Exam::bySchool($school->id)->count(), $exams->count());
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

### resources/views/components/exams-list.blade.php
<div class="card text-white bg-primary mb-3">
    <div class="card-header">@lang('Information')</div>
    <div class="card-body">
      @lang('An Examination represents a Semester. All Courses of a Semester belong to an Examination. So, all Quiz, Class Test, Assignment, Attendance, Written, Practical, etc. in a Course are subjected to that specific Examination.')
    </div>
</div>
{{$exams->links()}}
<div class="table-responsive">
  @foreach ($exams as $exam)
    <form id="form{{$exam->id}}" action="{{url('exams/activate-exam')}}" method="POST">
      {{csrf_field()}}
    </form>
  @endforeach
  <table class="table table-striped table-hover">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">@lang('Examination Name')</th>
      <th scope="col">@lang('Notice Published')</th>
      <th scope="col">@lang('Result Published')</th>
      <th scope="col">@lang('Created At')</th>
      <th scope="col">@lang('Set Active')</th>
    </tr>
  </thead>
  <tbody>
    @foreach ($exams as $exam)
    <tr>
      <th scope="row">{{($loop->index + 1)}}</th>
      <td scope="row">{{$exam->exam_name}}</td>
      <td scope="row">
        @if($exam->notice_published === 1)
          @lang('Yes')
        @else
          @if($exam->result_published === 1)
            @lang('No')
          @else
            <label class="checkbox-label"> @lang('Yes')
              <input type="checkbox" name="notice_published" form="form{{$exam->id}}" />
              <span class="checkmark"></span>
            </label>
          @endif
        @endif
      </td>
      <td scope="row">
        @if($exam->result_published === 1)
          @lang('Yes')
        @else
          <label class="checkbox-label"> @lang('Yes')
            <input type="checkbox" name="result_published" form="form{{$exam->id}}" />
            <span class="checkmark"></span>
          </label>
        @endif
      </td>
      <td scope="row">{{Carbon\Carbon::parse($exam->created_at)->format('d/m/Y')}}</td>
      <td scope="row">
        <input type="hidden" name="exam_id" value="{{$exam->id}}" form="form{{$exam->id}}"/>
        @if($exam->active === 1)
          <label class="checkbox-label">
              @lang('Active')
            <input type="checkbox" name="active" form="form{{$exam->id}}" checked />
            <span class="checkmark"></span>
          </label>
        @else
          @if($exam->result_published === 1)
            @lang('Completed')
          @else
            <label class="checkbox-label">
              @lang('Not Active')
              <input type="checkbox" name="active" form="form{
...[truncated]...

### tests/Feature/GradeModuleTest.php
<?php

namespace Tests\Feature;

use App\User;
use App\Section;
use App\Course;
use App\Exam;
use App\Grade;
use App\Gradesystem;
use Tests\TestCase;
use Illuminate\Foundation\Testing\WithFaker;
use Illuminate\Foundation\Testing\RefreshDatabase;

class GradeModuleTest extends TestCase
{
    use RefreshDatabase;

    public function setUp() {
        parent::setUp();
        $teacher = factory(User::class)->states('teacher')->create();
        $this->actingAs($teacher);
        $this->withoutExceptionHandling();
    }
    /** @test */
    public function can_view_classes_sections_for_students_grade(){
        $response = $this->get('grades/all-exams-grade');
        $response->assertStatus(200);
        $response->assertViewIs('grade.all-exams-grade');
        $response->assertViewHas(['classes','sections']);
    }
    /** @test */
    public function can_view_all_students_marks_under_a_section(){
        $section = factory(Section::class)->create();
        $response = $this->get('grades/section/'.$section->id);
        $response->assertStatus(200);
        $response->assertViewIs('grade.class-result');
        $response->assertViewHas('grades');
    }
    /** @test */
    public function can_view_grade_of_a_student(){
        $student = factory(User::class)->states('student')->create();
        $response = $this->get('grades/'.$student->id);
        $response->assertStatus(200);
        $response->assertViewIs('grade.student-grade');
        $response->assertViewHas(['grades','gradesystems','exams']);
    }
    /** @test */
    public function teacher_can_view_students_grades_of_a_section_of_his_course(){
        $teacher = factory(User::class)->states('teacher')->create();
        $course = factory(Course::class)->create();
        $exam = factory(Exam::class)->create();
        $section = factory(Section::class)->create();

        $response = $this->get('grades/t/'.$teacher->id.'/'.$course->id.'/'.$exam->id.'/'.$section->id);
        $response->assertStatus(200);
        $response->assertViewIs('grade.teacher-grade');
        $response->assertViewHas(['grades','gradesystems']);
    }
    /** @test */
    public function teacher_can_submit_students_grades_of_a_section_of_his_course(){
        $teacher = factory(User::class)->states('teacher')->create();
        $course = factory(Course::class)->create();
        $exam = factory(Exam::class)->create();
        $section = factory(Section::class)->create();

        $response = $this->get('grades/c/'.$teacher->id.'/'.$course->id.'/'.$exam->id.'/'.$section->id);
        $response->assertStatus(200);
     
...[truncated]...