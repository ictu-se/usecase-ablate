# README
## README.md
# Student Information Management System

## Architecture Diagram

![效果图](https://github.com/userqizegao/student_crud/blob/master/student-crud/%E6%9E%B6%E6%9E%84%E5%9B%BE.png)

## Technology Stack

The project is structured using Maven, developed with JSP + Servlet, and incorporates the Spring + SpringMVC + MyBatis frameworks. It utilizes the c3p0 open-source JDBC connection pool to connect to the MySql database. AJAX requests are sent to retrieve JSON data, which is then dynamically loaded onto the page via the DOM. Unit testing code is written using Spring-Test and Junit. The system employs a Restful design style, sending PUT and DELETE requests via AJAX. Dual-side validation is implemented, with front-end validation using JQuery and back-end validation conforming to the JSR303 standard.

# Code snippets
### student-crud/src/main/java/com/qizegao/controller/StudentController.java
package com.qizegao.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.qizegao.bean.Msg;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.qizegao.bean.Student;
import com.qizegao.service.StudentService;

@Controller
public class StudentController {
	
	@Autowired
	StudentService studentService;
	
	//分页查询学生数据
	@RequestMapping("/stus")
	@ResponseBody //导入Jackson包使用
	public Msg getStusWithJson(
			@RequestParam(value = "pn", defaultValue = "1") Integer pn) {
		PageHelper.startPage(pn, 5);
		List<Student> stus = studentService.getAll();
		PageInfo page = new PageInfo(stus, 5); //PageInfo封装了分页的详细信息
		return Msg.success().add("pageInfo", page);
	}
	
	//检查用户名是否已经存在于数据库
	@ResponseBody
	@RequestMapping("/checkuser")
	public Msg checkuser(@RequestParam("stuName")String stuName){
		
		//先判断用户名是否满足正则表达式，若不满足无需去数据库查询
		String regx = "^[\u2E80-\u9FFF]{2,5}";
		if(!stuName.matches(regx)){
			return Msg.fail().add("va_msg", "学生姓名必须是2-5位汉字");
		}
		
		//数据库用户名重复校验
		boolean b = studentService.checkUser(stuName);
		if(b){
			return Msg.success();
		}else{
			return Msg.fail().add("va_msg", "学生姓名已存在");
		}
	}
	
	//保存学生
	@RequestMapping(value="/stu",method=RequestMethod.POST)
	@ResponseBody
	public Msg saveStu(@Valid Student student, BindingResult result){
		
		if (result.hasErrors()) {
			
			//JSR303校验结果有错误时，将JSR303校验结果封装在map中
			
			Map<String, Object> map = new HashMap<String, Object>();
			//获取所有有错误的字段
			List<FieldError> errors = result.getFieldErrors();
			for (FieldError fieldError : errors) {
				//getFiled表示错误的字段名
				//getDefaultMessage表示JavaBean定义的错误信息
				map.put(fieldError.getField(), fieldError.getDefaultMessage());
			}
			return Msg.fail().add("errorFields", map);
		} else {
			//校验结果无误时
			studentService.saveStu(student);
			return Msg.success();
		}
	}
	
	//根据id查询学生信息
	@RequestMapping(value="/stu/{id}", method=RequestMethod.GET)
	@ResponseBody
	public Msg getSt
...[truncated]...

### student-crud/src/main/java/com/qizegao/controller/DepartmentController.java
package com.qizegao.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.qizegao.bean.Department;
import com.qizegao.bean.Msg;
import com.qizegao.service.DepartmentService;

@Controller
public class DepartmentController {
	
	@Autowired
	private DepartmentService departmentService;

	//以JSON的形式返回所有的社团信息
	@RequestMapping("/depts")
	@ResponseBody
	public Msg getDepts(){
		//查出的所有部门信息
		List<Department> list = departmentService.getDepts();
		return Msg.success().add("depts", list);
	}
	
	
	
}

### student-crud/src/main/java/com/qizegao/service/StudentService.java
package com.qizegao.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.qizegao.bean.Student;
import com.qizegao.bean.StudentExample;
import com.qizegao.bean.StudentExample.Criteria;
import com.qizegao.dao.StudentMapper;

@Service
public class StudentService {

	@Autowired
	StudentMapper studentMapper;
	
	//查询所有学生
	public List<Student> getAll() {
		//创建Example类定义查询条件
		StudentExample studentExample = new StudentExample();
		studentExample.setOrderByClause("stu_id asc");
		return studentMapper.selectByExampleWithDept(studentExample);
	}
	
	//校验用户名是否已经存在于数据库
	public boolean checkUser(String stuName) {
		//指定条件的查询
		StudentExample example = new StudentExample();
		Criteria criteria = example.createCriteria();
		criteria.andStuNameEqualTo(stuName);
		long count = studentMapper.countByExample(example);
		return count == 0;
	}
	
	//保存学生
	public void saveStu(Student student) {
		studentMapper.insertSelective(student); //MBG生成的方法
	}
	
	//根据id查询学生信息
	public Student getStu(Integer id) {
		Student student = studentMapper.selectByPrimaryKey(id);
		return student;
	}
	
	//保存更新后的学生的信息
	public void updateStu(Student student) {
		studentMapper.updateByPrimaryKeySelective(student);
	}
	
	//单个删除
	public void deleteStu(Integer id) {
		studentMapper.deleteByPrimaryKey(id);
	}
	
	//批量删除
	public void deleteBatch(List<Integer> ids) {
		StudentExample studentExample = new StudentExample();
		Criteria criteria = studentExample.createCriteria();
		
		//delete from tbl_stu where stu_id in(1,2,3...) 
		criteria.andStuIdIn(ids);
		
		studentMapper.deleteByExample(studentExample);
	}
}

### student-crud/src/main/java/com/qizegao/service/DepartmentService.java
package com.qizegao.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.qizegao.bean.Department;
import com.qizegao.dao.DepartmentMapper;

@Service
public class DepartmentService {
	
	@Autowired
	private DepartmentMapper departmentMapper;
	
	//查询所有社团
	public List<Department> getDepts() {
		List<Department> list = departmentMapper.selectByExample(null);
		return list;
	}
}