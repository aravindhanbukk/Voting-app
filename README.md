# Voting-app
Run code into AWS EBS

# Deploy to AWS Elastic Beanstalk - Upload & Deploy Method

## Step 1: Create Deployment Package
```bash
# Navigate to your project directory
cd /path/to/voteApp

# Create a ZIP file with all necessary files
zip -r voting-app.zip application.py requirements.txt .ebextensions/
```

## Step 2: Access AWS Console
1. Login to AWS Management Console
2. Navigate to Elastic Beanstalk service
3. Click "Create Application"

## Step 3: Create Application
1. **Application name**: `voting-app`
2. **Platform**: Python
3. **Platform version**: Python 3.9 (or latest)
4. **Application code**: Upload your code
5. Click "Choose file" and select `voting-app.zip`

## Step 4: Configure Environment
1. **Environment name**: `voting-app-env`
2. **Domain**: Leave default or customize
3. Click "Create application"

## Step 5: Monitor Deployment
- Wait 5-10 minutes for environment creation
- Check "Health" status becomes "Ok"
- Access your app via the provided URL

## Step 6: Update Application (Future Deployments)
1. Go to your Elastic Beanstalk application
2. Click "Upload and deploy"
3. Choose new ZIP file
4. Add version label
5. Click "Deploy"

## Files Included in ZIP:
- `application.py` (main Flask app)
- `requirements.txt` (dependencies)
- `.ebextensions/python.config` (EB configuration)
