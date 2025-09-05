**AWS Photo App**

A simple Flask-based web application deployed on Kubernetes (EKS) that demonstrates integration with AWS RDS (PostgreSQL) and AWS S3.

Users can:

Upload files via a web form or API endpoint

Store files securely in an S3 bucket

Connect to an RDS PostgreSQL instance for backend storage

Access the app through an external load balancer (ALB)

🚀 Tech Stack

Flask (Python web framework)

PostgreSQL (RDS) for database

Amazon S3 for file storage

Docker for containerization

Kubernetes (EKS) for orchestration

AWS Load Balancer for external access

📂 Project Structure
aws-photo-app/
│── app.py               # Flask application code
│── requirements.txt     # Python dependencies
│── Dockerfile           # Docker build instructions
│── deployment.yaml      # Kubernetes deployment + service
└── README.md            # Project documentation

🔧 Features

/ → Health check endpoint (Hello from AWS RDS + S3 via Flask!)

/upload → Upload files to S3 bucket

Secrets managed via Kubernetes Secrets for DB & S3 credentials

Deployment automated via kubectl + ECR

▶️ Running Locally
# Clone repository
git clone git@github.com:YashwanthKumar49/aws-photo-app.git
cd aws-photo-app

# Install dependencies
pip install -r requirements.txt

# Run Flask app
python app.py


App will be available at http://127.0.0.1:5000

☁️ Deploying to AWS EKS

Build and push Docker image to ECR

Apply Kubernetes manifests:

kubectl apply -f deployment.yaml


Get external LoadBalancer DNS:

kubectl get svc photo-app-service


Test upload:

curl -X POST -F "file=@test.txt" http://<ALB-DNS>/upload

📜 License

MIT License – feel free to use and modify.
