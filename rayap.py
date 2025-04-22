import time, csv, random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pyfiglet import Figlet

f = Figlet(font='banner3-D')  # tinggal ganti nama font di sini
print(f.renderText("MERAYAP"))
print("by Juki".center(60, "─"))

# ========== INPUT DARI USER ==========
query = input("🔍 Masukkan kata kunci (frasa): ").strip()
domains = input("🌐 Masukkan domain (pisahkan dengan koma, contoh: facebook.com,kompas.com): ").split(",")
time_range = input("⏱️ Pilih rentang waktu (1 = 24 jam, 2 = 1 minggu, 3 = 1 bulan, 4 = kapan saja): ").strip()

# ========== KONVERSI PARAMETER ==========

# Konversi rentang waktu
time_map = {
    "1": "qdr:d",   # 24 jam
    "2": "qdr:w",   # 1 minggu
    "3": "qdr:m",   # 1 bulan
    "4": "",        # kapan saja
}
tbs_param = time_map.get(time_range, "")

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

# Jalankan scraping untuk setiap domain
all_data = []

for domain in domains:
    domain = domain.strip()
    print(f"\n🔎 Sedang mencari di domain: {domain}...\n")
    search_url = f"https://www.google.com/search?as_epq={query.replace(' ', '+')}&as_sitesearch={domain}&tbs={tbs_param}"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(search_url)

    data = []
    max_pages = 30

    for page in range(max_pages):
        try:
            WebDriverWait(driver, 60).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.MjjYud"))
            )
            search_results = driver.find_elements(By.CSS_SELECTOR, "div.MjjYud")

            print(f"✅ Page {page+1}: {len(search_results)} hasil ditemukan")

            for result in search_results:
                try:
                    title = result.find_element(By.TAG_NAME, "h3").text.strip()
                    snippet = result.find_element(By.CSS_SELECTOR, "div.VwiC3b").text.strip()
                    link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
                    data.append([title, snippet, link])
                except:
                    continue

            # Klik tombol "Next"
            try:
                next_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.ID, "pnnext"))
                )
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(random.uniform(5, 8))
            except:
                print("⛔ Tidak ada tombol Next.")
                break
        except Exception as e:
            print("❌ Error:", e)
            break

    all_data.extend(data)
    driver.quit()

# ========== SIMPAN KE CSV ==========
with open("google_crawling.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Snippet", "Link"])
    for row in all_data:
        writer.writerow(row)

print(f"\n🎉 Total {len(all_data)} hasil disimpan ke google_crawling.csv")
