# Deterministic random code snippets
### student-crud/mbg.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE generatorConfiguration
  PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
  "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">
<generatorConfiguration>

	<context id="DB2Tables" targetRuntime="MyBatis3">
		
		<!-- 去掉生成的结构中多余的注释 -->
		<commentGenerator>
			<property name="suppressAllComments" value="true" />
		</commentGenerator>
		
		<!-- 配置数据库连接 -->
		<jdbcConnection driverClass="com.mysql.jdbc.Driver"
			connectionURL="jdbc:mysql://localhost:3306/ssm_crud?useUnicode=true&amp;characterEncoding=utf-8&amp;useSSL=false&amp;serverTimezone=GMT" 
			userId="root"
			password="root">
		</jdbcConnection>

		<javaTypeResolver>
			<property name="forceBigDecimals" value="false" />
		</javaTypeResolver>

		<!-- 指定javaBean生成的位置 -->
		<javaModelGenerator targetPackage="com.qizegao.bean"
			targetProject=".\src\main\java">
			<property name="enableSubPackages" value="true" />
			<property name="trimStrings" value="true" />
		</javaModelGenerator>

		<!--指定mapper.xml文件生成的位置 -->
		<sqlMapGenerator targetPackage="mapper" targetProject=".\src\main\resources">
			<property name="enableSubPackages" value="true" />
		</sqlMapGenerator>

		<!-- 指定mapper接口生成的位置 -->
		<javaClientGenerator type="XMLMAPPER"
			targetPackage="com.qizegao.dao" targetProject=".\src\main\java">
			<property name="enableSubPackages" value="true" />
		</javaClientGenerator>

		<!-- 指定每个表对应的java类型 -->
		<table tableName="tbl_stu" domainObjectName="Student"></table>
		<table tableName="tbl_dept" domainObjectName="Department"></table>
	</context>
</generatorConfiguration>

### student-crud/src/main/webapp/WEB-INF/dispatcherServlet-servlet.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:mvc="http://www.springframework.org/schema/mvc"
	xsi:schemaLocation="http://www.springframework.org/schema/mvc http://www.springframework.org/schema/mvc/spring-mvc-4.3.xsd
		http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">

	<!--SpringMVC的配置文件，包含网页跳转逻辑的控制 -->
	
	<!-- 只扫描控制器 -->
	<context:component-scan base-package="com.qizegao" use-default-filters="false">
		<context:include-filter type="annotation" expression="org.springframework.stereotype.Controller"/>
	</context:component-scan>
	
	<!--配置视图解析器，方便页面返回 -->
	<bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
		<property name="prefix" value="/WEB-INF/views/"></property>
		<property name="suffix" value=".jsp"></property>
	</bean>
	
	<!--两个标准配置  -->
	<mvc:default-servlet-handler/>
	
	<mvc:annotation-driven/>

</beans>

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

### student-crud/src/main/java/com/qizegao/dao/DepartmentMapper.java
package com.qizegao.dao;

import com.qizegao.bean.Department;
import com.qizegao.bean.DepartmentExample;
import java.util.List;
import org.apache.ibatis.annotations.Param;

public interface DepartmentMapper {
    long countByExample(DepartmentExample example);

    int deleteByExample(DepartmentExample example);

    int deleteByPrimaryKey(Integer deptId);

    int insert(Department record);

    int insertSelective(Department record);

    List<Department> selectByExample(DepartmentExample example);

    Department selectByPrimaryKey(Integer deptId);

    int updateByExampleSelective(@Param("record") Department record, @Param("example") DepartmentExample example);

    int updateByExample(@Param("record") Department record, @Param("example") DepartmentExample example);

    int updateByPrimaryKeySelective(Department record);

    int updateByPrimaryKey(Department record);
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

### student-crud/src/main/resources/applicationContext.xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:mybatis-spring="http://mybatis.org/schema/mybatis-spring"
	xmlns:tx="http://www.springframework.org/schema/tx"
	xmlns:aop="http://www.springframework.org/schema/aop"
	xsi:schemaLocation="http://mybatis.org/schema/mybatis-spring http://mybatis.org/schema/mybatis-spring-1.2.xsd
		http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd
		http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-4.3.xsd
		http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx-4.3.xsd">

	<!-- 不扫描已由springmvc扫描的controller注解 -->
	<context:component-scan base-package="com.qizegao">
		<context:exclude-filter type="annotation"
			expression="org.springframework.stereotype.Controller" />
	</context:component-scan>

