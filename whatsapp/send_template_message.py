import os
import requests

TEMPLATES = {
   "patient_invited_by_doctor": { # -> name to identify the template in the code 
       "name": "patient_invited_by_doctor", # -> name placed in the Meta Template (same name as above)
       "language_code": "es_PE",
       "variables": ["patient_name", "doctor_name", "invitation_id"], # -> variables placed in the Meta Template
   },
   "patient_created_by_doctor": {
        "name": "patient_created_by_doctor",
        "language_code": "es_PE",
        "variables": ["patient_name", "doctor_name"]
   }
}

def format_phone_number(phone_number):
    number = ''.join(str(phone_number).split())

    if number.startswith("+"):
        number = number[1:]
    if number.startswith("51"):
        return number
    if number.startswith("9") and len(number) == 9:
        return "51" + number

    return number

def send_whatsapp_template(phone_number, template_name, variables=None):
    template_info = TEMPLATES.get(template_name)
    
    if not template_info:
        raise ValueError(f"No template config found for {template_name}")
    
    phone_number = format_phone_number(phone_number)
    
    headers = {
        "Content-Type": "application/json",
        "Authorization":
        f"Bearer {os.getenv("WHATSAPP_TOKEN")}" 
    }

    parameters = []

    if variables is not None:
        for var in template_info["variables"]:
            param = {
                "type": "text",
                "text": str(variables[var])
            }
            parameters.append(param)

    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "template",
        "template": {
            "name": template_info["name"],
            "language": {"code": template_info["language_code"]},
            "components": [
                {
                    "type": "body", 
                    "parameters": parameters
                }
            ]
        }
    }

    response = requests.post(os.getenv("WHATSAPP_API_URL"), json=payload, headers=headers)
    if response.status_code != 200:
        return {"success": False, "error": response.text}
        
    response.raise_for_status()
    return {"success": True, "messageId": response.json().get("messages", [{}])[0].get("id")}