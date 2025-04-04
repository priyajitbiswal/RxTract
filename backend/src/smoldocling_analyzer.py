"""
SmolDocling integration for enhanced medical document analysis
"""
import os
import logging
import re

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SmolDoclingAnalyzer:
    def __init__(self):
        """Initialize the SmolDocling analyzer for medical document analysis"""
        try:
            # In a real implementation, we would load the model here
            # For now, we'll use a rule-based approach to simulate the model
            logger.info("Initializing SmolDocling analyzer (rule-based simulation)")
            self.model_loaded = True
            
            # Load medical knowledge base (simplified)
            self.medications = {
                "prednisone": {
                    "uses": ["inflammation", "autoimmune disorders", "allergic reactions"],
                    "side_effects": ["increased appetite", "mood changes", "weight gain", "high blood pressure"],
                    "diet": "Low sodium, high potassium diet. Avoid alcohol.",
                    "routine": "Take with food in the morning. Monitor blood pressure regularly."
                },
                "lialda": {
                    "uses": ["ulcerative colitis", "inflammatory bowel disease"],
                    "side_effects": ["headache", "nausea", "abdominal pain", "diarrhea"],
                    "diet": "High fiber diet. Stay well hydrated.",
                    "routine": "Take with food. Avoid antacids 2 hours before or after."
                },
                "metformin": {
                    "uses": ["type 2 diabetes", "insulin resistance"],
                    "side_effects": ["diarrhea", "nausea", "stomach upset", "vitamin B12 deficiency"],
                    "diet": "Low carbohydrate diet. Avoid excessive alcohol.",
                    "routine": "Take with meals to reduce stomach upset. Monitor blood sugar regularly."
                },
                "losartan": {
                    "uses": ["high blood pressure", "heart failure", "kidney protection"],
                    "side_effects": ["dizziness", "cough", "high potassium levels"],
                    "diet": "Low sodium diet. Rich in fruits and vegetables.",
                    "routine": "Take at the same time each day. Monitor blood pressure regularly."
                },
                "levothyroxine": {
                    "uses": ["hypothyroidism", "thyroid hormone replacement"],
                    "side_effects": ["weight loss", "increased appetite", "nervousness", "insomnia"],
                    "diet": "Take on empty stomach. Wait 30-60 minutes before eating.",
                    "routine": "Take in the morning. Avoid calcium and iron supplements within 4 hours."
                },
                "azithromycin": {
                    "uses": ["bacterial infections", "respiratory infections", "skin infections"],
                    "side_effects": ["nausea", "diarrhea", "abdominal pain", "allergic reactions"],
                    "diet": "Can be taken with or without food. Avoid antacids.",
                    "routine": "Complete the full course even if feeling better."
                }
            }
            
            # Common medical conditions
            self.conditions = {
                "hypertension": {
                    "diet": "Low sodium, high potassium diet. Rich in fruits and vegetables.",
                    "routine": "Regular exercise, stress management, limit alcohol."
                },
                "diabetes": {
                    "diet": "Low carbohydrate, low glycemic index foods. Regular meal timing.",
                    "routine": "Regular exercise, monitor blood sugar, foot care."
                },
                "hypothyroidism": {
                    "diet": "Iodine-rich foods. Limit cruciferous vegetables.",
                    "routine": "Take medication consistently, regular thyroid function tests."
                },
                "ulcerative colitis": {
                    "diet": "Low fiber during flares, well-cooked vegetables, avoid trigger foods.",
                    "routine": "Stress management, adequate rest, stay hydrated."
                },
                "migraine": {
                    "diet": "Avoid trigger foods (aged cheese, alcohol, chocolate). Regular meals.",
                    "routine": "Adequate sleep, stress management, stay hydrated."
                }
            }
            
        except Exception as e:
            logger.error(f"Failed to initialize SmolDocling analyzer: {str(e)}")
            self.model_loaded = False
    
    def is_model_available(self):
        """Check if the model is available"""
        return self.model_loaded
    
    def analyze_prescription(self, ocr_text):
        """
        Analyze prescription text using rule-based approach
        
        Args:
            ocr_text (str): The OCR extracted text from a prescription
            
        Returns:
            dict: Analysis results including diagnosis, routine, diet, and warnings
        """
        if not self.model_loaded:
            logger.warning("SmolDocling analyzer not available, skipping analysis")
            return {
                "diagnosis": "Model not available",
                "routine": "Model not available",
                "diet": "Model not available",
                "warnings": "Model not available"
            }
        
        try:
            # Extract medications from text
            medications_found = []
            for med in self.medications.keys():
                if re.search(r'\b' + med + r'\b', ocr_text.lower()):
                    medications_found.append(med)
            
            # Extract potential conditions from text
            conditions_found = []
            for condition in self.conditions.keys():
                if re.search(r'\b' + condition + r'\b', ocr_text.lower()):
                    conditions_found.append(condition)
            
            # Generate analysis based on found medications and conditions
            diagnosis = self._generate_diagnosis(medications_found, conditions_found)
            routine = self._generate_routine(medications_found, conditions_found)
            diet = self._generate_diet(medications_found, conditions_found)
            warnings = self._generate_warnings(medications_found)
            
            analysis_result = {
                "diagnosis": diagnosis,
                "routine": routine,
                "diet": diet,
                "warnings": warnings
            }
            
            logger.info("Successfully generated prescription analysis")
            return analysis_result
            
        except Exception as e:
            logger.error(f"Error analyzing prescription: {str(e)}")
            return {
                "diagnosis": f"Error: {str(e)}",
                "routine": "Not available due to error",
                "diet": "Not available due to error",
                "warnings": "Not available due to error"
            }
    
    def analyze_patient_details(self, ocr_text):
        """
        Analyze patient details using rule-based approach
        
        Args:
            ocr_text (str): The OCR extracted text from patient details
            
        Returns:
            dict: Analysis results including diagnosis, routine, diet, and warnings
        """
        # For now, use the same analysis as prescriptions
        return self.analyze_prescription(ocr_text)
    
    def _generate_diagnosis(self, medications, conditions):
        """Generate likely diagnosis based on medications and conditions"""
        if conditions:
            return f"Likely diagnosis: {', '.join(conditions).title()}"
        
        if not medications:
            return "Insufficient information to determine diagnosis"
        
        possible_conditions = []
        for med in medications:
            if med in self.medications:
                possible_conditions.extend(self.medications[med]["uses"])
        
        if possible_conditions:
            return f"Based on medications, possible conditions include: {', '.join(set(possible_conditions)).title()}"
        else:
            return "Insufficient information to determine diagnosis"
    
    def _generate_routine(self, medications, conditions):
        """Generate recommended routine based on medications and conditions"""
        routines = []
        
        # Add medication-specific routines
        for med in medications:
            if med in self.medications:
                routines.append(f"For {med}: {self.medications[med]['routine']}")
        
        # Add condition-specific routines
        for condition in conditions:
            if condition in self.conditions:
                routines.append(f"For {condition}: {self.conditions[condition]['routine']}")
        
        # Add general recommendations
        routines.append("General: Maintain regular sleep schedule and stay hydrated.")
        
        return "\n".join(routines)
    
    def _generate_diet(self, medications, conditions):
        """Generate dietary recommendations based on medications and conditions"""
        diets = []
        
        # Add medication-specific diets
        for med in medications:
            if med in self.medications:
                diets.append(f"For {med}: {self.medications[med]['diet']}")
        
        # Add condition-specific diets
        for condition in conditions:
            if condition in self.conditions:
                diets.append(f"For {condition}: {self.conditions[condition]['diet']}")
        
        # Add general recommendations
        diets.append("General: Balanced diet rich in fruits, vegetables, and whole grains.")
        
        return "\n".join(diets)
    
    def _generate_warnings(self, medications):
        """Generate warnings and side effects based on medications"""
        if not medications:
            return "No specific warnings without medication information"
        
        warnings = []
        for med in medications:
            if med in self.medications:
                side_effects = self.medications[med]["side_effects"]
                warnings.append(f"{med.title()} may cause: {', '.join(side_effects)}")
        
        if warnings:
            warnings.append("\nConsult your doctor if you experience severe or persistent side effects.")
            return "\n".join(warnings)
        else:
            return "No specific warnings for the identified medications"

# Test the module if run directly
if __name__ == "__main__":
    analyzer = SmolDoclingAnalyzer()
    
    test_text = """
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram

Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks
Lialda - take 2 pill everyday for 1 month

Refill: 3 times
"""
    
    if analyzer.is_model_available():
        result = analyzer.analyze_prescription(test_text)
        print("Analysis Result:")
        for key, value in result.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("SmolDocling analyzer is not available. Please check your installation.")
