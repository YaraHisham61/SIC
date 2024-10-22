import streamlit as st
import pandas as pd
import yaml
import pickle

skills_yaml_path = 'skills.yaml'

LABELS = ['Back-end dev', 'Data Scientist', 'Desktop dev', 'DevOps',
       'Embedded dev', 'Front-end dev', 'Full-stack dev', 'Mobile dev',
       ]

with open(skills_yaml_path, 'r') as yaml_file:
    skills_from_yaml = yaml.safe_load(yaml_file)


with open("features_skills_clusters_description.yaml", "r") as stream:
    clusters_config = yaml.safe_load(stream)

molten_clusters = [(cluster_name, cluster_skill)
                   for cluster_name, cluster_skills in clusters_config.items()
                   for cluster_skill in cluster_skills]

clusters_df = pd.DataFrame(molten_clusters, columns=["cluster_name", "skill"])



# Load the trained job recommendation model
model = pickle.load(open("best.pkl", 'rb'))    



def prepare_single_prediction(selected_skills):
    """
    Function to initialize all skills to 0 and set the selected skills to 1.
    
    Parameters:
    - selected_skills: list of skills to set to 1
    
    Returns:
    - prediction_input: dictionary of skills with values 0 or 1
    """
    # Initialize all skills with value 0
    prediction_input = {skill: 0 for skill in skills_from_yaml}

    # Iterate over the list of selected skills and set each to 1
    for skill in selected_skills:
        if skill in prediction_input:
            prediction_input[skill] = 1

    return prediction_input






st.title("Job Recommendation System")

# Lists of options for each category
programming_languages = ["APL","Ada","Apex","Assembly","Bash/Shell (all shells)","C","C#","C++",
                         "Clojure","Cobol","Crystal","Dart","Delphi","Elixir","Erlang","F#","Flow",
                         "Fortran","GDScript","Go","Groovy","Haskell","Java","JavaScript","Julia","Kotlin",
                         "Lisp","Lua","MATLAB","Nim","OCaml","Objective-C","PHP","Perl","PowerShell",
                         "Prolog","Python","R","Raku","Ruby","Rust","SAS","SQL","Scala","Solidity",
                         "Swift","TypeScript","VBA","Visual Basic (.Net)", "Zig"]


database_envs = [
    "BigQuery", "Cassandra", "Clickhouse", "Cloud Firestore", "CockroachDB",
    "Cosmos DB", "CouchDB", "Couchbase", "Datomic", "DuckDB", "DynamoDB",
    "Elasticsearch", "Firebase Realtime Database", "Firebird", "H2", "IBM DB2",
    "InfluxDB", "MariaDB", "Microsoft Access", "Microsoft SQL Server", "MongoDB",
    "MySQL", "Neo4J", "Oracle", "PostgreSQL", "RavenDB", "Redis", "SQLite",
    "Snowflake", "Solr", "Supabase", "TiDB"
]


cloud_platforms = [
    "Amazon Web Services (AWS)", "Cloudflare", "Colocation", "Digital Ocean", 
    "Firebase", "Fly.io", "Google Cloud", "Heroku", "Hetzner", 
    "IBM Cloud or Watson", "Linode (now Akamai)", "Managed Hosting", 
    "Microsoft Azure", "Netlify", "OVH", "OpenShift", "OpenStack", 
    "Oracle Cloud Infrastructure (OCI)", "Render", "Scaleway", "VMware", 
    "Vercel", "Vultr"
]
web_frameworks_technologies = [
    "ASP.NET", "ASP.NET CORE", "Angular", "AngularJS", "Blazor", "CodeIgniter", 
    "Deno", "Django", "Drupal", "Elm", "Express", "FastAPI", "Fastify", "Flask", 
    "Gatsby", "Laravel", "Lit", "NestJS", "Next.js", "Node.js", "Nuxt.js", 
    "Phoenix", "Play Framework", "Qwik", "React", "Remix", "Ruby on Rails", 
    "Solid.js", "Spring Boot", "Svelte", "Symfony", "Vue.js", "WordPress", 
    "jQuery", "HTML/CSS"
]

