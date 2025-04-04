import re
from parser_generic import MedicalDocParser


class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return{
            "patient_name": self.get_field("patient_name") or "",
            "patient_address": self.get_field("patient_address") or "",
            "medicines": self.get_field("medicines") or "",
            "directions": self.get_field("directions") or "",
            "refill": self.get_field("refill") or ""
        }        
    
    def get_field(self, field_name):
        pattern_dict = {
            # More flexible patterns to account for OCR variations
            "patient_name": {
                "pattern": [
                    r"[Nn]ame:?\s*([A-Za-z\s]+)(?:[^A-Za-z\n]|$)",
                    r"[Nn]ame\s*[:;]\s*([A-Za-z\s]+)",
                    r"[Pp]atient\s*[:;]?\s*([A-Za-z\s]+)",
                ]
            },
            "patient_address": {
                "pattern": [
                    r"[Aa]ddress:?\s*([^\n]+)",
                    r"[Aa]ddress\s*[:;]\s*([^\n]+)",
                    r"[Rr]esidence\s*[:;]?\s*([^\n]+)",
                ]
            },
            "medicines": {
                "pattern": [
                    r"(?:[Aa]ddress|[Rr]esidence)[^\n]*\n+([^D][^\n]*(?:\n[^D][^\n]*)*?)(?:[Dd]irections|[Ii]nstructions)",
                    r"(?:[Mm]edication|[Mm]edicines|[Pp]rescribed)[^\n]*\n+([^\n]*(?:\n[^\n]*)*?)(?:[Dd]irections|[Ii]nstructions)",
                ],
                "flags": re.DOTALL
            },
            "directions": {
                "pattern": [
                    r"[Dd]irections:?\s*([^\n]*(?:\n[^R][^\n]*)*?)(?:[Rr]efill|$)",
                    r"[Ii]nstructions:?\s*([^\n]*(?:\n[^R][^\n]*)*?)(?:[Rr]efill|$)",
                ],
                "flags": re.DOTALL
            },
            "refill": {
                "pattern": [
                    r"[Rr]efill:?\s*(\d+)",
                    r"[Rr]efill\s*[:;]?\s*(\d+)",
                    r"[Rr]efill:?\s*([A-Za-z0-9\s]+)",
                ],
                "flags": re.DOTALL
            },
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
                        return matches[0].strip()
            except Exception as e:
                print(f"Error extracting {field_name}: {str(e)}")
        return None


if __name__ == "__main__":
    document_text = """
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

Prednisone 20 md
Lialda 2.4 gram

Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks
Lialda - take 2 pill everyday for 1 month

Refill: 3 times
"""
    pp = PrescriptionParser(document_text)
    print(pp.parse())