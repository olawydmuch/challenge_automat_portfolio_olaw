## TASK 1

 ### Subtask 1- Dlaczego zdecydowałam się na udział w Challengu?
 
Zdecydowałam się na udział w tym Challengu, ponieważ niedawno uczestniczyłam w Challengu testera manualnego i wiele się tam nauczyłam. Liczę, że po zakoczeniu tego wyzwania mojawiedza w zakresie automatyzacji testów się poszerzy. Przyszłościowo chciałabym zostać testerem automatyzującym i testować strony internetowe w Selenium. 

### Subtask 4- Test ISTQB

13/15

--- 

## TASK 2: Selektory

### Subtask 2: Wyszukiwanie selektorów na stronie logowania. Wymień wszystkie elementy, które znajdują się na stronie logowania.

1. Scouts Panel title: 
	* //*[@id="__next"]/form/div/div[1]/h5
	* //*[text()="Scouts Panel"]
	* /html/body/div/form/div/div[1]/h5
	
2. Login input:
	* //*[@id="login"]
	* //*[@name='login']
	* //input[@type='text']
	
3. Password input
	* //*[@id="password"]
	* //*[@name= 'password']
	* //input[@type='password']
	
4. Remind password
	* //*[@id="__next"]/form/div/div[1]/a
	* //*[text()="Remind password"]
	
5. English
	* //*[@id="__next"]/form/div/div[2]/div/div
	* //*[text()='English']
	* //input[@value='en']

6. Polski
	* //*[@id="__next"]/form/div/div[2]/div/div
	* //*[text()='Polski']
	* //input[@value='pl']
	
7. Sign in button 
	* //*[@id="__next"]/form/div/div[2]/button/span[1]
	* //*[text()='Sign in']
	* //*[contains(@type,"submit")]

	
	