frameworks_libraries = [
    ".NET (5+)", ".NET Framework (1.0 - 4.8)", ".NET MAUI", "Apache Kafka", 
    "Apache Spark", "CUDA", "Capacitor", "Cordova", "Electron", "Flutter", "GTK", 
    "Hadoop", "Hugging Face Transformers", "Ionic", "JAX", "Keras", "Ktor", "MFC", 
    "Micronaut", "NumPy", "OpenGL", "OpenCV", "Pandas", "Qt", "Quarkus", "RabbitMQ", 
    "React Native", "Scikit-Learn", "Spring Framework", "SwiftUI", "Tauri", 
    "TensorFlow", "Tidyverse", "Torch/PyTorch", "Uno Platform", "Xamarin"
]


developer_tools = [
    "APT", "Ansible", "Ant", "Boost.Test", "Bun", "CMake", "CUTE", "Cargo", 
    "Catch2", "Chef", "Chocolatey", "Composer", "Dagger", "Docker", "ELFspy", 
    "GNU GCC", "Godot", "Google Test", "Gradle", "Homebrew", "Kubernetes", 
    "LLVM's Clang", "MSBuild", "MSVC", "Make", "Maven (build tool)", "Meson", 
    "Ninja", "Nix", "NuGet", "Pacman", "Pip", "Podman", "Pulumi", "Puppet", 
    "QMake", "SCons", "Terraform", "Unity 3D", "Unreal Engine", 
    "Visual Studio Solution", "Vite", "Wasmer", "Webpack", "Yarn", "bandit", 
    "build2", "cppunit", "doctest", "lest", "liblittletest", "npm", "pnpm", 
    "snitch", "tunit"
]


development_envs = [
    "Android Studio", "Atom", "BBEdit", "CLion", "Code::Blocks", "DataGrip", 
    "Eclipse", "Emacs", "Fleet", "Geany", "Goland", "Helix", "IPython", 
    "IntelliJ IDEA", "Jupyter Notebook/JupyterLab", "Kate", "Micro", "Nano", 
    "Neovim", "Netbeans", "Notepad++", "Nova", "PhpStorm", "PyCharm", 
    "Qt Creator", "RStudio", "Rad Studio (Delphi, C++ Builder)", "Rider", 
    "RubyMine", "Spyder", "Sublime Text", "TextMate", "VSCodium", "Vim", 
    "Visual Studio", "Visual Studio Code", "WebStorm", "Xcode", "condo"
]


collaboration_tools = ["JIRA", "Confluence", "GitHub", "GitLab", "Slack"]

# User inputs
st.subheader("Choose your expertise:")
selected_languages = st.multiselect("Programming Languages", programming_languages)
selected_databases = st.multiselect("Database Environments", database_envs)
selected_cloud = st.multiselect("Cloud Platforms", cloud_platforms)
selected_frameworks_technologies = st.multiselect("Web Frameworks & Technologies", web_frameworks_technologies)
selected_libraries = st.multiselect("Frameworks and Libraries", frameworks_libraries)
selected_tools = st.multiselect("Developer Tools", developer_tools)
selected_envs = st.multiselect("Development Environments", development_envs)
selected_collab = st.multiselect("Collaboration Tools", collaboration_tools)

# Combine inputs into a list of strings
user_input = selected_languages + selected_databases + selected_cloud + selected_frameworks_technologies + \
 selected_libraries + selected_tools + selected_envs + selected_collab

if st.button("Predict Recommended Job"):
    print("Hello")
    print(user_input)
    
    if user_input:



        prediction_input = prepare_single_prediction(user_input)

        singl_pred = pd.DataFrame([prediction_input])


        print("\n\n******************************""\n")
        print("Skills Pred \n")
        print(singl_pred)


        sample_clusters = clusters_df.copy()
        sample_clusters["sample_skills"] = sample_clusters["skill"].isin(user_input)

        cluster_features = sample_clusters.groupby("cluster_name")["sample_skills"].sum()

        cluster_features_df = cluster_features.reset_index()

        cluster_dict = cluster_features_df.set_index(cluster_features_df.columns[0])[cluster_features_df.columns[1]].to_dict()

        cluster_pred = pd.DataFrame([cluster_dict])

        print("\n\n******************************\n")
        print("Cluster Pred \n")
        print(cluster_pred)

        single_prediction =  pd.concat([singl_pred, cluster_pred], axis=1, join='inner')



        # Predict job
        probabilities = model.predict_proba(single_prediction)
        class_1_probs = [prob[0][1] for prob in probabilities]
        print(class_1_probs)
        max_index = class_1_probs.index(max(class_1_probs))
        prediction = LABELS[max_index]
        st.success(f"Recommended Job: {LABELS[max_index]}")
    else:
        st.error("Please select at least one option.")
