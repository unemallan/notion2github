
import os
from narkdown.exporter import NotionExporter
from narkdown.cli import main

if __name__ == "__main__":
    token_v2 = os.environ['NOTION_TOKEN']
    page_url = "https://www.notion.so/c192c7104ab341f8ae581d0697419986"
    database_url = "https://www.notion.so/c192c7104ab341f8ae581d0697419986?v=7962af9b51ff41f69f9ecc5e1dbef96d"
    email = "unemallan@gmail.com"
    
    notion_exporter = NotionExporter(token_v2)
    notion_exporter.get_notion_page(page_url)
    notion_exporter.get_notion_pages_from_database(database_url)

    main()
