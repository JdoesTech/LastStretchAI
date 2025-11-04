from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import unittest
import os

class LoginPageTest(unittest.TestCase):
    
    def setUp(self):
        """Initialize the browser and navigate to login page"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")  # Using demo site for testing
        self.wait = WebDriverWait(self.driver, 10)
        
    def test_valid_login(self):
        """Test successful login with valid credentials"""
        print("Testing valid login...")
        
        # Enter username
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_field.clear()
        username_field.send_keys("standard_user")
        
        # Enter password
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("secret_sauce")
        
        # Click login button
        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()
        
        # Verify successful login by checking inventory page
        try:
            inventory_container = self.wait.until(
                EC.presence_of_element_located((By.ID, "inventory_container"))
            )
            print("✓ Valid login test PASSED - User successfully logged in")
            return True
        except TimeoutException:
            print("✗ Valid login test FAILED - User not redirected to inventory page")
            return False
    
    def test_invalid_username(self):
        """Test login with invalid username"""
        print("Testing invalid username...")
        
        # Enter invalid username
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_field.clear()
        username_field.send_keys("invalid_user")
        
        # Enter valid password
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("secret_sauce")
        
        # Click login button
        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()
        
        # Check for error message
        try:
            error_message = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
            )
            expected_error = "Username and password do not match"
            if expected_error in error_message.text:
                print("✓ Invalid username test PASSED - Correct error message displayed")
                return True
            else:
                print("✗ Invalid username test FAILED - Incorrect error message")
                return False
        except TimeoutException:
            print("✗ Invalid username test FAILED - No error message displayed")
            return False
    
    def test_invalid_password(self):
        """Test login with invalid password"""
        print("Testing invalid password...")
        
        # Enter valid username
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_field.clear()
        username_field.send_keys("standard_user")
        
        # Enter invalid password
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("wrong_password")
        
        # Click login button
        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()
        
        # Check for error message
        try:
            error_message = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
            )
            expected_error = "Username and password do not match"
            if expected_error in error_message.text:
                print("✓ Invalid password test PASSED - Correct error message displayed")
                return True
            else:
                print("✗ Invalid password test FAILED - Incorrect error message")
                return False
        except TimeoutException:
            print("✗ Invalid password test FAILED - No error message displayed")
            return False
    
    def test_empty_credentials(self):
        """Test login with empty credentials"""
        print("Testing empty credentials...")
        
        # Click login without entering any credentials
        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()
        
        # Check for error message
        try:
            error_message = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
            )
            expected_error = "Username is required"
            if expected_error in error_message.text:
                print("✓ Empty credentials test PASSED - Correct error message displayed")
                return True
            else:
                print("✗ Empty credentials test FAILED - Incorrect error message")
                return False
        except TimeoutException:
            print("✗ Empty credentials test FAILED - No error message displayed")
            return False
    
    def tearDown(self):
        """Close the browser after each test"""
        self.driver.quit()

def run_all_tests():
    """Run all test cases and capture results"""
    print("=" * 50)
    print("LOGIN PAGE AUTOMATION TEST SUITE")
    print("=" * 50)
    
    # Create test suite
    test_suite = unittest.TestSuite()
    test_suite.addTest(LoginPageTest('test_valid_login'))
    test_suite.addTest(LoginPageTest('test_invalid_username'))
    test_suite.addTest(LoginPageTest('test_invalid_password'))
    test_suite.addTest(LoginPageTest('test_empty_credentials'))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=0)
    result = runner.run(test_suite)
    
    # Print summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    print(f"Total Tests: {result.testsRun}")
    print(f"Passed: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failed: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    return result

if __name__ == "__main__":
    run_all_tests()