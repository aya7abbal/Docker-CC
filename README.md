Assignment 3: Docker & Kubernetes Orchestration

Overview

This project demonstrates the orchestration and deployment of a Python script using Docker and Kubernetes. The Python script processes two text files (IF.txt and AlwaysRememberUsThisWay.txt) to calculate word counts, identify the most frequent words, and retrieve the container’s IP address. The results are saved in an output file result.txt.

Key Features:

	•	Dockerized Python Application: The script and its dependencies are containerized for portability.
	•	Kubernetes Orchestration: Kubernetes was used to deploy and manage the container with replicas.
	•	Extra Credit: Two replicas were orchestrated using Kubernetes, and the status of the pods was monitored.

Project Structure

	•	script.py: The Python script that processes the text files and writes the results to output/result.txt.
	•	Dockerfile: Docker configuration for containerizing the Python environment and the script.
	•	kubernetes-deployment.yaml: Kubernetes deployment manifest to orchestrate two replicas of the container.
	•	kube_output.txt: Output from the command kubectl get pods, showing the status of the containers during deployment.
	•	IF.txt & AlwaysRememberUsThisWay.txt: Input text files processed by the Python script.

Steps for Running the Project

1. Build and Run the Docker Container

	1.	Build Docker Image:

docker build -t assignment3_image .


	2.	Run the Docker Container:

docker run -v $(pwd):/home/data assignment3_image


	3.	The script will process the two text files and write the results to /home/data/output/result.txt.

2. Push Docker Image to Docker Hub

	1.	Tag the Docker Image:

docker tag assignment3_image:latest your_dockerhub_username/assignment3_image:latest


	2.	Push the Docker Image:

docker push your_dockerhub_username/assignment3_image:latest



3. Kubernetes Orchestration (Extra Credit)

	1.	Deploy with Kubernetes:
The kubernetes-deployment.yaml file defines a deployment with two replicas of the container. Apply the deployment using:

kubectl apply -f kubernetes-deployment.yaml


	2.	Monitor Pod Status:
Check the status of the pods:

kubectl get pods > kube_output.txt


	3.	The pod statuses are recorded in kube_output.txt.

Kubernetes Manifest (kubernetes-deployment.yaml)

The deployment defines two replicas of the container:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: assignment3-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: assignment3
  template:
    metadata:
      labels:
        app: assignment3
    spec:
      containers:
      - name: assignment3-container
        image: your_dockerhub_username/assignment3_image:latest
        ports:
        - containerPort: 80

Results

	•	Pod Status: The Kubernetes pods were successfully orchestrated and completed their tasks. The status of the pods is captured in kube_output.txt:

NAME                                     READY   STATUS      RESTARTS   AGE
assignment3-deployment-xxxxxx            0/1     Completed   1          Xs
assignment3-deployment-xxxxxx            0/1     Completed   1          Xs
assignment3-job-xxxxxx                   0/1     Completed   0          Xm


	•	Results File: The word counts and top 3 words for each file were written to output/result.txt:

Word count IF.txt: 287
Word count ARUTW.txt: 223
Grand total of words: 510
Top 3 words in IF.txt: [('you', 14), ('If', 13), ('can', 12)]
Top 3 words in AlwaysRememberUsThisWay.txt: [('I', 15), ('the', 12), ('not', 9)]
IP address: 10.1.0.13



Conclusion

This project successfully demonstrates the use of Docker to containerize a Python application, and Kubernetes to orchestrate the deployment with two replicas. Both the Docker image and Kubernetes configurations are included for future use.

This README outlines the entire process and can be directly added to your GitHub repository. Let me know if you need any changes!
