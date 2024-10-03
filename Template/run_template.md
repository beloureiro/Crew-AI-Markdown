# Create the directory structure
mkdir -p config logs outputs crew tools

# Create files inside each directory
touch config/{agents.yaml,tasks.yaml,tools.yaml,local_llm.yaml}
touch logs/crew_logs.log
touch outputs/report.md
touch .env
touch .gitignore
touch crew/{__init__.py,crew.py}
touch tools/{__init__.py,tool.py}
touch main.py
touch requirements.txt
touch README.md

# Example content for .gitignore (optional)
echo "# Ignore environment variables" >> .gitignore
echo ".env" >> .gitignore
echo "# Ignore logs" >> .gitignore
echo "logs/" >> .gitignore
echo "# Ignore output files" >> .gitignore
echo "outputs/" >> .gitignore
echo "# Ignore Python cache files" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
