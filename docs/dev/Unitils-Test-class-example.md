# Unitils Test class example

```java
package com.company; 

import com.company.DaoAssertUtil;
import com.company.SomeDaoImpl;
import org.apache.log4j.Logger;
import org.springframework.jdbc.core.simple.SimpleJdbcTemplate;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.TestExecutionListeners;
import org.springframework.test.context.testng.AbstractTestNGSpringContextTests;
import org.springframework.test.jdbc.SimpleJdbcTestUtils;
import org.testng.annotations.Test;
import org.unitils.UnitilsTestExecutionListener;
import org.unitils.dataset.annotation.CleanInsertDataSet;

import javax.annotation.Resource;
import java.sql.SQLException;

import static org.testng.Assert.*;

@Test(groups = "database-productA")
@ContextConfiguration
@TestExecutionListeners(UnitilsTestExecutionListener.class)
public class SomeTest extends AbstractTestNGSpringContextTests {
	@Resource
	private SimpleJdbcTemplate simpleJdbcTemplate;
	
	@Test
	public void testAppContextLoading() {
		assertNotNull(simpleJdbcTemplate);
	}

	@Test
	@CleanInsertDataSet({"SomeTest.testStoredProcedureOK.xml"})
	public void testStoredProcedureOK() throws SQLException {
		//call procedure

		//assert new state in database 
	}
}
```
