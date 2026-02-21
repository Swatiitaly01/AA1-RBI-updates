import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os
from typing import List, Dict

class RBIScraper:
    """Scraper for RBI official updates from Reserve Bank of India website"""
    
    def __init__(self):
        self.rbi_base_url = "https://www.rbi.org.in"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.scraped_data = []
    
    def scrape_circulars(self) -> List[Dict]:
        """Scrape RBI Circulars"""
        try:
            url = f"{self.rbi_base_url}/scripts/NotificationUser.aspx?Id=13"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.content, 'html.parser')
            
            circulars = []
            # Parse table rows containing circular information
            for row in soup.find_all('tr')[1:]:  # Skip header row
                cols = row.find_all('td')
                if len(cols) >= 3:
                    circular = {
                        'type': 'Circular',
                        'date': cols[0].text.strip(),
                        'title': cols[1].text.strip(),
                        'link': f"{self.rbi_base_url}{cols[1].find('a')['href']}" if cols[1].find('a') else '',
                        'reference': cols[2].text.strip(),
                        'scraped_at': datetime.now().isoformat()
                    }
                    circulars.append(circular)
            
            return circulars
        except Exception as e:
            print(f"Error scraping circulars: {e}")
            return []
    
    def scrape_notifications(self) -> List[Dict]:
        """Scrape RBI Notifications"""
        try:
            url = f"{self.rbi_base_url}/scripts/NotificationUser.aspx"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.content, 'html.parser')
            
            notifications = []
            for row in soup.find_all('tr')[1:]:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    notification = {
                        'type': 'Notification',
                        'date': cols[0].text.strip(),
                        'title': cols[1].text.strip(),
                        'link': f"{self.rbi_base_url}{cols[1].find('a')['href']}" if cols[1].find('a') else '',
                        'scraped_at': datetime.now().isoformat()
                    }
                    notifications.append(notification)
            
            return notifications
        except Exception as e:
            print(f"Error scraping notifications: {e}")
            return []
    
    def scrape_press_releases(self) -> List[Dict]:
        """Scrape RBI Press Releases"""
        try:
            url = f"{self.rbi_org.in}/press-release"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.content, 'html.parser')
            
            press_releases = []
            for article in soup.find_all('article')[:10]:  # Get recent 10
                title_elem = article.find('h2') or article.find('h3')
                date_elem = article.find('span', class_='date')
                link_elem = article.find('a')
                
                if title_elem and date_elem:
                    press_release = {
                        'type': 'Press Release',
                        'date': date_elem.text.strip(),
                        'title': title_elem.text.strip(),
                        'link': f"{self.rbi_base_url}{link_elem['href']}" if link_elem else '',
                        'scraped_at': datetime.now().isoformat()
                    }
                    press_releases.append(press_release)
            
            return press_releases
        except Exception as e:
            print(f"Error scraping press releases: {e}")
            return []
    
    def scrape_guidance_notes(self) -> List[Dict]:
        """Scrape RBI Guidance Notes and Master Circulars"""
        try:
            url = f"{self.rbi_base_url}/scripts/BS_ViewMasterCircular.aspx"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.content, 'html.parser')
            
            guidance_notes = []
            for row in soup.find_all('tr')[1:]:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    note = {
                        'type': 'Master Circular/Guidance',
                        'date': cols[0].text.strip() if len(cols) > 0 else '',
                        'title': cols[1].text.strip() if len(cols) > 1 else '',
                        'link': f"{self.rbi_base_url}{cols[1].find('a')['href']}" if cols[1].find('a') else '',
                        'scraped_at': datetime.now().isoformat()
                    }
                    guidance_notes.append(note)
            
            return guidance_notes
        except Exception as e:
            print(f"Error scraping guidance notes: {e}")
            return []
    
    def scrape_all_updates(self) -> List[Dict]:
        """Scrape all types of RBI updates"""
        all_updates = []
        
        print("Scraping RBI Circulars...")
        all_updates.extend(self.scrape_circulars())
        
        print("Scraping RBI Notifications...")
        all_updates.extend(self.scrape_notifications())
        
        print("Scraping RBI Press Releases...")
        all_updates.extend(self.scrape_press_releases())
        
        print("Scraping RBI Guidance Notes...")
        all_updates.extend(self.scrape_guidance_notes())
        
        return all_updates
    
    def save_updates_to_json(self, updates: List[Dict], filename: str = None) -> str:
        """Save scraped updates to JSON file"""
        if filename is None:
            filename = f"rbi_updates_{datetime.now().strftime('%Y-%m-%d')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(updates, f, indent=2, ensure_ascii=False)
        
        return filename


if __name__ == "__main__":
    scraper = RBIScraper()
    updates = scraper.scrape_all_updates()
    print(f"Total updates scraped: {len(updates)}")
    
    filename = scraper.save_updates_to_json(updates)
    print(f"Updates saved to {filename}")
