
import os
from narkdown.cli import main
from narkdown.exporter import NotionExporter

if __name__ == "__main__":
    token = "v02%3Auser_token_or_cookies%3AqrGl6ptb4FaRQVAiazKOUol_zkTOkIeVyapBEtd7JeESoLvedsv8sQY-tXHAhfc5_Toq6b5IkXy3kzhEDszm0MfNoBOa1M2nz0Yq1tuW8iXISYQMsmgVXX7Dr6_vi0NZVfi6"
    notion_exporter = NotionExporter(token)
    main()
