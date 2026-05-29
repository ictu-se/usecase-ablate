# Oracle upper-bound selected context
This condition is selected with checked trace paths and is used only as an upper-bound comparator.

# README
## README.md
# Student Information Management System

## Architecture Diagram

![效果图](https://github.com/userqizegao/student_crud/blob/master/student-crud/%E6%9E%B6%E6%9E%84%E5%9B%BE.png)

## Technology Stack

The project is structured using Maven, developed with JSP + Servlet, and incorporates the Spring + SpringMVC + MyBatis frameworks. It utilizes the c3p0 open-source JDBC connection pool to connect to the MySql database. AJAX requests are sent to retrieve JSON data, which is then dynamically loaded onto the page via the DOM. Unit testing code is written using Spring-Test and Junit. The system employs a Restful design style, sending PUT and DELETE requests via AJAX. Dual-side validation is implemented, with front-end validation using JQuery and back-end validation conforming to the JSR303 standard.

# File tree
README.md
student-crud
  .settings
    org.eclipse.wst.common.project.facet.core.xml
  mbg.xml
  pom.xml
  src
    main
      java
        com
          qizegao
      resources
        applicationContext.xml
        dbconfig.properties
        mapper
          DepartmentMapper.xml
          StudentMapper.xml
        mybatis-config.xml
      webapp
        WEB-INF
          dispatcherServlet-servlet.xml
          web.xml

# Oracle-selected code and test snippets
### README.md
# Student Information Management System

## Architecture Diagram

![效果图](https://github.com/userqizegao/student_crud/blob/master/student-crud/%E6%9E%B6%E6%9E%84%E5%9B%BE.png)

## Technology Stack

The project is structured using Maven, developed with JSP + Servlet, and incorporates the Spring + SpringMVC + MyBatis frameworks. It utilizes the c3p0 open-source JDBC connection pool to connect to the MySql database. AJAX requests are sent to retrieve JSON data, which is then dynamically loaded onto the page via the DOM. Unit testing code is written using Spring-Test and Junit. The system employs a Restful design style, sending PUT and DELETE requests via AJAX. Dual-side validation is implemented, with front-end validation using JQuery and back-end validation conforming to the JSR303 standard.

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

### student-crud/src/main/java/com/qizegao/bean/Student.java
package com.qizegao.bean;

import javax.validation.constraints.Pattern;

import org.hibernate.validator.constraints.Email;

public class Student {
	
    @Pattern(regexp="^[\u2E80-\u9FFF]{2,5}"
    		,message=" 学生姓名必须是2-5位汉字 ")
    private String stuName;

    @Email(message = "邮箱格式不正确")
    private String email;
    
    private Integer stuId;

    private String gender;


    private Integer dId;
    
    private Department department; 
    
    

    public Student() {
		super();
	}

	public Student(Integer stuId, String stuName, String gender, String email, Integer dId) {
		super();
		this.stuId = stuId;
		this.stuName = stuName;
		this.gender = gender;
		this.email = email;
		this.dId = dId;
	}

	public Department getDepartment() {
		return department;
	}

	public void setDepartment(Department department) {
		this.department = department;
	}

	public Integer getStuId() {
        return stuId;
    }

    public void setStuId(Integer stuId) {
        this.stuId = stuId;
    }

    public String getStuName() {
        return stuName;
    }

    public void setStuName(String stuName) {
        this.stuName = stuName == null ? null : stuName.trim();
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender == null ? null : gender.trim();
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email == null ? null : email.trim();
    }

    public Integer getdId() {
        return dId;
    }

    public void setdId(Integer dId) {
        this.dId = dId;
    }
}

### student-crud/src/main/resources/mapper/StudentMapper.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.qizegao.dao.StudentMapper">
  <resultMap id="BaseResultMap" type="com.qizegao.bean.Student">
    <id column="stu_id" jdbcType="INTEGER" property="stuId" />
    <result column="stu_name" jdbcType="VARCHAR" property="stuName" />
    <result column="gender" jdbcType="CHAR" property="gender" />
    <result column="email" jdbcType="VARCHAR" property="email" />
    <result column="d_id" jdbcType="INTEGER" property="dId" />
  </resultMap>
  <sql id="Example_Where_Clause">
    <where>
      <foreach collection="oredCriteria" item="criteria" separator="or">
        <if test="criteria.valid">
          <trim prefix="(" prefixOverrides="and" suffix=")">
            <foreach collection="criteria.criteria" item="criterion">
              <choose>
                <when test="criterion.noValue">
                  and ${criterion.condition}
                </when>
                <when test="criterion.singleValue">
                  and ${criterion.condition} #{criterion.value}
                </when>
                <when test="criterion.betweenValue">
                  and ${criterion.condition} #{criterion.value} and #{criterion.secondValue}
                </when>
                <when test="criterion.listValue">
                  and ${criterion.condition}
                  <foreach close=")" collection="criterion.value" item="listItem" open="(" separator=",">
                    #{listItem}
                  </foreach>
                </when>
              </choose>
            </foreach>
          </trim>
        </if>
      </foreach>
    </where>
  </sql>
  <sql id="Update_By_Example_Where_Clause">
    <where>
      <foreach collection="example.oredCriteria" item="criteria" separator="or">
        <if test="criteria.valid">
          <trim prefix="(" prefixOverrides="and" suffix=")">
            <foreach collection="criteria.criteria" item="criterion">
              <choose>
                <when test="criterion.noValue">
                  and ${criterion.condition}
                </when>
                <when test="criterion.singleValue">
                  and ${criterion.condition} #{criterion.value}
                </when>
                <when test="criterion.betweenValue">
                  and ${criterion.condition} #{criterion.value} and #{criterion.secondValue}
                </when>
                <when test="criterion.listValue">
                  and ${criterion.condition}
       
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

### student-crud/src/main/java/com/qizegao/bean/Department.java
package com.qizegao.bean;

public class Department {
    private Integer deptId;

    private String deptName;
    
    

    public Department() {
		super();
	}

	public Department(Integer deptId, String deptName) {
		super();
		this.deptId = deptId;
		this.deptName = deptName;
	}

	public Integer getDeptId() {
        return deptId;
    }

    public void setDeptId(Integer deptId) {
        this.deptId = deptId;
    }

    public String getDeptName() {
        return deptName;
    }

    public void setDeptName(String deptName) {
        this.deptName = deptName == null ? null : deptName.trim();
    }
}

### student-crud/src/main/resources/mapper/DepartmentMapper.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.qizegao.dao.DepartmentMapper">
  <resultMap id="BaseResultMap" type="com.qizegao.bean.Department">
    <id column="dept_id" jdbcType="INTEGER" property="deptId" />
    <result column="dept_name" jdbcType="VARCHAR" property="deptName" />
  </resultMap>
  <sql id="Example_Where_Clause">
    <where>
      <foreach collection="oredCriteria" item="criteria" separator="or">
        <if test="criteria.valid">
          <trim prefix="(" prefixOverrides="and" suffix=")">
            <foreach collection="criteria.criteria" item="criterion">
              <choose>
                <when test="criterion.noValue">
                  and ${criterion.condition}
                </when>
                <when test="criterion.singleValue">
                  and ${criterion.condition} #{criterion.value}
                </when>
                <when test="criterion.betweenValue">
                  and ${criterion.condition} #{criterion.value} and #{criterion.secondValue}
                </when>
                <when test="criterion.listValue">
                  and ${criterion.condition}
                  <foreach close=")" collection="criterion.value" item="listItem" open="(" separator=",">
                    #{listItem}
                  </foreach>
                </when>
              </choose>
            </foreach>
          </trim>
        </if>
      </foreach>
    </where>
  </sql>
  <sql id="Update_By_Example_Where_Clause">
    <where>
      <foreach collection="example.oredCriteria" item="criteria" separator="or">
        <if test="criteria.valid">
          <trim prefix="(" prefixOverrides="and" suffix=")">
            <foreach collection="criteria.criteria" item="criterion">
              <choose>
                <when test="criterion.noValue">
                  and ${criterion.condition}
                </when>
                <when test="criterion.singleValue">
                  and ${criterion.condition} #{criterion.value}
                </when>
                <when test="criterion.betweenValue">
                  and ${criterion.condition} #{criterion.value} and #{criterion.secondValue}
                </when>
                <when test="criterion.listValue">
                  and ${criterion.condition}
                  <foreach close=")" collection="criterion.value" item="listItem" open="(" separator=",">
                    #{listItem}
                  </foreach>
                </when>

...[truncated]...

### student-crud/src/main/java/com/qizegao/test/MBGTest.java
package com.qizegao.test;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

import org.mybatis.generator.api.MyBatisGenerator;
import org.mybatis.generator.config.Configuration;
import org.mybatis.generator.config.xml.ConfigurationParser;
import org.mybatis.generator.internal.DefaultShellCallback;;

public class MBGTest {
	public static void main(String[] args) throws Exception {
		List<String> warnings = new ArrayList<String>();
		boolean overwrite = true;
		File configFile = new File("mbg.xml");
		ConfigurationParser cp = new ConfigurationParser(warnings);
		Configuration config = cp.parseConfiguration(configFile);
		DefaultShellCallback callback = new DefaultShellCallback(overwrite);
		MyBatisGenerator myBatisGenerator = new MyBatisGenerator(config,
				callback, warnings);
		myBatisGenerator.generate(null);
		System.out.println("执行成功");
	}
}

### student-crud/src/main/java/com/qizegao/test/MapperTest.java
package com.qizegao.test;

import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.view;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import com.qizegao.bean.Department;
import com.qizegao.bean.Student;
import com.qizegao.dao.DepartmentMapper;
import com.qizegao.dao.StudentMapper;



@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(locations={"classpath:applicationContext.xml"})
public class MapperTest {

	@Autowired
	DepartmentMapper departmentMapper;
	
	@Autowired
	StudentMapper studentMapper;
	
	@Test
	public void test() {
//		System.out.println(departmentMapper);
		//org.apache.ibatis.binding.MapperProxy@53093491
		
//		//插入三个部门（使用逆向工程自动生成的方法）
//		departmentMapper.insertSelective(new Department(null, "学生部"));
//		departmentMapper.insertSelective(new Department(null, "信息部"));
//		departmentMapper.insertSelective(new Department(null, "记者部"));
//		departmentMapper.insertSelective(new Department(null, "实创部"));
		
		//插入学生
		
//		studentMapper.insertSelective(new Student(null, "白曜溥", "M", "yaopu@163.com", 3));
//		studentMapper.insertSelective(new Student(null, "柴高岩", "M", "gaoyan@163.com", 1));
//		studentMapper.insertSelective(new Student(null, "陈露", "M", "chenlu@163.com", 2));
//		studentMapper.insertSelective(new Student(null, "褚宸皓", "M", "chenhao@163.com", 1));
//		studentMapper.insertSelective(new Student(null, "冯金平", "M", "jinpin@163.com", 2));
//		studentMapper.insertSelective(new Student(null, "高奇泽", "M", "qize@163.com", 3));
//		studentMapper.insertSelective(new Student(null, "宫敏", "M", "gongmin@163.com", 4));
//		studentMapper.insertSelective(new Student(null, "郭旭", "M", "guoxu@163.com", 1));
//		studentMapper.insertSelective(new Student(null, "郝思远", "M", "siyuan@163.com", 2));
//		studentMapper.insertSelective(new Student(null, "呼晓辉", "M", "xiaohui@163.com", 3));
//		studentMapper.insertSelective(new Student(null, "家彦明", "M", "yanming@163.com", 4));
//		studentMapper.insertSelective(new Student(null, "焦晨帆", "F", "chenfan@163.com", 1));
//		studentMapper.insertSelective(new Student(null, "李兴栋", "M", "xindong@163.com", 2));
//		studentMapper.insertSelective(new Student(null, "李英", "F", "liying@163.com", 3));
//		studentMapper.insertSelective(new Student(null, "李源", "M", "liyuan@163.com", 4));
//		studentMapper.insertSelective(new Student(null, "刘丹", "F", "liudan@163.com", 1));
//		studentMapper.insertSe
...[truncated]...