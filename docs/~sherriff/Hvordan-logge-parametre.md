# Hvordan logge parametre

http://stackoverflow.com/questions/1710476/print<sub>~query</sub><sub>string</sub><sub>in</sub><sub>hibernate</sub><sub>with</sub>~parameter-values

http://www.instructables.com/id/How<sub>~To</sub><sub>DIY</sub><sub>2500</sub><sub>Soundproof</sub><sub>HiFi</sub>~Headphones/

```
@Test
	//@CleanInsertDataSet({"/no/norgesgruppen/bm/webservices/behkorr/BehkorrServiceImplExceptionTest.testHentSisteKiloprkisThrowsExceptionMedSpring.xml"})
	public void testHentSisteKiloprkisThrowsExceptionMedSpring() {
		//HibernateException blir ikke oversatt til DataAccessException, transaksjonen blir rullet tilbake.
		HibernateTemplate hibernateTemplateMock = Mockito.mock(HibernateTemplate.class);
	 	Mockito.when(hibernateTemplateMock.isAllowCreate()).thenThrow(new HibernateException("Fremprovosert feil i getSession"));

		//beholdningDao.setHibernateTemplate(hibernateTemplateMock);

		/*
		BeholdningDao beholdningDaoMock = Mockito.mock(BeholdningDaoImpl.class);
		BeholdningService beholdningServiceOverride = new BeholdningServiceImpl();
		beholdningServiceOverride.setBeholdningDao(beholdningDaoMock);
		TargetSource targetSource = new SingletonTargetSource(beholdningServiceOverride);
		((Advised) beholdningService).setTargetSource(targetSource);

		String hibernateExceptionMessage = "testHentSisteKiloprisThrowsExceptionMedSpring";
		Mockito.when(beholdningDaoMock.getSisteKilopris(Matchers.any(String.class), (Matchers.any(Long.class)))).thenThrow(new HibernateException(hibernateExceptionMessage));
		*/

		HentSisteKiloprisRequestType hentSisteKiloprisRequest = lagHentSisteKiloprisRequest("12", 123L);
		try {
			behkorrWebServiceImpl.hentSisteKilopris(hentSisteKiloprisRequest);
			fail("Forventet BMForExportRuntimeException.");
		} catch (BMForExportRuntimeException e) {
			assertEquals(e.getMessage(), "Feil i hentSisteKilopris");
			assertEquals(e.getCause().getClass(), DataAccessException.class);
			//assertEquals(e.getCause().getMessage(), hibernateExceptionMessage);
		}
	}
```
