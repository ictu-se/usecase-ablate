# Models/services
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

### tests/Unit/App/FormTest.php
<?php

namespace Test\Unit\App;

use App\Form;
use App\School;
use Tests\TestCase;
use Illuminate\Foundation\Testing\RefreshDatabase;

class FormTest extends TestCase
{
    use RefreshDatabase;

    /** @test */
    public function the_forms_are_filter_by_school() {
        $school = create(School::class);
        $forms  = create(Form::class, ['school_id' => $school->id], 2);

        $other_school = create(School::class);
        $other_forms  = create(Form::class, ['school_id' => $other_school->id], 4);

        $this->assertEquals(Form::bySchool($school->id)->count(), $forms->count());
    }
}

### app/Services/User/UserService.php
<?php
namespace App\Services\User;

use App\User;
use App\StudentInfo;
use Illuminate\Support\Facades\DB;
use Mavinoo\LaravelBatch\Batch;
use Illuminate\Support\Facades\Log;

class UserService {
    
    protected $user;
    protected $db;
    protected $batch;
    protected $st, $st2;

    public function __construct(User $user, DB $db, Batch $batch){
        $this->user = $user;
        $this->db = $db;
        $this->batch = $batch;
    }

    public function isListOfStudents($school_code, $student_code){
        return !empty($school_code) && $student_code == 1;
    }

    public function isListOfTeachers($school_code, $teacher_code){
        return !empty($school_code) && $teacher_code == 1;
    }

    public function indexView($view, $users){
        return view($view, [
            'users' => $users,
            'current_page' => $users->currentPage(),
            'per_page' => $users->perPage(),
        ]);
    }

    public function hasSectionId($section_id){
        return $section_id > 0;
    }

    public function updateStudentInfo($request, $id){
        $info = StudentInfo::firstOrCreate(['student_id' => $id]);
        $info->student_id = $id;
        $info->session = (!empty($request->session)) ? $request->session : '';
        $info->version = (!empty($request->
...[truncated]...