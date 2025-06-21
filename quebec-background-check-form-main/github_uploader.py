import os
from github import Github
import base64

class GitHubUploader:
    def __init__(self, token=None, repo_name=None):
        """
        Initialize GitHub uploader with token and repository name
        
        Args:
            token: GitHub personal access token
            repo_name: Repository name in format 'username/repo'
        """
        self.token = token or os.getenv('GITHUB_TOKEN')
        self.repo_name = repo_name or os.getenv('GITHUB_REPO')
        
        if not self.token:
            raise ValueError("GitHub token is required. Set GITHUB_TOKEN environment variable.")
        
        if not self.repo_name:
            raise ValueError("Repository name is required. Set GITHUB_REPO environment variable.")
        
        self.github = Github(self.token)
        self.repo = self.github.get_repo(self.repo_name)
    
    def upload_pdf(self, file_path, github_path=None):
        """
        Upload a PDF file to GitHub repository
        
        Args:
            file_path: Local path to the PDF file
            github_path: Path in GitHub repo (defaults to 'pdfs/filename')
            
        Returns:
            dict: Upload result with file URL and commit info
        """
        try:
            # Read file content
            with open(file_path, 'rb') as file:
                content = file.read()
            
            # Determine GitHub path
            if github_path is None:
                filename = os.path.basename(file_path)
                github_path = f"pdfs/{filename}"
            
            # Create commit message
            commit_message = f"Add PDF: {os.path.basename(github_path)}"
            
            # Check if file already exists
            try:
                existing_file = self.repo.get_contents(github_path)
                # Update existing file
                result = self.repo.update_file(
                    github_path,
                    commit_message,
                    content,
                    existing_file.sha
                )
            except:
                # Create new file
                result = self.repo.create_file(
                    github_path,
                    commit_message,
                    content
                )
            
            return {
                "success": True,
                "file_url": result['content'].html_url,
                "commit_sha": result['commit'].sha,
                "github_path": github_path
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def upload_pdf_from_bytes(self, pdf_bytes, filename, github_path=None):
        """
        Upload PDF from bytes data
        
        Args:
            pdf_bytes: PDF file content as bytes
            filename: Name for the file
            github_path: Path in GitHub repo (defaults to 'pdfs/filename')
            
        Returns:
            dict: Upload result
        """
        try:
            # Determine GitHub path
            if github_path is None:
                github_path = f"pdfs/{filename}"
            
            # Create commit message
            commit_message = f"Add PDF: {filename}"
            
            # Check if file already exists
            try:
                existing_file = self.repo.get_contents(github_path)
                # Update existing file
                result = self.repo.update_file(
                    github_path,
                    commit_message,
                    pdf_bytes,
                    existing_file.sha
                )
            except:
                # Create new file
                result = self.repo.create_file(
                    github_path,
                    commit_message,
                    pdf_bytes
                )
            
            return {
                "success": True,
                "file_url": result['content'].html_url,
                "commit_sha": result['commit'].sha,
                "github_path": github_path
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def list_pdfs(self, path="pdfs"):
        """
        List all PDFs in the repository
        
        Args:
            path: Directory path to search for PDFs
            
        Returns:
            list: List of PDF files with their details
        """
        try:
            contents = self.repo.get_contents(path)
            pdf_files = []
            
            for content in contents:
                if content.name.endswith('.pdf'):
                    pdf_files.append({
                        "name": content.name,
                        "path": content.path,
                        "size": content.size,
                        "url": content.html_url,
                        "download_url": content.download_url
                    })
            
            return pdf_files
            
        except Exception as e:
            print(f"Error listing PDFs: {str(e)}")
            return []