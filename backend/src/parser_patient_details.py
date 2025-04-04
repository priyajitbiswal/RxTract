import re
from parser_generic import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return{
            "patient_name": self.get_field("patient_name"),
            "phone_no": self.get_field("phone_no"),
            "vaccination_status": self.get_field("vaccination_status"),
            "medical_problems": self.get_field("medical_problems"),
            "has_insurance": self.get_field("has_insurance")
        }
    
    def get_field(self, field_name):
        pattern_dict = {
            "patient_name": {
                "pattern": [
                    r"[Pp]atient\s*[Nn]ame:?\s*([A-Za-z\s]+)",
                    r"[Nn]ame:?\s*([A-Za-z\s]+)",
                    r"[Pp]atient:?\s*([A-Za-z\s]+)",
                    r"[Pp]atient\s*[Ii]nformation[^\n]*\n+([A-Za-z\s]+)",
                    r"[Dd]ate\n+([a-zA-Z]+\s+[a-zA-Z]+)"
                ]
            },
            "phone_no": {
                "pattern": [
                    r"[Pp]hone:?\s*([\(\)\d\s\-\.]+)",
                    r"[Tt]el(?:ephone)?:?\s*([\(\)\d\s\-\.]+)",
                    r"(\(\d{3}\)[.\s-]?\d{3}[.\s-]?\d{4})",
                    r"(\d{3}[.\s-]?\d{3}[.\s-]?\d{4})"
                ]
            },
            "vaccination_status": {
                "pattern": [
                    r"[Vv]accination:?\s*(Yes|No|Y|N)",
                    r"[Vv]accinated:?\s*(Yes|No|Y|N)",
                    r"[Vv]accination\s*[Ss]tatus:?\s*(Yes|No|Y|N)",
                    r"[Vv]accination\?\s*(Yes|No|Y|N)"
                ]
            },
            "medical_problems": {
                "pattern": [
                    r"[Mm]edical\s*[Pp]roblems:?\s*([^\n]+(?:\n[^I][^\n]*)*)",
                    r"[Mm]edical\s*[Hh]istory:?\s*([^\n]+(?:\n[^I][^\n]*)*)",
                    r"[Hh]ealth\s*[Cc]oncerns:?\s*([^\n]+(?:\n[^I][^\n]*)*)",
                    r"[Hh]eadaches\):?\s*\n+([^\n]+(?:\n[^I][^\n]*)*)"
                ],
                "flags": re.DOTALL
            },
            "has_insurance": {
                "pattern": [
                    r"[Ii]nsurance:?\s*(Yes|No|Y|N)",
                    r"[Hh]as\s*[Ii]nsurance:?\s*(Yes|No|Y|N)",
                    r"[Ii]nsurance\s*[Cc]overage:?\s*(Yes|No|Y|N)",
                    r"[Ii]nsurance\?\s*(Yes|No|Y|N)"
                ]
            }
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            try:
                # Try multiple patterns for each field
                patterns = pattern_object["pattern"] if isinstance(pattern_object["pattern"], list) else [pattern_object["pattern"]]
                flags = pattern_object.get("flags", 0)
                
                for pattern in patterns:
                    matches = re.findall(pattern, self.text, flags=flags)
                    if matches and len(matches) > 0:
                        result = matches[0].strip()
                        
                        # Normalize values
                        if field_name == "vaccination_status" or field_name == "has_insurance":
                            if result.lower() in ["y", "yes"]:
                                return "Yes"
                            elif result.lower() in ["n", "no"]:
                                return "No"
                        
                        return result
            except Exception as e:
                print(f"Error extracting {field_name}: {str(e)}")
        return None
            
        
if __name__ == "__main__":
    text_1 = """
17/12/2020

Patient Medical Record

Patient Information Birth Date
Jerry Lucas May 2 1998
(279) 920-8204 Weight:
4218 Wheeler Ridge Dr 57
Buffalo, New York, 14201 Height:
5' 4"

In Case of Emergency
Joe Lucas
4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone
Work phone

General Medical History

Chicken Pox (Varicella): Yes
Measles: Yes
Mumps: Yes
Rubella: Yes
Whooping Cough: Yes
Scarlet Fever: No
Pneumonia: No
Tuberculosis: No

Immunizations
Polio: Yes
Tetanus: Yes
Hepatitis B: Yes
Hepatitis A: No
Influenza: Yes
MMR: Yes

Surgeries
Appendectomy: No
Cardiovascular procedure: No
Cholecystectomy: No
Tonsillectomy: No
Hernia repair: No

Current Medications
Metformin 1000mg tablet
Losartan 50mg tablet
Levothyroxine 50mcg tablet
Azithromycin 250mg tablet
Vitamin D 1000 IU tablet

Allergies
Penicillin
Morphine
Latex

Medical Problems (including past accidents or injuries)
Hypertension
Type 2 diabetes
Hypothyroidism
Recurrent UTIs
Migraine

Additional Notes
Patient is currently experiencing symptoms of upper respiratory infection. Advised to rest and increase fluid intake.

Primary Insurance
Medicare
Secondary Insurance
Medicaid

Physician Signature
Dr. Jane Smith, MD

Have you recently traveled outside the country?
No

Have you recently been hospitalized?
No

Have you had a flu vaccination?
Yes

Do you have health insurance?
Yes
"""
    pp = PatientDetailsParser(text_1)
    print(pp.parse())