	<!-- 引入properties配置文件 -->
	<context:property-placeholder location="classpath:dbconfig.properties" />
	<bean id="pooledDataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource">
		<property name="jdbcUrl" value="${jdbc.jdbcUrl}"></property>
		<property name="driverClass" value="${jdbc.driverClass}"></property>
		<property name="user" value="${jdbc.user}"></property>
		<property name="password" value="${jdbc.password}"></property>
	</bean>
	
	<!-- 和MyBatis整合 -->
	<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
		<property name="configLocation" value="classpath:mybatis-config.xml"></property>
		<property name="dataSource" ref="pooledDataSource"></property>
		<property name="mapperLocations" value="classpath:mapper/*.xml"></property>
	</bean>

	<!-- 扫描dao接口 -->
	<mybatis-spring:scan base-package="com.qizegao.dao"/>	
	
	<!-- 配置事务控制 -->
	<bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
		<property name="dataSource" ref="pooledDataSource"></property>
	</bean>
	
	<!-- 使用xml配置形式的事务 -->
	<aop:config>
		<aop:pointcut expression="execution(* com.qizegao.service..*(..))" id="txPoint"/>
		<aop:advisor advice-ref="txAdvice" pointcut-ref="txPoint"/>
	</aop:config>
	
	<!-- 配置事务增强 -->
	<tx:advice id="txAdvice" transaction-manager="transactionManager">
		<tx:attributes>
			<tx:method name="*"/>
			<tx:method name="get*" read-only="true"/>
		</tx:
...[truncated]...

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

### student-crud/src/main/java/com/qizegao/bean/DepartmentExample.java
package com.qizegao.bean;

import java.util.ArrayList;
import java.util.List;

public class DepartmentExample {
	
    protected String orderByClause; //排序方式

    protected boolean distinct; //是否去重

    protected List<Criteria> oredCriteria; //自定义查询条件

    public DepartmentExample() {
        oredCriteria = new ArrayList<Criteria>();
    }

    public void setOrderByClause(String orderByClause) {
        this.orderByClause = orderByClause;
    }

    public String getOrderByClause() {
        return orderByClause;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }

    public boolean isDistinct() {
        return distinct;
    }

    public List<Criteria> getOredCriteria() {
        return oredCriteria;
    }

    public void or(Criteria criteria) {
        oredCriteria.add(criteria);
    }

    public Criteria or() {
        Criteria criteria = createCriteriaInternal();
        oredCriteria.add(criteria);
        return criteria;
    }

    public Criteria createCriteria() {
        Criteria criteria = createCriteriaInternal();
        if (oredCriteria.size() == 0) {
            oredCriteria.add(criteria);
        }
        return criteria;
    }

    protected Criteria createCriteriaInternal() {
        Criteria criteria = new Criteria();
        return criteria;
    }

    public void clear() {
        oredCriteria.clear();
        orderByClause = null;
        distinct = false;
    }

    protected abstract static class GeneratedCriteria {
        protected List<Criterion> criteria;

        protected GeneratedCriteria() {
            super();
            criteria = new ArrayList<Criterion>();
        }

        public boolean isValid() {
            return criteria.size() > 0;
        }

        public List<Criterion> getAllCriteria() {
            return criteria;
        }

        public List<Criterion> getCriteria() {
            return criteria;
        }

        protected void addCriterion(String condition) {
            if (condition == null) {
                throw new RuntimeException("Value for condition cannot be null");
            }
            criteria.add(new Criterion(condition));
        }

        protected void addCriterion(String condition, Object value, String property) {
            if (value == null) {
                throw new RuntimeException("Value for " + property + " cannot be null");
            }
            criteria.add(new Criterion(condition, value));
        }

