import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/32f3c85b9513994c572613f2c8b376b633bfc43f/eden-marco-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://api.scrapin.io/v1/enrichment/profile"
        payload = {
            "linkedInUrl": linkedin_profile_url,
            "includes": {
            "includeCompany": True,
            "includeSummary": True,
            "includeFollowersCount": True,
            "includeCreationDate": True,
            "includeSkills": True,
            "includeLanguages": True,
            "includeExperience": True,
            "includeEducation": True,
            "includeCertifications": True
            }
         }
        query_params = {
            "apikey": os.environ["SCRAPIN_API_KEY"]
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post(api_endpoint, params=query_params, json=payload, headers=headers)
        print("Response is",response.json());
    
    data = response.json().get("person")
    # data = {
    #     k: v
    #     for k, v in data.items()
    #     if v not in ([], "", "", None) and k not in ["certifications"]
    # }

    return data
        
       
       
       
       
       
       

    # data = response.json();

  

    # print("data is",data);

    # return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/vagarwal16/"
        ),
    )
