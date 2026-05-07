import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

def clean_property_number(original):
    """Remove hyphen from property number (1234567891-2 → 12345678912)"""
    return str(original).replace("-", "")

def main():
    try:
        # Step 1: Open the website
        print("Opening browser...")
        driver = webdriver.Chrome()
        driver.get("https://www3.prefeitura.sp.gov.br/sf8663/formsinternet/principal.aspx")
        
        # Wait for login page to load
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "txt_SQL")))
        
        # Wait for user to manually login
        print("Please login manually...")
        input("After logging in, press ENTER here to continue...")
        
        # Verify login was successful
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "txt_SQL")))
        except:
            print("Login verification failed. Please check if login was successful.")
            return

        # Step 2: Open the Excel file
        print("Opening Excel file...")
        workbook = load_workbook('dados_extraidos.xlsx')
        sheet = workbook.active
        
        # Step 3: Check if column H exists, if not create it
        if sheet.max_column < 8:
            # Insert new column at position 8 (H)
            sheet.insert_cols(8)
            sheet.cell(row=1, column=8, value="Proprietário")
        elif sheet.cell(row=1, column=8).value != "Proprietário":
            # If column H exists but has different header
            sheet.insert_cols(8)
            sheet.cell(row=1, column=8, value="Proprietário")
        
        # Process each row starting from row 2
        total_rows = sheet.max_row
        print(f"Processing {total_rows-1} properties...")
        
        for row in range(2, total_rows + 1):
            # Get and clean the property number
            original_value = str(sheet.cell(row=row, column=1).value)
            clean_value = clean_property_number(original_value)
            
            # Validate we have exactly 11 digits (after removing hyphen)
            if len(clean_value) != 11 or not clean_value.isdigit():
                print(f"Row {row}: Invalid property number '{original_value}' (needs format 1234567891-2), skipping...")
                sheet.cell(row=row, column=8, value="INVALID NUMBER")
                continue
            
            print(f"\nProcessing row {row}: Original: {original_value} | Clean: {clean_value}")
            
            try:
                # Clear and fill the "Cadastro do Imóvel" field
                cadastro_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "txt_SQL")))
                cadastro_field.clear()
                cadastro_field.send_keys(clean_value)
                
                # Fill the "Exercício" field with 2026
                exercicio_field = driver.find_element(By.ID, "txt_Exercicio")
                exercicio_field.clear()
                exercicio_field.send_keys("2025")
                
                # Click the "Consultar" button
                consultar_button = driver.find_element(By.XPATH, "//input[@value='Consultar']")
                consultar_button.click()
                
                # Wait for the results to load
                time.sleep(3)
                
                try:
                    # Get the "Proprietário" data
                    proprietario_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "lblproprietario")))
                    proprietario_data = proprietario_element.text
                    
                    # Fill column H with the data
                    sheet.cell(row=row, column=8, value=proprietario_data)
                    print(f"Successfully retrieved owner: {proprietario_data}")
                    
                except Exception as e:
                    print(f"Error retrieving owner data: {str(e)}")
                    sheet.cell(row=row, column=8, value="OWNER DATA ERROR")
                    
            except Exception as e:
                print(f"Error processing property {clean_value}: {str(e)}")
                sheet.cell(row=row, column=8, value="PROCESSING ERROR")
                # Refresh page for next attempt
                driver.refresh()
                time.sleep(2)
        
        # Save the file and close the browser
        print("\nSaving results...")
        workbook.save('dados_extraidos_IPTU.xlsx')
        print("Results saved to dados_extraidos_IPTU.xlsx")
        
    except Exception as e:
        print(f"Fatal error: {str(e)}")
    finally:
        if 'driver' in locals():
            driver.quit()
            print("Browser closed. Process completed.")

if __name__ == "__main__":
    main()