# DeepGuardian  
##### Docker Image CI
[![Docker](https://github.com/TechieNK/DeepGuardian/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/TechieNK/DeepGuardian/actions/workflows/docker-publish.yml)&nbsp;[![Docker Image CI](https://github.com/TechieNK/DeepGuardian/actions/workflows/docker-image.yml/badge.svg)](https://github.com/TechieNK/DeepGuardian/actions/workflows/docker-image.yml)  
##### Code Quality CI  
[![CodeQL](https://github.com/TechieNK/DeepGuardian/actions/workflows/codeql.yml/badge.svg)](https://github.com/TechieNK/DeepGuardian/actions/workflows/codeql.yml)  
  
----
## Motivation  
Deepfakes pose a significant risk because they use advanced artificial intelligence to create highly convincing forged videos and audio recordings that are often indistinguishable from genuine content. These tampered with media can be used maliciously to disseminate false information, manipulate public opinion, and deceive individuals. Political instability, reputational harm, and a loss of trust in digital media are all possible outcomes. As deepfake technology advances, the challenges of detecting and mitigating these deceptive creations become more complex, raising concerns about the possibility of widespread misinformation and its impact on various aspects of society such as politics, business, and personal relationships. To address the risks posed by deepfakes, a combination of technological advancements, regulatory measures, and increased public awareness is required.  

## Installation Instructions  
1) **Openshift (Recommended)**
     
   i) Copy the repository URL ([https://github.com/TechieNK/DeepGuardian](https://github.com/TechieNK/DeepGuardian))  
   ii) From OpenShift console, click on "+ Add" from the sidebar  
   iii) Select "Import from Git" from the various options displayed.  
   iv) Paste the repository URL and set the resource type as "Deployment"  
   v) Check the "Add pipeline" checkbox for ease of use in case of keeping up with latest code changes (Optional)  
   vi) Hit the "Create" button and wait until the pipeline execution is completed.  
   vii) The application will be served over the deployment route generated in the console.  

2) **Docker**
     
   i) Clone the repository
      ```
        git clone https://github.com/TechieNK/DeepGuardian.git
      ```
   ii) Build the docker container
      ```
        docker build -t imagename .
      ```
   iii) Run the built container image
     ```
        docker run imagename
     ```

3) **GitHub Container Registry Image** (No scope of customization)

   i) Pull the image from GitHub container registry (GHCR)
   ```
      docker pull ghcr.io/techienk/deepguardian:main
   ```
   ii) Run the docker image
   ```
      docker run deepguardian:main
   ```

## License  
  This application is applied with [GNU General Public License v3](https://github.com/TechieNK/DeepGuardian/blob/main/LICENSE) and is compliant with Open Source Initiative (OSI)

## Tech Stack  
- django (Python)
- PyTorch
- OpenCV
- Docker
- Openshift Sandbox (Deployment and manual testing)
- Bootstrap
- HTML, CSS, JavaScript
----

## Screenshots (Demo)  
<img width="1707" alt="image" src="https://github.com/TechieNK/DeepGuardian/assets/42594454/f1659854-4b3b-4b00-a866-39b7ef1ab234">  
<img width="1707" alt="image" src="https://github.com/TechieNK/DeepGuardian/assets/42594454/35501275-07eb-4849-907b-f2fa8de8dc43">
<img width="1707" alt="image" src="https://github.com/TechieNK/DeepGuardian/assets/42594454/01fe3693-a80b-47c3-96ce-23036bc5cf1c">  
<img width="1707" alt="image" src="https://github.com/TechieNK/DeepGuardian/assets/42594454/9dcb6cde-e636-46c3-af2d-661574cd87c3">



