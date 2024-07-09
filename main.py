
import os
from narkdown.cli import main
from narkdown.exporter import NotionExporter

if __name__ == "__main__":
    token = "v02%3Auser_token_or_cookies%3AqrGl6ptb4FaRQVAiazKOUol_zkTOkIeVyapBEtd7JeESoLvedsv8sQY-tXHAhfc5_Toq6b5IkXy3kzhEDszm0MfNoBOa1M2nz0Yq1tuW8iXISYQMsmgVXX7Dr6_vi0NZVfi6"
    page_url = "https://www.notion.so/c192c7104ab341f8ae581d0697419986"

    notion_exporter = NotionExporter(token)
    notion_exporter.get_notion_page(page_url)
    main()
