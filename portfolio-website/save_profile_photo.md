# How to Add Your Profile Photo

To add your profile photo to the portfolio website, follow these steps:

1. Save your profile photo as `profile.jpg`
2. Copy the file to this location: `portfolio-website/frontend/static/images/profile.jpg`

## Using PowerShell (Windows)

```powershell
# Navigate to your portfolio website directory
cd C:\path\to\portfolio-website

# Create the images directory if it doesn't exist
mkdir -p frontend\static\images

# Copy your profile photo (assuming it's in your Downloads folder)
# Replace the path with the actual location of your photo
Copy-Item C:\Users\YourUsername\Downloads\profile.jpg -Destination frontend\static\images\profile.jpg
```

## Using Bash (macOS/Linux)

```bash
# Navigate to your portfolio website directory
cd /path/to/portfolio-website

# Create the images directory if it doesn't exist
mkdir -p frontend/static/images

# Copy your profile photo (assuming it's in your Downloads folder)
# Replace the path with the actual location of your photo
cp ~/Downloads/profile.jpg frontend/static/images/profile.jpg
```

After copying the file, restart your Flask application to see the changes. 