        protected void addCriterion(String condition, Object value1, Object value2, String property) {
          
...[truncated]...

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

### student-crud/pom.xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.qizegao</groupId>
  <artifactId>my-crud</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <packaging>war</packaging>
  
	  <dependencies>
  		<!-- SpringMVC与Spring整合 -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-webmvc</artifactId>
			<version>4.3.7.RELEASE</version>
		</dependency>

		<!-- Spring-Jdbc -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-jdbc</artifactId>
			<version>4.3.7.RELEASE</version>
		</dependency>

		<!-- Spring面向切面编程 -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-aspects</artifactId>
			<version>4.3.7.RELEASE</version>
		</dependency>

		<!--MyBatis -->
		<dependency>
			<groupId>org.mybatis</groupId>
			<artifactId>mybatis</artifactId>
			<version>3.4.2</version>
		</dependency>
		
		<!-- MyBatis整合Spring-->
		<dependency>
			<groupId>org.mybatis</groupId>
			<artifactId>mybatis-spring</artifactId>
			<version>1.3.1</version>
		</dependency>

		<!-- 数据库连接池、驱动 -->
		<dependency>
    		<groupId>com.mchange</groupId>
   		 	<artifactId>c3p0</artifactId>
   			<version>0.9.5.2</version>
		</dependency>
		
		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<version>5.1.49</version>
		</dependency>
		
		<!-- jstl，servlet-api，junit -->
		<dependency>
			<groupId>jstl</groupId>
			<artifactId>jstl</artifactId>
			<version>1.2</version>
		</dependency>

		<dependency>
			<groupId>javax.servlet</groupId>
			<artifactId>javax.servlet-api</artifactId>
			<version>3.0.1</version>
			<scope>provided</scope>
		</dependency>

		<dependency>
			<groupId>junit</groupId>
			<artifactId>junit</artifactId>
			<version>4.12</version>
		</dependency>
		
		<!-- MBG -->
		<dependency>
			<groupId>org.mybatis.generator</groupId>
			<artifactId>mybatis-generator-core</artifactId>
			<version>1.3.5</version>
		</dependency>
		
		<!--Spring-test -->
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-test</artifactId>
			<version>4.3.7.RELEASE</version>
		</dependency>
		
		<!--引入pageHelper分页插件 -->
		<dependency>
			<groupId>com.github.pagehelper</groupId>
			<artifactId>pagehelper</artifactId>
			<version>5.0.0</version>
		</dependency>
		
		<!-- Jackson -->
		<dependency>
			<groupId>com.fasterxml.jackson.core</groupId>
			<artif
...[truncated]...

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

### student-crud/src/main/resources/mybatis-config.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
  PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>

	<!-- 启用驼峰命名 -->
	<settings>
		<setting name="mapUnderscoreToCamelCase" value="true"/>
	</settings>
	
	<typeAliases>
		<package name="com.qizegao.bean"/>
	</typeAliases>
	
	<plugins>
		<plugin interceptor="com.github.pagehelper.PageInterceptor">
			<!--分页参数合理化，页数小于1到第一页，大于最后一页到最后一页  -->
			<property name="reasonable" value="true"/>
			<!-- 还可以设置其他属性 -->
		</plugin>
	</plugins>

</configuration>

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

### student-crud/.settings/org.eclipse.wst.common.project.facet.core.xml
<?xml version="1.0" encoding="UTF-8"?>
<faceted-project>
  <fixed facet="wst.jsdt.web"/>
  <installed facet="java" version="1.8"/>
  <installed facet="wst.jsdt.web" version="1.0"/>
  <installed facet="jst.web" version="2.5"/>
</faceted-project>

### student-crud/src/main/java/com/qizegao/bean/Msg.java
package com.qizegao.bean;

import java.util.HashMap;
import java.util.Map;

public class Msg {
	
	//状态码(设定100表示成功，200表示失败)
	private int code;
	
	//提示信息
	private String msg;
	
	//用户要返回给浏览器的数据
	private Map<String, Object> extend = new HashMap<String, Object>();

	public static Msg success(){
		Msg result = new Msg();
		result.setCode(100);
		result.setMsg("处理成功！");
		return result;
	}
	
	public static Msg fail(){
		Msg result = new Msg();
		result.setCode(200);
		result.setMsg("处理失败！");
		return result;
	}
	
	//添加用户返回给浏览器的数据
	public Msg add(String key,Object value){
		this.getExtend().put(key, value);
		return this;
	}
	
	
	public int getCode() {
		return code;
	}

	public void setCode(int code) {
		this.code = code;
	}

	public String getMsg() {
		return msg;
	}

	public void setMsg(String msg) {
		this.msg = msg;
	}

	public Map<String, Object> getExtend() {
		return extend;
	}

	public void setExtend(Map<String, Object> extend) {
		this.extend = extend;
	}
	
	
}

### student-crud/src/main/webapp/WEB-INF/web.xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app id="WebApp_ID" version="2.5" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">

	<!-- 1. 配置监听器启动Spring的容器 -->
	<!-- needed for ContextLoaderListener -->
	<context-param>
		<param-name>contextConfigLocation</param-name>
		<param-value>classpath:applicationContext.xml</param-value>
	</context-param>

	<!-- Bootstraps the root web application context before servlet initialization -->
	<listener>
		<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
	</listener>
	
	
	<!-- 2. springmvc的前端控制器 -->
	<!-- The front controller of this Spring Web application, responsible for handling all application requests -->
	<servlet>
		<servlet-name>dispatcherServlet</servlet-name>
		<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
		
		<!-- 没有使用init-param标签，需要将springmvc配置文件放在正确的位置 -->
		
		<load-on-startup>1</load-on-startup>
	</servlet>

	<!-- Map all requests to the DispatcherServlet for handling -->
	<servlet-mapping>
		<servlet-name>dispatcherServlet</servlet-name>
		<url-pattern>/</url-pattern>
	</servlet-mapping>


	<!-- 3. 字符编码过滤器，一定在其余filter之前 -->
	<filter>
		<filter-name>CharacterEncodingFilter</filter-name>
		<filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
		<init-param>
			<param-name>encoding</param-name>
			<param-value>utf-8</param-value>
		</init-param>
		<init-param>
			<param-name>forceRequestEncoding</param-name>
			<param-value>true</param-value>
		</init-param>
		<init-param>
			<param-name>forceResponseEncoding</param-name>
			<param-value>true</param-value>
		</init-param>
	</filter>
	<filter-mapping>
		<filter-name>CharacterEncodingFilter</filter-name>
		<url-pattern>/*</url-pattern>
	</filter-mapping>
	
	
	<!-- 4. Restful风格的配置 -->
	<filter>
		<filter-name>HiddenHttpMethodFilter</filter-name>
		<filter-class>org.springframework.web.filter.HiddenHttpMethodFilter</filter-class>
	</filter>
	<filter-mapping>
		<filter-name>HiddenHttpMethodFilter</filter-name>
		<url-pattern>/*</url-pattern>
	</filter-mapping>
	<filter>
		<filter-name>HttpPutFormContentFilter</filter-name>
		<filter-class>org.springframework.web.filter.HttpPutFormContentFilter</filter-class>
	</filter>
	<filter-mapping>
		<filter-name>HttpPutFormContentFilter</filter-name>
		<url-pattern>/*</url-pattern>
	</filter-mapping>


</web-app>

### student-crud/src/main/java/com/qizegao/bean/StudentExample.java
package com.qizegao.bean;

import java.util.ArrayList;
import java.util.List;

public class StudentExample {
    protected String orderByClause;

    protected boolean distinct;

    protected List<Criteria> oredCriteria;

    public StudentExample() {
        oredCriteria = new ArrayList<Criteria>();
    }

    public void setOrderByClause(String orderByClause) {
        this.orderByClause = orderByClause;
    }

    public String getOrderByClause() {
        return orderByClause;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }

    public boolean isDistinct() {
        return distinct;
    }

    public List<Criteria> getOredCriteria() {
        return oredCriteria;
    }

    public void or(Criteria criteria) {
        oredCriteria.add(criteria);
    }

    public Criteria or() {
        Criteria criteria = createCriteriaInternal();
        oredCriteria.add(criteria);
        return criteria;
    }

    public Criteria createCriteria() {
        Criteria criteria = createCriteriaInternal();
        if (oredCriteria.size() == 0) {
            oredCriteria.add(criteria);
        }
        return criteria;
    }

    protected Criteria createCriteriaInternal() {
        Criteria criteria = new Criteria();
        return criteria;
    }

    public void clear() {
        oredCriteria.clear();
        orderByClause = null;
        distinct = false;
    }

    protected abstract static class GeneratedCriteria {
        protected List<Criterion> criteria;

        protected GeneratedCriteria() {
            super();
            criteria = new ArrayList<Criterion>();
        }

        public boolean isValid() {
            return criteria.size() > 0;
        }

        public List<Criterion> getAllCriteria() {
            return criteria;
        }

        public List<Criterion> getCriteria() {
            return criteria;
        }

        protected void addCriterion(String condition) {
            if (condition == null) {
                throw new RuntimeException("Value for condition cannot be null");
            }
            criteria.add(new Criterion(condition));
        }

        protected void addCriterion(String condition, Object value, String property) {
            if (value == null) {
                throw new RuntimeException("Value for " + property + " cannot be null");
            }
            criteria.add(new Criterion(condition, value));
        }

        protected void addCriterion(String condition, Object value1, Object value2, String property) {
            if (value1 == null || value2 =
...[truncated]...

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
				map.put(fieldError.ge
...[truncated]...