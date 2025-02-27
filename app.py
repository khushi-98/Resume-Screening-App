# import streamlit as st
# import pickle
# import re
# import nltk
# import seaborn as sns
#
# nltk.download('punkt')
# nltk.download('stopwords')
#
# #loading models
# knn = pickle.load(open('knn.pkl','rb'))
# tfidfd = pickle.load(open('tfidf.pkl','rb'))
#
# def clean_resume(resume_text):
#     clean_text = re.sub('http\S+\s*', ' ', resume_text)
#     clean_text = re.sub('RT|cc', ' ', clean_text)
#     clean_text = re.sub('#\S+', '', clean_text)
#     clean_text = re.sub('@\S+', '  ', clean_text)
#     clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
#     clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
#     clean_text = re.sub('\s+', ' ', clean_text)
#     return clean_text
# # web app
# def main():
#     st.title("Resume Screening App")
#     uploaded_file = st.file_uploader('Upload Resume', type=['txt','pdf'])
#
#     if uploaded_file is not None:
#         try:
#             resume_bytes = uploaded_file.read()
#             resume_text = resume_bytes.decode('utf-8')
#         except UnicodeDecodeError:
#             # If UTF-8 decoding fails, try decoding with 'latin-1'
#             resume_text = resume_bytes.decode('latin-1')
#
#         cleaned_resume = clean_resume(resume_text)
#         input_features = tfidfd.transform([cleaned_resume])
#         prediction_id = knn.predict(input_features)[0]
#         st.write(prediction_id)
#
#         # Map category ID to category name
#         category_mapping = {
#             15: "Java Developer",
#             23: "Testing",
#             8: "DevOps Engineer",
#             20: "Python Developer",
#             24: "Web Designing",
#             12: "HR",
#             13: "Hadoop",
#             3: "Blockchain",
#             10: "ETL Developer",
#             18: "Operations Manager",
#             6: "Data Science",
#             22: "Sales",
#             16: "Mechanical Engineer",
#             1: "Arts",
#             7: "Database",
#             11: "Electrical Engineering",
#             14: "Health and fitness",
#             19: "PMO",
#             4: "Business Analyst",
#             9: "DotNet Developer",
#             2: "Automation Testing",
#             17: "Network Security Engineer",
#             21: "SAP Developer",
#             5: "Civil Engineer",
#             0: "Advocate",
#         }
#
#         category_name = category_mapping.get(prediction_id, "Unknown")
#
#         st.write("Predicted Category:", category_name)
#
#
#
#
# if __name__ == "__main__":
#     main()

import streamlit as st
import pickle
import re
import nltk
import seaborn as sns
import zipfile

# Set page config for white background
st.set_page_config(
    page_title="Resume Screening App",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS to inject contained in a string
background_style = """
<style>
.stApp {
    background-color: pink;
    color: green;
}
.title {
    color: #000000;
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 20px;
}
</style>
"""

# Inject CSS with Markdown
st.markdown(background_style, unsafe_allow_html=True)

nltk.download('punkt')
nltk.download('stopwords')

# #loading models
# knn = pickle.load(open('knn.pkl','rb'))
# tfidfd = pickle.load(open('tfidf.pkl','rb'))
###########################################

# Path to the ZIP file
zip_file_path = 'models.zip'

# Names of the files within the ZIP archive
knn_filename = 'knn.pkl'
tfidf_filename = 'tfidf.pkl'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    with zip_ref.open(knn_filename) as knn_file:
        knn = pickle.load(knn_file)
    with zip_ref.open(tfidf_filename) as tfidf_file:
        tfidfd = pickle.load(tfidf_file)



def clean_resume(resume_text):
    clean_text = re.sub('http\S+\s*', ' ', resume_text)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+', '', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', r' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text

# web app
def main():
    st.title("Resume Screening App")
    uploaded_file = st.file_uploader('Upload Resume', type=['txt','pdf'])

    if uploaded_file is not None:
        try:
            resume_bytes = uploaded_file.read()
            resume_text = resume_bytes.decode('utf-8')
        except UnicodeDecodeError:
            # If UTF-8 decoding fails, try decoding with 'latin-1'
            resume_text = resume_bytes.decode('latin-1')

        cleaned_resume = clean_resume(resume_text)
        input_features = tfidfd.transform([cleaned_resume])
        prediction_id = knn.predict(input_features)[0]
        st.write(prediction_id)

        # Map category ID to category name
        category_mapping = {
            15: "Java Developer",
            23: "Testing",
            8: "DevOps Engineer",
            20: "Python Developer",
            24: "Web Designing",
            12: "HR",
            13: "Hadoop",
            3: "Blockchain",
            10: "ETL Developer",
            18: "Operations Manager",
            6: "Data Science",
            22: "Sales",
            16: "Mechanical Engineer",
            1: "Arts",
            7: "Database",
            11: "Electrical Engineering",
            14: "Health and fitness",
            19: "PMO",
            4: "Business Analyst",
            9: "DotNet Developer",
            2: "Automation Testing",
            17: "Network Security Engineer",
            21: "SAP Developer",
            5: "Civil Engineer",
            0: "Advocate",
        }

        category_name = category_mapping.get(prediction_id, "Unknown")

        st.write("Predicted Category:", category_name)

if __name__ == "__main__":
    main()


