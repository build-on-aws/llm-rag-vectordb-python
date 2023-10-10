import os
import requests


def scrape_linkedin_profile(linkedin_profile_url):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    # For production
    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    # # For test and development
    # response = requests.get(
    #     "https://gist.githubusercontent.com/debnsuma/07afaf3939dcc2b5cc404de58016fdd2/raw/9e4b8f942364f6ee9759d1cdb1b6d7b8078ceb4e/suman.json"
    # )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k
        not in [
            "people_also_viewed",
            "certifications",
            "accomplishment_publications",
            "accomplishment_honors_awards",
            "accomplishment_projects",
        ]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
