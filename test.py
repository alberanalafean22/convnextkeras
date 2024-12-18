
# Kode Streamlit

import streamlit as st
import git

# Repository GitHub
repo_url = "(link unavailable)"

# Nama model
model_name = "model.h5"

# Fungsi load model
def load_model(repo_url, model_name):
    repo = git.Repo.clone_from(repo_url, "temp_repo")
    git-lfs install
    git-lfs pull
    return "temp_repo/" + model_name

# Load model
model_path = load_model(repo_url, model_name)

# Tampilkan model
st.write("Model berhasil di-load dari GitHub!")
st.write(model_path)