import PyPDF2
import re

def parse_resume(file_path: str) -> dict:
    """
    Parses a resume in PDF format and extracts its content into a structured dictionary.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        dict: A dictionary containing the extracted data.
    """
    resume_data = {
        "name": None,
        "email": None,
        "phone": None,
        "skills": [],
        "experience": None,
        "education": None,
        "summary": None,
        "projects": [],
    }

    try:
        # Open the PDF file
        with open(file_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""

            # Extract text from each page
            for page in reader.pages:
                text += page.extract_text()

        # Process the text to extract structured data
        lines = text.split("\n")

        # Extract name (assuming it's the first non-empty line)
        for line in lines:
            if line.strip():
                resume_data["name"] = line.strip()
                break

        # Extract email using regex
        email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
        if email_match:
            resume_data["email"] = email_match.group(0)

        # Extract phone number using regex
        phone_match = re.search(r"\+?\d[\d -]{8,}\d", text)
        if phone_match:
            resume_data["phone"] = phone_match.group(0)

        # Define section headers and their corresponding keys
        section_headers = {
            "Skills": "skills",
            "Experience": "experience",
            "Education": "education",
            "Summary": "summary",
            "Projects": "projects",
        }

        # Parse sections dynamically
        current_section = None
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Check if the line is a section header
            for header, key in section_headers.items():
                if header.lower() in line.lower():
                    current_section = key
                    if key == "skills":  # Initialize skills as a list
                        resume_data[key] = []
                    elif key == "projects":  # Initialize projects as a list
                        resume_data[key] = []
                    else:
                        resume_data[key] = ""
                    break
            else:
                # Add content to the current section
                if current_section:
                    if current_section in ["skills", "projects"]:
                        resume_data[current_section].append(line)
                    else:
                        resume_data[current_section] += f" {line}"

        # Clean up skills and projects
        if resume_data["skills"]:
            resume_data["skills"] = [skill.strip() for skill in " ".join(resume_data["skills"]).split(",") if skill.strip()]
        if resume_data["projects"]:
            resume_data["projects"] = [project.strip() for project in resume_data["projects"]]

    except Exception as e:
        print(f"Error parsing resume: {e}")

    return resume_data


# Example usage
if __name__ == "__main__":
    file_path = "/Users/sreeramsutraye/Developer/candidate-manager-python/app/ats_parser/SreeramPythonFullStackDeveloper.pdf"
    parsed_data = parse_resume(file_path)
    print(parsed_data)